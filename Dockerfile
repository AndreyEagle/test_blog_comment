FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY test_blog_comments/ /app

CMD ["gunicorn", "test_blog_comments.wsgi:application", "--bind", "0:8000" ]