import resend
import os
from app.config import IS_PROD

resend.api_key = os.getenv("RESEND_API_KEY")


def send_gentle_mail(to_email: str, content: str):
    """
    发送一封温和的 AI 邮件
    """
    if not IS_PROD:
        # 开发环境：不真正发信，只打印
        print("[DEV MODE] 邮件内容如下：")
        print("To:", to_email)
        print(content)
        return {"status": "skipped", "reason": "dev mode"}

    params = {
        "from": "Gentle Mailer <onboarding@resend.dev>",
        "to": [to_email],
        "subject": "🌿 一封温和的问候",
        "html": f"""
        <div style="font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                    line-height: 1.6; font-size: 16px;">
            <p>{content}</p>
            <hr/>
            <p style="color:#888;font-size:12px;">
                由 Gentle Mailer · AI 自动生成
            </p>
        </div>
        """
    }

    return resend.Emails.send(params)
