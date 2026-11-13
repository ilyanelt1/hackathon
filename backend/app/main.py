from fastapi import FastAPI

app = FastAPI(
    title="MTS Intern Dashboard API",
    description="API интеллектуального аналитического дашборда стажировок МГТС.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
