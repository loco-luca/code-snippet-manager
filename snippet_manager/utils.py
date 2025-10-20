from .storage import CodeSnippets
from dataclasses import asdict
from .manager import get_file_path
import uuid
import shutil


def data_formator(title, language, code):
    # turns dataclass obj into dictionary
    return asdict(
        CodeSnippets(
            id=str(uuid.uuid4()),
            title=title.strip(),
            language=language.strip(),
            code=code.strip(),
        )
    )


def data_generator_formatted(lang: str):
    # complies data into dictionary so the json can process it
    title = input("Enter snippet title: ").strip()
    language = lang.strip()
    code = input("Enter code snippet: ").strip()
    return data_formator(title, language, code)


def print_centered(text):
    width = shutil.get_terminal_size().columns
    for line in text.splitlines():
        print(line.center(width))
