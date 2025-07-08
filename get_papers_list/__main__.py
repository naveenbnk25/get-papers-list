# get_papers_list/__main__.py

import argparse
import logging
from get_papers_list.fetch import fetch_papers
from get_papers_list.filter import filter_non_academic_authors
from get_papers_list.output import output_results

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors")
    parser.add_argument("query", help="PubMed query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    logging.debug("Fetching papers for query: %s", args.query)
    papers = fetch_papers(args.query)
    logging.debug("Fetched %d papers", len(papers))

    filtered = filter_non_academic_authors(papers)
    logging.debug("Filtered down to %d papers with non-academic authors", len(filtered))

    output_results(filtered, args.file)

if __name__ == "__main__":
    main()
