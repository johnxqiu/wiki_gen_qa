## Wikipedia QA Generation
`wiki_gen_qa` is a tool for generating questions and answer datasets from Wikipedia articles. It is intended to aid in the evaluation of Retrieval-Augmented Generation (RAG) based Question Answering systems.

The main runtime `run_qa_gen.py` takes a wikipedia article and parses the sentence in the article summary. Then for each grounding sentence, it uses GPT3.5 via the OpenAI API to generate a test question and a list of factual claims within that sentence. The generating prompt templates are a work in progress and can be improved over time.

The result is a `json` with the following schema:

### JSON Schema Documentation

| Field Name         | Type           | Description                                             | Example                                                  |
| ------------------ | -------------- | ------------------------------------------------------- | -------------------------------------------------------- |
| `id`               | int        | A unique identifier for the data object.                | 0                                                        |
| `original_sentence`| str         | Grounding Sentence from article Summary. | "Python is a high-level, general-purpose programming language." |
| `generated_question`| str        | A question generated based on the `original_sentence`.  | "What are the key characteristics of Python as a programming language?" |
| `generated_facts`  | List[str] | A list of granular facts extracted from the `original_sentence`. | ["Python is a high-level programming language." <br> "Python is a general-purpose programming language."] |


To obtain the detailed sections of a wikipedia article for retrieval, use the function `wiki_gen_qa.wiki_tools.get_wiki_article_sections`

### Quickstart:
- Obtain an OpenAI API key and set it as environment variable `OPENAI_API_KEY`
- Install [poetry](https://python-poetry.org/docs/#installation) for python dependency management.
- Clone this repo with `git clone https://github.com/johnxqiu/wiki_gen_qa.git`
- `cd` into this repo and install dependencies with `poetry install`
- Enter the poetry python environment with `poetry shell`
- Run the main script with `python run_qa_gen.py [wiki_article_name] [output_json_path]`. Output path is optional and defaults to `generated_qa.json`

Example for the wikipedia article on Python:

```
python run_qa_gen.py "Python (programming language)"
```
