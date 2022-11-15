import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 5.00 euroa')

    def test_saldo_muutu_jos_ei_rahaa_riittävästi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')

    def test_palauttaa_true_jos_onnistui(self):
        value=self.maksukortti.ota_rahaa(1000)
        self.assertEqual(value, True)

    def test_palauttaa_false_jos_ei_onnistunut(self):
        value=self.maksukortti.ota_rahaa(2000)
        self.assertEqual(value, False)
    def test_saldo_suurenee_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 20.00 euroa')
