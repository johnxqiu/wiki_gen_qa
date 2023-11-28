"""Module for QA generation from string data"""
from typing import List

from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain_core.language_models.chat_models import BaseChatModel

FACT_SPLIT_TEMPLATE = "Extract the individual facts out of this text. Don't \
    include opinions. Return each claim on a new line with no header and keep \
        them short sentences.\n"
INPUT_QUERY_TEMPLATE = "{query}"
QUESTION_GENERATION_TEMPLATE = "Given the following claim about {page_title}, \
    generate a single sentence question that comprehensively answers the \
        following statement. \n"

fact_split_instruction_template = SystemMessagePromptTemplate.from_template(
    FACT_SPLIT_TEMPLATE
)
query_template = HumanMessagePromptTemplate.from_template(INPUT_QUERY_TEMPLATE)


def get_facts_from_sentence(in_query: str, in_chat: BaseChatModel) -> List[str]:
    fact_splitting_prompt = ChatPromptTemplate.from_messages(
        [FACT_SPLIT_TEMPLATE, query_template]
    )
    response = in_chat(
        fact_splitting_prompt.format_prompt(query=in_query).to_messages()
    )
    return response.content.split("\n")


def get_question_from_sentence(
    in_page_title: str, in_test_sentence: str, in_chat: BaseChatModel
) -> str:
    question_generating_prompt = ChatPromptTemplate.from_messages(
        [QUESTION_GENERATION_TEMPLATE, INPUT_QUERY_TEMPLATE]
    )
    response = in_chat(
        question_generating_prompt.format_prompt(
            page_title=in_page_title, query=in_test_sentence
        ).to_messages()
    )
    return response.content
