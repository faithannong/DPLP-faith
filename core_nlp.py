from pprint import pprint

import stanza
from stanza.server import CoreNLPClient

# stanza.install_corenlp()
# print("finished install corenlp")
# stanza.download_corenlp_models(model='english', version='4.1.0')
# print("finished downloading english model")

# -annotators tokenize,ssplit,pos,lemma,ner,parse -ssplit.eolonly -tokenize.whitespace true
text = "CMV: Religion is not violent or not violent, its followers are. this doesn't say anything about christianity"
text1 = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
with CoreNLPClient(
        annotators=['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse'],
        # properties={"ssplit.eolonly": True, "tokenize.whitespace": True},
        timeout=30000,
        memory='16G') as client:
    ann = client.annotate(text, output_format='xml')
    # ann1 = client.annotate(text1, output_format='xml')

# get the first sentence
pprint(ann)

# get the constituency parse of the first sentence
# constituency_parse = sentence.parseTree
# print(constituency_parse)
