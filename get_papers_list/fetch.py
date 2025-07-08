import requests
import logging
import xml.etree.ElementTree as ET
import re
from typing import List, Dict


def fetch_papers(query: str) -> List[Dict]:
    # Step 1: Search for paper IDs using esearch
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 50
    }
    search_resp = requests.get(search_url, params=params)
    search_resp.raise_for_status()
    ids = search_resp.json().get("esearchresult", {}).get("idlist", [])

    if not ids:
        logging.warning("No papers found for query.")
        return []

    # Step 2: Fetch details using efetch
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    fetch_resp = requests.get(fetch_url, params=fetch_params)
    fetch_resp.raise_for_status()

    return parse_pubmed_xml(fetch_resp.text)


def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        try:
            medline = article.find("MedlineCitation")
            article_info = medline.find("Article")
            pmid = medline.findtext("PMID")

            title = article_info.findtext("ArticleTitle", default="N/A")

            # Get publication date
            pub_date_elem = article_info.find(".//Journal/JournalIssue/PubDate")
            year = pub_date_elem.findtext("Year") if pub_date_elem is not None else "N/A"
            month = pub_date_elem.findtext("Month") if pub_date_elem is not None else ""
            day = pub_date_elem.findtext("Day") if pub_date_elem is not None else ""
            pub_date = f"{day} {month} {year}".strip()

            authors_data = []
            for author in article_info.findall(".//AuthorList/Author"):
                last = author.findtext("LastName", default="")
                fore = author.findtext("ForeName", default="")
                full_name = f"{fore} {last}".strip()

                affil_elem = author.find(".//AffiliationInfo/Affiliation")
                affiliation = affil_elem.text.strip() if affil_elem is not None else ""

                email_match = None
                if affiliation:
                    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", affiliation)
                    email_match = match.group(0) if match else None

                authors_data.append({
                    "name": full_name,
                    "affiliation": affiliation,
                    "email": email_match,
                })

            # Use the first email found as the corresponding author email (fallback logic)
            corresponding_email = next((a["email"] for a in authors_data if a["email"]), "")

            papers.append({
                "pubmed_id": pmid,
                "title": title,
                "pub_date": pub_date,
                "authors": authors_data,
                "corresponding_email": corresponding_email,
            })

        except Exception as e:
            logging.warning(f"Error parsing article: {e}")
            continue

    return papers
