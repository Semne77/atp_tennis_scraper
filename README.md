# 🎾 ATP Tennis Scraper

![license](https://img.shields.io/badge/license-MIT-green) ![pypi](https://img.shields.io/pypi/v/atp-tennis-scraper)

ATP Tennis Scraper is a Python package that fetches and displays the top ATP-ranked players from the official [ATP Tour website](https://www.atptour.com/en/rankings/singles). The scraper extracts player rankings, names, points, age, and nationality.

---

## 📦 Installation

To install the package, simply run:

```bash
pip install atp-tennis-scraper
```

### Usage

To see top 10 curent tennis players:

```python
from atp_tennis_scraper import display_top_10

display_top_10()
```
## Running Tests

To run the tests locally:

1. Clone the repository:

```bash
git clone https://github.com/Semne77/atp_tennis_scraper.git
cd atp-tennis-scraper
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the tests from the **project root directory** (the folder containing `tests/` and `atp_tennis_scraper/`):

```bash
pytest -q
```

On the first run, HTTP responses will be recorded using VCR.  
Subsequent runs will replay recorded responses (no internet connection required).
