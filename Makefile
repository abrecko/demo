run:
uvicorn app.main:app --reload --port 8000

test:
pytest

lint:
ruff .

format:
black .

coverage:
pytest --cov=app --cov-report=term-missing

docker-build:
docker build -t abrecko-demo .

docker-run:
docker run -p 8000:8000 abrecko-demo
