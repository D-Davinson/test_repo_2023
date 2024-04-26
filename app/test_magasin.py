import unittest
from unittest.mock import Mock
from Magasin_class import Magasin

class test_magasin(unittest.TestCase):
    def setUp(self):
        self.magasin = Magasin(type_magasin="RAP")
        self.musique_valid = Mock(titre='Spring', nom_artiste='DDavi',immatriculation='DD/250/RAP/1234', duration=250, type_musique='RAP')
        self.musique_invalid = Mock(titre='Spring', nom_artiste='HLamia',immatriculation='DD/250/POP/2676',duration=250, type_musique='POP')
    def test_ajouter_vynille_musique(self):
        self.magasin.ajouter_vynille_musique(self.musique_valid)
        self.assertIn(self.musique_valid,self.magasin.vynille_musique)

    def test_remove_vynille_musique(self):
        self.magasin.vynille_musique = [self.musique_valid]
        self.magasin.remove_vynille_musique(self.musique_valid)
        self.assertEqual(len(self.magasin.vynille_musique),0)
    
    def test_ajouter_dvd_musique(self):
        self.magasin.ajouter_dvd_musique(self.musique_valid)
        self.assertEqual(len(self.magasin.dvd_musique),1)
    
    def test_remove_dvd_musique(self):
        self.magasin.dvd_musique = [self.musique_valid]
        self.magasin.remove_dvd_musique(self.musique_valid)
        self.assertEqual(len(self.magasin.dvd_musique),0)
    def tearDown(self):
        del self.magasin
        del self.musique_valid
        del self.musique_invalid

    

if __name__ == '__main__':
    unittest.main()