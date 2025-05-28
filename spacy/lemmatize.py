from pathlib import Path
import spacy
import tomllib

def read_source(name: str) -> str:
    with Path(__file__).parents[1].joinpath('source').joinpath(f'{name}.toml').open('rb') as f:
        return tomllib.load(f)['text']

nlp = spacy.load('ru_core_news_sm')
doc = nlp('Он не знает ни одного поражения.')
for w in doc:
    print(f'{w.text}\t{w.lemma_}')
