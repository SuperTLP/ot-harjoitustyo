

# Rikun Repo

## Snake

Snake on helppo sekä kevyt peli, jossa käärmettä ohjaamalla pyritään syömään mahdollisimman paljon ruokaa kasvattaen samalla käärmeen pituutta. Peli on saanut vaikutteita perinteisestä matopelistä, joka tuli suosituksi 1990-luvulla matkapuhelinpelinä.

### Pelaaminen
Pelissä käärmettä ohjataan nuolinäppäimillä, ja pyritään syömään mahdollisimman paljon punaisia karkkeja. Peli päättyy, kun pelaaja osuu omaan häntäänsä tai seinään.

## Dokumentaatio

[vaatimusmäärittely.md](https://github.com/SuperTLP/ot-harjoitustyo/blob/master/laskarit/viikko1/vaatimusmäärittely.md)

[tuntikirjanpito.md](https://github.com/SuperTLP/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri.md](https://github.com/SuperTLP/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[changelog.md](https://github.com/SuperTLP/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)



## Asennus

Asenna riippuvuudet komennolla
~~~
Poetry install
~~~
Suorita alustustoimenpiteet komennolla
~~~
Poetry run invoke build
~~~

## Komennot

### Pelaaminen
Pelin pystyy käynnistämään komennolla
~~~
Poetry run invoke start
~~~

### Testaaminen
Testit pystyy ajamaan komennolla
~~~
poetry run invoke test
~~~

## Testikattavuus
Testikattavuusraportin pystyy luomaan komennolla
~~~
poetry run invoke coverate-report
~~~
Komennon suorittamisen jälkeen testiraportti ilmestyy htmlcov-kansioon.

