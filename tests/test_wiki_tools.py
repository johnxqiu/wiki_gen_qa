"""Tests for wiki_gen_qa.wiki_tools"""
from wiki_gen_qa.wiki_tools import try_get_wikipedia_page, split_str_to_sentences


def test_wiki_tools():
    test_page_name = "Python (programming language)"
    page = try_get_wikipedia_page(test_page_name)
    text = page.summary

    assert page.title == test_page_name

    sentences = split_str_to_sentences(text)
    # Process the text
    # Split the document into sentences - check that the first two sentences are correct
    print(sentences[0])
    correct_sents = 'Python is a high-level, general-purpose programming language.'
    assert sentences[0] == correct_sents

