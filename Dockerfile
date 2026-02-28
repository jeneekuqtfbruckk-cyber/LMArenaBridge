FROM python:3.12-slim

# 创建非 root 用户 (HF Spaces 要求 UID 1000)
RUN useradd -m -u 1000 user

WORKDIR /home/user/app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 预创建可写目录
RUN mkdir -p /home/user/app /home/user/.cache && \
    chown -R user:user /home/user

# 切换到非 root 用户
USER user
ENV PATH="/home/user/.local/bin:${PATH}"
ENV HOME=/home/user

# 复制全部项目代码
COPY --chown=user:user . /home/user/app

# 设置启动脚本可执行
RUN chmod +x /home/user/app/startup.sh

EXPOSE 7860

CMD ["/bin/bash", "/home/user/app/startup.sh"]
