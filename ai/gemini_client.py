"""
=========================================================
AI Career Intelligence Platform
Gemini Client Wrapper (google-genai SDK)
=========================================================
"""

import os
import json
from typing import Optional, Dict, Any


class GeminiClient:
    """
    Unified client wrapper for Google Gemini API using official google-genai SDK.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        self._client = None

        if self.api_key:
            try:
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                print(f"[GeminiClient] Google GenAI SDK initialization notice: {e}")

    def generate_text(self, prompt: str, system_instruction: Optional[str] = None) -> Optional[str]:
        """
        Generate text response from Gemini API using google-genai SDK.
        """
        if not self.api_key or not self._client:
            return None

        full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt

        try:
            response = self._client.models.generate_content(
                model=self.model_name,
                contents=full_prompt
            )
            if response and hasattr(response, "text") and response.text:
                return response.text.strip()
        except Exception as err:
            print(f"[GeminiClient] API generation error: {err}")

        return None

    def generate_json(self, prompt: str, system_instruction: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Generate structured JSON response from Gemini API.
        """
        raw_response = self.generate_text(prompt, system_instruction)
        if not raw_response:
            return None

        try:
            cleaned = raw_response.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            elif cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            return json.loads(cleaned.strip())
        except Exception as err:
            print(f"[GeminiClient] Error parsing JSON output: {err}")

        return None
