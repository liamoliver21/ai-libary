from __future__ import annotations

from abc import ABC, abstractmethod

from .message import Message


class LLMBackend(ABC):
    """Provider/model abstraction used by LLMConversation."""

    @abstractmethod
    def generate(self, messages: list[Message]) -> str:
        """Generate an assistant response from the supplied messages."""
        raise NotImplementedError
