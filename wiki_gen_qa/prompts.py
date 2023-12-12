# pylint: disable=line-too-long
FACT_SPLIT = "You are a Question-Answer annotator. Extract all individual facts out of this text. Don't include opinions. Return each claim as a short sentence on a new line with no delimiter.\n"
INPUT_PROMPT = "{query}"
QUESTION_GENERATION = "Given the following statement about {page_title}, generate a single sentence question that would be comprehensively answered by the following statement. \n"
