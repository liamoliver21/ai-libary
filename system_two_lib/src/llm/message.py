from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


@dataclass(frozen=True, slots=True)
class Message:
    role: Role
    content: str
    timestamp: datetime

    @classmethod
    def create(cls, role: Role, content: str) -> "Message":
        if not isinstance(content, str):
            raise TypeError("content must be a string")

        return cls(
            role=role,
            content=content,
            timestamp=datetime.now(timezone.utc),
        )
