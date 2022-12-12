# Ohjelman rakenne

## Arkkitehtuuri

### Peli noudattaa seuraavanlaista rakennetta:

![Pakkauskaavio](./kuvat/pakkauskaavio.png)

Ui sisältää käyttöliittymään liittyvän koodin. Services sisältää pelilogiikkaan liittyvän koodin. Tämä tarkoittaa käytännössä pysyviä luokka-olioita, joista luodaan vain yksi olio koko ohjelman suorituksen aikana. Entities sisältää lyhytikäisiä kulutettavia komponentteja. Lähinnä karkkeihin liittyvää koodia. Repositories sisältää pysyväistallennukseen liittyvän koodin.

## Käyttöliittymä
Pelin käyttöliittymällä on kolme näkymää:
- Päävalikko
- Peli
- High Score

Päävalikossa pelaaja syöttää nimensä pelille. Päävalikosta voi siirtyä tarkastelemaan korkeimpia pisteitä high-score näkymään, tai peli-näkymään pelaamaan peliä.

Käyttöliittymässä Peli-näkymä kutsuu jokaisella peliloopin kierroksella Game-luokan advance funktiota, joka edistää peliä yhden askeleen. Täten Käyttöliittymä on myös vastuussa pelin taajuudesta.

## Pelilogiikka

Pelilogiikka on keskitetty Game-luokalle. Tämä tarkoittaa sitä, että Game-luokka on ainoa yhteys käyttöliittymästä pelilogiikkaan. Luokka säilyttää pelin tilan, ja päivittää muut pelilogiikan oliot kutsumalla niiden metodeja. se päivittää esimerkiksi mato-olion kutsumalla tämän advance-metodia ja pyytää TreatFactory-luokkaa luomaan uuden karkin peliin jokaisella pelin iteraatiolla.
Snake-luokka on vastuussa kaikesta matoon liittyvien tietojen tallentamisesta. Tähän sisältyy esimerkiksi madon sijainti.
TreatFactory on vastuussa pelissä ilmestyvien karkkien luomisesta ja tiettyjen karkkien ilmestymisen todennäköisyydestä.

### Luokkien suhteet
Seuraava luokka/pakkauskaavio kuvaa luokkien suhdetta

![Luokkakaavio](./kuvat/luokkakaavio.png)

- Game->Snake:
Peli pyytää pelin jokaisella iteraatiolla Snake-oliota päivittämään itsensä kutsumalla tämän .advance-metodia argumentilla self.direction. Tämä metodi palauttaa pelille madon uuden sijainnin pelissä.
- Game->TreatFactory:
Peli pyytää pelin jokaisella iteraatiolla TreatFactory-oliota luomaan uuden karkin kutsumalla tämän .generate_random_treat metodia. Metodi palauttaa uuden karkkiolion, jonka peli lisää kartalle.
- Game->MatrixElement:
Peli tarkastaa jokaisella pelin iteraatiolla, onko madon pään kohdalla karkki. Se tekee tämän tarkistamalla kyseisessä lokaatiossa sijaitsevan MatrixElement-olion .type attribuutin. Jos tämä on "treat", "dual_treat" tai "matrix_treat", peli kutsuu olion action.consume metodia. Peli tarkastaa myös, onko kyseinen elementti madon ruumista tarkastamalla, onko olion .type attribuutti "snake". Peli päättyy, jos näin on.
- TreatFactory->MatrixElement:
TreatFactory arpoo uutta karkkia luodessaan numeron, joka päättää minkä tasoinen karkki luodaan. Tietyn numeron perusteella peli valitsee tason 1, 2 tai 3 ja suodattaa kaikkien karkkien listasta tasoa vastaavat MatrixElement-oliot joiden .tier attribuutti on kyseinen taso.



### Pelin eteneminen

Kun pelaaja syöttää alkuvalikossa nimekseen "Name" ja aloittaa pelin ja painaa kerran nuolta alaspäin, voi pelin toiminta näyttää seuraavalta:

![Sekvenssikaavio](./kuvat/sekvenssikaavio.png)

Ui kutsuu olion Game advance metodia edistääkseen pelin tilaa yhdellä. Kun pelaaja painaa nuolinäppäintä, Ui kutsuu Game-olion change_direction metodia nuolinäppäintä vastaavalla numerolla. Gamen advance-metodi kutsuu Snake-olion advance metodia pelin senhetkisellä suunnalla, ja mato päivittää oman tilansa. Tämän jälkeen mato palauttaa sijaintinsa Game-oliolle, ja Game päivittää oman tilansa. Jos peli huomaa että mato on DefaultTreat-olion päällä, se kutsuu olion consume metodia ja antaa sille snake-olion argumentiksi. DefaultTreat kutsuu madon metodia set_pending_blocks(1), jos mato on matoa pidentävän karkin päällä. Lopulta mato osuu seinään, ja peli tallentaa pelaajan pisteet kutsumalla score-oliota argumenteilla "Name" ja sore, missä score on syötyjen karkkien lukumäärä. Tämän jälkeen Game-olio palauttaa Ui-oliolle tietyn matriisin, jonka jälkeen Ui tietää päättää pelin.
