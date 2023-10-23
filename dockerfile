FROM python:latest

WORKDIR /JS_CALCULADORA

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "index.py"]