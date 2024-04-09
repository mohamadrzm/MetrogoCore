from dijkstar import Graph, find_path
import logging
import Levenshtein
# Metro stations in English
line_1 = (

    'tajrish',
    'gheytariyeh',
    'shahid-sadr',
    'gholhak',
    'doctor-shariati',
    'shahid-haghani',
    'shahid-hemmat',
    'mosalla-ye-emam-khomeini',
    'shahid-beheshti',
    'shohada-ye-haftom-e-tir',
    'ayatollah-taleghani',
    'darvazeh-dowlat',
    'sadi',
    'emam-khomeini',
    'panzdah-e-khordad',
    'khayyam',
    'meydan-e-mohammadiyeh',
    'shoush',
    'shahid-bokharaei',
    'ali-abad',
    'javanmard-e-ghassab',
    'shahr-e-rey',
    'palayeshgah',
    'shahed',
    'namayeshgah-e-shahr-e-aftab',
    'vavan',
    'imam-khomeini-airport',
    'shahed',
    'haram-motahhar-e-imam-khomeini',
    'kahrizak'

)
line_2 = (

    'farhangsara',
    'tehranpars',
    'shahid-bagheri',
    'daneshgah-e-elm-o-sanat',
    'sarsabz',
    'janbazan',
    'fadak',
    'sabalan',
    'shahid-madani',
    'emam-hossein',
    'darvazeh-shemiran',
    'baharestan',
    'mellat',
    'emam-khomeini',
    'hasan-abad',
    'daneshgah-e-emam-ali',
    'meydan-e-horr',
    'shahid-navab-e-safavi',
    'shademan',
    'daneshgah-e-sharif',
    'tardasht',
    'sadeghiyeh',

)
line_3 = (

    'azadegan',
    'nemat-abad',
    'abdol-abad',
    'shahrak-e-valiasr',
    'zamzam',
    'javadiyeh',
    'rahahan',
    'mahdiyeh',
    'moniriyeh',
    'teatr-e-shahr',
    'meydan-e-hazrat-e-valiasr',
    'meydan-e-jahad',
    'mirza-ye-shirazi',
    'shahid-beheshti',
    'sohrevardi',
    'shahid-ghodousi',
    'shahid-sayyad-e-shirazi',
    'khajeh-abdollah-e-ansari',
    'shahid-zeynoddin',
    'meydan-e-heravi',
    'hossein-abad',
    'nobonyad',
    'aghdasiyeh',
    'shahid-mahallati',
    'ghaem',

)
line_4 = (

    'shahid-kolahdouz',
    'nirou-havaei',
    'nabard',
    'pirouzi',
    'ebn-e-sina',
    'meydan-e-shohada',
    'darvazeh-shemiran',
    'darvazeh-dowlat',
    'ferdowsi',
    'teatr-e-shahr',
    'meydan-e-enghelab-e-eslam',
    'towhid',
    'shademan',
    'doctor-habibollah',
    'ostad-moein',
    'meydan-e-azadi',
    'bimeh',
    'shahrak-e-ekbatan',
    'eram-e-sabz',
    'allameh-jafari',
    'ayatollah-kashani',
    'chaharbagh',

)
line_5 = (

    'sadeghiyeh',
    'eram-e-sabz',
    'varzeshgah-e-azadi',
    'chitgar',
    'iran-khodro',
    'vardavard',
    'garmdarreh',
    'atmosfer',
    'karaj',
    'mohammad-shahr',
    'golshahr',
    'shahid-sepahbod-ghasem-soleimani',

)
line_6 = (

    'haram-e-hazrat-e-abdolazim',
    'meydan-e-hazrat-e-abdolazim',
    'ebn-e-babviyeh',
    'cheshmeh-ali',
    'shohada-ye-dowlat-abad',
    'kiyan-shahr',
    'besat',
    'shahid-rezaei',
    'meydan-e-khorasan',
    'shohada-ye-hefdah-e-shahrivar',
    'amir-kabir',
    'meydan-e-shohada',
    'emam-hossein',
    'sarbaz',
    'bahar-shiraz',
    'shohada-ye-haftom-e-tir',
    'shahid-nejatollahi',
    'meydan-e-hazrat-e-valiasr',
    'boostan-e-laleh',
    'kargar',
    'daneshgah-e-tarbiat-modarres',
    'shahrak-e-azmayesh',
    'marzdaran',
    'yadegar-e-emam',
    'shahid-ashrafi-esfahani',
    'shahid-satari',
    'ayatollah-kashani',
    'shahr-e-ziba',
    'shahran',
    'shohada-ye-kan',
    'kouhsar',

)
line_7 = (

    'varzeshgah-e-takhti',
    'basij',
    'ahang',
    'cheheltan-e-doulab',
    'shohada-ye-hefdah-e-shahrivar',
    'meydan-e-ghiyam',
    'mowlavi',
    'eydan-e-mohammadiyeh',
    'mahdiyeh',
    'helal-ahmar',
    'beryanak',
    'komeyl',
    'roudaki',
    'shahid-navab-e-safavi',
    'towhid',
    'modafean-e-salamat',
    'daneshgah-e-tarbiat-modarres',
    'boostan-e-goftegou',
    'borj-e-milan-e-tehran',
    'meydan-e-sanat',
    'shahid-dadman',


)


