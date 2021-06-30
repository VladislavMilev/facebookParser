from bs4 import BeautifulSoup
from datetime import datetime
import CONFIG as conf
import time
import re
import os

def path(path):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)


def month_compare(month_name, fault=True):
    all_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for m in all_month:
        if fault == False:
            if m == month_name:
                return all_month[all_month.index(m) - 1]
        else:
            if m == month_name:
                return all_month[all_month.index(m)]


# Возврат условия при совпадении переданной даты - если True - значит дата обновдения фото меньше месяца
def coincidence_date(date):
    # 0 - МЕСЯЦ
    # 6 - ЧИСЛО
    # 1 - ГОД

    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")

    split_date = date.split()

    for i in split_date:
        if ',' in i:
            split_date.remove(i)
            split_date.append(i[:-1])

    if year == split_date[1]:
        if month_compare(month) == split_date[0] or month_compare(month, fault=False) == split_date[0]:
            return True
        else:
            return False
    else:
        return False


def find_location(info_block, link):
    location_pattern = [' st', ' street', ' drive', ' avenue', ' road', ' rd', ' ave', ' qld']

    pattern = r"[a-zA-Z][0-9]"
    number_re = re.compile(pattern)

    location = None
    found = False

    for i in info_block:
        if found == True:
            break
        else:
            for j in location_pattern:
                if j in i.lower() or number_re.search(i):
                    location = i
                    found = True
                    break
                else:
                    location = f'Локация не указана на странице {link}'
                    continue
    return location


def find_email(info_block, link):
    pattern = r"[a-zA-Z0-9]{1,100}[@][a-z]{2,40}\.[a-z]{2,4}"
    number_re = re.compile(pattern)
    email = None

    for i in info_block:
        if number_re.findall(i):
            email = i
            break
        else:
            email = f'Имейл не указан на странице {link}'

    return email


def find_phone(info_block, link):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    pattern = r"[0-9\x20]{5,25}"
    number_re = re.compile(pattern)
    phone = None
    found = False

    for i in info_block:
        if found == True:
            break
        else:
            for j in alpha:
                if j.lower() in i.lower():
                    break
                else:
                    if number_re.findall(i):
                        phone = i
                        found = True
                        break
                    else:
                        phone = f'Телефон не указан на странице {link}'
                        continue

    return phone


def find_site(info, link):
    site = None

    for i in info:
        if 'http' in i:
            site = i
            break
        else:
            site = f'Сайт не указан на странице {link}'

    return site


def writer_relevant_link_to_file(link):
    with open(path(f'../files/{conf.RELEVANT_LINKS}'), 'a+') as relevant:
        relevant.write(f'{link}\n')

def reader_relevant_links_in_file():
    with open(path(f'../files/{conf.RELEVANT_LINKS}'), 'a+') as relevant:
        return relevant.readlines()

def writer_brand_new_link_in_file(link):
    with open(path(f'../files/{conf.PREVIOUSLY_CHECKED_LINKS}'), 'a+') as checked_links:
        checked_links.write(f'{link}\n')

def reader_brand_new_link_in_file():
    with open(path(f'../files/{conf.PREVIOUSLY_CHECKED_LINKS}'), 'a+') as checked_links:
        return checked_links.readlines()

def writer_page_info(link):
    with open(path(f'../files/{conf.DATA_FILE}'), 'a+') as data_file:
        data_file.write(f'{link}\n')

def truncate():
    with open(path(f'../files/{conf.PREVIOUSLY_CHECKED_LINKS}'), 'r+') as f:
        f.truncate(0)


# Скроллим страницу профилей с фильтром
def scroll_and_collect_pages(driver_manager, links_count, scroll_pause, find_brand_new_link=True, truncate_before=False):
    pages = []
    read_relevant_links = reader_relevant_links_in_file()
    read_brand_new_links = reader_brand_new_link_in_file()

    if truncate_before:
        truncate()

    try:
        driver_manager.execute_script("return document.body.scrollHeight")

        while len(pages) <= links_count:
            driver_manager.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(scroll_pause)

            # Достаем все линки стринц по фильтру
            html = driver_manager.page_source
            soup = BeautifulSoup(html, 'html.parser')

            feed = soup.find('div', {'role': 'feed'})
            links = feed.find_all('a')
            feed.find_all('div', {'role': 'article'})

            # Достаем ссылки из списка отбираем только нужные и чистые ссылки
            # Не сохраняем повторные ссылки в pages[]

            for link in links:
                if link.get('href') not in pages:
                    pages.append(link.get('href'))

                if '__tn__=%3C' in link.get('href'):
                    pages.remove(link.get('href'))

            # Если не нужно при повторном проходе сравнивать ссылки с предыдущими проходами
            if find_brand_new_link == False:
                for p in pages:
                    if p + '\n' in set(read_relevant_links):
                        pages.remove(p)
                    else:
                        pass
            else:
                for p2 in pages:
                    if p2 + '\n' not in set(read_brand_new_links):
                        writer_brand_new_link_in_file(p2)
                    else:
                        if p2 + '\n' in set(read_relevant_links) or p2 + '\n' in set(read_brand_new_links):
                            pages.remove(p2)
                        else:
                            pass

    except Exception as e:
        print(e)

    return pages
