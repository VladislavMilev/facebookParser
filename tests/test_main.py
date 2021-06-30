from webdriver.collect_data import Login
from webdriver import util
import CONFIG as conf
import time


def test_login(driver_manager):

    # Логин на фейсбук
    lo = Login(driver=driver_manager, url=conf.FACEBOOK_URL)
    lo.go_to_search_engine()
    lo.enter_login(user_login=conf.LOGIN)
    lo.enter_password(user_password=conf.PASSWORD)
    lo.click_button()

    # Открытие ссылки
    time.sleep(10)
    pars = Login(driver=driver_manager, url=conf.FILTER_URL)
    pars.go_to_search_engine()


    # Скроллим страницу профилей с фильтром по заданным параметрам
    pages = util.scroll_and_collect_pages(
        driver_manager,
        links_count=conf.LINKS_COUNT,
        scroll_pause=conf.SCROLL_PAUSE,
        find_brand_new_link=conf.FIND_BRAND_NEW_LINKS,
        truncate_before=conf.TRUNCATE_BEFORE
    )

    # Вызов главной функции сборщика
    # for tab in range(1):
    #     pars.open_tab(pages[tab])
    # print(pages)

    for tab in pages:
        pars.open_tab(tab)
