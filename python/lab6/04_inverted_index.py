# Inverted index
docs = {1: "python is easy", 2: "python is useful"}
index = {}

for doc_id, text in docs.items():
    for word in text.split():
        index.setdefault(word, []).append(doc_id)

word = input("Search word: ").lower()
print(index.get(word, []))
