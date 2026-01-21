# 温和的邮件 (Gentle Email)

一个基于 **FastAPI** 的轻量级、温和的邮件自动化工具/服务。

## 项目简介

“温和的邮件” 旨在提供一个低调、高效、可自托管的邮件调度与发送解决方案。适用于个人/小型团队的自动化邮件任务（如通知提醒、批量温和推送、定时报告等），强调“温和”原则：避免骚扰式群发，支持环境隔离、生产就绪部署。

核心功能（正在开发中）：
- **调度器**：支持 cron-like 定时任务、延迟执行
- **环境隔离**：虚拟环境/容器化隔离不同邮件配置
- **生产环境部署**：支持 Docker、Gunicorn + Uvicorn 等高效部署
- **邮件发送**：集成常见 SMTP（如 Gmail、QQ、企业邮箱），支持 HTML/附件
- **安全与合规**：限流、防滥用、日志记录

## 当前状态
- 项目处于**开发初期**，核心骨架已基于 FastAPI 搭建。
- 已完成：基础 FastAPI 应用结构、requirements.txt 依赖管理、.gitignore 配置。
- 正在完善：调度模块、邮件发送逻辑、环境隔离实现、生产部署脚本。
- 预计后续添加：API 接口文档（Swagger）、用户配置、监控 dashboard。

## 技术栈
- **后端**：FastAPI (异步 Web 框架)
- **依赖**：详见 requirements.txt（包括 uvicorn、pydantic 等）
- **部署**：计划支持 Docker Compose 一键部署

## 安装与运行（开发中，示例）
```bash
# 克隆仓库
git clone https://github.com/name007-S/温和的邮件.git
cd 温和的邮件

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
uvicorn main:app --reload
