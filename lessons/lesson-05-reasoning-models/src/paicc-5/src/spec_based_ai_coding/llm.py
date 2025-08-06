from typing import List
from pydantic import BaseModel
import google.generativeai as genai
import os
from .data_types import TranscriptAnalysis

# Set up Gemini client using API key from environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

def analyze_transcript(transcript: str, word_count: dict) -> TranscriptAnalysis:
    prompt = (
        "You are a helpful assistant analyzing transcripts.\n\n"
        f"Transcript:\n{transcript}\n\n"
        f"Word Count: {word_count}\n\n"
        "Return a structured response for TranscriptAnalysis."
    )

    response = model.generate_content(prompt)

    try:
        # Try to parse the text response as JSON and load into TranscriptAnalysis
        import json
        parsed = json.loads(response.text)
        return TranscriptAnalysis(**parsed)
    except Exception as e:
        raise ValueError(f"Failed to parse Gemini response: {e}\nRaw response: {response.text}")