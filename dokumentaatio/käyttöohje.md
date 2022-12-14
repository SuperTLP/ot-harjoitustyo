# Käyttöohje

## Pelin käynnistäminen
Pelin käynnistäminen ei vaadi konfiguraatiota, vaan pelkästään kolmen komennon suorittamista pelin hakemistossa.
Pelin riippuvuudet tulee asentaa komennolla
```
poetry install
```
Tämän jälkeen Pelin tietokanta tulee alustaa komennolla
```
poetry run invoke build
```
Nyt pelin voi käynnistää komennolla
```
poetry run invoke start
```

## Pelin alkuvalikko
Pelissä voidaan liikkua näkymästä toiseen klikkaamalla hiirellä valikoissa näkyviä nappeja. Klikkaamalla Play-nappia pääsee valitsemaan nimensä. Klikkaamalla High-scores-nappia pääsee tarkastelemaan korkeimpia pisteitä. Missä tahansa valikon ikkunassa pääsee takaisin alkuvalikkoon Vasemmassa yläkulmassa sijaitsevaa Menu-nappia painamalla.

## High-score näkymä
Korkeimpia pisteitä tarkasteltaessa näytetään yhdellä sivulla viisi tulosta kerrallaan. Viiden tuloksen sivuja voi selata painamalla Next- tai Previous-nappeja vasemmassa ja oikeassa alakulmassa. Takaisin alkuvalikkoon pääsee painamalla vasemmassa yläkulmassa sijaitsevaa Menu-painiketta. Tässä näkymässä nähdään pelaajien saavuttamat pisteet, sekä millä vaikeustasolla pisteet on saatu.

## Nimen valinta
Nimen valintaan päästään alkuvalikosta painamalla Play-nappia. Tässä näkymässä pelaajan tulee syöttää pelille oma nimensä tallentaakseen pisteensä. Nimen syöttämisen jälkeen pelaaja voi siirtyä valitsemaan vaikeustason painamalla Next-nappia.

## Vaikeustason valinta
Syötettyään nimensä pelille ja vaikeustasonäkymään siirtymisen jälkeen voi pelaaja valita vaikeustasoksi Hard, Medium tai Easy. Eroa vaikeustasoilla on nopeus, jolla peli etenee. Vaikeustason valinnan jälkeen peli alkaa.

## Pelaaminen
Mato lähtee liikkeelle, kun pelaaja painaa ensimmäisen kerran oikeaa nuolinäppäintä pelissä. Pelissä liikutaan nuolinäppäimillä. Mato etenee viimeksi painetun nuolinäppäimen osoittamaan suuntaan. Pelissä tarkoituksena on kerätä mahdollisimman paljon pisteitä syömällä erilaisia karkkeja. Peli päättyy, kun pelaaja osuu omaan häntäänsä tai seinään.

Pelin päättymisen jälkeen pelaaja näkee saavuttamansa pisteet. Takaisin päävalikkoon pääsee painamalla keskellä ruutua olevaa Menu-paniketta.

## Pelissä esiintyvät Karkit

### Tavalliset karkit
- Punainen karkki lyhentää matoa karkissa ilmoitetun määrän verran.

![DefaultTreat](./kuvat/negative_default_treat.png)

- Vihreä karkki pidentää matoa karkissa ilmoitetun määrän verran.

![DefaultTreat](./kuvat/positive_default_treat.png)

### Erikoiskarkit
Pelissä esiintyy useita erikoiskarkkeja, jotka ovat väriltään kullanvärisiä ja sinisiä. Sininen väri kuvastaa tason 2 karkkia, ja kultainen karkki tason 3 karkkia.
- **Sininen karkki** joka on merkitty **rasti**lla poistaa kaikki pelin kentällä olevat karkit.

![PurgeTreat](./kuvat/purge_treat.png)

- **Sininen karkki** jossa on merkintä **<-** kääntää madon suunnan päinvastaiseksi.

![ReverseTreat](./kuvat/reverse_treat.png)

- **Kultainen karkki** Jossa on merkintä **$** Lisää kartalle suuren määrän matoa lyhentäviä karkkeja.

![FloodTreat](./kuvat/flood_treat.png)

Kultaiset karkit antavat pelaajalle 40 pistettä, ja siniset karkit 20 pistettä. Tavalliset karkit antavat yhden pisteen.



