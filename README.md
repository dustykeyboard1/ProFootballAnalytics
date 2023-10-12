# ProFootballAnalytics

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Class Responsibilities](#class-responsibilities)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

`ProFootballAnalytics` is a Python-based project designed to scrape, clean, analyze, and visualize data from Pro Football Reference. The project aims to provide valuable insights into player performance, team dynamics, and other football-related statistics.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ProFootballAnalytics.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ProFootballAnalytics
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

---

## Directory Structure

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

## Usage

Run the main script to execute the entire pipeline:

```bash
python main.py
```

---

## Class Responsibilities

- **WebScraper**: Scrapes data from Pro Football Reference.
  - Methods: `fetch_data()`, `parse_data()`
  
- **DataOrganizer**: Cleans and organizes the scraped data.
  - Methods: `clean_data()`, `organize_data()`
  
- **StatisticalTesting**: Runs statistical tests on the organized data.
  - Methods: `run_t_test()`, `run_anova()`, `run_correlation()`
  
- **Plotting**: Plots data and statistical results.
  - Methods: `plot_histogram()`, `plot_scatter()`, `plot_boxplot()`

---

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.