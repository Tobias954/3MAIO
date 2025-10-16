.PHONY: train-v01 train-v02 run build docker-run test lint

train-v01:
	python -m training.train --version v0.1

train-v02:
	python -m training.train --version v0.2

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

build:
	docker build -t ghcr.io/ORG/REPO:dev .

docker-run:
	docker run --rm -p 8000:8000 ghcr.io/ORG/REPO:dev

test:
	pytest -q

lint:
	ruff check .
