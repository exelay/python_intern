FROM python:3.9

WORKDIR /usr/src/python_intern

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]