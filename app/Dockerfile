FROM python:alpine
WORKDIR /app
RUN pip install fastapi pydantic pymongo uvicorn
COPY . .
CMD ["uvicorn","app:app", "--host", "0.0.0.0", "--port", "4850"]