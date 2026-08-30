"""Small, testable scripting examples based on verified IT 140 exercises."""
from collections import Counter


def sort_tv_shows(lines: list[str]) -> list[tuple[int, str]]:
    """Parse `count,title`-style lines and sort by count, then title."""
    records = []
    for line in lines:
        parts = line.strip().split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError(f"Expected '<count> <title>': {line!r}")
        count = int(parts[0])
        if count < 0:
            raise ValueError("count cannot be negative")
        records.append((count, parts[1]))
    return sorted(records, key=lambda item: (item[0], item[1].casefold()))


def word_frequencies(words: list[str]) -> dict[str, int]:
    """Return case-insensitive word counts with stable lowercase keys."""
    return dict(sorted(Counter(word.strip().lower() for word in words if word.strip()).items()))


if __name__ == "__main__":
    print(word_frequencies("hello cat man hey dog boy Hello man".split()))
