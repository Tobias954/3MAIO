# Virtual Diabetes Clinic Triage (FastAPI + Docker + GitHub Actions)

Ett litet ML-API som förutspår kortsiktig försämring (sklearn diabetes dataset) och returnerar ett kontinuerligt riskscore.
Byggt för att köras i Docker och släppas via GitHub Actions till GHCR.

## Snabbstart lokalt (VS Code eller valfri IDE)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Träna modeller (det finns redan färdigtränade i repo:t, men så här återskapar du)
python -m training.train --version v0.1
python -m training.train --version v0.2

# Starta API
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Testa API:t

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":0.02,"sex":-0.044,"bmi":0.06,"bp":-0.03,"s1":-0.02,"s2":0.03,"s3":-0.02,"s4":0.02,"s5":0.02,"s6":-0.001}'
```

## Docker

```bash
docker build -t clinic-triage:dev .
docker run --rm -p 8000:8000 clinic-triage:dev
```

## GitHub Actions

- **CI** (på push/PR): lint, tester, snabbträning, bygga & röktesta container, ladda upp artefakter.
- **Release** (på tag `v*`): bygga image, röktest, pusha till GHCR och skapa GitHub Release med metrics.

### Publicera v0.1 och v0.2

```bash
git tag v0.1 && git push origin v0.1
git tag v0.2 && git push origin v0.2
```

Se till att GitHub Packages (GHCR) är aktiverat i organisationen/repot. Image hamnar på:
`ghcr.io/<org>/<repo>:v0.1` och `:v0.2`.

## Modell och features

Features (måste skickas exakt i denna ordning/namn): `age, sex, bmi, bp, s1, s2, s3, s4, s5, s6`.

Svaret från `/predict`:
```json
{ "prediction": <float>, "model_version": "v0.2" }
```

## Reproducerbarhet

- Fasta seeds (`random_state=42`), deterministisk train/test-split.
- Pinnar Python och lib-versioner i `requirements.txt`.
- `models/metrics.json` uppdateras av träningsscriptet.

## Utveckling

```bash
make lint
make test
make run
```