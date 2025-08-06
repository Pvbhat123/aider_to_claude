import os
import json
from collections import Counter
from typing import Dict
from dotenv import load_dotenv
import google.generativeai as genai

from .data_types import TranscriptAnalysis, TranscriptAnalysisV2
from .constants import word_blacklist, DEFAULT_THRESHOLD

load_dotenv()


def analyze_transcript(text: str, threshold: int = DEFAULT_THRESHOLD) -> TranscriptAnalysis:
    words = text.lower().split()
    word_counts = Counter(words)
    
    filtered_counts = {
        word: count for word, count in word_counts.items()
        if word not in word_blacklist and count >= threshold
    }
    
    word_count_dict = dict(sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True))
    
    total_words = len(words)
    unique_words = len(set(words))
    
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Analyze the following transcript and provide:
        1. A concise executive summary (2-3 sentences)
        2. 5 key bullet points
        3. 5-10 most important keywords
        4. Overall sentiment (positive, negative, or neutral)
        
        Transcript:
        {text[:3000]}
        
        Please respond in JSON format with keys: summary, bullet_points, keywords, sentiment
        """
        
        response = model.generate_content(prompt)
        response_text = response.text
        
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        ai_data = json.loads(response_text.strip())
        
        return TranscriptAnalysis(
            summary=ai_data.get("summary", "Summary not available"),
            bullet_points=ai_data.get("bullet_points", ["No bullet points available"]),
            keywords=ai_data.get("keywords", ["No keywords available"]),
            word_count=word_count_dict,
            total_words=total_words,
            unique_words=unique_words
        )
    
    except Exception as e:
        print(f"Warning: AI analysis failed: {e}")
        return TranscriptAnalysis(
            summary="AI analysis unavailable - please check your GEMINI_API_KEY",
            bullet_points=["Word frequency analysis completed"],
            keywords=list(word_count_dict.keys())[:10],
            word_count=word_count_dict,
            total_words=total_words,
            unique_words=unique_words
        )


def analyze_with_sentiment(text: str, threshold: int = DEFAULT_THRESHOLD) -> TranscriptAnalysisV2:
    words = text.lower().split()
    word_counts = Counter(words)
    
    filtered_counts = {
        word: count for word, count in word_counts.items()
        if word not in word_blacklist and count >= threshold
    }
    
    word_count_dict = dict(sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True))
    
    total_words = len(words)
    unique_words = len(set(words))
    
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Analyze the following transcript and provide:
        1. A concise executive summary (2-3 sentences)
        2. 5 key bullet points
        3. 5-10 most important keywords
        4. Overall sentiment (positive, negative, or neutral) with reasoning
        
        Transcript:
        {text[:3000]}
        
        Please respond in JSON format with keys: summary, bullet_points, keywords, sentiment
        """
        
        response = model.generate_content(prompt)
        response_text = response.text
        
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        ai_data = json.loads(response_text.strip())
        
        return TranscriptAnalysisV2(
            summary=ai_data.get("summary", "Summary not available"),
            bullet_points=ai_data.get("bullet_points", ["No bullet points available"]),
            keywords=ai_data.get("keywords", ["No keywords available"]),
            sentiment=ai_data.get("sentiment", "neutral"),
            word_count=word_count_dict,
            total_words=total_words,
            unique_words=unique_words
        )
    
    except Exception as e:
        print(f"Warning: AI analysis failed: {e}")
        return TranscriptAnalysisV2(
            summary="AI analysis unavailable - please check your GEMINI_API_KEY",
            bullet_points=["Word frequency analysis completed"],
            keywords=list(word_count_dict.keys())[:10],
            sentiment="neutral",
            word_count=word_count_dict,
            total_words=total_words,
            unique_words=unique_words
        )