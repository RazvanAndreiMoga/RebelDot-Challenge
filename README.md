# Semantic FAQ Assistant (FastAPI)

A simple FAQ assistant that matches user questions to a local FAQ database using string similarity. Works offline.

## Requirements
- Python 3.10+
- PostgreSQL
- `pip` packages (install via `requirements.txt`)

## Setup
1. Clone repo and enter directory:
```bash
git clone <repo-url>
cd RebelDot
```

2. Create and activate virtual environment:
```bash
python -m venv venv
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure .env with your DB URL, e.g.:
```bash
DATABASE_URL=postgresql+psycopg2://postgres:admin@localhost:5432/faqdb
```

5. Seed the FAQ database:
```bash
python -m scripts.seed_faq
```

6. Run the App
```bash
uvicorn app.main:app --reload
```

API available at http://127.0.0.1:8000

7. Test the API
PowerShell example:

```bash
$body = @{ "user_question" = "How do I reset my password?" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask-question" `
    -Method POST `
    -Headers @{ "Content-Type" = "application/json"; "X-Token" = "supersecret" } `
    -Body $body

Expected response:
{
    "source": "local",
    "matched_question": "What steps do I take to reset my password?",
    "answer": "Go to account settings, select 'Change Password', enter your current password and then the new one. Confirm the new password and save the changes."
}
```

