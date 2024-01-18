# TweetBot
## Projekta uzdevums
Šī projekta uzdevums bija izveidot programmu, kas izmantojot ievadi (lietotājvārdu, paroli, tekstu), spēj automātiski ielogoties vietnē twitter.com / x.com un nosūtīt ("tweetot") norādīto jeb ievadīto tekstu. Jāpiemin, ka jau ir daudz un dažādas līdzīgas programmas, taču man bija svarīgi pašam izprast un iemācīties, kā šis process strādā, kā arī, lai to varētu pielāgot savām vajadzībām.

## Programmatūras izmantošanas iespējas
Programma NAV paredzēta ļaunprātīgai izmantošanai. To var izmantot lai nosūtītu kaut kādu informāciju vai domu graudu, pašam neatverot vietni. To var arī izmantot gadījumā, ja cilvēkam ir vairāki Twitter konti un dažāda informācija, ko nosūtīt, tad ši programma spēj importēt/atvērt failus Excel formātā, kur dati sakārtoti šādi - (Lietotājvārds - kollona A, Parole - kollona B, Vēlamais teksts - kollona C). Protams, šo programmu var izmantot apvienojumā ar citām programmām, piemēram nolasot kādus datus no citas vietnes un šo informāciju nododot tālāk (kā piemērs varētu būt dažādas statistiskās vietnes, piemēram, Covid-19 saslimušo skaits dienā).

## Izmantotās bibliotēkas
Tkinter - lai izveidotu grafisko saskarni, kur ievadīt informāciju vai izvēlētos citas iespējas, kā arī tā padara programmu pieejamāku plašākam lietotāju lokam
Selenium - lai nodrošinātu lietotāja darbību automatizāciju tīmekļa vietnē (automātiski ievadītu informāciju; nospiestu pogas)
Openpyxl - lai nodrošinātu Excel failu un to saturošās informācijas nolasīšanu
Time - lai nodrošinātu programmas aizkavi gadījumā, ja tīmekļa vietne nespēj ielādēties pietiekami ātrā laikā

## Funkcijas. ko vēlos pievienot
Headless režīms, lai programma strādātu nemanāmi (pašlaik to var nomainīt kodā)
Programmas aktivizēšanu noteiktā laikā un/vai datumā
Template (paraugu) izmantošana

## Izmantotie avoti, pamācības
https://www.youtube.com/watch?v=aSeqMYNhEHo
https://www.youtube.com/watch?v=t0PBBPuPgaw
https://www.selenium.dev/documentation/
