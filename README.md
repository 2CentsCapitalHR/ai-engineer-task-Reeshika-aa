ADGM Compliance Document Reviewer 
 ADGM Compliance Document Reviewer — RAG + Groq
This project is a Retrieval-Augmented Generation (RAG) pipeline integrated with Groq LLM API for reviewing ADGM corporate documents.
It automatically downloads reference materials, builds a vector database, and analyzes uploaded documents for compliance issues — inserting inline comments in `.docx` files.


 Flowchart:
(Data Sources) → Download → Extract Text → Vector Database (Chroma)
(User Upload) → Extract Text → Chunk & Query Groq → LLM Analysis → Issues JSON + Comments → Reviewed DOCX + Metadata JSON → Download Results


 How It Works:
1. Extract Resource URLs from Data Sources.docx and Task.pdf.
2. Download & Parse (PDF/DOCX/HTML).
3. Create Vector Store with Chroma.
4. RAG Pipeline for retrieval + LLM analysis.
5. LLM detects jurisdiction errors, missing signatures, ambiguous clauses, non-compliance.
6. Annotated Output in reviewed DOCX with inline comments.


 Getting a Groq API Key:
1. Go to https://console.groq.com/keys
2. Sign in or create an account.
3. Create API Key.
4. Save it in `.env` file:
   GROQ_API_KEY=your_api_key_here


 Running the Project:
1. Install dependencies: pip install -r requirements.txt
2. Prepare reference data: python chroma_store.py
3. Run the review app: streamlit run app.py
4. Upload document → Get reviewed DOCX.


 Project Structure:
app.py              — Streamlit front-end
chroma_store.py     — Builds Chroma vector DB from reference docs
requirements.txt    — Python dependencies
Data Sources.docx   — Official ADGM links
notes.txt           — Development notes
.env                — API keys (ignored in Git)
vector_store/       — Vector DB storage (generated)
data/               — Raw, extracted, reviewed docs
