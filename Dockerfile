#1. Base Image (Lightweight Python)
FROM python:3.11-slim

# 2. Set Working Directory (in docker container,Working directory is app folder)
WORKDIR /app

# 3. Copy Requirements first (for caching)
COPY requirements.txt .

#Install Dependencies
RUN pip install --no--cache-dir -r requirements.txt

# 4. Copy Source Code and move to container app folder (app/ (source code)  and .app/ (container folder))
COPY app/ .app/

# 5. Environment variable for Python path
ENV PYTHONPATH=/app

# 6. Command to run the app 
CMD ["python","app/main.py"]