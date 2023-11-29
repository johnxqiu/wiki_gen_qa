"""Runs the wikipedia article QA generation pipeline"""
import argparse
import json
import os
from typing import List

from langchain.chat_models.openai import ChatOpenAI

from wiki_gen_qa.generate_qa import get_facts_from_sentence, get_question_from_sentence
from wiki_gen_qa.wiki_tools import get_wikipedia_summary_sentences


def get_wiki_article_qa(wiki_article_name: str) -> List[dict]:
    assert os.environ["OPENAI_API_KEY"] is not None
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    summary_sentence_list = get_wikipedia_summary_sentences(wiki_article_name)
    out_generated_data = []
    print(f'Wikpiedia page for "{wiki_article_name}" found!')
    print(f"Generating QA for {len(summary_sentence_list)} sentences...")
    for ith_sentence, summary_sentence in enumerate(summary_sentence_list):
        generated_question = get_question_from_sentence(
            wiki_article_name, summary_sentence, chat
        )
        generated_facts = get_facts_from_sentence(summary_sentence, chat)
        generated_question = get_question_from_sentence(
            wiki_article_name, summary_sentence, chat
        )
        out_generated_data.append(
            {
                "id": ith_sentence,
                "original_sentence": summary_sentence,
                "generated_question": generated_question,
                "generated_facts": generated_facts,
            }
        )
    return out_generated_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a Wikipedia article")
    parser.add_argument(
        "wiki_article_name", type=str, help="Name of the Wikipedia article"
    )
    parser.add_argument(
        "-o", type=str, default="generated_qa.json", help="Path to output JSON file"
    )
    args = parser.parse_args()
    generated_data = get_wiki_article_qa(args.wiki_article_name)
    with open(args.o, "w", encoding="utf-8") as f:
        json.dump(generated_data, f, indent=4)
    print(
        f"Successfully generated QA for {args.wiki_article_name} and saved to {args.o}!"
    )
