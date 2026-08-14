"""
=========================================================
AI Career Intelligence Platform
Chatbot Conversation Memory
=========================================================
"""

from typing import List, Dict, Any


class ChatMemory:
    """
    In-memory chat buffer manager for sliding window conversation history.
    """

    def __init__(self, max_history: int = 15):
        self.max_history = max_history
        self.history: List[Dict[str, Any]] = []

    def add_message(self, role: str, content: str, meta: Dict[str, Any] = None):
        """Add message entry to memory buffer."""
        entry = {
            "role": role,
            "content": content
        }
        if meta:
            entry.update(meta)

        self.history.append(entry)
        if len(self.history) > self.max_history * 2:
            self.history = self.history[-self.max_history * 2:]

    def get_history(self) -> List[Dict[str, Any]]:
        """Return full history list."""
        return self.history

    def set_history(self, history: List[Dict[str, Any]]):
        """Set history list."""
        self.history = history

    def clear(self):
        """Clear memory buffer."""
        self.history = []

    def export_summary(self) -> str:
        """Format history for export."""
        lines = []
        for msg in self.history:
            role = msg.get("role", "user").upper()
            content = msg.get("content", "")
            lines.append(f"[{role}]: {content}\n")
        return "\n".join(lines)
