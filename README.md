# AI

AI 写代码专属仓库。

## 目录检查结果（FastAPI 后端）

当前后端目录建议至少包含：

- `backend/app.py`：FastAPI 入口
- `backend/requirements.txt`：Python 依赖
- `backend/Dockerfile`：容器化部署配置

以上文件已补齐为可运行的最小配置。

## 本地启动

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## 健康检查

- `GET /`：服务基础响应
- `GET /health`：健康状态
