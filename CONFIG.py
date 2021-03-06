# URL страницы с фильтром поиска для сбора и перебора этих страниц
FILTER_URL = 'https://www.facebook.com/search/pages?q=restaurant&filters=eyJmaWx0ZXJfcGFnZXNfbG9jYXRpb246MCI6IntcIm5hbWVcIjpcImZpbHRlcl9wYWdlc19sb2NhdGlvblwiLFwiYXJnc1wiOlwiMTA4MjUyNTUyNTI5MzMyXCJ9In0%3D'

# Константа FACEBOOK URL
FACEBOOK_URL = 'https://www.facebook.com/'
LOGIN = ''
PASSWORD = ''

# Количество страниц, которые необходимо проверить
LINKS_COUNT = 400

# Время в секундах - сколько нужно подождать перед подгрузкой пагинации на странице отфильтрованных профилей
SCROLL_PAUSE = 1

# Параметр, который отвечает за то, чтобы не учитывать уже проверенные профили,
# собирая и проходя всегда по новым страницам
# True - по умолчанию
FIND_BRAND_NEW_LINKS = True

# Названия файлов
# Найденных подходящие под условия ссылки
RELEVANT_LINKS = 'relevant_links.txt'
# Ранее пройденные ссылки
PREVIOUSLY_CHECKED_LINKS = 'previously_checked_links.txt'
# Сохранение Json данных с подходящих под условие профилей
# DATA_FILE = 'data.txt'
DATA_FILE = None

# Параметр, который отвечает за то, чтобы очистить файл 'previously_checked_links.txt' перед запуском скрипта
# False - по умолчанию (всегда собирает и хранит ссылки уже пройденных профилей)
TRUNCATE_BEFORE = False


# Telegram ID пользователя который будет получать уведомления
ID = 411345638
# Токен Telegram Bot
API_TOKEN = '1892966747:AAE5nz4kHAtbdWyFKa0UitVcK7qYKuL2tEY'

# Адрес Telegram Bot для получения отчетов - Надо нажать "START"
# https://t.me/facebook_parsing_bot