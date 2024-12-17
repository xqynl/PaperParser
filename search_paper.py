import requests
import json

S2_API_KEY = "your_api_key_here"

def search_for_llm_papers(query, result_limit=10):
    if not query:
        print("Query is empty.")
        return None

    try:
        rsp = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            headers={"X-API-KEY": S2_API_KEY},
            params={
                "query": query,
                "limit": result_limit,
                "fields": "title,authors,venue,year,abstract,citationStyles,citationCount",
            },
        )

        print(f"Response Status Code: {rsp.status_code}")
        print(f"Response Content: {rsp.text[:500]}")

        rsp.raise_for_status()

        results = rsp.json()
        total = results["total"]
        if not total:
            print("No papers found.")
            return None

        papers = results["data"]
        return papers

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def main():
    query = "large language model"
    papers = search_for_llm_papers(query, result_limit=5)

    if papers:
        print(f"Found {len(papers)} papers:")
        for i, paper in enumerate(papers):
            print(f"\nPaper {i + 1}:")
            print(f"Title: {paper['title']}")
            print(f"Authors: {paper['authors']}")
            print(f"Venue: {paper['venue']}")
            print(f"Year: {paper['year']}")
            print(f"Abstract: {paper['abstract']}")
            print(f"Citation Count: {paper['citationCount']}")
            print(f"Citation Styles: {json.dumps(paper['citationStyles'], indent=2)}")
    else:
        print("No papers found.")


if __name__ == '__main__':
    main()
