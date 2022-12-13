## Ohjeet pelaamiseen

## Pelin käynnistäminen
Pelin käynnistäminen ei vaadi konfiguraatiota, vaan pelkästään kahden komennon suorittamista pelin hakemistossa.
Pelin riippuvuudet tulee asentaa komennolla
```
poetry install
```
Tämän jälkeen Pelin tietokanta tulee alustaa komennolla
```
poetry run invoke build
```



## Pelin alkuvalikko
Alkuvalikossa navigoidaan nuolinäppäimillä. Ylös-nuolella liikutaan valinnoissa ylöspäin ja alas-nuolella alaspäin. Oikealla nuolella voidaan valinnan play kohdalla aloittaa peli, tai valinnan high scores kohdalla siirtyä tarkastelemaan korkeimpia pisteitä.

Jotta pelaaja voi tallentaa tuloksensa nimellä, tulee hänen liikkua nuolinäppäimillä Valinnan Name kohdalle ja kirjoittaa oma nimensä.

## High-score näkymä
Korkeimpia pisteitä tarkasteltaessa näytetään yhdellä sivulla viisi tulosta kerrallaan. Pelaaja voi liikkua sivujen välillä nuolinäppäimillä. Takaisin alkuvalikkoon pääsee sulkemalla ikkunan rastista, tai painamalla go back-nappia vasemassa yläkulmassa.

## Pelaaminen
Pelissä liikutaan nuolinäppäimillä. Mato etenee viimeksi painetun nuolinäppäimen osoittamaan suuntaan. Pelissä tarkoituksena on kerätä mahdollisimman paljon pisteitä syömällä erilaisia karkkeja.Punaiset ja vihreät karkit antavat yhden pisteen ja muun väriset erikoiskarkit antavat 20 pistettä. Punainen karkki lyhentää madon pituutta karkissa ilmoitetun määrän verran. Vihreä karkki pidentää matoa samalla periaatteella. Erikoiskarkeilla on erilaisia toimintoja jotka helpottavat pelaamista. Peli päättyy, kun pelaaja osuu omaan häntäänsä tai seinään.

## Erikoiskarkit
Pelissä esiintyy useita erikoiskarkkeja, jotka ovat väriltään kullanvärisiä ja sinisiä. Sininen väri kuvastaa tason 2 karkkia, ja kultainen karkki tason 3 karkkia.
Sininen karkki joka on merkitty rastilla poistaa kaikki pelin kentällä olevat karkit
Sininen karkki jossa on merkintä "<-" kääntää madon suunnan päinvastaiseksi.
