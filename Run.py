try:
    import requests, re, json, time, random, string, os, datetime
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from rich.columns import Columns
    from rich.panel import Panel
    from rich.console import Console
    from rich import print as printf
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    exit(f"[Error] {str(e).capitalize()}!")

LOOPING, TEXT, SUKSES, KOMENTAR, GAGAL, FOTO, POSTINGAN, LIKE = 0, {
    "TYPE": "DEFAULT"
}, [], {
    "STATUS": True
}, [], {
    "TYPE": "1"
}, [], {
    "STATUS": True
}

def PROMPT():
    return ([
        "1. Gambar pegunungan dengan matahari terbit di latar belakang.",
        "2. Hutan yang lebat dengan air terjun di tengahnya.",
        "3. Pantai berpasir putih dengan pohon kelapa yang menjulang tinggi.",
        "4. Danau tenang dengan pantulan langit biru.",
        "5. Lembah hijau dengan sungai yang mengalir di tengahnya.",
        "6. Padang bunga liar dengan berbagai warna cerah.",
        "7. Bukit berumput hijau dengan angin yang berhembus lembut.",
        "8. Lautan luas dengan ombak yang menggulung ke pantai.",
        "9. Hutan pinus dengan kabut tipis di pagi hari.",
        "10. Gurun pasir dengan langit senja yang berwarna-warni.",
        "11. Kebun teh dengan barisan tanaman yang rapi.",
        "12. Sawah terasering dengan petani yang bekerja.",
        "13. Gunung berapi dengan lava yang mengalir.",
        "14. Pulau kecil di tengah lautan biru.",
        "15. Hutan bambu dengan sinar matahari yang menembus celah-celah.",
        "16. Rawa-rawa dengan burung bangau yang berdiri di air.",
        "17. Air terjun besar dengan pelangi di dekatnya.",
        "18. Sungai deras yang mengalir di antara bebatuan.",
        "19. Hutan tropis dengan berbagai macam satwa liar.",
        "20. Taman nasional dengan pemandangan yang menakjubkan.",
        "21. Gua bawah tanah dengan stalaktit dan stalagmit.",
        "22. Tebing tinggi dengan ombak yang menghantam di bawahnya.",
        "23. Pohon sakura yang berbunga di musim semi.",
        "24. Jalan setapak di hutan dengan daun-daun yang berguguran.",
        "25. Danau dengan perahu yang mengapung tenang.",
        "26. Pegunungan salju dengan langit biru cerah.",
        "27. Air terjun kecil di tengah hutan hujan.",
        "28. Bukit pasir di tepi pantai dengan jejak kaki.",
        "29. Taman bunga dengan berbagai jenis dan warna.",
        "30. Gunung yang tertutup salju dengan hutan pinus di bawahnya.",
        "31. Sungai berliku dengan tebing curam di kedua sisinya.",
        "32. Padang rumput luas dengan kawanan hewan liar.",
        "33. Laut biru dengan kapal nelayan di kejauhan.",
        "34. Pohon ek besar di tengah padang rumput.",
        "35. Tebing berbatu dengan tanaman yang tumbuh di celah-celahnya.",
        "36. Pemandangan matahari terbenam di atas danau.",
        "37. Hutan cemara dengan salju yang menutupi tanah.",
        "38. Pantai berbatu dengan ombak besar.",
        "39. Gunung berapi aktif dengan awan abu.",
        "40. Ladang lavender dengan warna ungu yang mencolok.",
        "41. Pegunungan Andes dengan puncak yang tertutup salju.",
        "42. Pantai karang dengan ikan-ikan berwarna-warni.",
        "43. Padang rumput savana dengan pohon-pohon akasia.",
        "44. Air terjun di dalam gua.",
        "45. Hutan lebat dengan jalan setapak yang tersembunyi.",
        "46. Danau vulkanik dengan air yang berwarna hijau toska.",
        "47. Pegunungan Himalaya dengan puncak yang megah.",
        "48. Lembah yang subur dengan tanaman hijau.",
        "49. Sungai Amazon dengan hutan hujan tropis di kedua sisinya.",
        "50. Pemandangan desa dengan sawah dan pegunungan di latar belakang."
    ])

def TAMPILKAN_BANNER():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(Panel(r"""[bold red]  _____ _           _  __                          
 |  ___| |__       | |/ /___  _ __ ___   ___ _ __  
 | |_  | '_ \ _____| ' // _ \| '_ ` _ \ / _ \ '_ \ 
 |  _| | |_) |_____| . \ (_) | | | | | |  __/ | | |
[bold white] |_|   |_.__/      |_|\_\___/|_| |_| |_|\___|_| |_|

    [underline red]Facebook Comments Home Page - Coded by Rozhak""", width=57, style="bold light_slate_grey"))

def HEADERS(your_cookies):
    return({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "{}".format(your_cookies),
        "dpr": "1.5",
        "Host": "m.facebook.com",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Accept-Language": "id",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Site": "same-origin",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
    })

