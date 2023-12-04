"""code for getting data from using wikipedia-api"""

import spacy
import wikipediaapi

USER_AGENT = "MyProjectName (merlin@example.com)"

NLP = spacy.load("en_core_web_sm")


def split_str_to_sentences(text: str) -> list[str]:
    # Process the text
    doc = NLP(text)
    # Split the document into sentences
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences


def try_get_wikipedia_page(in_page_name: str) -> wikipediaapi.WikipediaPage:
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent=USER_AGENT,
        language="en",
        extract_format=wikipediaapi.ExtractFormat.WIKI,
    )
    assert wiki_wiki.page(in_page_name).exists()
    return wiki_wiki.page(in_page_name)


def get_wikipedia_summary_sentences(in_page: wikipediaapi.WikipediaPage) -> list[str]:
    summary_sentences = split_str_to_sentences(in_page.summary)
    return summary_sentences


def get_wikipedia_content(in_page: wikipediaapi.WikipediaPage) -> str:
    sections = in_page.sections
    out_content = ""
    for section in sections:
        out_content += section.title + "\n" + section.text + "\n"
    return out_content
