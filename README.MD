

# Snake Ultimate

Snake Ultimate on helppo sekä kevyt peli, jossa käärmettä ohjaamalla pyritään syömään mahdollisimman paljon ruokaa kasvattaen samalla käärmeen pituutta. Peli on saanut vaikutteita perinteisestä matopelistä, joka tuli suosituksi 1990-luvulla matkapuhelinpelinä.

### Pelaaminen
Pelissä käärmettä ohjataan nuolinäppäimillä, ja pyritään syömään mahdollisimman paljon karkkeja. Peli päättyy, kun pelaaja osuu omaan häntäänsä tai seinään.

## Dokumentaatio

- [käyttöohje.md](dokumentaatio/käyttöohje.md)

- [vaatimusmäärittely.md](dokumentaatio/vaatimusmäärittely.md)

- [tuntikirjanpito.md](dokumentaatio/tuntikirjanpito.md)

- [arkkitehtuuri.md](dokumentaatio/arkkitehtuuri.md)

- [changelog.md](dokumentaatio/changelog.md)

- [testaus.md](dokumentaatio/testaus.md)

## Pelin julkaisut
[Ensimmäinen julkaisu](https://github.com/SuperTLP/ot-harjoitustyo/releases/tag/viikko5)

[Toinen julkaisu](https://github.com/SuperTLP/ot-harjoitustyo/releases/tag/viikko6)

[Loppupalautus](https://github.com/SuperTLP/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus

1. Asenna riippuvuudet komennolla
~~~
poetry install
~~~
2. Suorita alustustoimenpiteet komennolla
~~~
poetry run invoke build
~~~

## Komennot

*Komennot suoritetaan pelin hakemistossa komentorivillä*

### Pelaaminen
Pelin pystyy käynnistämään komennolla
~~~
poetry run invoke start
~~~

### Testaaminen
Testit pystyy ajamaan komennolla
~~~
poetry run invoke test
~~~

## Testikattavuus
Testikattavuusraportin pystyy luomaan komennolla
~~~
poetry run invoke coverage-report
~~~
Komennon suorittamisen jälkeen testiraportti ilmestyy htmlcov-kansioon.

## Pylint

tiedoston .pylintrc määrittelemän koodin laatutarkastuksen voi suorittaa komennolla
~~~
poetry run invoke lint
~~~


