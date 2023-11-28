"""code for getting data from using wikipedia-api"""
from typing import List

import nltk
import wikipediaapi
from nltk.tokenize import sent_tokenize

USER_AGENT = "MyProjectName (merlin@example.com)"
nltk.download("punkt")


def try_get_wikipedia_page(in_page_name: str) -> wikipediaapi.WikipediaPage:
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent=USER_AGENT,
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI,
    )
    assert wiki_wiki.page(in_page_name).exists()
    return wiki_wiki.page(in_page_name)


def get_wikipedia_summary_sentences(in_page_name: str) -> List[str]:
    wiki_page = try_get_wikipedia_page(in_page_name)
    summary_sentences = sent_tokenize(wiki_page.summary)
    return summary_sentences


def get_wikipedia_content(in_page_name: str) -> str:
    wiki_page = try_get_wikipedia_page(in_page_name)
    sections = wiki_page.sections
    out_content = ""
    for section in sections:
        out_content += section.title + "\n" + section.text + "\n"
    return out_content
