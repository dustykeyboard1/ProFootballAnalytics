# ProFootballAnalytics

## Quick Links

- [Overview](#overview)
- [Setup](#setup)
- [File Structure](#file-structure)
- [How to Use](#how-to-use)
- [Classes & Methods](#classes--methods)
- [Contribute](#contribute)
- [License](#license)

---

## Overview

`ProFootballAnalytics` is a Python project for scraping and analyzing Pro Football Reference data. Gain insights into player stats, team performance, and more.

---

## Setup

1. Clone repo: `git clone https://github.com/yourusername/ProFootballAnalytics.git`
2. Go to directory: `cd ProFootballAnalytics`
3. Install packages: `pip install -r requirements.txt`

---

## File Structure

```
ProFootballAnalytics/
|-- main.py
|-- README.md
|-- requirements.txt
|
|-- WebScraper/
|-- DataOrganizer/
|-- StatisticalTesting/
|-- Plotting/
|-- Utils/
|-- Tests/
```

---

## How to Use

Run `python main.py` to start the pipeline.

---

## Classes & Methods

- **WebScraper**: `fetch_data()`, `parse_data()`
- **DataOrganizer**: `clean_data()`, `organize_data()`
- **StatisticalTesting**: `run_t_test()`, `run_anova()`, `run_correlation()`
- **Plotting**: `plot_histogram()`, `plot_scatter()`, `plot_boxplot()`

---

## Contribute

1. Fork repo
2. Create branch
3. Make changes
4. Open PR

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

MIT License. See [LICENSE.md](LICENSE.md).