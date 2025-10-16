# CHANGELOG

## v0.2
- Byter från LinearRegression till Ridge(alpha=1.0) i en StandardScaler-pipeline.
- Förbättrad RMSE jämfört med v0.1 (se metrics nedan).
- API:t är oförändrat men `MODEL_VERSION` kan sättas via env variabel.

**Metrics** (RMSE på held-out split, `random_state=42`):

- v0.1 RMSE: 53.8534
- v0.2 RMSE: 53.7775

## v0.1
- Baseline: StandardScaler + LinearRegression.
- `/health` och `/predict` finns.
- Docker-image med inbakat tränat modelobjekt.