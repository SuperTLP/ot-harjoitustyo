# Työaikakirjanpito

| päivä | aika | mitä tein  |
| :----:|:-----| :-----|
| 15.11. | 0:15    | Alustava määrittelydokumentti |
| 22.11. | 7:00    | Perusta pelille, ensimmäinen testi, käyttöliittymä. |
| 24.11. | 0:15    | Paranneltiin readme-tiedostoa|
| 25.11. | 0:15    | Paranneltiin readme-tiedostoa|
| 26.11. | 5:00    | Luotiin pelille menu, luotiin MatrixElement ja DefaultTreat - luokat. Luotiin ensimmäiset testit DefaultTreat-luokalle. Refaktorointi: Vaihdettiin matriisin alkiot numeroista MatrixElement-olioiksi.|
| 27.11. | 2:00    | DefaultTreat-luokka ei enää muuta suoraan Snake-luokan muuttujia. DefaultTreat-luokka laskee Uuden position Snake-luokalle, ja kutsuu tämän jälkeen set_pending_blocks ja set_position metodeja.|
|29.11|0:15|Poistettiin käyttöliittymästä high-score ohjeistus toistaiseksi.|
|2.12|2:00|Päivitettiin käyttöliittymä ja lisättiin high-score ikkuna|
|4.12|0:30|Lisättiin testejä|
|5.12|2:00|Luotiin PurgeTreat luokka ja refaktoroitiin game-luokkaa|
|7.12|3:00|Päivitettiin high-score näkymää: lisättiin linkki alkuvalikkoon, lisättiin sivunumerot. Luotiin merkittävä määrä docstringejä eri luokkiin, ja luotiin integraatiotestejä, sekä lisää testejä Game-luokalle.
|11.12|6:00|Luotiin FloodTreat, ReverseTreat, CustomMatrixElement ja TreatFactory - luokat. Poistettiin MatrixElement luokka.|
|12.12|6:00|lisättiin testejä. Poistettiin CustomMatrixElement luokka, palautettiin MatrixElement luokka |
|17.12|6:00|Lisättiin peliin uusia näkymiä, lisättiin 3 vaikeustasoa ja helpotettiin käytettävyyttä vaihtamalla menun napit klikattavaksi.|
|20.12|3:00|Muutettiin High-score näkymän napit klikattavaksi, lisättiin vaikeustasot high-score näkymän tuloksien viereen|
|21.12|4:00|refaktorointia|
|22.12|2:00|Poistettiin madon suunta Game-oliosta ja siirrettiin se mato-luokan attribuutiksi. Refaktoroitiin muutoksen hajottama koodi. Korjattiin bugi jossa mato voisi kääntyä itsensä päälle juuri lyhentyessään yhden pituiseksi.|
| yht| 49:30||



