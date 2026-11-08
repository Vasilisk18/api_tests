# api_tests
# API Tests: JSONPlaceholder

Automated API tests for the public REST service
[JSONPlaceholder](https://jsonplaceholder.typicode.com).

## Tech stack
- Python 3
- pytest
- requests

## What is tested
- GET: single post, non-existent post (404), posts filtered by user
- POST: create a post (201)
- PUT / PATCH: full and partial update
- DELETE: delete a post

## Project structure
```
tests/
├── conftest.py      # shared fixtures (base_url, session)
└── test_posts.py    # API tests
```

## Installation
```bash
git clone https://github.com/Vasilisk18/api_tests.git
cd api_tests
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests
```bash
pytest -v
```
