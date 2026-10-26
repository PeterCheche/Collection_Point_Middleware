# Collection_Point_Middleware

## Setup
```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```

## Run
```
uvicorn app.main:app --reload
```
Docs: http://127.0.0.1:8000/docs#

## Test
```
pytest
```
