from fastapi import FastAPI
from pymongo import MongoClient
from Musique_class import Musique

app = FastAPI()

client = MongoClient(host="mongodb")

db = client["mabase"]
col = db["musique"]

@app.get("/musique", response_model=list[Musique])
def get_musique():
    musique = col.find()
    return list(musique)

@app.post("/add_musique")
def add_musique(musique : Musique):
    col.insert_one(musique.model_dump()).inserted_id
    return musique

@app.delete("/delete_musique")
def delete_musique(musique : Musique):
    col.delete_one(musique.model_dump())
