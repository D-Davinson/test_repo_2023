from pymongo import MongoClient
from Musique_class import Musique

client = MongoClient(host="mongodb")
db = client['mabase']
collection = db['musique']

def populate():

    n = 20
    for i in range(n):
        titre_id = "Titre" + str(i)
        musique = Musique(titre=titre_id,nom_artiste="Davi",immatriculation="DA/250/POP/1234",type_musique="POP",duration=250)
        musique_id = collection.insert_one(musique.model_dump()).inserted_id


if __name__ == '__main__':
    populate()
    print("test")