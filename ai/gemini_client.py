"""
=========================================================
AI Career Intelligence Platform
Gemini Client Wrapper
=========================================================
"""

import os
import json
from typing import Optional, Dict, Any


class GeminiClient:
    """
    Wrapper for Google Gemini API with fallback capabilities.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.model_name = "gemini-1.5-flash"
        self._genai = None

        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._genai = genai
            except Exception as e:
                print(f"[GeminiClient] Failed to initialize Google Generative AI: {e}")

    def generate_text(self, prompt: str, system_instruction: Optional[str] = None) -> Optional[str]:
        """
        Generate raw text response from Gemini API.
        """
        if not self._genai or not self.api_key:
            return None

        try:
            full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt
            model = self._genai.GenerativeModel(self.model_name)
            response = model.generate_content(full_prompt)
            if response and response.text:
                return response.text.strip()
        except Exception as err:
            print(f"[GeminiClient] Error during text generation: {err}")

        return None

    def generate_json(self, prompt: str, system_instruction: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """
        Generate structured JSON response from Gemini API.
        """
        raw_response = self.generate_text(prompt, system_instruction)
        if not raw_response:
            return None

        try:
            # Strip markdown block if present
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
