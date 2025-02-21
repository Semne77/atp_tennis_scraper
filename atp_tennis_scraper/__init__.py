from bs4 import BeautifulSoup
import requests


"""
ATP Tennis Scraper package
"""

__version__ = "0.1.0"

from .main import fetch_atp_rankings, display_top_10

# Expose functions for direct import
__all__ = ["fetch_atp_rankings", "display_top_10"]

