from telebot import types
import telebot 

bot = telebot.TeleBot('8051828808:AAH0uxGl4Jm4lfFZ6BahJ6wWbKoO6FsVhGI')


user_languages = {}

# Kinolar janrlari
movie_genres = {
    "en": {
        "action": "Action Movies",
        "comedy": "Comedy Movies",
        "drama": "Drama Movies",
        "horror": "Horror Movies",
        "detective": "Detective Movies",
        "melodrama": "Melodrama Movies",
        "adventures": "Adventures Movies",
        "romantic": "Romantic Movies",
        "fantasy": "Fantasy Movies",
        "cartoons": "Cartoons",
        "zombi": "Zombi Movies"
    },
    "ru": {
        "action": "Боевики",
        "comedy": "Комедии",
        "drama": "Драмы",
        "horror": "Ужасы",
        "detective": "Детектив",
        "melodrama": "Мелодрама",
        "adventures": "Приключения",
        "romantic": "Романтические",
        "fantasy": "Фантастические",
        "cartoons": "Мультфильмы",
        "zombi": "Зомби "
    },
    "uz": {
        "action": "Jangari Kinolar",
        "comedy": "Komediya Kinolar",
        "drama": "Drama Kinolar",
        "horror": "Qo`rqinchli Kinolar",
        "detective": "Detektiv kinolar",
        "melodrama": "Melodrama Kinolar",
        "adventures": "Sarguzasht Kinolar",
        "romantic": "Romantik Kinolar",
        "fantasy": "Fantastik Kinolar",
        "cartoons": "Multifilimlar",
        "zombi": "Zombi Kinolar"
    }
}
# Kinolar ro'yxati
movie_list = {
    "en": {
        "action": ["Mad Max - https://www.imdb.com/title/tt1392190/?ref_=ext_shr_lnk"  , "John Wick - https://www.imdb.com/title/tt2911666/?ref_=ext_shr_lnk", "Bullet Train - https://www.imdb.com/title/tt12593682/?ref_=ext_shr_lnk","The Dark Knight - https://www.imdb.com/title/tt0468569/?ref_=ext_shr_lnk ", "Gladiator - https://www.imdb.com/title/tt0172495/?ref_=ext_shr_lnk", "Inception - https://www.imdb.com/title/tt1375666/?ref_=ext_shr_lnk",],
        "comedy": ["The Hangover - https://www.imdb.com/title/tt1119646/?ref_=ext_shr_lnk", "Superbad - https://www.imdb.com/title/tt0829482/?ref_=ext_shr_lnk", "Rush Hour - https://www.imdb.com/title/tt0120812/?ref_=ext_shr_lnk","Dumb and Dumber - https://www.imdb.com/title/tt0109686/?ref_=ext_shr_lnk", "Step Brothers - https://www.imdb.com/title/tt0838283/?ref_=ext_shr_lnk", "21 Jump Street - https://www.imdb.com/title/tt1232829/?ref_=ext_shr_lnk", "Ace Ventura - https://www.imdb.com/title/tt0109040/?ref_=ext_shr_lnk", "Mask - https://www.imdb.com/title/tt0110475/?ref_=ext_shr_lnk"],
        "drama": ["The Shawshank Redemption - https://www.imdb.com/title/tt0111161/?ref_=ext_shr_lnk", "Forrest Gump - https://www.imdb.com/title/tt0109830/?ref_=ext_shr_lnk", "The Godfather - https://www.imdb.com/title/tt0068646/?ref_=ext_shr_lnk","A Beautiful Mind - https://www.imdb.com/title/tt0268978/?ref_=ext_shr_lnk", "The Green Mile - https://www.imdb.com/title/tt0120689/?ref_=ext_shr_lnk", "Good Will Hunting - https://www.imdb.com/title/tt0119217/?ref_=ext_shr_lnk", "Schindler’s List - https://www.imdb.com/title/tt0108052/?ref_=ext_shr_lnk", "The Pursuit of Happyness - https://www.imdb.com/title/tt0454921/?ref_=ext_shr_lnk"],
        "horror": ["The Conjuring - https://www.imdb.com/title/tt1457767/?ref_=ext_shr_lnk", "It - https://www.imdb.com/title/tt1396484/?ref_=ext_shr_lnk ", "A Nightmare on Elm Street - https://www.imdb.com/title/tt1179056/?ref_=ext_shr_lnk", "The Exorcist - https://www.imdb.com/title/tt5368542/?ref_=ext_shr_lnk", "Hereditary - https://www.imdb.com/title/tt7784604/?ref_=ext_shr_lnk", "The Babadook - https://www.imdb.com/title/tt2321549/?ref_=ext_shr_lnk", "Insidious - https://www.imdb.com/title/tt1591095/?ref_=ext_shr_lnk", "Sinister - https://www.imdb.com/title/tt1922777/?ref_=ext_shr_lnk"],
        "detective": ["Sherlock Holmes - https://www.imdb.com/title/tt0988045/?ref_=ext_shr_lnk", "Seven - https://www.imdb.com/title/tt0114369/?ref_=ext_shr_lnk", "Tourist - https://www.imdb.com/title/tt1243957/?ref_=ext_shr_lnk", "Knives Out - https://www.imdb.com/title/tt8946378/?ref_=ext_shr_lnk", "Gone Girl - https://www.imdb.com/title/tt2267998/?ref_=ext_shr_lnk", "Old Boy - https://www.imdb.com/title/tt0364569/?ref_=ext_shr_lnk", "Prisoners - https://www.imdb.com/title/tt1392214/?ref_=ext_shr_lnk", "Parasite - https://www.imdb.com/title/tt6751668/?ref_=ext_shr_lnk"],
        "melodrama": ["Titanic - https://www.imdb.com/title/tt0120338/?ref_=ext_shr_lnk", "The Notebook - https://www.imdb.com/title/tt0332280/?ref_=ext_shr_lnk", " Mr & Mrs smith - https://www.imdb.com/title/tt0356910/?ref_=ext_shr_lnk", "Meet Joe Black - https://www.imdb.com/title/tt0119643/?ref_=ext_shr_lnk", "A Star is Born - https://www.imdb.com/title/tt1517451/?ref_=ext_shr_lnk", "Me before you - https://www.imdb.com/title/tt2674426/?ref_=ext_shr_lnk", "Romeo and Juliet - https://www.imdb.com/title/tt0117509/?ref_=ext_shr_lnk", "Ghost - https://www.imdb.com/title/tt0099653/?ref_=ext_shr_lnk", "My girl - https://www.imdb.com/title/tt0102492/?ref_=ext_shr_lnk"],
        "adventures": ["Indiana Jones - https://www.imdb.com/title/tt0097576/?ref_=ext_shr_lnk", "Pirates of the Caribbean - https://www.imdb.com/title/tt0325980/?ref_=ext_shr_lnk", "Jumanji - https://www.imdb.com/title/tt2283362/?ref_=ext_shr_lnk"," Mr Been Holiday -  https://youtu.be/hSxLUd8aly4?si=dMlC573D_H6Y76TU", "Django - https://www.imdb.com/title/tt1853728/?ref_=ext_shr_lnk", "The crew -  https://youtu.be/TrGuYJX2tYM?si=mlX0XYDYgPTXG0eM" ],
        "romantic": ["Pride and Prejudice - https://www.imdb.com/title/tt0414387/?ref_=ext_shr_lnk", "La La Land - https://www.imdb.com/title/tt3783958/?ref_=ext_shr_lnk", "The FaultStars in Our  -  https://www.imdb.com/title/tt2582846/?ref_=ext_shr_lnk","Notting Hill - https://www.imdb.com/title/tt0125439/?ref_=ext_shr_lnk", "10 Things I Hate About You - https://www.imdb.com/title/tt0147800/?ref_=ext_shr_lnk", "Love Actually - https://www.imdb.com/title/tt0314331/?ref_=ext_shr_lnk", "Benjamin Button - https://www.imdb.com/title/tt0421715/?ref_=ext_shr_lnk"],
        "fantasy": ["The Lord of the Rings - https://www.imdb.com/title/tt0120737/?ref_=ext_shr_lnk", "Harry Potter - https://www.imdb.com/title/tt0241527/?ref_=ext_shr_lnk", "The Chronicles of Narnia - https://www.imdb.com/title/tt0363771/?ref_=ext_shr_lnk", "Alice in Wonderland - https://www.imdb.com/title/tt1014759/?ref_=ext_shr_lnk", "Stardust - https://www.imdb.com/title/tt0486655/?ref_=ext_shr_lnk", "Pan’s Labyrinth - https://www.imdb.com/title/tt0457430/?ref_=ext_shr_lnk", "The Hobbit - https://www.imdb.com/title/tt0903624/?ref_=ext_shr_lnk", "Percy Jackson - https://www.imdb.com/title/tt0814255/?ref_=ext_shr_lnk", " Maze Runner - https://www.imdb.com/title/tt1790864/?ref_=ext_shr_lnk"],
        "cartoons": ["The Lion King","Frozen", "Toy Story","Finding Nemo","Shrek","Moana","Coco","Madagascar","Up","Inside Out"],
        "zombi": ["World War Z", "Resident Evil","Train to Busan","28 Days Later","Dawn of the Dead","Zombieland","Army of the Dead","I Am Legend"]
    },

    "ru": {
        "action": ["Безумный Макс - https://yandex.ru/video/preview/12034942780454102348"," Джон Уик - https://yandex.ru/video/preview/10641844962732418263 ","быстрее пули - https://yandex.ru/video/preview/6153522411346263997 ","Черный рыцарь Бетмана - https://yandex.ru/video/preview/2608680403987910967","Гладиатор - https://yandex.ru/video/preview/2414603818404336508"," Начало - https://yandex.ru/video/preview/15093385460223896238",],
        "comedy": [" мальчик в вегасе - https://yandex.ru/video/preview/10235573619305627702"," SuperПерцы - https://yandex.ru/video/preview/8730584173425568302","час пик - https://yandex.ru/video/preview/16560468121289408783"," тупой еще тупее - https://yandex.ru/video/preview/14520068193249061166"," сводный братья - https://yandex.ru/video/preview/16829949076606585980","мачо и ботан - https://yandex.ru/video/preview/1736019921186315022"," Эйс Вентура - https://yandex.ru/video/preview/8402094611903032656","маска - https://yandex.ru/video/preview/16577272776041814523"],
        "drama": ["Побег из Шоушенка - https://yandex.ru/video/preview/16281330000920821396", "Форрест Гамп - https://yandex.ru/video/preview/286161629633046129","Крестный отец - https://yandex.ru/video/preview/7258750674900658372", "Игры разума - https://yandex.ru/video/preview/8205493610281887211", "зеленая мыля -  https://yandex.ru/video/preview/5503041099233749159", "Умница Уилл Хантинг - https://yandex.ru/video/preview/7068238162444269956", "Список Шиндлера - https://yandex.ru/video/preview/1747846058158849525", "В поисках счастья - https://yandex.ru/video/preview/6875455071189281063"],
        "horror": ["проклятие - https://yandex.ru/video/preview/16789063793990413949", "оно - https://yandex.ru/video/preview/13601113100241636869", "ужас на улице Вязов - https://yandex.ru/video/preview/11142835794257013205", "Экзорцист - https://yandex.ru/video/preview/7014508484003974921", "Реинкарнация - https://yandex.ru/video/preview/16778655416784443214", "Бабадук - https://yandex.ru/video/preview/11073019934273019617", "астрал  - https://yandex.ru/video/preview/2491590929854220076", "Синистер  - https://yandex.ru/video/preview/6644946582230537249"],
        "detective": ["Шерлок Холмс -  https://yandex.ru/video/preview/15793541728329115914"," семь - https://yandex.ru/video/preview/307086500442259807","турист - https://yandex.ru/video/preview/8590670155744106330", "Достать ножи - https://yandex.ru/video/preview/14906436005183366061","Исчезнувшая - https://yandex.ru/video/preview/7547630591646287521"," олдбой  - https://yandex.ru/video/preview/4110829553826744794","Пленницы - https://yandex.ru/video/preview/2747402130202894414 ","паразиты - https://yandex.ru/video/preview/3246945268619132565"],
        "melodrama": ["Титаник - https://yandex.ru/video/preview/15725940565755690730","Дневник памяти - https://yandex.ru/video/preview/2310616134923302127 "," Мистер и миссис Смит - https://yandex.ru/video/preview/2353269466624609524"," Знакомьтесь, Джо Блэк - https://yandex.ru/video/preview/15929178578549142347"," Звезда родилась - https://yandex.ru/video/preview/205116134661761565"," До встречи с тобой - https://yandex.ru/video/preview/4311312537361631611"," Ромео и Джульетта - https://yandex.ru/video/preview/12843887855521099112", "призрак - https://yandex.ru/video/preview/8066443198876726868", "Моя девочка - https://yandex.ru/video/preview/6568658603939062084"],
        "adventures": ["Индиана Джонс - https://yandex.ru/video/preview/1465286013999443512"," Пираты Карибского моря - https://yandex.ru/video/preview/2484618363851037162 ","Джуманджи - https://yandex.ru/video/preview/12581397459883651274","Мистер Бин на отдыхе - https://yandex.ru/video/preview/9701536745634806876","Джанго освобожденный - https://yandex.ru/video/preview/11709251018688485847","Экипаж - https://yandex.ru/video/preview/1181983750134664029"],
        "romantic": ["гордость и предубеждение - https://yandex.ru/video/preview/699521713314786762 "," La La Land - https://yandex.ru/video/preview/9909980561903561788","Виноваты звёзды  - https://yandex.ru/video/preview/1029374615191832428"," Ноттинг-Хилл - https://yandex.ru/video/preview/12162102337876979936"," 10 вещей, которые я ненавижу в тебе - https://yandex.ru/video/preview/7971243644093620662"," настоящая любовь - https://yandex.ru/video/preview/15464780081932162155","benjamin button - https://yandex.ru/video/preview/11337546526107439557"],
        "fantasy": ["Властелин колец  - https://yandex.ru/video/preview/5753178030029492832","Гарри Поттер - https://yandex.ru/video/preview/8941262572811513554 "," Королевство Нарния - https://yandex.ru/video/preview/6637898489663527616 "," Алиса в Стране Чудес - https://yandex.ru/video/preview/12202391922250238400"," Звездная пыль - https://yandex.ru/video/preview/12123862917419392420"," Лабиринт Пан - https://yandex.ru/video/preview/1216798461472116672","Хоббит - https://yandex.ru/video/preview/16037394492439347218", "Перси Джексон - https://yandex.ru/video/preview/15476031515185226004","бегущий в лабиринте - https://yandex.ru/video/preview/14678305615702676294"],
        "cartoons": ["Король Лев - https://yandex.ru/video/preview/7373168796289264027","Холодное сердце - https://yandex.ru/video/preview/3931557286666517001", "История игрушек - https://yandex.ru/video/preview/11579379110369664194", "В поисках Немо - https://yandex.ru/video/preview/7614631620522292714",  "Шрек - https://yandex.ru/video/preview/17885180959692684453",   "Моана - https://yandex.ru/video/preview/1908661046523880724",  "Тайна Коко - https://yandex.ru/video/preview/6448277326917432983",   "Мадагаскар - https://yandex.ru/video/preview/6262207131847990480","Вверх - https://yandex.ru/video/preview/13427568553488888523","Головоломка  - https://yandex.ru/video/preview/2036830259156938755"],
        "zombi": [ "Война миров Z - https://yandex.ru/video/preview/15834093964777652438", "Обитель зла - https://yandex.ru/video/preview/12725293418865249480", "Поезд в Пусан - https://yandex.ru/video/preview/1058089952645602086","28 дней спустя - https://yandex.ru/video/preview/207721904695828637","Рассвет мертвецов - https://yandex.ru/video/preview/16160611712617596589","Добро пожаловать в Zомбилэнд - https://yandex.ru/video/preview/9861466346593021887", "Армия мертвецов - https://yandex.ru/video/preview/10276233339808130409","Я — легенда - https://yandex.ru/video/preview/16909271728467165316"] 
    },

    "uz": {
        "action": ["Telba Max - http://asilmedia.org/9775-aqlsiz-maks-uzbek-tilida-2015-full-hd-4k-ozbek-tarjima-tas-ix-skachat.html", "Jon Uik - http://asilmedia.org/7189-jon-uik-uzbek-ozbek-tilida-tas-ix-skachat-download.html", "O`qdan tez - http://asilmedia.org/14491-oqdan-tez-tezkor-oqlar-bred-pitt-ishtirokida-uzbek-tilida-2022-ozbekcha-tarjima-film-full-hd-skachat.html","Betman Qora ritser - http://asilmedia.org/8580-betmen-jokerga-qarshi-qora-ritsar-temnyy-rycar-betmen-protiv-dzhokera-hd-uzbek-ozbek-tilida-tas-ix-skachat-download.html","Gladiator - http://asilmedia.org/7922-gladiator-uzbek-ozbek-tilida-tas-ix-skachat-download.html","Muqqadima - http://asilmedia.org/10761-muqaddima-uzbek-tilida-2010-ozbek-tarjima-kino-hd.html",],
        "comedy": [ "Ajoyib dostlar - https://yandex.ru/video/preview/10235573619305627702", "Tig`iz payt  - http://asilmedia.org/2673-tigiz-payt-chas-pik.html","Ahmoqdan ahmoqroq - https://yandex.ru/video/preview/5240208174658768640","Birodarlar - https://yandex.ru/video/preview/16829949076606585980", "Ko`rkam va semiz  - https://yandex.ru/video/preview/1736019921186315022", "Ace Ventura - http://asilmedia.org/7912-eys-ventura-super-komediya-uzbek-ozbek-tilida-tas-ix-skachat-download.html", "Niqob - http://asilmedia.org/10008-niqob-uzbek-tilida-1994-hd-ozbek-tarjima-tas-ix-skachat.html"],
        "drama": ["Showshankdan Qochish - http://asilmedia.org/7540-shoushenkdan-qochsih-uzbek-ozbek-tilida-tas-ix-skachat-download.html", "Forrest Gump - https://kinolar.tv/load/komedija/forrest_gamp_uzbek_tilida_1994_kino_skachat_fhd/17-1-0-5107", "Cho`qintirgan ota - https://yandex.ru/video/preview/12097537868097486232","Qoidalarsiz o'yin - http://asilmedia.org/11423-qoidalarsiz-oyin-girrom-oyin-uzbek-tilida-2010-ozbekcha-tarjima-kino-hd.html", "yashil maskan - https://yandex.ru/video/preview/14249570244539021863", "Metin Iroda ovi - https://yandex.ru/video/preview/16491320964520153494", "Shindler ro'yxati - https://yandex.ru/video/preview/10833520297864770630", "Baxt izlab - https://yandex.ru/video/preview/8775926908991309239"],
        "horror": ["Lanat - https://yandex.ru/video/preview/1645476799433543386", "Ono -  http://asilmedia.org/10770-u-u-1-ono-1-ozbekcha-subtitr-uzbek-tilida-2017-ozbek-tarjima-kino-hd.html", "Exorcist - http://asilmedia.org/15250-ekzorsist-vatikan-jin-chiqaruvchisi-ujas-kino-uzbek-tilida-2023-ozbekcha-tarjima-kino-hd.html",  " Babaduk - https://yandex.ru/video/preview/2788913059885672821", "Astral - https://yandex.ru/video/preview/3203663039931224226", "Sinister dahshati - https://uzmovi.co/tarjima-kinolar/1082-sinister-1-uzbek-tilida.html"],
        "detective": ["Sherlok Xolms - http://asilmedia.org/7732-sherlok-holms-uzbek-ozbek-tilida-tas-ix-skachat-download.html", "Yetti - http://asilmedia.org/15841-yetti-se7en-uzbek-tilida-1995-ozbekcha-tarjima-kino-hd.html", "Turist - http://asilmedia.org/9590-turist-ozbek-tilida-2010-uzbekcha-tarjima-turist-the-tourist-tas-ix-skachat.html","Tig`idan chiqqan Pichoqlar - https://yandex.ru/video/preview/3140119434558002749", "Old boy - http://asilmedia.org/12306-oldboy-uzbek-tilida-2003-ozbekcha-tarjima-kino-hd.html", "Asiralar - https://yandex.ru/video/preview/17691507523491699988 ", "Parazitlar - https://yandex.ru/video/preview/13235961790498591313"],
        "melodrama": ["Titanik - http://kinolaruz.ru/films/tarjima_kinolar/9516-titanik-uzbekcha-tarjima-1997-ozbek-tilida-titanik-titanic-tas-ix-skachat.html", "Xotira kundaligi - https://yandex.ru/video/preview/136725144904590379", "Janob va Xonim smit - https://yandex.ru/video/preview/2457399387001541533","Tanishing Joe Black - https://yandex.ru/video/preview/17948082466725053144", "sizdan oldingi hayotim - http://asilmedia.org/10756-sen-bilan-uchrashguncha-uzbek-tilida-2016-ozbek-tarjima-kino-hd.html","Romeo va Julieta - https://yandex.ru/video/preview/12843887855521099112", "Arvoh - https://yandex.ru/video/preview/8066443198876726868", "mening qizim - https://yandex.ru/video/preview/16407352390098880157"],
        "adventures": ["Indiana Jones - https://yandex.ru/video/preview/16330929273905173469", "Karib Dengizi Qaroqchilari - https://yandex.ru/video/preview/12542628625363550149", "Jumanji - http://asilmedia.org/2179-jumanji-2-jungle-chorlaydi-premyera.html", "Mr Bin sayohatda - https://yandex.ru/video/preview/2534396966292719590 ","Jango -  http://asilmedia.org/10979-ozod-jango-uzbek-tilida-2012-ozbekcha-tarjima-kino-hd.html", "Ekipaj - https://uzbeklar.tv/1900-ekipaj.html"],
        "romantic": ["Mag'rurlik va Xurofot  - https://yandex.ru/video/preview/9088161923029610950", "La La Land - http://asilmedia.org/8478-la-la-lend-zheleznyy-chelovek-3-uzbek-ozbek-tilida-tas-ix-skachat-download.html","Yulduzlar Aybi - https://yandex.ru/video/preview/17276876668447674446","Noting Hill - https://yandex.ru/video/preview/15200152430813361107"," Men Sizdan Nafratlanadigan 10 Narsa - https://yandex.ru/video/preview/7971243644093620662", "Asl Sevgi - http://asilmedia.org/7448-asl-sevgi-uzbek-ozbek-tilida-tas-ix-skachat-download.html", "Benjamin Button - https://uzmovii.org/tarjima-kinolar/5443-benjamin-buttonning-qiziq-voqeasi-uzbek-tilida.html"],
        "fantasy": ["Uzuklar Humdori - http://asilmedia.org/4349-uzuklar-hukmdori-1-ozbek-tilida.html", "Garri Potter - http://asilmedia.org/9060-garri-potter-1-hikmatlar-toshi-uzbek-tarjima-2001-hd-ozbek-tilida-tas-ix-skachat.html", "Narniya Saltanati - https://yandex.ru/video/preview/7015118863288643731","Alisa mojizalar mamlakatida - https://yandex.ru/video/preview/12202391922250238400", "Samoviy yo`l - https://yandex.ru/video/preview/12659530076485604669", "Pan labirint - https://yandex.ru/video/preview/1216798461472116672", "Xobbit - http://asilmedia.org/3242-hobbit-ozbek-tilida.html", "Persi Jekson - https://yandex.ru/video/preview/14563292618104779272","labirintdagilar - https://yandex.ru/video/preview/11183099952095180430"],
        "cartoons": ["Qirol Sher - https://yandex.ru/video/preview/4059648044563124773","Muzlagan Yurak - https://yandex.ru/video/preview/10304723914127994097","O‘yinchoqlar Tarixi - https://yandex.ru/video/preview/7680820679287429279","Nemoni izlab - https://uzmovi.bot/multfilmlar/110-nemoni-izlab-uzbek-tilida.html","Shrek - http://asilmedia.org/10124-shrek-1-multfilm-uzbek-tilida-2001-ozbek-tarjima-tas-ix-skachat.html","Moana - https://yandex.ru/video/preview/886739817132031323","Koko Siri - https://uzmovi.bot/multfilmlar/417-kokoning-siri-koko-siri-uzbek-tilida.html","Madagaskar - https://yandex.ru/video/preview/9385154595883608549","Yuqoriga - https://yandex.ru/video/preview/13427568553488888523","Boshqotirma - https://yandex.ru/video/preview/4941111220720963070"],
        "zombi": ["Z jahon urushi - https://yandex.ru/video/preview/17869777242893002046", "Yovuzlik maskani - https://yandex.ru/video/preview/16851678046823618734", "Pusanga  ketyotgan poyezd - https://yandex.ru/video/preview/1058089952645602086", "28 kundan keyin - https://yandex.ru/video/preview/207721904695828637", "O‘liklar tongi - https://yandex.ru/video/preview/16160611712617596589",  "Zombilend - https://yandex.ru/video/preview/9861466346593021887", "O‘liklar armiyasi - https://yandex.ru/video/preview/10916926107580855028","Men afsonaman - https://yandex.ru/video/preview/5671921437243688738"]
    }
}


