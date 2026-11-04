
# AI Document Intelligence Assistant

Multimodal document ingestion, search, analysis, and workspace application.

## Run locally

1. Copy `.env.example` to `.env` and replace the example secrets.
2. Start the development stack: `docker compose up --build`.
3. Open the frontend at `http://localhost:3000`; the API health endpoint is at `http://localhost:8000/health`.

For direct development, run `npm install && npm run dev` in `frontend`, and create a Python environment in `backend` before installing its dependencies.

PostgreSQL runs from the `pgvector/pgvector:pg16` image. The `vector` extension is enabled automatically the first time its data volume is initialized.
