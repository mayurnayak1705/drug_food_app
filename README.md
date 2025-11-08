🚀 Drug–Food Interaction App

Link to webapp: https://lnkd.in/gtAn3Jmn

I recently built an AI-powered Drug–Food Interaction App that analyzes how different medicines interact with various foods — identifying what’s safe to consume and what should be avoided during a specific medication cycle.

Many people are unaware that certain foods can alter how medicines work in the body — reducing their effectiveness or even causing side effects. This project aims to make that knowledge easily accessible through an intelligent web interface.

Workflow:

1. User enters a medicine name (e.g., DOLO 650).

2. The app fetches and analyzes its active ingredients - entitiy extraction using LLM call.

3. Once the entity is extracted , search the database for the drug-food interaction

4. AI models identify food interactions, classifying them as:

- Safe to consume
- To be avoided
- Neutral

The output provides clear dietary recommendations and explanations.


Framework & Technologies Used

Python (FastAPI) – backend and API framework

OpenAI GPT models – for contextual analysis of drug compositions and food interactions

Docker – containerized deployment

Google Cloud Platform (GCP) – hosting and deployment using Cloud Run, Artifact Registry, and Container Registry

HTML/CSS/JS – frontend interface

Uvicorn – lightweight ASGI serv
