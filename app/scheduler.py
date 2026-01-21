from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.ai.generator import generate_gentle_message
from app.mail.sender import send_gentle_mail


def send_daily_gentle_mail():
    content = generate_gentle_message()
    send_gentle_mail(
        to_email="jyybjgu@outlook.com",
        content=content
    )
    print(f"[{datetime.now()}] Gentle mail sent.")


def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai")

    scheduler.add_job(
        send_daily_gentle_mail,
        trigger="cron",
        hour=9,
        minute=0,
        id="gentle_mail_job",
        replace_existing=True
    )

    scheduler.start()
