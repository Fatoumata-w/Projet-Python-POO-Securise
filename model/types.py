from dataclasses import dataclass
from datetime import datetime

@dataclass
class ParticipantItem:
    userId: int
    username: str
    isOnline: bool = False

@dataclass
class ConversationItem:
    content: str
    date: datetime
    username: str
    role: str
    userId: int

@dataclass
class RegisterResponse:
    success: bool = False
    message: str = ""