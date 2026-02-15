# tests/test_unit.py

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import vcr
from bs4 import BeautifulSoup

from atp_tennis_scraper.main import (
    fetch_rankings_html,
    parse_rankings_html,
    fetch_player_details
)

# Folder where VCR saves recordings
CASSETTE_DIR = Path(__file__).parent / "cassettes"
CASSETTE_DIR.mkdir(parents=True, exist_ok=True)

my_vcr = vcr.VCR(
    cassette_library_dir=str(CASSETTE_DIR),
    record_mode="once",  # record first time, replay after
    match_on=["method", "scheme", "host", "port", "path", "query"],
    decode_compressed_response=True,
)


# ---------------------------------------------------
# UNIT TEST 1
# Page fetched contains a <table> element
# ---------------------------------------------------
@my_vcr.use_cassette("unit_fetch_page.yaml")
def test_fetch_rankings_html_contains_table():
    html = fetch_rankings_html()
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")
    assert table is not None


# ---------------------------------------------------
# UNIT TEST 2
# parse_rankings_html returns 10 rows
# ---------------------------------------------------
@my_vcr.use_cassette("unit_parse_rows.yaml")
def test_parse_rankings_html_returns_10_rows():
    html = fetch_rankings_html()
    trs = parse_rankings_html(html, limit=10)

    assert len(trs) == 10


# ---------------------------------------------------
# UNIT TEST 3
# fetch_player_details returns JSON with Age and Nationality
# ---------------------------------------------------
@my_vcr.use_cassette("unit_player_details.yaml")
def test_fetch_player_details_returns_age_and_nationality():
    # Use known player id for Carlos Alcaraz
    # Profile link looks like:
    # /en/players/carlos-alcaraz/a0e2/overview
    # So player_id = "a0e2"
    player_id = "a0e2"

    data = fetch_player_details(player_id)

    assert isinstance(data, dict)
    assert "Age" in data
    assert "Nationality" in data

    assert data["Age"] is not None
    assert data["Nationality"] is not None
