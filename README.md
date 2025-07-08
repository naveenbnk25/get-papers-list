# get-papers-list

A command-line Python tool to fetch PubMed research papers that include at least one author affiliated with a **pharmaceutical or biotech company**, and export the results to a CSV file.

---

## 🚀 Features

* Fetches papers from PubMed using its full query syntax
* Filters papers to include only those with at least one **non-academic author**
* Outputs results to **CSV** or prints them to the console
* Fully typed Python code with modular design
* Easily installable and runnable using **Poetry**

---

## 🛠️ Requirements

* Python 3.9 to 3.12
* [Poetry](https://python-poetry.org/docs/#installation)

---

## 📦 Installation

```bash
# Clone the repository
cd path/to/project-root

# Install dependencies
poetry install
```

---

## 🧪 Usage

Run from the project directory:

```bash
poetry run get-papers-list "your pubmed search query"
```

### Optional flags:

* `-f`, `--file`: Save results to a CSV file
* `-d`, `--debug`: Print debug information
* `-h`, `--help`: Show usage instructions

### Examples:

```bash
# Fetch and display results
poetry run get-papers-list "cancer immunotherapy"

# Save results to CSV
poetry run get-papers-list "covid vaccine" -f output.csv

# Enable debug mode
poetry run get-papers-list "drug discovery" --debug
```

### Windows (PowerShell example with full path to Poetry)

```powershell
# Navigate to your project folder
cd "C:\Users\Naveen B\OneDrive\Desktop\pubmed-fetcher"

# Basic query
& "C:\Users\Naveen B\AppData\Roaming\Python\Scripts\poetry" run get-papers-list "cancer immunotherapy"

# Save to CSV
& "C:\Users\Naveen B\AppData\Roaming\Python\Scripts\poetry" run get-papers-list "cancer immunotherapy" -f results.csv

# Debug mode
& "C:\Users\Naveen B\AppData\Roaming\Python\Scripts\poetry" run get-papers-list "cancer immunotherapy" --debug

```

---

## 📁 Project Structure

```
get_papers_list/
├── __main__.py         # CLI interface
├── fetch.py            # PubMed API + XML parsing
├── filter.py           # Author filtering logic
├── output.py           # CSV and console output
pyproject.toml          # Poetry config and CLI binding
README.md               # Project documentation
```

---

## 📚 Tools & Libraries Used

* [PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
* [Poetry](https://python-poetry.org/): Dependency and package management
* [requests](https://pypi.org/project/requests/): For HTTP calls
* [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html): For XML parsing

> Built with help from [ChatGPT](https://openai.com/chatgpt)

---

## 🧪 Bonus (Optional)

To install this CLI tool globally:

```bash
poetry build
pip install dist/get_papers_list-0.1.0-py3-none-any.whl
get-papers-list "vaccine trial" -f results.csv
```

---

## ✅ License

MIT License

---

## 🙋‍♂️ Author

Naveen B
[GitHub Profile](https://github.com/naveenbnk25/get-papers-list.git)