class LOGIN:

    def __init__(self) -> None:
        pass

    def COOKIES(self):
        try:
            TAMPILKAN_BANNER()
            printf(Panel(f"[bold white]Silahkan masukan cookies akun Facebook kamu, gunakan bahasa Indonesia di akun\nagar tidak terjadi kesalahan saat login!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Login Cookies] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
            self.YOUR_COOKIES = Console().input("[bold light_slate_grey]   ╰─> ")
            self.NAME, self.USER = self.VALIDASI_COOKIES(cookies=self.YOUR_COOKIES)
            with open('Penyimpanan/Cookie.json', 'w+') as W:
                W.write(json.dumps({
                    "Cookie": self.YOUR_COOKIES
                }))
            W.close()
            printf(Panel(f"""[bold white]Name :[bold green] {self.NAME.title()}
[bold white]User :[bold red] https://m.facebook.com/profile.php?id={self.USER}""", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Selamat Datang] <<"))
            time.sleep(4.5)
            FITUR()
        except (Exception) as e:
            printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
            exit()

    def VALIDASI_COOKIES(self, cookies):
        with requests.Session() as SESSION:
            SESSION.headers.update(
                HEADERS(your_cookies=cookies)
            )
            response = SESSION.get('https://m.facebook.com/home.php?hrc=1&paipv=0&eav=&_rdr')
            if 'id="mbasic_logout_button"' in str(response.text):
                try:
                    self.NAME = re.search(r'id="mbasic_logout_button">Keluar \((.*?)\)</a>', str(response.text)).group(1)
                    self.USER = re.search(r'c_user=(\d+);', str(cookies)).group(1)
                except (AttributeError):
                    self.NAME, self.USER = ('null', 'null')
                return (self.NAME, self.USER)
            else:
                printf(Panel(f"[bold red]Ada masalah dengan cookies anda pastikan akun tidak terkena checkpoint dan\ntidak dalam keadaan mode gratis!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Login Gagal] <<"))
                time.sleep(5.7)
                self.COOKIES()

class FITUR:

    def __init__(self):
        global LOOPING, POSTINGAN
        try:
            TAMPILKAN_BANNER()
            self.COOKIES = json.loads(open('Penyimpanan/Cookie.json', 'r').read())['Cookie']
            self.NAME, self.USER = LOGIN().VALIDASI_COOKIES(cookies=self.COOKIES)
            printf(Columns([
                Panel(f"[bold white]Name: [bold green]{self.NAME[:17]}", width=28, style="bold light_slate_grey"),
                Panel(f"[bold white]User: [bold red]{self.USER[:17]}", width=28, style="bold light_slate_grey")
            ]))
        except (Exception) as e:
            printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
            time.sleep(5.7)
            LOGIN().COOKIES()

        printf(Panel(f"""[bold green]1[bold white]. Komentar Dan Reaction Bergambar ([bold green]koala.sh[bold white])
[bold green]2[bold white]. Komentar Bergambar ([bold red]ephoto360.com[bold white])
[bold green]3[bold white]. Komentar Dan Reaction Target
[bold green]4[bold white]. Ganti Teks Komentar
[bold green]5[bold white]. Sukai Postingan Beranda ([bold green]Like Only[bold white])
[bold green]6[bold white]. Keluar ([bold yellow]Exit[bold white])""", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Feature] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
        self.PILIHAN = Console().input("[bold light_slate_grey]   ╰─> ")
        if self.PILIHAN in ['1', '01']:
            try:
                printf(Panel(f"[bold white]Silahkan masukan jeda untuk menjalankan komentar, gunakan delay lebih\ndari 60 detik agar tidak terdeteksi spam!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Delay] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
                self.DETIK = int(Console().input("[bold light_slate_grey]   ╰─> "))
                printf(Panel(f"[bold white]Sedang menjalankan komentar dan reaction, Kamu bisa menggunakan[bold  red] CTRL + Z[bold  white] jika\ningin berhenti dan[bold  yellow] CTRL + C[bold  white] jika stuck!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Catatan] <<"))
                if os.path.exists('Trash/Sudah.txt') == False:
                    open('Trash/Sudah.txt', 'w+').write('')
                FOTO.update({
                    "TYPE": "1"
                })
                while True:
                    try:
                        if len(POSTINGAN) == 0:
                            FACEBOOK().MENDAPATKAN_POSTINGAN_TERBARU(cookies=self.COOKIES)
                            continue
                        else:
                            for URL in POSTINGAN:
                                try:
                                    if str(URL) in str(open('Trash/Sudah.txt', 'r').read().splitlines()):
                                        continue
                                    else:
                                        self.LINK_POSTINGAN = URL
                                        FACEBOOK().KOMENTAR(self.COOKIES, self.LINK_POSTINGAN)
                                        LOOPING += 1
                                        DELAY(self.DETIK)
                                except (AttributeError):
                                    continue
                            POSTINGAN.clear()
                            continue
                    except (KeyboardInterrupt):
                        printf(f"                                                    ", end='\r')
                        time.sleep(1.7)
                        continue
                    except (RequestException):
                        printf(f"                                                    ", end='\r')
                        printf(f"[bold light_slate_grey]   ──>[bold red] KONEKSI ANDA BERMASALAH!", end='\r')
                        time.sleep(9.7)
                        continue
            except (Exception) as e:
                printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
                exit()
        elif self.PILIHAN in ['2', '02']:
            try:
                printf(Panel(f"[bold white]Silahkan masukan jeda untuk menjalankan komentar, gunakan delay lebih\ndari 60 detik agar tidak terdeteksi spam!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Delay] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
                self.DETIK = int(Console().input("[bold light_slate_grey]   ╰─> "))
                printf(Panel(f"[bold white]Sedang menjalankan komentar dan reaction, Kamu bisa menggunakan[bold  red] CTRL + Z[bold  white] jika\ningin berhenti dan[bold  yellow] CTRL + C[bold  white] jika stuck!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Catatan] <<"))
                if os.path.exists('Trash/Sudah.txt') == False:
                    open('Trash/Sudah.txt', 'w+').write('')
                FOTO.update({
                    "TYPE": "2"
                })
                while True:
                    try:
                        if len(POSTINGAN) == 0:
                            FACEBOOK().MENDAPATKAN_POSTINGAN_TERBARU(cookies=self.COOKIES)
                            continue
                        else:
                            for URL in POSTINGAN:
                                try:
                                    if str(URL) in str(open('Trash/Sudah.txt', 'r').read().splitlines()):
                                        continue
                                    else:
                                        self.LINK_POSTINGAN = URL
                                        FACEBOOK().KOMENTAR(self.COOKIES, self.LINK_POSTINGAN)
                                        LOOPING += 1
                                        DELAY(self.DETIK)
                                except (AttributeError):
                                    continue
                            POSTINGAN.clear()
                            continue
                    except (KeyboardInterrupt):
                        printf(f"                                                    ", end='\r')
                        time.sleep(1.7)
                        continue
                    except (RequestException):
                        printf(f"                                                    ", end='\r')
                        printf(f"[bold light_slate_grey]   ──>[bold red] KONEKSI ANDA BERMASALAH!", end='\r')
                        time.sleep(9.7)
                        continue
            except (Exception) as e:
                printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
                exit()
        elif self.PILIHAN in ['3', '03']:
            try:
                printf(Panel(f"[bold white]Silahkan masukan link postingan, pastikan postingan bisa dikomentari dan link benar. Misalnya :[bold  green] https://m.facebook.com/rozhak.official/posts/pfbid02Jvk96rMX37dMFRvsFyBXvazuCfMhiPKpK1AaHovjez3ZrR1vRhKXddu6HJidKupHl?_rdc=1&_rdr", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Link Postingan] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
                self.LINK_POSTINGAN = Console().input("[bold light_slate_grey]   ╰─> ")
                printf(Panel(f"[bold white]Sedang menjalankan komentar dan reaction, Kamu bisa menggunakan[bold  red] CTRL + Z[bold  white] jika\ningin berhenti dan[bold  yellow] CTRL + C[bold  white] jika stuck!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Catatan] <<"))
                FOTO.update({
                    "TYPE": "2"
                })
                DELAY(30)
                FACEBOOK().KOMENTAR(self.COOKIES, self.LINK_POSTINGAN)
                exit()
            except (Exception) as e:
                printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
                exit()
        elif self.PILIHAN in ['4', '04']:
            try:
                printf(Panel(f"[bold white]Silahkan masukan teks komentar, gunakan[bold  red] $[bold  white] untuk melakukan tag dan gunakan[bold  red] +[bold  white] jika ingin\nmemasukan banyak teks. Misalnya :[bold  green] Hallo $+Mantap $", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Teks Komentar] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
                self.TEKS_KOMENTAR = Console().input("[bold light_slate_grey]   ╰─> ")
                if len(self.TEKS_KOMENTAR.split('+')) != 0:
                    if os.path.exists('Teks/Teks.txt') != False:
                        open('Teks/Teks.txt', 'w+').write('')
                    for TEKS in self.TEKS_KOMENTAR.split('+'):
                        self.FINAL_TEKS = TEKS.replace('$', '{}')
                        open('Teks/Teks.txt', 'a+').write(f'{self.FINAL_TEKS}\n')
                    printf(Panel(f"[bold white]Kami sudah berhasil mengubah teks komentar menjadi yang anda inginkan, anda bisa\nmelihatnya di file[bold  green] Teks/Teks.txt!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Sukses] <<"))
                    exit()
                else:
                    printf(Panel(f"[bold red]Anda harus memasukan setidaknya satu kalimat untuk menganti teks komentar default!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Tidak Boleh Kosong] <<"))
                    exit()
            except (Exception) as e:
                printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
                exit()
        elif self.PILIHAN in ['5', '05']:
            try:
                printf(Panel(f"[bold white]Silahkan masukan jeda untuk menjalankan reaction, gunakan delay lebih\ndari 60 detik agar tidak terdeteksi spam!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Delay] <<", subtitle="[bold light_slate_grey]╭─────", subtitle_align="left"))
                self.DETIK = int(Console().input("[bold light_slate_grey]   ╰─> "))
                printf(Panel(f"[bold white]Sedang menjalankan reaction halaman beranda, Kamu bisa menggunakan[bold  red] CTRL + Z[bold  white] jika\ningin berhenti dan[bold  yellow] CTRL + C[bold  white] jika stuck!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Catatan] <<"))
                if os.path.exists('Trash/Sudah.txt') == False:
                    open('Trash/Sudah.txt', 'w+').write('')
                KOMENTAR.update({
                    "STATUS": False
                })
                while True:
                    try:
                        if len(POSTINGAN) == 0:
                            FACEBOOK().MENDAPATKAN_POSTINGAN_TERBARU(cookies=self.COOKIES)
                            continue
                        else:
                            for URL in POSTINGAN:
                                try:
                                    if str(URL) in str(open('Trash/Sudah.txt', 'r').read().splitlines()):
                                        continue
                                    else:
                                        self.LINK_POSTINGAN = URL
                                        FACEBOOK().KOMENTAR(self.COOKIES, self.LINK_POSTINGAN)
                                        LOOPING += 1
                                        DELAY(self.DETIK)
                                except (AttributeError):
                                    continue
                            POSTINGAN.clear()
                            continue
                    except (KeyboardInterrupt):
                        printf(f"                                                    ", end='\r')
                        time.sleep(1.7)
                        continue
                    except (RequestException):
                        printf(f"                                                    ", end='\r')
                        printf(f"[bold light_slate_grey]   ──>[bold red] KONEKSI ANDA BERMASALAH!", end='\r')
                        time.sleep(9.7)
                        continue
            except (Exception) as e:
                printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
                exit()
        elif self.PILIHAN in ['6', '06']:
            try:
                os.remove('Penyimpanan/Cookie.json')
                printf(Panel(f"[bold white]Kami sudah berhasil menghapus data akun anda, terima kasih telah menggunakan program ini!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Keluar] <<"))
                time.sleep(2.7)
                exit()
            except:
                exit()
        else:
            printf(Panel(f"[bold red]Pilihan yang kamu masukan tidak ada dalam fitur dari program ini, silahkan\nmasukan pilihan dengan benar!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Pilihan Salah] <<"))
            time.sleep(4.7)
            FITUR()


def TEKS_KOMENTAR(object_id):
    FILE_MAP = {
        "DEFAULT": "Teks/Teks.txt","MOTIVASI": "Teks/Motivasi.txt","HUMOR": "Teks/Humor.txt","QUOTES": "Teks/Quotes.txt"
    }
    FILE_PATH = FILE_MAP.get(TEXT['TYPE'])
    if FILE_PATH:
        with open(FILE_PATH, 'r') as file:
            LINES = file.read().splitlines()
        return random.choice(LINES).format(f'@[{object_id}:]')
    else:
        RANDOM_STRING = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        return f'{RANDOM_STRING}\n@[{object_id}:]'

def DELAY(times):
    global SUKSES, GAGAL, LOOPING
    for SLEEP in range(int(times), 0, -1):
        time.sleep(1.0)
        printf(f"[bold light_slate_grey]   ──>[bold white] RUNNING[bold green] {len(POSTINGAN)}[bold white]/[bold green]{SLEEP}[bold white]/[bold green]{LOOPING}[bold white] SUKSES:[bold yellow]-{len(SUKSES)}[bold white] GAGAL:[bold red]-{len(GAGAL)}[bold white]     ", end='\r')
    return ("0_0")

class FACEBOOK:

    def __init__(self) -> None:
        pass

    def MENDAPATKAN_POSTINGAN_TERBARU(self, cookies):
        global POSTINGAN
        with requests.Session() as SESSION:
            SESSION.headers.update(
                HEADERS(your_cookies=cookies)
            )
            response = SESSION.get('https://m.facebook.com/home.php?hrc=1&paipv=0&eav=&_rdr')
            self.FIND_POSTINGAN = re.findall(r'href="(/story\.php\?[^"]+)"', str(response.text))
            for POST in self.FIND_POSTINGAN:
                try:
                    self.FINAL_POSTINGAN = POST.replace('amp;', '')
                    if 'story_fbid=' in str(self.FINAL_POSTINGAN):
                        self.STORY_FBID = re.search(r'story_fbid=([^&]+)', str(self.FINAL_POSTINGAN)).group(1)
                        if str(self.STORY_FBID) in str(POSTINGAN):
                            continue
                        else:
                            printf(f"[bold light_slate_grey]   ──>[bold white] MENGUMPULKAN[bold green] {str(self.STORY_FBID)[:17]}[bold white]/[bold green]{len(POSTINGAN)}[bold white] POSTINGAN!   ", end='\r')
                            time.sleep(0.5)
                            POSTINGAN.append(f'https://m.facebook.com{self.FINAL_POSTINGAN}')
                    else:
                        continue
                except:
                    continue
            self.FIND_POSTINGAN_GROUP = re.findall(r'href="(https://m.facebook.com/groups/[^"]+)".*? Komentar</a>', str(response.text))
            for POST in self.FIND_POSTINGAN_GROUP:
                try:
                    self.FINAL_POSTINGAN = POST.replace('amp;', '')
                    if '/permalink/' in str(self.FINAL_POSTINGAN):
                        self.PERMALINK = re.search(r'/permalink/(\d+)/', str(self.FINAL_POSTINGAN)).group(1)
                        if str(self.PERMALINK) in str(POSTINGAN):
                            continue
                        else:
                            printf(f"[bold light_slate_grey]   ──>[bold white] MENGUMPULKAN[bold green] {str(self.PERMALINK)[:17]}[bold white]/[bold green]{len(POSTINGAN)}[bold white] POSTINGAN!   ", end='\r')
                            time.sleep(0.5)
                            POSTINGAN.append(f'{self.FINAL_POSTINGAN}')
                    else:
                        continue
                except:
                    continue
            if len(POSTINGAN) == 0:
                printf(f"                                                    ", end='\r')
                printf(f"[bold light_slate_grey]   ──>[bold red] TIDAK MENDAPATKAN POSTINGAN TERBARU!", end='\r')
                time.sleep(4.7)
                self.MENDAPATKAN_POSTINGAN_TERBARU(cookies=cookies)
            else:
                printf(f"                                                    ", end='\r')
                printf(f"[bold light_slate_grey]   ──>[bold green] BERHASIL MENDAPATKAN {len(POSTINGAN)} POSTINGAN!", end='\r')
                time.sleep(4.7)
                return ("0_0")

    def KOMENTAR(self, cookies, link_postingan):
        with requests.Session() as SESSION:
            SESSION.headers.update(
                HEADERS(your_cookies=cookies)
            )
            response = SESSION.get('{}'.format(link_postingan))
            if not '/groups/' in str(link_postingan):
                try:
                    self.OBJECT_ID = re.search(r'&id=(\d+)&', str(link_postingan)).group(1)
                except (AttributeError):
                    self.OBJECT_ID = ('4')
            else:
                try:
                    self.OBJECT_ID = re.search(r'story_id=S%3A_I(\d+)%', str(response.text)).group(1)
                except (AttributeError):
                    self.OBJECT_ID = ('4')
            if bool(KOMENTAR['STATUS']) == True:
                if int(FOTO['TYPE']) == 1:
                    self.PROMPT = random.choice(
                        PROMPT()
                    )
                    GENERATE().IMAGE_KOALA(prompt=self.PROMPT)
                else:
                    try:
                        if not '/groups/' in str(link_postingan):
                            self.FULL_NAME = re.search(r'property="og:title" content="([^<]+)"', str(response.text)).group(1)
                        else:
                            self.FULL_NAME = re.search(r'href="/[^"]*">([^<]*)</a></strong>', str(response.text)).group(1)
                        if len(self.FULL_NAME) >= 35:
                            self.FULL_NAME = self.FULL_NAME[:40]
                        elif len(self.FULL_NAME) == 0:
                            GENERATE().IMAGE_KOALA(prompt=PROMPT())
                        else:
                            self.FULL_NAME = self.FULL_NAME.title()
                    except (AttributeError):
                        GENERATE().IMAGE_KOALA(prompt=PROMPT())
                    GENERATE().IMAGE_EPHOTO360(full_name=self.FULL_NAME)
            self.COMMENT_ADVANCED = re.search(r'href="(/mbasic/comment/advanced/[^"]+)"', str(response.text)).group(1).replace('amp;', '')

            SESSION.headers.update({
                "Referer": "{}".format(link_postingan),
            })

            if bool(LIKE['STATUS']) == True:
                self.RANDOM_REAKSI = random.choice(['1', '2', '16', '4', '3', '7', '8'])
                self.TIPE_REAKSI = TIPE().REACTION(self.RANDOM_REAKSI)
                self.REAKSI(SESSION, response.text, link_postingan, self.RANDOM_REAKSI)
            else:
                self.TIPE_REAKSI = ('null')
            if bool(KOMENTAR['STATUS']) == True:
                response2 = SESSION.get('https://m.facebook.com{}'.format(self.COMMENT_ADVANCED))

                self._MUPLOAD_ = re.search(r'action="(https://upload.facebook.com/_mupload_/ufi/mbasic/advanced/[^"]+)"', str(response2.text)).group(1).replace('amp;', '')
                self.FB_DTSG = re.search(r'name="fb_dtsg" value="([^"]+)"', str(response2.text)).group(1)
                self.JAZOEST = re.search(r'name="jazoest" value="([^"]+)"', str(response2.text)).group(1)

                BOUNDARY = '----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16))

                self.TEKS_KOMENTAR = TEKS_KOMENTAR(object_id=self.OBJECT_ID)
                self.COMMENT_TEXT = (f"""{self.TEKS_KOMENTAR}

{datetime.datetime.now().strftime('%A, %d/%B/%Y:%H.%M.%S')}""")
                data = MultipartEncoder(
                    fields={
                        "comment_text": "{}".format(self.COMMENT_TEXT),
                        "fb_dtsg": "{}".format(self.FB_DTSG),
                        "photo": (f"{str(int(time.time()))}.jpg", open("Penyimpanan/Images.jpg", "rb"), "image/jpeg"),
                        "jazoest": "{}".format(self.JAZOEST),
                        "post": "Komentari"
                    },
                    boundary=BOUNDARY
                )

                SESSION.headers.update({
                    "Content-Type": "multipart/form-data; boundary={}".format(BOUNDARY),
                    "Origin": "https://m.facebook.com",
                    "Connection": "keep-alive",
                    "Referer": "https://m.facebook.com/",
                    "Host": "upload.facebook.com",
                })
                response3 = SESSION.post('{}'.format(self._MUPLOAD_), data = data)
                if 'story.php?story_fbid=' in str(response3.text) or '/groups/' in str(response3.text):
                    printf(Panel(f"""[bold white]Status :[italic green] Commented successfully...[/]
[bold white]Link :[bold red] {str(link_postingan)[:134]}
[bold white]Komentar :[bold yellow] {self.COMMENT_TEXT}
[bold white]Reaksi :[bold green] {str(self.TIPE_REAKSI).upper()}""", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Sukses] <<"))
                    open('Trash/Sudah.txt', 'a+').write(f'{link_postingan}\n')
                    SUKSES.append(f'{link_postingan}')
                    return ("0_0")
                elif 'Komentar+Foto+Tidak+Diizinkan' in str(response3.text):
                    printf(f"                                                    ", end='\r')
                    printf(f"[bold light_slate_grey]   ──>[bold red] KOMENTAR FOTO TIDAK DIIZINKAN!", end='\r')
                    GAGAL.append(f'{link_postingan}')
                    time.sleep(3.7)
                    return ("-_0")
                else:
                    printf(f"                                                    ", end='\r')
                    printf(f"[bold light_slate_grey]   ──>[bold red] GAGAL MENGOMENTARI POSTINGAN INI!", end='\r')
                    GAGAL.append(f'{link_postingan}')
                    time.sleep(3.7)
                    return ("-_-")
            else:
                return ("0_0")
                
    def REAKSI(self, SESSION, response, link_postingan, TYPE_):
        self.REACTION_PICKER = re.search(r'href="(/reactions/picker/[^"]+)"', str(response)).group(1).replace('amp;', '')
        response4 = SESSION.get('https://m.facebook.com{}'.format(self.REACTION_PICKER))

        self.UFI_REACTION = re.findall(r'href="(/ufi/reaction/[^"]+)"', str(response4.text))
        for URLS in self.UFI_REACTION: # 1=LIKE, 2=SUPER, 16=PEDULI, 4=HAHA, 3=WOW, 7=SEDIH, 8=MARAH
            if f'reaction_type={TYPE_}' in str(URLS):
                self.REACTION_URL = URLS.replace('amp;', '')
            else:
                continue
        response5 = SESSION.get('https://m.facebook.com{}'.format(self.REACTION_URL))
        if 'story.php?story_fbid=' in str(response5.text) or '/groups/' in str(response5.text):
            if bool(KOMENTAR['STATUS']) == False:
                printf(Panel(f"""[bold white]Status :[italic green] Successfully liked...[/]
[bold white]Link :[bold red] {str(link_postingan)[:134]}
[bold white]Reaksi :[bold green] {str(TIPE().REACTION(TYPE_)).upper()}""", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Sukses] <<"))
                SUKSES.append(f'{link_postingan}')
                return ("0_0")
            else:
                return ("0_0")
        else:
            printf(f"                                                    ", end='\r')
            printf(f"[bold light_slate_grey]   ──>[bold red] GAGAL MENYUKAI POSTINGAN INI!", end='\r')
            GAGAL.append(f'{link_postingan}')
            time.sleep(3.7)
            return ("-_-")

class TIPE:
    
    def __init__(self) -> None:
        pass

    def REACTION(self, number):
        self.REACTIONS = {
            1: "Like",
            2: "Super",
            16: "Peduli",
            4: "Haha",
            3: "Wow",
            7: "Sedih"
        }
        return self.REACTIONS.get(int(number), "Marah")

class GENERATE:

    def __init__(self) -> None:
        pass

    def IMAGE_KOALA(self, prompt):
        try:
            with requests.Session() as SESSION:
                SESSION.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Origin': 'https://koala.sh',
                    'Accept': '*/*',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://koala.sh/images',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Host': 'koala.sh',
                    'Content-Type': 'application/json',
                })
                data = json.dumps({
                    'size': '1024x1024',
                    'prompt': prompt,
                    'style': 'photo',
                })
                response = SESSION.post('https://koala.sh/api/image-generation/', data = data)
                if '"url":"' in str(response.text):
                    image_url = json.loads(response.text)[0]['url']
                    SESSION.headers.pop('Content-Type')
                    SESSION.headers.pop('Origin')
                    SESSION.headers.update({
                        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                        'Sec-Fetch-Dest': 'image',
                        'Sec-Fetch-Mode': 'no-cors',
                    })
                    response = SESSION.get(image_url)
                    with open('Penyimpanan/Images.jpg', 'wb') as W:
                        W.write(response.content)
                    W.close()
                    printf(f"                                                    ", end='\r')
                    printf(f"[bold light_slate_grey]   ──>[bold green] BERHASIL MEMBUAT GAMBAR!", end='\r')
                    time.sleep(2.7)
                    return ("0_0")
                else:
                    printf(f"                                                    ", end='\r')
                    printf(f"[bold light_slate_grey]   ──>[bold red] GAGAL MEMBUAT GAMBAR!", end='\r')
                    time.sleep(4.7)
                    self.IMAGE_KOALA(prompt=prompt)
        except (Exception):
            printf(f"                                                    ", end='\r')
            printf(f"[bold light_slate_grey]   ──>[bold red] GAGAL MEMBUAT GAMBAR!", end='\r')
            time.sleep(4.7)
            self.IMAGE_KOALA(prompt=random.choice(PROMPT()))

    def IMAGE_EPHOTO360(self, full_name):
        try:
            with requests.Session() as SESSION:
                self.URL = (
                    random.choice(['https://en.ephoto360.com/create-online-3d-comic-style-text-effects-817.html', 'https://en.ephoto360.com/create-dragon-ball-style-text-effects-online-809.html', 'https://en.ephoto360.com/create-glossy-silver-3d-text-effect-online-802.html', 'https://en.ephoto360.com/create-colorful-neon-light-text-effects-online-797.html', 'https://en.ephoto360.com/create-typography-text-effect-on-pavement-online-774.html', 'https://en.ephoto360.com/create-digital-glitch-text-effects-online-767.html', 'https://en.ephoto360.com/write-text-on-wet-glass-online-589.html', 'https://en.ephoto360.com/create-pornhub-style-logos-online-free-549.html', 'https://en.ephoto360.com/create-online-typography-art-effects-with-multiple-layers-811.html', 'https://en.ephoto360.com/naruto-shippuden-logo-style-text-effect-online-808.html', 'https://en.ephoto360.com/beautiful-3d-foil-balloon-effects-for-holidays-and-birthday-803.html', 'https://en.ephoto360.com/create-3d-colorful-paint-text-effect-online-801.html', 'https://en.ephoto360.com/create-pixel-glitch-text-effect-online-769.html', 'https://en.ephoto360.com/create-impressive-neon-glitch-text-effects-online-768.html', 'https://en.ephoto360.com/free-online-american-flag-3d-text-effect-generator-725.html', 'https://en.ephoto360.com/create-eraser-deleting-text-effect-online-717.html', 'https://en.ephoto360.com/create-multicolored-signature-attachment-arrow-effect-714.html', 'https://en.ephoto360.com/online-blackpink-style-logo-maker-effect-711.html', 'https://en.ephoto360.com/create-glowing-text-effects-online-706.html', 'https://en.ephoto360.com/3d-underwater-text-effect-online-682.html', 'https://en.ephoto360.com/free-bear-logo-maker-online-673.html', 'https://en.ephoto360.com/write-text-on-vintage-television-online-670.html', 'https://en.ephoto360.com/create-a-cartoon-style-graffiti-text-effect-online-668.html', 'https://en.ephoto360.com/create-a-graffiti-text-effect-on-the-wall-online-665.html', 'https://en.ephoto360.com/create-a-realistic-embroidery-text-effect-online-662.html', 'https://en.ephoto360.com/multicolor-3d-paper-cut-style-text-effect-658.html', 'https://en.ephoto360.com/free-glitter-text-effect-maker-online-656.html', 'https://en.ephoto360.com/create-a-watercolor-text-effect-online-655.html', 'https://en.ephoto360.com/write-text-effect-clouds-in-the-sky-online-619.html', 'https://en.ephoto360.com/create-realistic-vintage-3d-light-bulb-608.html', 'https://en.ephoto360.com/create-blackpink-logo-online-free-607.html', 'https://en.ephoto360.com/create-funny-warning-sign-602.html', 'https://en.ephoto360.com/create-3d-gradient-text-effect-online-600.html', 'https://en.ephoto360.com/write-in-sand-summer-beach-online-free-595.html', 'https://en.ephoto360.com/create-a-luxury-gold-text-effect-online-594.html', 'https://en.ephoto360.com/create-multicolored-neon-light-signatures-591.html', 'https://en.ephoto360.com/write-in-sand-summer-beach-online-576.html', 'https://en.ephoto360.com/create-galaxy-wallpaper-mobile-online-528.html', 'https://en.ephoto360.com/1917-style-text-effect-523.html', 'https://en.ephoto360.com/making-neon-light-text-effect-with-galaxy-style-521.html', 'https://en.ephoto360.com/tik-tok-text-effects-online-generator-485.html', 'https://en.ephoto360.com/write-letters-on-life-buoys-484.html', 'https://en.ephoto360.com/royal-text-effect-online-free-471.html', 'https://en.ephoto360.com/create-double-exposure-inspired-text-effect-online-free-468.html', 'https://en.ephoto360.com/write-status-quotes-on-photo-online-free-455.html', 'https://en.ephoto360.com/create-typography-status-quotes-images-online-for-free-452.html', 'https://en.ephoto360.com/print-name-on-hollywood-walk-of-fame-star-451.html', 'https://en.ephoto360.com/free-minimal-logo-maker-online-445.html', 'https://en.ephoto360.com/free-create-a-3d-hologram-text-effect-441.html', 'https://en.ephoto360.com/create-galaxy-style-free-name-logo-438.html', 'https://en.ephoto360.com/create-mascot-logo-astronaut-space-galaxy-online-free-437.html', 'https://en.ephoto360.com/create-light-effects-green-neon-online-429.html', 'https://en.ephoto360.com/create-logo-3d-style-avengers-online-427.html', 'https://en.ephoto360.com/glossy-chrome-text-effect-online-424.html', 'https://en.ephoto360.com/create-marvel-style-logo-419.html', 'https://en.ephoto360.com/green-brush-text-effect-typography-maker-online-153.html', 'https://en.ephoto360.com/writing-on-the-cakes-127.html', 'https://en.ephoto360.com/metal-logo-online-108.html', 'https://en.ephoto360.com/noel-text-effect-online-99.html', 'https://en.ephoto360.com/glitter-gold-98.html', 'https://en.ephoto360.com/text-cake-90.html', 'https://en.ephoto360.com/stars-night-online-1-85.html', 'https://en.ephoto360.com/advanced-glow-effects-74.html', 'https://en.ephoto360.com/road-paint-text-effect-70.html', 'https://en.ephoto360.com/wooden-3d-text-effect-59.html', 'https://en.ephoto360.com/create-text-by-name-effect-58.html', 'https://en.ephoto360.com/write-galaxy-online-18.html', 'https://en.ephoto360.com/write-galaxy-bat-17.html', 'https://en.ephoto360.com/create-the-titanium-text-effect-to-introduce-iphone-15-812.html', 'https://en.ephoto360.com/create-sunset-light-text-effects-online-807.html', 'https://en.ephoto360.com/impressive-decorative-3d-metal-text-effect-798.html', 'https://en.ephoto360.com/nigeria-3d-flag-text-effect-online-free-753.html', 'https://en.ephoto360.com/national-flag-text-effect-according-to-your-country-752.html', 'https://en.ephoto360.com/create-colorful-angel-wing-avatars-731.html', 'https://en.ephoto360.com/create-3d-crack-text-effect-online-704.html', 'https://en.ephoto360.com/create-broken-glass-text-effect-online-698.html', 'https://en.ephoto360.com/free-online-art-paper-cut-text-effects-695.html', 'https://en.ephoto360.com/create-3d-gradient-text-effect-online-686.html', 'https://en.ephoto360.com/create-a-3d-shiny-metallic-text-effect-online-685.html', 'https://en.ephoto360.com/neon-devil-wings-text-effect-online-683.html', 'https://en.ephoto360.com/christmas-snow-text-effect-online-631.html', 'https://en.ephoto360.com/create-a-snow-3d-text-effect-free-online-621.html', 'https://en.ephoto360.com/colorful-birthday-foil-balloon-text-effects-620.html', 'https://en.ephoto360.com/create-a-cloud-text-effect-in-the-sky-618.html', 'https://en.ephoto360.com/create-realistic-cloud-text-effect-606.html', 'https://en.ephoto360.com/lovely-floral-ornamental-banner-online-603.html', 'https://en.ephoto360.com/create-circle-football-logo-online-592.html', 'https://en.ephoto360.com/write-names-and-messages-on-the-sand-online-582.html', 'https://en.ephoto360.com/realistic-3d-sand-text-effect-online-580.html', 'https://en.ephoto360.com/create-a-summery-sand-writing-text-effect-577.html', 'https://en.ephoto360.com/create-a-gaming-mascot-logo-free-560.html', 'https://en.ephoto360.com/latest-space-3d-text-effect-online-559.html', 'https://en.ephoto360.com/funny-minion-text-effect-online-544.html', 'https://en.ephoto360.com/writing-your-name-on-hot-air-balloon-506.html', 'https://en.ephoto360.com/create-a-awesome-logo-sci-fi-effects-492.html', 'https://en.ephoto360.com/lovely-cute-3d-text-effect-with-pig-397.html', 'https://en.ephoto360.com/green-neon-text-effect-395.html', 'https://en.ephoto360.com/create-logo-3d-metal-online-374.html', 'https://en.ephoto360.com/create-logo-avatar-wolf-galaxy-online-366.html', 'https://en.ephoto360.com/create-avatar-online-style-joker-365.html', 'https://en.ephoto360.com/create-logo-templates-according-to-online-icons-361.html', 'https://en.ephoto360.com/dark-green-typography-online-359.html', 'https://en.ephoto360.com/typography-online-leaf-autumn-358.html', 'https://en.ephoto360.com/create-typography-status-online-with-impressive-leaves-357.html', 'https://en.ephoto360.com/text-firework-effect-356.html', 'https://en.ephoto360.com/chocolate-text-effect-353.html', 'https://en.ephoto360.com/dragon-steel-text-effect-online-347.html', 'https://en.ephoto360.com/text-light-galaxy-effectt-345.html', 'https://en.ephoto360.com/typography-maker-online-5-343.html', 'https://en.ephoto360.com/typography-texture-online-nature-theme-342.html', 'https://en.ephoto360.com/online-hot-metallic-effect-341.html', 'https://en.ephoto360.com/typography-maker-facebook-online-340.html', 'https://en.ephoto360.com/make-typography-text-online-338.html', 'https://en.ephoto360.com/paul-scholes-shirt-foot-ball-335.html', 'https://en.ephoto360.com/angel-wing-effect-329.html', 'https://en.ephoto360.com/create-logo-avatar-online-style-polygon-logo-320.html', 'https://en.ephoto360.com/metallic-text-effect-with-impressive-font-307.html', 'https://en.ephoto360.com/create-your-name-in-a-mechanical-style-306.html', 'https://en.ephoto360.com/metal-text-effect-online-new-305.html', 'https://en.ephoto360.com/text-effect-on-jean-fabric-304.html', 'https://en.ephoto360.com/create-avatar-gold-online-303.html', 'https://en.ephoto360.com/create-a-metal-avatar-by-your-name-299.html', 'https://en.ephoto360.com/create-metallic-cover-online-297.html', 'https://en.ephoto360.com/create-water-effect-text-online-295.html', 'https://en.ephoto360.com/create-metal-border-294.html', 'https://en.ephoto360.com/the-effect-of-galaxy-angel-wings-289.html', 'https://en.ephoto360.com/text-galaxy-tree-effect-288.html', 'https://en.ephoto360.com/write-gold-letters-online-285.html', 'https://en.ephoto360.com/gemstone-text-effect-283.html', 'https://en.ephoto360.com/3d-ruby-stone-text-281.html', 'https://en.ephoto360.com/write-gold-letters-online-279.html', 'https://en.ephoto360.com/magic-text-effect-278.html', 'https://en.ephoto360.com/text-metal-3d-277.html', 'https://en.ephoto360.com/snake-text-effect-276.html', 'https://en.ephoto360.com/jewel-text-effect-275.html', 'https://en.ephoto360.com/3d-text-effects-style-274.html', 'https://en.ephoto360.com/3d-silver-text-effect-273.html', 'https://en.ephoto360.com/gold-text-effect-style-272.html', 'https://en.ephoto360.com/gold-text-effect-pro-271.html', 'https://en.ephoto360.com/music-equalizer-text-effect-259.html', 'https://en.ephoto360.com/galaxy-text-effect-new-258.html', 'https://en.ephoto360.com/write-letters-on-the-leaves-248.html', 'https://en.ephoto360.com/fabric-text-effect-247.html', 'https://en.ephoto360.com/message-coffee-245.html', 'https://en.ephoto360.com/text-light-effets-234.html', 'https://en.ephoto360.com/text-effects-incandescent-bulbs-219.html', 'https://en.ephoto360.com/modern-gold-5-215.html', 'https://en.ephoto360.com/modern-gold-4-213.html', 'https://en.ephoto360.com/modern-gold-3-212.html', 'https://en.ephoto360.com/modern-gold-silver-210.html', 'https://en.ephoto360.com/text-graffiti-3d-208.html', 'https://en.ephoto360.com/wings-galaxy-206.html', 'https://en.ephoto360.com/neon-text-effect-light-200.html', 'https://en.ephoto360.com/graffiti-color-199.html', 'https://en.ephoto360.com/write-text-on-chocolate-186.html', 'https://en.ephoto360.com/caper-cut-effect-184.html', 'https://en.ephoto360.com/modern-gold-red-183.html', 'https://en.ephoto360.com/cover-graffiti-181.html', 'https://en.ephoto360.com/graffiti-text-5-180.html', 'https://en.ephoto360.com/graffiti-text-3-179.html', 'https://en.ephoto360.com/graffiti-text-text-effect-online-178.html', 'https://en.ephoto360.com/wings-text-effect-176.html', 'https://en.ephoto360.com/modern-gold-purple-175.html', 'https://en.ephoto360.com/metal-text-effect-blue-174.html', 'https://en.ephoto360.com/3d-text-effect-172.html', 'https://en.ephoto360.com/neon-text-effect-171.html', 'https://en.ephoto360.com/color-text-effects-160.html', 'https://en.ephoto360.com/embroider-159.html', 'https://en.ephoto360.com/gold-text-effect-158.html', 'https://en.ephoto360.com/modern-gold-157.html', 'https://en.ephoto360.com/logo-viettel-156.html', 'https://en.ephoto360.com/shadow-text-effects-155.html', 'https://en.ephoto360.com/matrix-text-effect-154.html', 'https://en.ephoto360.com/creating-text-effects-night-lend-for-word-effect-147.html', 'https://en.ephoto360.com/ligatures-effects-from-leaves-146.html', 'https://en.ephoto360.com/zombie-3d-text-effect-143.html', 'https://en.ephoto360.com/create-word-green-flares-140.html', 'https://en.ephoto360.com/cloud-text-effect-139.html', 'https://en.ephoto360.com/water-3d-text-effect-online-126.html', 'https://en.ephoto360.com/beautiful-gold-text-effect-122.html', 'https://en.ephoto360.com/blue-neon-text-effect-117.html', 'https://en.ephoto360.com/galaxy-text-effect-116.html', 'https://en.ephoto360.com/gold-text-effect-online-112.html', 'https://en.ephoto360.com/dragon-fire-text-effect-111.html', 'https://en.ephoto360.com/metal-text-effect-online-110.html', 'https://en.ephoto360.com/metal-star-text-online-109.html', 'https://en.ephoto360.com/snow-on-text-online-107.html', 'https://en.ephoto360.com/water-text-effects-online-106.html', 'https://en.ephoto360.com/3d-wooden-text-effects-online-104.html', 'https://en.ephoto360.com/cake-text-effect-online-103.html', 'https://en.ephoto360.com/milk-cake-text-effects-102.html', 'https://en.ephoto360.com/purple-text-effect-online-100.html', 'https://en.ephoto360.com/thunder-text-effect-online-97.html', 'https://en.ephoto360.com/diamond-text-95.html', 'https://en.ephoto360.com/candy-text-effect-94.html', 'https://en.ephoto360.com/colorful-text-effects-93.html', 'https://en.ephoto360.com/chrome-text-effect-91.html', 'https://en.ephoto360.com/3d-cubic-text-effect-online-88.html', 'https://en.ephoto360.com/bokeh-text-effect-86.html', 'https://en.ephoto360.com/stars-night-online-84.html', 'https://en.ephoto360.com/foggy-rainy-text-effect-75.html', 'https://en.ephoto360.com/underwater-text-73.html', 'https://en.ephoto360.com/paint-splatter-text-effect-72.html', 'https://en.ephoto360.com/plasma-text-effects-online-71.html', 'https://en.ephoto360.com/colorful-glowing-text-effect-69.html', 'https://en.ephoto360.com/neon-text-effect-68.html', 'https://en.ephoto360.com/retro-text-effect-67.html', 'https://en.ephoto360.com/steel-text-effect-66.html', 'https://en.ephoto360.com/heated-steel-lettering-effect-65.html', 'https://en.ephoto360.com/graffiti-lettering-online-64.html', 'https://en.ephoto360.com/create-unique-word-green-light-63.html', 'https://en.ephoto360.com/text-on-cloth-effect-62.html', 'https://en.ephoto360.com/writing-chalk-on-the-blackboard-61.html', 'https://en.ephoto360.com/cake-text-60.html'])
                )
                SESSION.headers.update({
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate",
                    "Sec-Fetch-Site": "same-origin",
                    "Connection": "keep-alive",
                    "Accept-Language": "id",
                    "Host": "en.ephoto360.com",
                    "Referer": "{}".format(self.URL),
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
                })
                response = SESSION.get('{}'.format(self.URL))

                BOUNDARY = '----WebKitFormBoundary' \
                    + ''.join(random.sample(string.ascii_letters + string.digits, 16))
                
                SESSION.headers.update({
                    "Content-Type": "multipart/form-data; boundary={}".format(BOUNDARY)
                })

                self.BUILD_SERVER = re.search(r'name="build_server" value="(.*?)"', str(response.text)).group(1)
                self.TOKEN = re.search(r'name="token" value="(.*?)"', str(response.text)).group(1)
                self.BUILD_SERVER_ID = re.search(r'name="build_server_id" value="(.*?)"', str(response.text)).group(1)

                data = MultipartEncoder({
                    "build_server_id": (None, self.BUILD_SERVER_ID),
                    "text[]": (None, f"{full_name}"),
                    "submit": (None, "Go"),
                    "token": (None, self.TOKEN),
                    "build_server": (None, self.BUILD_SERVER)
                }, boundary=BOUNDARY)

                response2 = SESSION.post('{}'.format(self.URL), data = data)

                self.BUILD_SERVER_ID = re.search(r'build_server_id&quot;:&quot;(.*?)&', str(response2.text)).group(1)
                self.ID = re.search(r'id&quot;:&quot;(\d+)&', str(response2.text)).group(1)
                self.TEXT = re.search(r'\[&quot;(.*?)&quot;\]', str(response2.text)).group(1)
                self.TOKEN = str(re.search(r'token&quot;:&quot;(.*?)&', str(response2.text)).group(1)).replace('\\','')
                self.BUILD_SERVER = str(re.search(r'build_server&quot;:&quot;(.*?)&', str(response2.text)).group(1)).replace('\\','')

                SESSION.headers.update({
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://en.ephoto360.com",
                    "Accept": "*/*",
                })
                data = {
                    "build_server_id": "{}".format(self.BUILD_SERVER_ID),
                    "id": "{}".format(self.ID),
                    "build_server": "{}".format(self.BUILD_SERVER),
                    "text[]": "{}".format(self.TEXT),
                    "token": "{}".format(self.TOKEN)
                }
                response3 = SESSION.post('https://en.ephoto360.com/effect/create-image', data = data)
                if '"success":true' in str(response3.text):
                    self.JSON_DATA = json.loads(response3.text)
                    SESSION.headers.clear()
                    SESSION.headers.update({
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                        "Sec-Fetch-Dest": "image",
                        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                    })
                    response4 = SESSION.get('https://e2.yotools.net/save-image/{}/{}'.format(self.JSON_DATA['image_code'], self.JSON_DATA['session_id']))
                    with open('Penyimpanan/Images.jpg', 'wb') as W:
                        W.write(response4.content)
                    W.close()
                    if not "href='https://ephoto360.com'" in str(open('Penyimpanan/Images.jpg', 'rb').read()):
                        printf(f"                                                    ", end='\r')
                        printf(f"[bold light_slate_grey]   ──>[bold green] BERHASIL MEMBUAT GAMBAR!", end='\r')
                        time.sleep(2.5)
                        return ("0_0")
                    else:
                        printf(f"                                                    ", end='\r')
                        printf(f"[bold light_slate_grey]   ──>[bold blue] GAGAL MEMBUAT GAMBAR!", end='\r')
                        time.sleep(4.7)
                        self.IMAGE_EPHOTO360(full_name=full_name)
                else:
                    printf(f"                                                    ", end='\r')
                    printf(f"[bold light_slate_grey]   ──>[bold yellow] GAGAL MEMBUAT GAMBAR!", end='\r')
                    time.sleep(4.7)
                    self.IMAGE_EPHOTO360(full_name=full_name)
        except (AttributeError):
            printf(f"                                                    ", end='\r')
            printf(f"[bold light_slate_grey]   ──>[bold green] MENCOBA UNTUK MEMBUAT GAMBAR!", end='\r')
            time.sleep(2.7)
            self.IMAGE_EPHOTO360(full_name=full_name)
        except (Exception):
            printf(f"                                                    ", end='\r')
            printf(f"[bold light_slate_grey]   ──>[bold red] GAGAL MEMBUAT GAMBAR!", end='\r')
            time.sleep(4.7)
            self.IMAGE_KOALA(prompt=random.choice(PROMPT()))

if __name__ == '__main__':
    try:
        if os.path.exists("Penyimpanan/Subscribe.json") == False:
            YOUTUBE_URL = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Fb-Komen/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {YOUTUBE_URL}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        FITUR()
    except (Exception) as e:
        printf(Panel(f"[bold red]{str(e).capitalize()}!", width=57, style="bold light_slate_grey", title="[bold light_slate_grey]>> [Error] <<"))
        exit()
    except (KeyboardInterrupt):
        exit()