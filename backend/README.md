# Backend Setup

## 1. Create virtual environment
```bash
python -m venv .venv
```

## 2. Activate it

Windows
```bash
.venv\Scripts\activate
```
Linux/Mac
```bash
source .venv/bin/activate
```

## 3. Install dependencies
```bash
pip install -r backend/requirements.txt
```

## 4. Environment variables

Create a file .env in the backend directory based on .env.example.


## 5. Run FastAPI (later)
```bash
uvicorn main:app --reload
```

