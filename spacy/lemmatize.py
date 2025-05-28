from pathlib import Path
import spacy
import sys
import time
import tomllib

def read_source(name: str) -> str:
    with Path(__file__).parents[1].joinpath('source').joinpath(f'{name}.toml').open('rb') as f:
        return tomllib.load(f)['text']

load_start = time.perf_counter()
nlp = spacy.load('ru_core_news_sm')
print(f'model loading: {time.perf_counter() - load_start} sec', file=sys.stderr)

lemma_start = time.perf_counter()
# doc = nlp('Он не знает ни одного поражения.')
doc = nlp(read_source('19410703_stalin_speech'))
print(f'lemmatization: {time.perf_counter() - lemma_start} sec', file=sys.stderr)

for w in doc:
    print(f'{w.text}\t{w.lemma_}')
