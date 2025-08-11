import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

TEXT_DIR = "data/text"
META_FILE = "data/metadata.json"
CHROMA_DIR = "vector_store"

# Load metadata
with open(META_FILE, "r", encoding="utf-8") as f:
    metadata_records = json.load(f)

metadata_map = {
    os.path.basename(record["text_file"]): {
        "category": record["category"],
        "document_type": record["document_type"],
        "source_url": record["source_url"]
    }
    for record in metadata_records
}

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300,
    length_function=len
)

docs = []
metas = []
for file_name in os.listdir(TEXT_DIR):
    if file_name.endswith(".txt"):
        with open(os.path.join(TEXT_DIR, file_name), "r", encoding="utf-8") as f:
            chunks = text_splitter.split_text(f.read())
        for chunk in chunks:
            docs.append(chunk)
            metas.append(metadata_map.get(file_name, {}))

print(f"[INFO] Prepared {len(docs)} chunks.")

# Use Hugging Face embeddings (free, local)
embedding_fn = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_texts(
    texts=docs,
    embedding=embedding_fn,
    metadatas=metas,
    persist_directory=CHROMA_DIR
)

vectorstore.persist()
print(f"[DONE] Chroma DB saved to {CHROMA_DIR}")