series_list = {
    "en": [
        "Breaking Bad", "Game of Thrones", "Stranger Things", "All of us are dead", "Bloodhound",
        "Prison Break", "Chernobyl", "alice in borderland", "from", "Better Call Saul",
        "Peaky Blinders", "Money Heist", "Friends", "Succesion", "House of Cards",
        "Narcos", "Squid game", "The Boys", "Loki", "The Last of Us"
    ],
    "ru": [
       "Во все тяжкие", "Игра престолов", "Очень странные дела", "Мы все мертвы", "",
        "Побег", "Чернобыль", "Алиса в Пограничье", "Извне", "Лучше звоните Солу",
        "Острые козырьки", "Бумажный дом", "Друзья", "наследники", "Карточный домик",
        "Нарко", "Игра в кальмара", "Пацаны", "Локи", "Одни из нас"
    ],
    "uz": [
        "Mashaqqatlar sari", "Taxtlar o‘yini", "G‘alati ishlar", "Biz Hammamiz o`likmiz", "Qonxor itlar",
        "Panjara ortida", "Chernobil", "Ajal o`yini", "Dan", "Yaxshisi Saulga qo‘ng‘iroq qiling",
        "SHelbilar oilasi", "Qog`oz bino", "Do‘stlar", "Vorislar", "Kartalar uyi ",
        "Narkos", "Klamar o`yini", "Yiggitlar", "Loki", "Biz so`ngilarmiz"
    ]
}



