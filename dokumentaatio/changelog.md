# Changelog


## viikko 3
- Luotiin View luokka, joka on pelin käyttöliittymä.
- Luotiin Game luokka, joka on vastuussa pelissä käytettävän matriisin muokkaamisesta ja pelilogiikasta
- luotiin Snake luokka, joka on vastuussa madon liikuttamisesta.
- luotiin perusta pelille. pelaaja pystyy liikkumaan madolla vapaasti ja peli päättyy kun pelaaja osuu seinään tai omaan häntäänsä.
- Luotiin ensimmäinen testi Game-luokalle, joka testaa että peli päättyy kun mato osuu oikeaan seinään.

## viikko 4
- Luotiin MatrixElement luokka, joka on vastuussa matriisin erilaisten elementtien geneerisen tiedon tallentamisesta.
- luotiin DefaultTreat luokka, joka on vastuussa tavallisten karkkien (vihreiden ja punaisten) toiminnallisuudesta.
- Toiminnallisuuden lisäämisen helpottamiseksi matriisin oliot muutettiin numeroista MatrixElement-olioiksi.
- Karkkien toiminnallisuus ei rajoitu enää madon pidentymiseen yhdellä palikalla, vaan jotkin karkit lyhentävät matoa, ja jotkin pidentävät sitä.
- Karkkeja luodaan nyt pelin jokaisella iteraatiolla
- hidastettiin pelin kulkua
- Luotiin Score luokka,joka on vastuussa pelin pisteiden tallentamisesta tietokantaan.
- luotiin pelille alkeellinen valikko
- Luotiin muutama testi DefaultTreat luokalle, jotka tarkistavat että madon funktioita kutsutaan oikein kun karkki syödään.
- 

## viikko 5
- Uudistettu käyttöliittymä: käyttäjäystävällisempi valikko
- lisättiin high-score ikkuna käyttöliittymälle
- Lisättiin PurgeTreat-luokka, joka on vastuussa karkit poistavan erikoiskarkin toiminnallisuudesta.

## viikko 6
- päivitettiin high-score näkymä
- Luotiin FloodTreat luokka, joka on vastuussa matoa lyhentäviä karkkeja luovan erikoiskarkin toiminnallisuudesta.
- Luotiin ReverseTreat luokka, joka on vastuussa madon suunnan kääntävän erikoiskarkin toiminnallisuudesta
- Luotiin TreatFactory luokka, joka on vastuussa karkkien luomisesta.
## viikko 7
- Luotiin vaikeustasot: 3 eri vaihtoehtoa madon nopeudelle.
- Luotiin uusia näkymiä valikkoon - Nimi syötetään Play-napin painamisen jälkeen, jonka jälkeen valitaan vaikeustaso.
- Lisättiin hiirellä klikattavat napit High-score näkymään.
- Lisättiin high-score näkymän tuloksiin vasemmalle vaikeustaso jolla tulos saatiin.
