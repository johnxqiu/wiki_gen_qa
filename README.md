## Wikipedia QA Generation
`wiki_gen_qa` is a tool for generating questions and answer datasets from Wikipedia articles. It is intended to aid in the evaluation of Retrieval-Augmented Generation (RAG) based Question Answering systems.

The main call takes a wikipedia article, parses only the summary section and performs sentence segmentation with spacy. Then for each summary sentence, it uses GPT via the OpenAI API to generate a test question a list of factual claims within that sentence. The generating prompts are a work in progress and can be improved over time.

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
