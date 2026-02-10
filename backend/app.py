from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mini Program Backend",
    version="0.1.0",
    description="FastAPI backend service for a mini program product.",
)

# 小程序开发阶段常见跨域请求，生产环境请替换为精确域名。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "FastAPI backend is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
