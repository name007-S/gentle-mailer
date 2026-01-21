from fastapi import FastAPI
from app.ai.generator import generate_gentle_message
from app.config import IS_PROD
from app.scheduler import start_scheduler

app = FastAPI()


@app.on_event("startup")
def startup_event():
    """
    仅在生产环境启动定时任务
    """
    if IS_PROD:
        start_scheduler()


@app.post("/preview")
def preview_message():
    """
    开发 / 测试用：
    只生成 AI 内容，不发邮件
    """
    content = generate_gentle_message()
    return {
        "preview": content
    }
