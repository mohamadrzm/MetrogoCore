from dijkstar import Graph, find_path
import Levenshtein
stations_changes_fa = (
    'میدان شهدا',
    'امام حسین',
    'شهدای هفده شهریور',
    'دروازه شمیران',
    'شهید بهشتی',
    'شهدای هفتم تیر',
    'دروازه دولت',
    'امام خمینی',
    'میدان محمدیه',
    'میدان حضرت ولیعصر',
    'تئاتر شهر',
    'مهدیه',
    'شهید نواب صفوی',
    'توحید',
    'شادمان',
    'دانشگاه تربیت مدرس',
    'صادقیه',
    'ارم سبز',
    'آیت الله کاشانی',
)

line_1 = (
    'تجریش', 'قیطریه', 'شهید صدر', 'قلهک', 'دکتر شریعتی', 'شهید حقانی', 'شهید همت', 'مصلی امام خمینی',
    'شهید بهشتی', 'شهدای هفتم تیر', 'آیت الله طالقانی', 'دروازه دولت', 'سعدی', 'امام خمینی', 'پانزده خرداد',
    'خیام', 'میدان محمدیه', 'شوش', 'شهید بخارایی', 'علی آباد', 'جوانمرد قصاب', 'شهری ری', 'پالایشگاه', 'شاهد',
    'نمایشگاه شهر آفتاب', 'واوان', 'فرودگاه امام خمینی', 'شاهد', 'حرم مطهر امام خمینی', 'کهریزیک'
)
line_2 = (
    'فرهنگسرا', 'تهرانپارس', 'شهید باقری', 'دانشگاه علم و صنعت', 'سرسبز', 'جانبازان', 'فدک', 'سبلان',
    'شهید مدنی', 'امام حسین', 'دروازه شمیران', 'بهارستان', 'ملت', 'امام خمینی', 'حسن آباد', 'دانشگاه امام علی',
    'میدان حر', 'شهید نواب صفوی', 'شادمان', 'دانشگاه شریف', 'طردشت', 'صادقیه'
)
line_3 = (
    'آزادگان', 'نعمت آباد', 'عبدل آباد', 'شهرک ولیعصر', 'زمزم', 'جوادیه', 'راه آهن', 'مهدیه', 'منیریه',
    'تئاتر شهر', 'میدان حضرت ولیعصر', 'میدان جهاد', 'میرزای شیرازی', 'شهید بهشتی', 'سهروردی', 'شهید قدوسی',
    'شهید سید شیرازی', 'خاجه ابدالله انصاری', 'شهید زین الدین', 'میدان هروی', 'حسین آباد', 'نبنیاد', 'اقدسیه',
    'شهید محلاتی', 'قائم'
)
line_4 = (
    'شهید کلاهدوز', 'نیرو هوایی', 'نبرد', 'پیروزی', 'ابن سینا', 'میدان شهدا', 'دروازه شمیران', 'دروازه دولت',
    'فردوسی', 'تئاتر شهر', 'میدان انقلاب اسلامی', 'توحید', 'شادمان', 'دکتر حبیب الله', 'استاد معین',
    'میدان آزادی', 'بیمه', 'شهرک اکباتان', 'ارم سبز', 'علامه جعفری', 'آیت الله کاشانی', 'چهارباغ'
)
line_5 = (
    'صادقیه', 'ارم سبز', 'ورزشگاه آزادی', 'چیتگر', 'ایران خودرو', 'ورداورد', 'گرم دره', 'اتمسفر', 'کرج',
    'محمد شهر', 'گلشهر', 'شهید سپهبد قاسم سلیمانی'
)
line_6 = (
    'حرم حضرت عبدالعظیم', 'میدان حضرت عبدالعظیم', 'ابن بابویه', 'چشمه علی', 'شهدای دولت آباد', 'کیان شهر',
    'بعثت', 'شهید رضایی', 'میدان خراسان', 'شهدای هفده شهریور', 'امیر کبیر', 'میدان شهدا', 'امام حسین',
    'سرباز', 'بهار شیراز', 'شهدای هفتم تیر', 'شهید تجات اللهی', 'میدان حضرت ولیعصر', 'بوستان لاله', 'کارگر',
    'دانشگاه تربیت مدرس', 'شهرک آزمایش', 'مرزداران', 'یادگار امام', 'شهید اشرفی اصفهانی', 'شهید ستاری',
    'آیت الله کاشانی', 'شهره زیبا', 'شهران', 'شهدای کن', 'کوهسار'
)
line_7 = (
    'ورزشگاه تختی', 'بسیج', 'آهنگ', 'چهل تن دولاب', 'شهدای هفتم شهریور', 'میدان قیام', 'مولوی', 'میدان محمدیه',
    'مهدیه', 'هلال احمر', 'بریانک', 'کمیل', 'رودکی', 'شهید نواب صفوی', 'توحید', 'مدافعان سلامت', 'دانشگاه تربیت مدرس',
    'بوستان گفت و گو', 'برج میلاد تهران', 'میدان صنعت', 'شهید دادمان'
)

lines = [line_1, line_2, line_3, line_4, line_5, line_6, line_7]
line_colors = ['red', 'blue', 'sky', 'yellow', 'green', 'pink', 'purple']

def add_edges(graph, line):
    for i in range(len(line) - 1):
        graph.add_edge(line[i], line[i + 1], 1)
        graph.add_edge(line[i + 1], line[i], 1)

def find_best_path(source, dist, color=False):
    graph = Graph()

    for line in lines:
        add_edges(graph, line)

    if color:
        dictpath = {}
        paths = find_path(graph, source, dist)[0]
        for station in paths:
            for i, line in enumerate(lines):
                if station in line:
                    dictpath[station] = line_colors[i]
                    break
        return dictpath
    else:
        return find_path(graph, source, dist)[0]


print(find_best_path('زمزم','قلهک'))
def Checking_validity_station(station: str):

    if station in line_1 or station in line_2 or station in line_3 or station in line_4 or station in line_5 or station in line_6 or station in line_7 or station in line_1 or station in line_2 or station in line_3 or station in line_4 or station in line_5 or station in line_6 or station in line_7:
        return True

    else:
        return False


def find_line_of_station(station : str):

    if station in line_1 or station in line_1 :
        return 'line1'
    elif station in line_2 or station in line_2 :
        return 'line2'
    elif station in line_3 or station in line_3 :
        return 'line3'
    elif station in line_4 or station in line_4 :
        return 'line4'
    elif station in line_5 or station in line_5 :
        return 'line5'
    elif station in line_6 or station in line_6 :
        return 'line6'
    elif station in line_7 or station in line_7 :
        return 'line7'
    else :
        return 1
    



def check_match_name(station: str) :

    allstations = line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7 + \
        line_1 + line_2 + line_3 + line_4 + line_5 + line_6 + line_7

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
    return False
    
