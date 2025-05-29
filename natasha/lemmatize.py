import natasha
from pathlib import Path
import sys
import time
import tomllib

def read_source(name: str) -> str:
    with Path(__file__).parents[1].joinpath('source').joinpath(f'{name}.toml').open('rb') as f:
        return tomllib.load(f)['text']

start = time.perf_counter()
emb = natasha.NewsEmbedding()
morph_vocab = natasha.MorphVocab()
doc = natasha.Doc(read_source('19410703_stalin_speech'))
doc.segment(natasha.Segmenter())
doc.tag_morph(natasha.NewsMorphTagger(emb))
for token in doc.tokens:
    token.lemmatize(morph_vocab)
print(f'total: {time.perf_counter() - start} sec', file=sys.stderr)

for token in doc.tokens:
    print(f'{token.text}\t{token.lemma}')
