from pathlib import Path
import sys
import time
import tomli
from trankit import Pipeline

def read_source(name: str) -> str:
    with Path(__file__).parents[1].joinpath('source').joinpath(f'{name}.toml').open('rb') as f:
        return tomli.load(f)['text']

pipeline_start = time.perf_counter()
p = Pipeline('russian')
print(f'pipeline creation: {time.perf_counter() - pipeline_start} sec', file=sys.stderr)


doc_text = read_source('19410703_stalin_speech')

lemma_start = time.perf_counter()
lemmatized_doc = p.lemmatize(doc_text)
print(f'lemmatization: {time.perf_counter() - lemma_start} sec', file=sys.stderr)
for sentence in lemmatized_doc['sentences']:
    for token in sentence['tokens']:
        print(f"{token['text']}\t{token['lemma']}")
