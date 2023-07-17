FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

# EXPOSE 8000

CMD ["uvicorn", "myapp.asgi:application","--host", "127.0.0.1", "--port", "8000", "--reload"]
