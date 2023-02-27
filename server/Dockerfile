FROM python:3.9-slim


COPY . .

RUN pip install -r requirements.txt


CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]
