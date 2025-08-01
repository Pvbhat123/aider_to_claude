"""OpenAI API integration for transcript analysis."""

import os
from typing import List, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def analyze_transcript_with_llm(transcript: str) -> dict:
    """Analyze transcript using OpenAI's GPT-4o-mini model."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return {
            "summary": "No OpenAI API key found. Please set OPENAI_API_KEY in .env file.",
            "topics": []
        }
    
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = f"""Analyze the following transcript and provide:
1. A concise summary (2-3 sentences)
2. A list of 3-5 key topics discussed

Transcript:
{transcript[:3000]}  # Limit to first 3000 characters to manage token usage

Please format your response as:
SUMMARY: [your summary here]
TOPICS: [topic1], [topic2], [topic3], etc.
"""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes transcripts."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Parse the response
        content = response.choices[0].message.content
        lines = content.strip().split('\n')
        
        summary = ""
        topics = []
        
        for line in lines:
            if line.startswith("SUMMARY:"):
                summary = line.replace("SUMMARY:", "").strip()
            elif line.startswith("TOPICS:"):
                topics_str = line.replace("TOPICS:", "").strip()
                topics = [t.strip() for t in topics_str.split(',')]
        
        return {
            "summary": summary or "Unable to generate summary.",
            "topics": topics
        }
        
    except Exception as e:
        return {
            "summary": f"Error analyzing transcript: {str(e)}",
            "topics": []
        }


def get_sentiment(text: str) -> tuple[str, float]:
    """Analyze sentiment of the text using OpenAI."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "neutral", 0.0
    
    try:
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Analyze the sentiment of the text. Respond with only: SENTIMENT: [positive/negative/neutral] SCORE: [float between -1 and 1]"},
                {"role": "user", "content": text[:1000]}  # Limit text length
            ],
            temperature=0.3,
            max_tokens=50
        )
        
        content = response.choices[0].message.content
        
        # Parse response
        sentiment = "neutral"
        score = 0.0
        
        if "SENTIMENT:" in content and "SCORE:" in content:
            parts = content.split("SCORE:")
            sentiment_part = parts[0].replace("SENTIMENT:", "").strip()
            score_part = parts[1].strip()
            
            sentiment = sentiment_part.lower()
            try:
                score = float(score_part)
            except:
                score = 0.0
        
        return sentiment, score
        
    except Exception:
        return "neutral", 0.0