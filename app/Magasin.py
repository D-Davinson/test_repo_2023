from typing import List
from pydantic import BaseModel, Field
from Musique_class import Musique

class Magasin(BaseModel):
    type_magasin: str
    dvd_musique: List[Musique] = Field(default_factory=list)
    vynille_musique: List[Musique] = Field(default_factory=list)

    def ajouter_vynille_musique(self, musique : Musique):
        if self.type_magasin == musique.type_musique:
            self.vynille_musique.append(musique)
    def remove_vynille_musique(self, musique : Musique):
        self.vynille_musique.remove(musique)

    def ajouter_dvd_musique(self, musique : Musique):
        if self.type_magasin == musique.type_musique:
            self.dvd_musique.append(musique)
    def remove_dvd_musique(self, musique : Musique):
        self.dvd_musique.remove(musique)