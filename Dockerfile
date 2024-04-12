FROM python:3.9-slim-bullseye

WORKDIR /app

COPY req.txt .

RUN pip3 install --no-cache-dir -r req.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]