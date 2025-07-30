import os
import json
from typing import Dict
import google.generativeai as genai
from dotenv import load_dotenv
from .data_types import TranscriptAnalysis


def analyze_transcript(transcript_text: str, word_frequency: Dict[str, int]) -> TranscriptAnalysis:
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    prompt = f"""
    Analyze the following transcript and provide a structured analysis.
    
    Transcript:
    {transcript_text}
    
    Word Frequency Data (top words):
    {json.dumps(dict(list(word_frequency.items())[:20]), indent=2)}
    
    Please provide your analysis in the following JSON format:
    {{
        "quick_summary": "A brief 2-3 sentence overview of the transcript's main topic and key points",
        "bullet_point_highlights": [
            "First key highlight",
            "Second key highlight",
            "... (5-7 total highlights)"
        ],
        "sentiment_analysis": "Analysis of the overall emotional tone and sentiment",
        "keywords": ["keyword1", "keyword2", "... (5-10 keywords)"]
    }}
    
    Ensure your response is valid JSON format only, with no additional text.
    """
    
    response = model.generate_content(prompt)
    
    try:
        response_text = response.text.strip()
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        analysis_dict = json.loads(response_text.strip())
        
        return TranscriptAnalysis(**analysis_dict)
    
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        print(f"Raw response: {response.text}")
        
        return TranscriptAnalysis(
            quick_summary="Error: Unable to parse LLM response",
            bullet_point_highlights=["Analysis failed"],
            sentiment_analysis="Unknown",
            keywords=["error"]
        )
    except Exception as e:
        print(f"Error during analysis: {e}")
        return TranscriptAnalysis(
            quick_summary=f"Error: {str(e)}",
            bullet_point_highlights=["Analysis failed"],
            sentiment_analysis="Unknown",
            keywords=["error"]
        )