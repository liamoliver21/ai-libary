from __future__ import annotations

import ollama

from .backend import LLMBackend
from .message import Message


class OllamaBackend(LLMBackend):
    def __init__(self, model: str, host: str | None = None) -> None:
        self.model = model
        self.host = host
        self._client = ollama.Client(host=host) if host else ollama.Client()

    def generate(self, messages: list[Message]) -> str:
        response = self._client.chat(
            model=self.model,
            messages=[
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in messages
            ],
        )

        return response["message"]["content"]
