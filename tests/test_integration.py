# tests/test_integration.py
"""
Integration test using vcrpy.

What it tests:
- Runs the FULL pipeline: fetch rankings page -> parse -> fetch player details -> build list
- Asserts the first player's name is Carlos Alcaraz

How it works:
- First run records real HTTP responses into tests/cassettes/atp_rankings_integration.yaml
- Future runs replay the cassette (no internet needed, fast + deterministic)

Install deps:
    pip install pytest vcrpy
Run:
    pytest -q
"""

from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vcr
from atp_tennis_scraper.main import fetch_atp_rankings 


CASSETTE_DIR = Path(__file__).parent / "cassettes"
CASSETTE_DIR.mkdir(parents=True, exist_ok=True)

my_vcr = vcr.VCR(
    cassette_library_dir=str(CASSETTE_DIR),
    record_mode="once",  # record only if cassette doesn't exist; otherwise replay
    match_on=["method", "scheme", "host", "port", "path", "query"],
    decode_compressed_response=True,
    filter_headers=["authorization", "cookie"],  # avoid saving sensitive headers if any
)


@my_vcr.use_cassette("atp_rankings_integration.yaml")
def test_integration_first_player_is_alcaraz():
    players = fetch_atp_rankings()

    assert isinstance(players, list)
    assert len(players) >= 1

    first = players[0]
    assert "Name" in first

    # Your scraper returns full name in your output: "Carlos Alcaraz"
    assert first["Name"] == "Carlos Alcaraz"
