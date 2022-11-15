import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti=Maksukortti(400)

    def test_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_ei_myytyja_lounaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_lounaan_voi_ostaa_kateisella(self):
        val = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(val, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaan_lounaan_voi_ostaa_kateisella(self):
        val=self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(val, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullista_ei_voi_ostaa_kateisella_jos_raha_ei_riita(self):
        val=self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(val, 100)

    def test_ei_voi_ostaa_maukasta_kateisella_jos_raha_ei_riita(self):
        val=self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(val, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_voi_ostaa_kortilla(self):
        val=self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 1.60 euroa')
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(val, True)

    def test_maukkaan_lounaan_voi_ostaa_kortilla(self):
        val= self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 0.00 euroa')
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(val, True)


    def test_ei_voi_ostaa_edullista_kortilla_jos_raha_ei_riita(self):
        maksukortti=Maksukortti(200)
        val=self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), 'Kortilla on rahaa 2.00 euroa')
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(val, False)

    def test_ei_voi_ostaa_maukasta_kortilla_jos_raha_ei_riita(self):
        maksukortti=Maksukortti(200)
        val=self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(str(maksukortti), 'Kortilla on rahaa 2.00 euroa')
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(val, False)

    def test_voi_ladata_kortille_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    def test_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    
    