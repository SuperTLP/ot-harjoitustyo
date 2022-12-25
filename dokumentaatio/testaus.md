# Testausdokumentti

Ohjelmaa testataan unittestillä automaattisilla yksikkö- sekä integraatiotesteillä. Ohjelmaa on testattu myös manuaalisilla järjestelmätesteillä.

## yksikkötestaus

### Sovelluslogiikka
**Game**-oliota testataan TestGame - testiluokalla. TestGamen testeissä Testattavalle Game-luokalle injektoidaan MagicMock Snake-, GameMatrix- ja ScoreService-oliot , Joilla on ennalta määrätyt paluuarvot.

**TreatFactory ja ScoreService** luokilla ei toistaiseksi ole omaa testiluokkaansa.

### Entities-luokkien testaus

**Treat**-olioita testataan kutsumalla niiden .consume-metodia MagicMock-argumentein. Testeissä varmistetaan, että karkit syötynä kutsuvat muutettavan olion oikeaa metodia oikealla arvolla.

**Snake**-oliota testataan TestSnake - testiluokalla. Snake-luokkaa testataan antamalla sille parametriksi lähtötilanne, ja varmistamalla että mato liikkuu oikein, Eli että sen self.position attribuutti on .advance-metodin kutsujen jälkeen haluttu arvo.

**GameMatrix-,Score- ja MatrixElement**-luokilla ei toistaiseksi ole omia testiluokkia.

### Repositories-luokkien testaus
Pelin repositories-kansiossa olevia luokka-olioita, eli tietokantatauluja vastaavia luokkia testataan injektoimalla niille MagicMock-olio db-parametrinä, eli tietokantana. Testeissä varmistetaan, että tietyillä parametreillä luokat kutsuvat tietokantaa oikealla SQL-kyselyllä.

## Integraatiotestaus

Ohjelman Integraatiotestaus tapahtuu yhdessä testiluokassa TestIntegration. Tässä luokassa testattaville luokille injektoidaan todelliset sovelluslogiikan luokkaoliot, eikä Mock-olioita. Testiluokan jokaisessa testimetodissa luodaan Game-olio, jolle injektoidaan Snake-olio, GameMatrix-, sekä ScoreService oliot. Toisin kuin repositories-luokan testeissä, integraatiotestissä luodaan oikea tietokanta, jonne testien tulokset tallennetaan.

TestIntegration-luokan testeissä pelissä matoa liikutellaan useiden karkkien päälle, ja tarkistetaan, että jokaisen luokan tiedot päivittyvät oikein.
Tähän kuuluu Snake-olion position, Pending_blocks ja direction, sekä Game-olion points.

## Testikattavuus
25.12.2022 Testikattavuus on 97%
![Pakkauskaavio](./kuvat/testikattavuus.png)

## Järjestelmätestaus

Pelin järjestelmätestaus suoritetaa manuaalisesti pelaamalla peliä ja kokeilemalla sen erilaisia toimintoja ja näiden yhdistelmiä.

## Sovelluksen laatuongelmat

Sovellus kaatuu pelin päättyessä, mikäli tietokantaa ei ole alustettu komennolla poetry run invoke build.






