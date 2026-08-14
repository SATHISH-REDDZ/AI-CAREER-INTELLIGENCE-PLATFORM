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
    Wrapper for Google Gemini API using official google-genai SDK with resilient fallbacks.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
        self._client = None

        if self.api_key:
            try:
                # Primary: Official Google GenAI SDK (from google import genai)
                from google import genai
                self._client = genai.Client(api_key=self.api_key)
            except Exception as e:
                # Fallback to legacy SDK if google-genai not available in local environment
                try:
                    import google.generativeai as legacy_genai
                    legacy_genai.configure(api_key=self.api_key)
                    self._legacy_genai = legacy_genai
                except Exception as legacy_err:
                    print(f"[GeminiClient] Failed to initialize Google GenAI SDK: {e} / Legacy: {legacy_err}")

    def generate_text(self, prompt: str, system_instruction: Optional[str] = None) -> Optional[str]:
        """
        Generate text response from Gemini API using google-genai SDK.
        """
        if not self.api_key:
            return None

        full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt

        # 1. Try Google GenAI SDK client
        if hasattr(self, "_client") and self._client:
            try:
                response = self._client.models.generate_content(
                    model=self.model_name,
                    contents=full_prompt
                )
                if response and hasattr(response, "text") and response.text:
                    return response.text.strip()
            except Exception as err:
                print(f"[GeminiClient] genai.Client error: {err}")

        # 2. Try Legacy SDK fallback
        if hasattr(self, "_legacy_genai") and self._legacy_genai:
            try:
                model = self._legacy_genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(full_prompt)
                if response and response.text:
                    return response.text.strip()
            except Exception as err:
                print(f"[GeminiClient] legacy genai error: {err}")

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
