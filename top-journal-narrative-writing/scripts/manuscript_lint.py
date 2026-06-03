#!/usr/bin/env python3
"""Basic manuscript narrative lint for Markdown/plain-text files.

This script performs lightweight checks only. It does not judge scientific validity.
It uses Python's standard library and makes no network calls.

Usage:
    python scripts/manuscript_lint.py manuscript.md
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from statistics import mean

HYPE_WORDS = {
    "groundbreaking", "revolutionary", "paradigm", "unprecedented", "novel",
    "first", "prove", "proves", "proved", "proven", "transformative", "unique",
    "remarkable", "dramatic", "robust", "significant", "significantly",
}

VAGUE_WORDS = {
    "important", "interesting", "various", "several", "many", "substantial",
    "considerable", "highly", "clearly", "obviously", "some", "numerous",
    "potentially", "broadly", "notably",
}

SECTION_PATTERNS = [
    "abstract", "summary", "introduction", "results", "methods", "materials and methods",
    "discussion", "conclusion", "references", "acknowledgements", "data availability",
    "code availability", "competing interests", "author contributions",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_sentences(text: str) -> list[str]:
    # Conservative sentence splitter for English manuscripts. Chinese manuscripts will still get word/section checks.
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", cleaned)
    return [p.strip() for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9\-']*", text.lower())


def find_sections(text: str) -> list[str]:
    found = []
    lines = text.splitlines()
    for line in lines:
        normalized = re.sub(r"^[#\s\d.:-]+", "", line.strip().lower())
        normalized = re.sub(r"\s+", " ", normalized)
        if normalized in SECTION_PATTERNS:
            found.append(normalized)
    return found


def count_figures(text: str) -> Counter[str]:
    matches = re.findall(r"\b(?:Fig\.?|Figure)\s*(\d+[A-Za-z]?)", text, flags=re.IGNORECASE)
    return Counter(matches)


def find_flagged_terms(tokens: list[str], terms: set[str]) -> Counter[str]:
    return Counter(t for t in tokens if t in terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="Basic manuscript narrative lint")
    parser.add_argument("file", type=Path, help="Markdown or plain-text manuscript")
    parser.add_argument("--long-sentence", type=int, default=40, help="Word threshold for long English sentences")
    args = parser.parse_args()

    if not args.file.exists():
        raise SystemExit(f"File not found: {args.file}")

    text = read_text(args.file)
    token_list = words(text)
    sentences = split_sentences(text)
    sentence_lengths = [len(words(s)) for s in sentences if words(s)]
    long_sentences = [(i + 1, s, len(words(s))) for i, s in enumerate(sentences) if len(words(s)) > args.long_sentence]
    sections = find_sections(text)
    figures = count_figures(text)
    hype = find_flagged_terms(token_list, HYPE_WORDS)
    vague = find_flagged_terms(token_list, VAGUE_WORDS)

    print("# Manuscript Lint Report")
    print()
    print(f"File: `{args.file}`")
    print(f"Approx. English word count: {len(token_list)}")
    print(f"Approx. sentence count: {len(sentences)}")
    if sentence_lengths:
        print(f"Average sentence length: {mean(sentence_lengths):.1f} words")
        print(f"Long sentences > {args.long_sentence} words: {len(long_sentences)}")
    print()

    print("## Detected sections")
    if sections:
        for s in sections:
            print(f"- {s}")
    else:
        print("- No standard section headings detected. This may be fine for non-IMRaD formats, but check navigation.")
    print()

    print("## Figure callouts")
    if figures:
        for fig, count in sorted(figures.items(), key=lambda item: item[0]):
            print(f"- Figure {fig}: {count} callout(s)")
    else:
        print("- No figure callouts detected. If this is a research article, verify figure-driven flow.")
    print()

    print("## Potentially inflated or risky terms")
    if hype:
        for term, count in hype.most_common():
            print(f"- {term}: {count}")
    else:
        print("- None detected from the built-in list.")
    print()

    print("## Potentially vague terms")
    if vague:
        for term, count in vague.most_common(20):
            print(f"- {term}: {count}")
    else:
        print("- None detected from the built-in list.")
    print()

    if long_sentences:
        print("## Long sentence samples")
        for idx, sentence, length in long_sentences[:10]:
            print(f"- Sentence {idx} ({length} words): {sentence[:300]}{'...' if len(sentence) > 300 else ''}")
        print()

    print("## Reminder")
    print("This lint report flags style and structure signals only. It cannot verify novelty, data quality, statistics, or journal policy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
