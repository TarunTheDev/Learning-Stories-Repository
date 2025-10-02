"""
story_summary_extractor.py

Given a “learning story” (text), this script extracts a short summary
using a simple heuristic: first, middle, last sentences.

Useful for making previews / cards on web UI for stories.
"""

import re
from typing import List

def split_into_sentences(text: str) -> List[str]:
    # naive split by periods, exclamation, question marks
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s for s in sentences if s]

def extract_summary(text: str, max_sentences: int = 3) -> str:
    """
    Return up to `max_sentences` as a summary by selecting:
        first sentence, middle sentence(s), last sentence.
    """
    sentences = split_into_sentences(text)
    n = len(sentences)
    if n <= max_sentences:
        return " ".join(sentences)

    summary = [sentences[0]]
    if max_sentences >= 3:
        mid = sentences[n // 2]
        summary.append(mid)
    if max_sentences >= 2:
        summary.append(sentences[-1])
    return " ".join(summary[:max_sentences])


# Demo / test
if __name__ == "__main__":
    story = (
        "I started my career in engineering after college. "
        "At first I faced many challenges. "
        "I learned persistence, made mistakes, and grew. "
        "Now I mentor younger engineers and enjoy sharing knowledge."
    )
    print("Full story:", story)
    print("Summary:", extract_summary(story, max_sentences=3))
