from dataclasses import dataclass
from datetime import datetime

@dataclass
class ParticipantItem:
    userId: int
    username: str

@dataclass
class ConversationItem:
    content: str
    date: datetime
    username: str
    role: str
    userId: int