#!/usr/bin/env python3
"""Validate the public reproducibility package without study data."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "ARTIFACT_SHA256.txt"
TEXT_SUFFIXES = {".csv", ".json", ".md", ".txt", ".py", ".gitignore"}
FORBIDDEN_PATTERNS = {
    "absolute home path": re.compile("/" + "home/"),
    "local username": re.compile("khol" + "anaseem", re.IGNORECASE),
    "access token": re.compile(
        "(?:gh" + "p_|github" + "_pat_|AK" + "IA)[A-Za-z0-9_\\-]{8,}"
    ),
}
EXPECTED_CHECKPOINTS = {
    "VoxTell v1.1": "f45e61c34c56af7b71711a6de54e8414dbc4cb52441003894f3370ed68d8feaa",
    "SAT-Pro": "f9813a76196dbdd99d5c5d1d8c68bb413173b449c275dbf53b3cceece6707b19",
    "SegVol": "500f2758a8f989339b2b2baf09a819169bc87549795193d3cfe505726ac0b399",
    "Medical-SAM3": "31fd6a05995800dd1de888d71249d8357d0804a471266343f43d104eda49440e",
    "BiomedParse v2": "6ea0bee43b983a7490e0b48689add96440c4405ca4b50b9f2fe21d5d03fd9440",
}


def public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path != MANIFEST
        and not path.name.endswith(".pyc")
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for path in (ROOT / "configs").glob("*.json"):
        with path.open(encoding="utf-8") as handle:
            json.load(handle)

    with (ROOT / "provenance" / "checkpoints.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        rows = list(csv.DictReader(handle))
    observed = {row["model"]: row["checkpoint_sha256"] for row in rows}
    if observed != EXPECTED_CHECKPOINTS:
        fail("checkpoint table differs from the five directly verified digests")

    for path in (ROOT / "results").glob("*.csv"):
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        if len(rows) < 2:
            fail(f"aggregate table has no data rows: {path.relative_to(ROOT)}")

    for path in public_files():
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name != ".gitignore":
            continue
        text = path.read_text(encoding="utf-8", errors="strict")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(ROOT)}")

    expected_lines = [
        f"{sha256(path)}  ./{path.relative_to(ROOT).as_posix()}" for path in public_files()
    ]
    if not MANIFEST.exists():
        fail("ARTIFACT_SHA256.txt is missing")
    observed_lines = [line for line in MANIFEST.read_text().splitlines() if line]
    if observed_lines != expected_lines:
        fail("ARTIFACT_SHA256.txt is stale; regenerate it before release")

    print(
        f"Release validation passed: {len(public_files())} files, "
        f"{len(rows)} rows in final aggregate table, five checkpoint digests."
    )


if __name__ == "__main__":
    main()
