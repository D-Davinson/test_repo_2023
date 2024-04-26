FROM python:alpine
WORKDIR /app/seeder
COPY . .
RUN pip install pymongo pydantic
CMD ["python", "seeder.py"]