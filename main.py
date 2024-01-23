# just a simple test for now.

from serpapi import GoogleSearch

params = {
  "q": "PI",
  "hl": "en",
  "gl": "us",
  "api_key": "secret_api_key"
}

search = GoogleSearch(params)
results = search.get_dict()
answer_box = results["answer_box"]