# Metro stations in Persian
line_1_fa = (

    'تجریش',
    'قیطریه',
    'شهید صدر',
    'قلهک',
    'دکتر شریعتی',
    'شهید حقانی',
    'شهید همت',
    'مصلی امام خمینی',
    'شهید بهشتی',
    'شهدای هفتم تیر',
    'آیت الله طالقانی',
    'دروازه دولت',
    'سعدی',
    'امام خمینی',
    'پانزده خرداد',
    'خیام',
    'میدان محمدیه',
    'شوش',
    'شهید بخارایی',
    'علی آباد',
    'جوانمرد قصاب',
    'شهری ری',
    'پالایشگاه',
    'شاهد',
    'نمایشگاه شهر آفتاب',
    'واوان',
    'فرودگاه امام خمینی',
    'شاهد',
    'حرم مطهر امام خمینی',
    'کهریزیک'

)
line_2_fa = (

    'فرهنگسرا',
    'تهرانپارس',
    'شهید باقری',
    'دانشگاه علم و صنعت',
    'سرسبز',
    'جانبازان',
    'فدک',
    'سبلان',
    'شهید مدنی',
    'امام حسین',
    'دروازه شمیران',
    'بهارستان',
    'ملت',
    'امام خمینی',
    'حسن آباد',
    'دانشگاه امام علی',
    'میدان حر',
    'شهید نواب صفوی',
    'شادمان',
    'دانشگاه شریف',
    'طردشت',
    'صادقیه',

)
line_3_fa = (

    'آزادگان',
    'نعمت آباد',
    'عبدل آباد',
    'شهرک ولیعصر',
    'زمزم',
    'جوادیه',
    'راه آهن',
    'مهدیه',
    'منیریه',
    'تئاتر شهر',
    'میدان حضرت ولیعصر',
    'میدان جهاد',
    'میرزای شیرازی',
    'شهید بهشتی',
    'سهروردی',
    'شهید قدوسی',
    'شهید سید شیرازی',
    'خاجه ابدالله انصاری',
    'شهید زین الدین',
    'میدان هروی',
    'حسین آباد',
    'نبنیاد',
    'اقدسیه',
    'شهید محلاتی',
    'قائم',

)
line_4_fa = (

    'شهید کلاهدوز',
    'نیرو هوایی',
    'نبرد',
    'پیروزی',
    'ابن سینا',
    'میدان شهدا',
    'دروازه شمیران',
    'دروازه دولت',
    'فردوسی',
    'تئاتر شهر',
    'میدان انقلاب اسلامی',
    'توحید',
    'شادمان',
    'دکتر حبیب الله',
    'استاد معین',
    'میدان آزادی',
    'بیمه',
    'شهرک اکباتان',
    'ارم سبز',
    'علامه جعفری',
    'آیت الله کاشانی',
    'چهارباغ',

)
line_5_fa = (

    'صادقیه',
    'ارم سبز',
    'ورزشگاه آزادی',
    'چیتگر',
    'ایران خودرو',
    'ورداورد',
    'گرم دره',
    'اتمسفر',
    'کرج',
    'محمد شهر',
    'گلشهر',
    'شهید سپهبد قاسم سلیمانی',

)
line_6_fa = (

    'حرم حضرت عبدالعظیم',
    'میدان حضرت عبدالعظیم',
    'ابن بابویه',
    'چشمه علی',
    'شهدای دولت آباد',
    'کیان شهر',
    'بعثت',
    'شهید رضایی',
    'میدان خراسان',
    'شهدای هفده شهریور',
    'امیر کبیر',
    'میدان شهدا',
    'امام حسین',
    'سرسبز',
    'بهار شیراز',
    'شهدای هفتم تیر',
    'شهید تجات اللهی',
    'میدان حضرت ولیعصر',
    'بوستان لاله',
    'کارگر',
    'دانشگاه تربیت مدرس',
    'شهرک آزمایش',
    'مرزداران',
    'یادگار امام',
    'شهید اشرفی اصفهانی',
    'شهید ستاری',
    'آیت الله کاشانی',
    'شهره زیبا',
    'شهران',
    'شهدای کن',
    'کوهسار',

)
line_7_fa = (

    'ورزشگاه تختی',
    'بسیج',
    'آهنگ',
    'چهل تن دولاب',
    'شهدای هفتم شهریور',
    'میدان قیام',
    'مولوی',
    'میدان محمدیه',
    'مهدیه',
    'هلال احمر',
    'بریانک',
    'کمیل',
    'رودکی',
    'شهید نواب صفوی',
    'توحید',
    'مدافعان سلامت',
    'دانشگاه تربیت مدرس',
    'بوستان گفت و گو',
    'برج میلاد تهران',
    'میدان صنعت',
    'شهید دادمان',


)


