import spacy

nlp = spacy.load('de')
#print(nlp.vocab.vectors_length)

doc = nlp('katze')
print(doc.similarity(nlp("katzen")))

# show vectors
"""
for token in doc:
    print("{} : {}".format(token, token.vector[:3]))
"""

# Entity recognition
doc2 = nlp("Mein Freund Mike arbeitet seit 2009 bei Google.")

for ent in doc2.ents:
    print(ent.text, ent.label_)