import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from typing import Dict, List, Tuple

try:
    from .data_types import TranscriptAnalysis
except ImportError:
    from data_types import TranscriptAnalysis

load_dotenv()

def analyze_transcript(transcript: str, word_count: List[Tuple[str, int]]) -> TranscriptAnalysis:
    # Configure Gemini API
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_actual_gemini_api_key_here":
        print("WARNING: No valid Gemini API key found. Using fallback analysis.")
        return TranscriptAnalysis(
            quick_summary="API key not configured. Please add your Gemini API key to the .env file.",
            bullet_point_highlights=["Set GEMINI_API_KEY in .env file", "Get key from https://makersuite.google.com/app/apikey"],
            sentiment_analysis="Unable to analyze without API key",
            keywords=[word for word, _ in word_count[:5]]
        )
    
    genai.configure(api_key=api_key)
    
    # Create the model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prepare the word count data
    top_words = word_count[:10] if len(word_count) >= 10 else word_count
    word_freq_text = "\n".join([f"- {word}: {count} occurrences" for word, count in top_words])
    
    # Create the prompt
    prompt = f"""Analyze the following transcript and provide a structured analysis.

Transcript:
{transcript}

Top word frequencies (excluding common words):
{word_freq_text}

Please provide:
1. A quick summary (2-3 sentences)
2. 3-5 bullet point highlights of key topics or themes
3. Overall sentiment analysis (positive, negative, neutral, or mixed)
4. 5-10 keywords that best represent the content

Format your response as a JSON object with the following structure:
{{
    "quick_summary": "...",
    "bullet_point_highlights": ["...", "...", "..."],
    "sentiment_analysis": "...",
    "keywords": ["...", "...", "..."]
}}"""
    
    # Generate the response
    response = model.generate_content(prompt)
    
    # Parse the JSON response
    try:
        # Extract JSON from the response text
        response_text = response.text
        # Find the JSON object in the response
        start_idx = response_text.find('{')
        end_idx = response_text.rfind('}') + 1
        json_text = response_text[start_idx:end_idx]
        
        analysis_data = json.loads(json_text)
        
        # Create and return the TranscriptAnalysis object
        return TranscriptAnalysis(
            quick_summary=analysis_data["quick_summary"],
            bullet_point_highlights=analysis_data["bullet_point_highlights"],
            sentiment_analysis=analysis_data["sentiment_analysis"],
            keywords=analysis_data["keywords"]
        )
    except Exception as e:
        # Fallback if JSON parsing fails
        return TranscriptAnalysis(
            quick_summary="Error analyzing transcript",
            bullet_point_highlights=["Analysis failed"],
            sentiment_analysis="unknown",
            keywords=[]
        )