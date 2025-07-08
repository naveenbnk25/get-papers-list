# get_papers_list/filter.py

from typing import List, Dict
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = [
        "university", "college", "institute", "school", "faculty", "department", "centre", "center", "hospital"
    ]
    return not any(kw in affiliation.lower() for kw in academic_keywords)

def extract_non_academic_authors(authors: List[Dict]) -> List[Dict]:
    non_academics = []
    for author in authors:
        affil = author.get("affiliation", "")
        if is_non_academic(affil):
            non_academics.append({
                "name": author.get("name"),
                "affiliation": affil
            })
    return non_academics

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    results = []
    for paper in papers:
        non_academics = extract_non_academic_authors(paper.get("authors", []))
        if non_academics:
            results.append({
                "PubmedID": paper.get("pubmed_id"),
                "Title": paper.get("title"),
                "Publication Date": paper.get("pub_date"),
                "Non-academic Author(s)": ", ".join(a["name"] for a in non_academics),
                "Company Affiliation(s)": ", ".join(a["affiliation"] for a in non_academics),
                "Corresponding Author Email": paper.get("corresponding_email", "")
            })
    return results
