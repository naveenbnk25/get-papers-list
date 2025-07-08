import csv
import sys
from typing import List, Dict


def output_results(results: List[Dict], filename: str = None) -> None:
    if not results:
        print("No matching papers found.")
        return

    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email"
    ]

    if filename:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        print(f"✅ Results written to '{filename}'")
    else:
        # Print to console
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
