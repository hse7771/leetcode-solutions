import os
import re
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple


@dataclass
class ProblemEntry:
    number: str
    title: str
    folder: str
    difficulty: str
    langs: Set[str]


# Map file extensions to a human-readable language name
EXT_TO_LANG: Dict[str, str] = {
    ".py": "Python",
    ".cpp": "C++",
}


def scan_difficulty(readme_path: str, max_lines: int = 20) -> str:
    if not os.path.exists(readme_path):
        return ""

    with open(readme_path, encoding="utf8") as f:
        for _ in range(max_lines):
            line = f.readline()
            if not line:
                break  # EOF
            if "difficulty:" in line.lower():
                diff_raw = line.split(":")[1]
                return diff_raw.split("**")[1].strip()
    return ""  # default if not found


def detect_languages(folder: str) -> Set[str]:
    langs: Set[str] = set()
    for f_name in os.listdir(folder):
        root, ext = os.path.splitext(f_name)
        if not root.startswith("solution"):
            continue
        lang = EXT_TO_LANG.get(ext.lower())
        if lang:
            langs.add(lang)
    return langs


def get_problems() -> Tuple[List[ProblemEntry], List[str]]:
    problems: List[ProblemEntry] = []
    global_langs: Set[str] = {"Python"}
    for folder in sorted(os.listdir(".")):
        if not re.match(r"\d{4}-", folder):
            continue

        number, name = folder.split('-', 1)
        readme_path = os.path.join(folder, "README.md")
        difficulty = scan_difficulty(readme_path)
        langs = detect_languages(folder)
        global_langs.update(langs)

        problems.append(
            ProblemEntry(
                number=number,
                title=name.replace("-", " ").title(),
                folder=folder,
                difficulty=difficulty,
                langs=langs,
            )
        )
    return problems, sorted(global_langs)


def generate_index_md(problems: List[ProblemEntry], languages: List[str]) -> str:
    lang_headers = " | ".join(languages)
    header = f"| Number | Problem | Difficulty | {lang_headers} |"
    sep = "|" + "--------|" * (3 + len(languages))

    lines = [header, sep]
    for p in problems:
        marks = ["✔️" if lang in p.langs else "" for lang in languages]
        lang_cells = " | ".join(marks)
        lines.append(
            f"| {p.number} | [{p.title}](./{p.folder}/) | {p.difficulty} | {lang_cells} |"
        )

    return "\n".join(lines)


def update_readme(readme_path: str = "README.md") -> None:
    with open(readme_path, encoding='utf8') as f:
        content = f.read()
    problems, languages = get_problems()
    new_index = generate_index_md(problems, languages)

    # Insert or replace the index section
    pattern = re.compile(
        r"(## 📋 Index\n\n<details>[\s\S]*?<summary>Click to expand problem index</summary>\n\n)([\s\S]*?)(</details>)",
        re.MULTILINE)
    match = pattern.search(content)
    if match:
        start, _, end = match.groups()
        new_content = pattern.sub(f"{start}{new_index}\n\n{end}", content)
    else:
        new_content = content

    with open(readme_path, 'w', encoding='utf8') as f:
        f.write(new_content)


if __name__ == "__main__":
    update_readme()
