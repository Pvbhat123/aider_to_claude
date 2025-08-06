import json
import re
from collections import Counter
from typing import Dict, List

import google.generativeai as genai

from constants import GEMINI_API_KEY, GEMINI_MODEL_NAME, STOPWORDS, PUNCTUATION_BLACKLIST
from datatypes import TranscriptAnalysis

class GeminiAnalyzer:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL_NAME)
    
    def analyze_transcript(self, text: str, min_count: int = 3) -> TranscriptAnalysis:
        word_freq = self._calculate_word_frequency(text, min_count)
        
        prompt = f"""
        Analyze the following transcript and provide a structured response in JSON format:

        Transcript:
        {text[:3000]}

        Please provide:
        1. A concise executive summary (2-3 sentences)
        2. 5 key bullet points
        3. 5-7 relevant keywords
        4. Overall sentiment (positive, negative, neutral, or mixed)

        Respond in this exact JSON format:
        {{
            "summary": "Your summary here",
            "bullet_points": ["point 1", "point 2", "point 3", "point 4", "point 5"],
            "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
            "sentiment": "positive/negative/neutral/mixed"
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            response_text = response.text
            
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                ai_analysis = json.loads(json_match.group())
            else:
                ai_analysis = {
                    "summary": "Unable to generate summary",
                    "bullet_points": ["Analysis not available"],
                    "keywords": ["transcript"],
                    "sentiment": "neutral"
                }
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            ai_analysis = {
                "summary": "Error generating summary",
                "bullet_points": ["Analysis failed"],
                "keywords": ["error"],
                "sentiment": "neutral"
            }
        
        total_words = len(text.split())
        unique_words = len(set(text.lower().split()))
        
        return TranscriptAnalysis(
            summary=ai_analysis.get("summary", ""),
            bullet_points=ai_analysis.get("bullet_points", []),
            keywords=ai_analysis.get("keywords", []),
            sentiment=ai_analysis.get("sentiment", "neutral"),
            word_count=word_freq,
            total_words=total_words,
            unique_words=unique_words
        )
    
    def _calculate_word_frequency(self, text: str, min_count: int) -> Dict[str, int]:
        text = text.lower()
        
        for punct in PUNCTUATION_BLACKLIST:
            text = text.replace(punct, " ")
        
        words = text.split()
        
        filtered_words = [word for word in words if word not in STOPWORDS and len(word) > 1]
        
        word_count = Counter(filtered_words)
        
        filtered_count = {word: count for word, count in word_count.items() if count >= min_count}
        
        sorted_count = dict(sorted(filtered_count.items(), key=lambda x: x[1], reverse=True))
        
        return sorted_count