import os
import re

from bs4 import BeautifulSoup


# Очистить список ссылок страницы
def cleanup_list(raw_list, undefined_list):
    clean_list = [wiki for wiki in raw_list if wiki in undefined_list]

    return clean_list


# Получить список неотмеченных файлов
def get_undefined_list(dict_wiki_files):
    undefined_list = [wiki for wiki in dict_wiki_files if dict_wiki_files[wiki] == None]

    return undefined_list


# pages_list: список страниц, из которых берем ссылки на другие страницы
# undefined_list: список страниц, у которых нет ссылок
# attr_list:
#   path: путь к хранилищу страниц
#   files: словарь, который изменяем алгоритмом
#   page_stop: страница, при достижении которой алгоритм останавливается
def recursion_tree(pages_list, undefined_list, attr_list):
    if len(pages_list) == 0 or len(undefined_list) == 0:
        return

    path = attr_list[0]
    dict_wiki_files = attr_list[1]
    stop = attr_list[2]

    set_pages_level = set()

    for page in pages_list:
        storage_path = os.path.join(path, page)

        with open(storage_path, "r", encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, "lxml")
        body = str(soup.find(id='bodyContent'))

        article_list = set(re.findall(r"(?<=/wiki/)[\w()]+", body))
        undefined_list = get_undefined_list(dict_wiki_files)

        refs_page = cleanup_list(article_list, undefined_list)
        set_pages_level.update(refs_page)

        for ref in refs_page:
            dict_wiki_files[ref] = page
            if ref == stop:
                return

    refs_pages_level = list(set_pages_level)
    undefined_list = get_undefined_list(dict_wiki_files)

    recursion_tree(refs_pages_level, undefined_list, attr_list)


def build_tree(start, end, path):
    wiki_files = os.listdir(path)
    files = dict.fromkeys(wiki_files)  # Словарь вида {"filename1": None, "filename2": None, ...}

    # Первый вызов: стартовая страница, весь список страниц - undefined
    recursion_tree([start], wiki_files, [path, files, end])

    return files


def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    page = end

    while page != start:
        bridge.append(page)
        page = files[page]

    bridge.append(start)

    return bridge


def count_imgs(source):
    img_list = source.find_all("img")
    imgs = 0

    for img_current in img_list:
        if img_current.get("width") != None:
            width = int(img_current['width'])
            imgs += 1 if width >= 200 else 0
    return imgs


def count_headers(source):
    headers_list = source.find_all(name=re.compile('h[1-6]'))
    headers = 0
    count = 0

    for header_current in headers_list:
        if header_current.string != None:
            if re.search('^[ETC]', header_current.string):
                count += 1
                print("ok")
            headers += 1 if re.search('^[ETC]', header_current.string) else 0

    return headers


def parse(start, end, path):
    bridge = build_bridge(start, end, path)

    out = {}
    for file in bridge:
        print(f"-----{file}---------")
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")
        imgs = count_imgs(body)
        headers = count_headers(body)


        # imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        # headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out
