from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict

class CrawlRequest(BaseModel):
    url: HttpUrl

class ChatMessage(BaseModel):
    role: str
    content: str
    refusal: Optional[str] = None

class Choice(BaseModel):
    index: int
    message: ChatMessage
    logprobs: Optional[str] = None
    finish_reason: str

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class GPTResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage
    system_fingerprint: Optional[str] = None

class CrawlResponse(BaseModel):
    url: str
    data: GPTResponse