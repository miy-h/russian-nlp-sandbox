from pathlib import Path
import stanza
import sys
import time
import tomllib

def read_source(name: str) -> str:
    with Path(__file__).parents[1].joinpath('source').joinpath(f'{name}.toml').open('rb') as f:
        return tomllib.load(f)['text']

pipeline_start = time.perf_counter()
nlp = stanza.Pipeline(lang='ru', processors='tokenize,pos,lemma')
print(f'pipeline creation: {time.perf_counter() - pipeline_start} sec', file=sys.stderr)

lemma_start = time.perf_counter()
doc = nlp(read_source('19410703_stalin_speech'))
print(f'lemmatization: {time.perf_counter() - lemma_start} sec', file=sys.stderr)

for sent in doc.sentences:
    for word in sent.words:
        print(f'{word.text}\t{word.lemma}')
