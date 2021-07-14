from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver.engine import SearchEngine
from webdriver import util
import time


class Facebook_login:
    # login
    login_locator = (By.XPATH, '//*[@id="email"]')
    password_locator = (By.XPATH, '//*[@id="pass"]')
    login_button_locator = (By.NAME, 'login')

    # click to avatar
    avatar_locator = (By.XPATH, str("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]/*[local-name()='svg'][1]/*[name()='g'][1]/*[name()='image'][1]"))
    avatar2_locator = (By.XPATH, str('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div/a/div'))
    avatar_circle_locator = (By.XPATH, str("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"))
    avatar_dropdown_locator = (By.XPATH, str("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[2]"))

    # click to find date
    dot_menu_locator = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[3]')
    dot_menu_item_locator = (By.XPATH, "//span[normalize-space()='Embed']")
    date_popup_locator = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/a/abbr")
    data = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/div[2]/span/span")
    tooltip = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[4]/div')

    # Info page
    page_name_locator = (By.CSS_SELECTOR, "span[class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 ns63r2gh fe6kdd0r mau55g9w c8b282yb rwim8176 m6dqt4wy h7mekvxk hnhda86s oo9gr5id hzawbc8m'] span")
    html_popup = (By.XPATH, str('/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[2]'))

    info_block_locator1 = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[2]/div/div/div")
    info_block_locator2 = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]")
    info_block_locator3 = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div")


class Login(SearchEngine):

    def enter_login(self, user_login):
        login = self.find_element(Facebook_login.login_locator)
        login.send_keys(user_login)

        return login


    def enter_password(self, user_password):
        password = self.find_element(Facebook_login.password_locator)
        password.send_keys(user_password)

        return password


    def click_button(self):
        button = self.find_element(Facebook_login.login_button_locator).click()

        return button


    def open_tab(self, link):

        # print(link)

        # Открыть новое окно и переключиться на него
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(f"{link}")

        ib = None
        try:
            ib = self.find_element(Facebook_login.info_block_locator1)

            if ib == None:
                ib = self.find_element(Facebook_login.info_block_locator3)
        except:
            pass

        try:
            if 'About' in ib.text:
                info_block = self.find_element(Facebook_login.info_block_locator1).text
                info = info_block.split('\n')
            elif 'Intro' in ib.text:
                info_block = self.find_element(Facebook_login.info_block_locator3).text
                info = info_block.split('\n')
            else:
                info_block = self.find_element(Facebook_login.info_block_locator2).text
                info = info_block.split('\n')
        except Exception as e:
            # print(e)
            return


        # Находим данные из блока информации на странице
        try:
            location = util.find_location(info, link)
            email = util.find_email(info, link)
            phone = util.find_phone(info, link)
            site = util.find_site(info, link)
        except Exception as e:
            # print(e)
            return


        # Находим название страницы
        try:
            page_name = self.find_element(Facebook_login.page_name_locator).text
        except:
            try:
                pn = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/span/h1')
                page_name = self.find_element(pn).text
            except:
                page_name = f'Название страницы не распознано на странице {link}'


        # Жмакаем на аву если нет стори на 2 вида аккаунтов
        try:
            try:
                # Если это первый вид профиля - то находим аватар второго вида аккаунтов
                if self.find_element(Facebook_login.avatar_locator) != None:
                    self.find_element(Facebook_login.avatar_locator).click()
                else:
                    self.find_element(Facebook_login.avatar_circle_locator).click()
                    self.find_element(Facebook_login.avatar_dropdown_locator).click()
            except:
                try:
                    self.find_element(Facebook_login.avatar2_locator).click()
                except Exception as e:
                    # print(e)
                    return
        except Exception as e:
            # print(e)
            return


        # Ховер на дату чтобы появился tooltip и вытаскиваем его из dom
        try:
            element = self.find_element(Facebook_login.data)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(1)

            last_photo_date_update = self.find_element(Facebook_login.tooltip).text
        except:
            return

        date = util.coincidence_date(last_photo_date_update)

        if date:
            util.writer_relevant_link_to_file(link)
            util.writer_page_info(str({link: {'Page name': page_name, 'Email': email, 'Phone': phone, 'Site': site, 'Location': location, 'Last photo update': last_photo_date_update}}))

        # close the active tab
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
