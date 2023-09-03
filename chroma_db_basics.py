# export HNSWLIB_NO_NATIVE = 1 bash
# Set-Item -Path Env:HNSWLIB_NO_NATIVE -Value 1 powershells

import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=[" my name is salim", "my name is not know"],
    metadatas=[{"source": "name is true"}, {"source": "name is false"}],
    ids=["id1", "id2"],
)

results = collection.query(
    query_texts=["what is my name ?"],
    n_results=1
)

print(results)
