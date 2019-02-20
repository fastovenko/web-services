import os
import re

from bs4 import BeautifulSoup


# pages_list: список страниц, из которых берем ссылки на другие страницы
# undefined_list: список страниц, у которых нет ссылок
# attr_list:
#   path: путь к хранилищу страниц
#   files: словарь, который изменяем алгоритмом
#   page_stop: страница, при достижении которой алгоритм останавливается
def recursion_tree(pages_list, undefined_list, attr_list):
    print(f"Rec---{len(pages_list)}----{len(undefined_list)}---------------")
    if len(pages_list) == 0 or len(undefined_list) == 0:
        return

    path = attr_list[0]
    refs = list()

    for page in pages_list:
        storage_path = os.path.join(path, page)

        with open(storage_path, "r", encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, "lxml")
        body = str(soup.find(id='bodyContent'))

        article_list = set(re.findall(r"(?<=/wiki/)[\w()]+", body))
        refs = [x for x in article_list if x in undefined_list]

        new_files = attr_list[1]
        stop = attr_list[2]

        for ref in refs:
            new_files[ref] = page
            if ref == stop:
                return

    # Prepare new list of undefined members: new_list = undefined_list - refs
    new_list = [element for element in undefined_list if element not in refs]
    recursion_tree(refs, new_list, attr_list)

def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    files_list = files.keys()

    recursion_tree([start], files_list, [path, files, end])

    # storage_path = os.path.join(path, start)
    # # print(storage_path)
    #
    # with open(storage_path, "r", encoding='utf-8') as f:
    #     html = f.read()
    #
    # soup = BeautifulSoup(html, "lxml")
    # body = str(soup.find(id='bodyContent'))
    #
    # article_list = set(re.findall(r"(?<=/wiki/)[\w()]+", body))
    # refs = [x for x in article_list if x in files_list]
    # # files[start] = refs
    # for ref in refs:
    #     files[ref] = {0: [start]}
    #     # print(f"{ref} --- {files[ref]}")
    #
    # # Create new list = files_list - refs
    # list1 = [element for element in files_list if element not in refs]
    #
    # files_list = refs
    #
    # for file_1 in files_list:
    #     storage_path = os.path.join(path, file_1)
    #
    #     with open(storage_path, "r", encoding='utf-8') as f:
    #         html = f.read()
    #
    #     soup = BeautifulSoup(html, "lxml")
    #     body = str(soup.find(id='bodyContent'))
    #
    #     article_list = set(re.findall(r"(?<=/wiki/)[\w()]+", body))
    #     refs = [x for x in article_list if x in list1]
    #
    #     for xx in list1:
    #         print(xx)
    #
    #     for xx in refs:
    #         print(xx)
    #
    #     for ref in refs:
    #         files[ref] = {1: [ref]}
    #
    # for i in files.keys():
    #     print(f"{files[i]}-------{i}")

    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    print(files['Brain'])
    print(files['Artificial_intelligence'])
    print(files['Python_(programming_language)'])
    return files


def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start
    до end, то, по крайней мере, известны сами start и end, и можно распарсить хотя бы их:
    bridge = [end, start]. Оценка за тест, в этом случае, будет сильно снижена, но на минимальный
    проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так:
    # bridge = [end, start]
    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out
