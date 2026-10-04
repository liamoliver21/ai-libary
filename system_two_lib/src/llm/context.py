from __future__ import annotations

from abc import ABC, abstractmethod

from .history import ConversationHistory
from .message import Message


class ContextManager(ABC):
    """Chooses which stored messages should be sent to the backend."""

    @abstractmethod
    def build(self, history: ConversationHistory) -> list[Message]:
        raise NotImplementedError


class RecentContextManager(ContextManager):
    """Returns the most recent N messages."""

    def __init__(self, count: int = 10) -> None:
        if count < 0:
            raise ValueError("count must be >= 0")
        self.count = count

    def build(self, history: ConversationHistory) -> list[Message]:
        return history.recent(self.count)
