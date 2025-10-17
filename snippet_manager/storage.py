# storage
from dataclasses import dataclass


@dataclass
class CodeSnippets:
    id: str
    title: str
    language: str
    code: str