# Start komandasini ishlatish
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("O'zbek🇺🇿",callback_data = "uz" )
    btn2 = types.InlineKeyboardButton("English🇺🇸",callback_data = "en" )
    markup.row(btn1)
    btn3 = types.InlineKeyboardButton("Русский🇷🇺",callback_data = "ru" )   
    markup.add(btn2, btn3) 


    bot.send_message(message.chat.id, "Please choose your language: \n Выберите язык: \n Iltimos janrni tanlang:", reply_markup=markup)

    
    # Reply Keyboard (doimiy pastda turadigan tugmalar)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_movie = types.KeyboardButton("/movie")
    btn_clear = types.KeyboardButton("/clear")
    btn_series = types.KeyboardButton("/series")
    markup.add(btn_movie,  btn_series, btn_clear)

    bot.send_message(message.chat.id, "@searchmovie77_bot", reply_markup=markup)


 
# Til tanlashni qayta ishlash
@bot.callback_query_handler(func=lambda call: call.data in ["en", "ru", "uz"])
def handle_language_selection(call):
    language = call.data
    user_languages[call.from_user.id] = language  # Foydalanuvchi tilini saqlash

    # "Kinolar" va "Seriallar" tugmalarini chiqarish
    markup = types.InlineKeyboardMarkup()
    btn_movies = types.InlineKeyboardButton("🎬 Kino", callback_data="category_movies")
    btn_series = types.InlineKeyboardButton("📺 Serial", callback_data="category_series")
    markup.add(btn_movies, btn_series)

    if language == "en":
        bot.send_message(call.message.chat.id, "What would you like to watch?", reply_markup=markup)
    elif language == "ru":
        bot.send_message(call.message.chat.id, "Что вы хотите посмотреть?", reply_markup=markup)
    elif language == "uz":
        bot.send_message(call.message.chat.id, "Nimani ko‘rmoqchisiz?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("category"))
def handle_category_selection(call):
    language = user_languages.get(call.from_user.id, "en")  # Foydalanuvchining tilini olish

    if call.data == "category_movies":
        show_genre_selection(call, language )
    elif call.data == "category_series":
        show_series_selection(call)


@bot.callback_query_handler(func=lambda call: call.data == "category_series")
def show_series_selection(call):
    language = user_languages.get(call.from_user.id, "en")  # Foydalanuvchining tilini olish

    selected_series = series_list.get(language, [])  # Serial ro‘yxatini olish

    if not selected_series:
        bot.answer_callback_query(call.id, "No series available.")
        return

    markup = types.InlineKeyboardMarkup()  # Xatolikni tuzatish
    for series in selected_series:
        if " - " in series:  # Agar serial havolasi bo‘lsa
            series_name, series_link = series.split(" - ")
            btn = types.InlineKeyboardButton(series_name, url=series_link)
        else:
            btn = types.InlineKeyboardButton(series, callback_data="none")
        markup.add(btn)

    messages = {
        "uz": "📺 Mavjud seriallar:",
        "ru": "📺 Доступные сериалы:",
        "en": "📺 Available series:"
    }

    bot.send_message(  # `edit_message_text` o‘rniga `send_message` ishlatamiz
        chat_id=call.message.chat.id,
        text=messages.get(language, messages["uz"]),
        reply_markup=markup
    )


# kinolarni korsatish
def show_genre_selection(call, language):
    markup = types.InlineKeyboardMarkup()
    for genre_key, genre_name in movie_genres[language].items():
        btn = types.InlineKeyboardButton(genre_name, callback_data=f"genre_{genre_key}")
        markup.add(btn)

    if language == "en":
        bot.send_message(call.message.chat.id, "Choose a movie genre:", reply_markup=markup)
    elif language == "ru":
        bot.send_message(call.message.chat.id, "Выберите жанр фильма:", reply_markup=markup)
    elif language == "uz":
        bot.send_message(call.message.chat.id, "Kino janrini tanlang:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("genre"))
def handle_genre_selection(call):
    genre_key = call.data.split("_")[1]  # Tanlangan janrni olish
    language = user_languages.get(call.from_user.id, "en")  # Foydalanuvchining tilini olish
    genre_name = movie_genres[language].get(genre_key, "Unknown Genre")

    # Tanlangan janrga mos kinolarni topish
    selected_movies = movie_list.get(language, {}).get(genre_key, [])

    if not selected_movies:
        bot.answer_callback_query(call.id, "No movies available for this genre.")
        return  



    
# Inline tugmalar yaratish
    markup = types.InlineKeyboardMarkup()
    for movie in selected_movies:
        if " - " in movie:  # Agar film havolasi bo'lsa
            movie_name, movie_link = movie.split(" - ")
            btn = types.InlineKeyboardButton(movie_name, url=movie_link)
        else:
            btn = types.InlineKeyboardButton(movie, callback_data="none")
        markup.add(btn)

    # Uch tilda chiqarish
    messages = {
        "uz": f"🎬 {genre_name} :",
        "ru": f"🎬 Фильмы в жанре {genre_name}:",
        "en": f"🎬 Movies in the {genre_name} genre:"
    }

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=messages.get(language, messages["uz"]),
        reply_markup=markup

    )

@bot.message_handler(commands=['clear'])
def clear_messages(message):

    # So‘nggi 10 ta xabarni o‘chirish
    for i in range(message.message_id, message.message_id - 2, -1):
        try:
            bot.delete_message(message.chat.id, i)
        except Exception:
            continue
    
 

@bot.message_handler(commands=['search'])
def search_movie(message):
    query = message.text.replace('/search', '').strip().lower()
    results = []

    # Foydalanuvchining tilini aniqlash (bu joyni foydalanuvchining real tanloviga bog'lash mumkin)
    user_language = "uz"  # Buni dinamik qilish uchun foydalanuvchi tilini saqlash mexanizmi qo'shish kerak

    # Har bir til uchun natija xabarlari
    messages = {
        "uz": {"found": "🔍 Natijalar:\n", "not_found": "😕 Hech narsa topilmadi."},
        "ru": {"found": "🔍 Результаты:\n", "not_found": "😕 Ничего не найдено."},
        "en": {"found": "🔍 Results:\n", "not_found": "😕 Nothing found."}
    }

    # Qidiruv natijalarini olish
    if user_language in movie_list:
        for genre in movie_list[user_language]:
            for movie in movie_list[user_language][genre]:
                if query in movie.lower():
                    results.append(movie)

    # Natijalarni chiqarish
    if results:
        bot.send_message(message.chat.id, messages[user_language]["found"] + "\n".join(results))
    else:
        bot.send_message(message.chat.id, messages[user_language]["not_found"])

     

# /movie komandasi uchun handler
@bot.message_handler(commands=['movie'])
def movie(message):
    # Foydalanuvchi tilini aniqlash
    language = user_languages.get(message.from_user.id, "en")


    # Inline tugmalarini yaratish
    markup = types.InlineKeyboardMarkup()
    for genre_key, genre_name in movie_genres[language].items():
        markup.add(types.InlineKeyboardButton(genre_name, callback_data=f"genre_{genre_key}"))

    if language == "en":
        bot.send_message(message.chat.id, "Choose a movie genre",reply_markup=markup)
    elif language == "ru":
        bot.send_message(message.chat.id, "выберите жанр фильма:", reply_markup=markup)
    elif language == "uz":
        bot.send_message(message.chat.id, "Kino janrini tanlang:", reply_markup=markup)

        
@bot.message_handler(commands=['series'])
def series(message):
    # Foydalanuvchi tilini aniqlash
    language = user_languages.get(message.from_user.id, "en")

    # Inline tugmalarini yaratish
    markup = types.InlineKeyboardMarkup()
    for series_name in series_list[language]:  # Serial nomlarini olish
        markup.add(types.InlineKeyboardButton(series_name, callback_data=f"series_{series_name}"))

    if language == "en":
        bot.send_message(message.chat.id, "Choose a series:", reply_markup=markup)
    elif language == "ru":
        bot.send_message(message.chat.id, "Выберите сериал:", reply_markup=markup)
    elif language == "uz":
        bot.send_message(message.chat.id, "Serialni tanlang:", reply_markup=markup)
        

# Help komandasini ishlatish
@bot.message_handler(commands=['help'])
def help(message):
    language = user_languages.get(message.from_user.id, "en")  # Foydalanuvchining tilini olish
    


    if language == "en":
        bot.send_message(message.chat.id, "/start - updates bot \n /movie - releases the genre of movies \n /search found movie if you write name")
    elif language == "ru":
        bot.send_message(message.chat.id, "/start - обновляет bot \n /movie - выпускает жанр \n /search  найденный фильм, если вы введете название")
    elif language == "uz":
        bot.send_message(message.chat.id, "/start - botni yangilaydi \n /movie - kinolar janrini chiqaradi \n /search bilan kino nomini yozsangiz topib beradi")

# Google orqali qidirish
"""
def search_google(query):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx=GOOGLE_CSE_ID).execute()
    return res.get("items", [])

# Rasmni Google Vision AI orqali tahlil qilish
def analyze_image(image_bytes):
    image = vision.Image(content=image_bytes)
    response = VISION_CLIENT.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    return labels

# Foydalanuvchi rasm yuborganda ishlov berish
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_info.file_path}"
    
    # Rasmni yuklab olish
    image_response = requests.get(file_url)
    image_bytes = image_response.content

    # Rasmni Google Vision AI orqali tekshirish
    labels = analyze_image(image_bytes)
    
    # Kino nomini taxmin qilish
    possible_movies = [label for label in labels if "film" in label.lower() or "movie" in label.lower()]
    if not possible_movies:
        bot.reply_to(message, "Bu rasm kinoga tegishli ekanligini aniqlay olmadim.")
        return

    movie_name = possible_movies[0]  # Eng mos kelgan nomni olish
    search_results = search_google(movie_name)

    # Natijalarni foydalanuvchiga jo‘natish
    if search_results:
        result = search_results[0]  # Eng birinchi natijani olish
        title = result.get("title", "Noma'lum film")
        link = result.get("link", "Havola topilmadi")
        snippet = result.get("snippet", "Tavsif mavjud emas")

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Batafsil ma’lumot", url=link))

        bot.reply_to(message, f"🔍 **Topilgan film:** {title}\n📖 {snippet}", reply_markup=markup)
    else:
        bot.reply_to(message, "Bu rasmga oid film haqida ma’lumot topilmadi.")



"""
bot.polling(none_stop=True)

