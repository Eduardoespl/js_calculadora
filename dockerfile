FROM python:latest

WORKDIR /JS_CALCULADORA

COPY . .

CMD ["python", "index.py"]