def find_best_path_en(source: str, dist: str):
    graph = Graph()

# --- Line 1
    number = -2
    number2 = -1
    for i in range(len(line_1)):
        try:
            graph.add_edge(
                line_1[number2], line_1[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass

    number = 0
    number2 = 1
    for i in range(len(line_1)):
        try:
            graph.add_edge(
                line_1[number], line_1[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 2

    number = -2
    number2 = -1

    for i in range(len(line_2)):
        try:
            graph.add_edge(
                line_2[number2], line_2[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_2)):
        try:
            graph.add_edge(
                line_2[number], line_2[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 3

    number = -2
    number2 = -1

    for i in range(len(line_3)):
        try:
            graph.add_edge(
                line_3[number2], line_3[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_3)):
        try:
            graph.add_edge(
                line_3[number], line_3[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 4

    number = -2
    number2 = -1

    for i in range(len(line_4)):
        try:
            graph.add_edge(
                line_4[number2], line_4[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_4)):
        try:
            graph.add_edge(
                line_4[number], line_4[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 5

    number = -2
    number2 = -1
    for i in range(len(line_5)):
        try:
            graph.add_edge(
                line_5[number2], line_5[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_5)):
        try:
            graph.add_edge(
                line_5[number], line_5[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 6

    number = -2
    number2 = -1

    for i in range(len(line_6)):
        try:
            graph.add_edge(
                line_6[number2], line_6[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass

    number = 0
    number2 = 1
    for i in range(len(line_6)):
        try:
            graph.add_edge(
                line_6[number], line_6[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 7

    number = -2
    number2 = -1

    for i in range(len(line_7)):
        try:
            graph.add_edge(
                line_7[number2], line_7[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_7)):
        try:
            graph.add_edge(
                line_7[number], line_7[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

    return find_path(graph, source, dist)[0]
    del number
    del number2
    del graph


def find_best_path_fa(source: str, dist: str):

    graph = Graph()
# --- Line 1
    number = -2
    number2 = -1

    for i in range(len(line_1_fa)):
        try:
            graph.add_edge(
                line_1_fa[number2], line_1_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass

    number = 0
    number2 = 1

    for i in range(len(line_1_fa)):
        try:
            graph.add_edge(
                line_1_fa[number], line_1_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 2

    number = -2
    number2 = -1

    for i in range(len(line_2_fa)):
        try:
            graph.add_edge(
                line_2_fa[number2], line_2_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_2_fa)):
        try:
            graph.add_edge(
                line_2_fa[number], line_2_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 3

    number = -2
    number2 = -1

    for i in range(len(line_3_fa)):
        try:
            graph.add_edge(
                line_3_fa[number2], line_3_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_3_fa)):
        try:
            graph.add_edge(
                line_3_fa[number], line_3_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 4

    number = -2
    number2 = -1

    for i in range(len(line_4_fa)):
        try:
            graph.add_edge(
                line_4_fa[number2], line_4_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_4_fa)):
        try:
            graph.add_edge(
                line_4_fa[number], line_4_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 5

    number = -2
    number2 = -1
    for i in range(len(line_5_fa)):
        try:
            graph.add_edge(
                line_5_fa[number2], line_5_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_5_fa)):
        try:
            graph.add_edge(
                line_5_fa[number], line_5_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 6

    number = -2
    number2 = -1

    for i in range(len(line_6_fa)):
        try:
            graph.add_edge(
                line_6_fa[number2], line_6_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass

    number = 0
    number2 = 1
    for i in range(len(line_6_fa)):
        try:
            graph.add_edge(
                line_6_fa[number], line_6_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

# --- Line 7

    number = -2
    number2 = -1

    for i in range(len(line_7_fa)):
        try:
            graph.add_edge(
                line_7_fa[number2], line_7_fa[number], 1)
            number = number - 1
            number2 = number2 - 1
        except:
            pass
    number = 0
    number2 = 1
    for i in range(len(line_7_fa)):
        try:
            graph.add_edge(
                line_7_fa[number], line_7_fa[number2], 1)
            number = number + 1
            number2 = number2 + 1
        except:
            pass

    dictpath = {}
    paths = find_path(graph, source, dist)[0]
    for i in paths :

        if i in line_1_fa :
            dictpath[i] = 'red'
        elif i in line_2_fa :
            dictpath[i] = 'blue'
        elif i in line_3_fa :
            dictpath[i] = 'sky'
        elif i in line_4_fa :
            dictpath[i] = 'yellow'
        elif i in line_5_fa :
            dictpath[i] = 'green'
        elif i in line_6_fa :
            dictpath[i] = 'pink'
        elif i in line_7_fa :
            dictpath[i] = 'purple'

    return dictpath


def check_source_station(station: str):

    if station in line_1 or station in line_2 or station in line_3 or station in line_4 or station in line_5 or station in line_6 or station in line_7 or station in line_1_fa or station in line_2_fa or station in line_3_fa or station in line_4_fa or station in line_5_fa or station in line_6_fa or station in line_7_fa:
        return True

    else:
        return False


def check_dist_station(station: str):

    if station in line_1 or station in line_2 or station in line_3 or station in line_4 or station in line_5 or station in line_6 or station in line_7 or station in line_1_fa or station in line_2_fa or station in line_3_fa or station in line_4_fa or station in line_5_fa or station in line_6_fa or station in line_7_fa:
        return True

    else:
        return False


def check_match_name(station: str):

    allstations = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7 + \
        line_1_fa + line_2_fa + line_3_fa + line_4_fa + line_5_fa + line_6_fa + line_7_fa

    for i in allstations:

        if Levenshtein.distance(i, station) == 0:
            return i

    for i in allstations:

        if Levenshtein.distance(i, station) == 1:
            return i

    for i in allstations:

        if Levenshtein.distance(i, station) == 2:
            return i
    for i in allstations:

        if Levenshtein.distance(i, station) == 3:
            return i
    for i in allstations:

        if Levenshtein.distance(i, station) == 4:
            return i
    return 1

