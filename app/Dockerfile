FROM python:3.12-slim

WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "main.py", "run", "--host=0.0.0.0"]
#default port 5000, -p for custom port