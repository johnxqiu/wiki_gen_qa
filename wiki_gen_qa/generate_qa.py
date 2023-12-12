"""Module for QA generation from string data"""
from typing import List

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.chat_models.base import BaseChatModel
from wiki_gen_qa.prompts import (FACT_SPLIT, INPUT_PROMPT, QUESTION_GENERATION)

fact_split_template = SystemMessagePromptTemplate.from_template(
    FACT_SPLIT
)

question_generation_template = SystemMessagePromptTemplate.from_template(
    QUESTION_GENERATION
)

input_template = HumanMessagePromptTemplate.from_template(INPUT_PROMPT)

def get_facts_from_sentence(in_query: str, in_chat: BaseChatModel) -> List[str]:
    fact_splitting_prompt = ChatPromptTemplate.from_messages(
        [fact_split_template, input_template]
    )
    response = in_chat(
        fact_splitting_prompt.format_prompt(query=in_query).to_messages()
    )
    return response.content.split("\n")


def get_question_from_sentence(
    in_page_title: str, in_test_sentence: str, in_chat: BaseChatModel
) -> str:
    question_generating_prompt = ChatPromptTemplate.from_messages(
        [question_generation_template, input_template]
    )
    response = in_chat(
        question_generating_prompt.format_prompt(
            page_title=in_page_title, query=in_test_sentence
        ).to_messages()
    )
    return response.content


def get_wiki_article_qa_facts(
    sent_id: int,
    wiki_article_name: str,
    summary_sentence: str,
    chat: BaseChatModel,
) -> List[dict]:
    generated_question = get_question_from_sentence(
        wiki_article_name, summary_sentence, chat
    )
    generated_facts = get_facts_from_sentence(summary_sentence, chat)
    generated_question = get_question_from_sentence(
        wiki_article_name, summary_sentence, chat
    )
    return {
        "sent_id": sent_id,
        "original_sentence": summary_sentence,
        "generated_question": generated_question,
        "generated_facts": generated_facts,
    }
