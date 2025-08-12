import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Конфигурация бота
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
PRIVATE_CHANNEL_ID = os.getenv('PRIVATE_CHANNEL_ID')

# Путь к PDF файлу
PDF_PATH = os.path.join(os.path.dirname(__file__), 'docs', 'avito_structure.pdf')

# Настройки для одноразовых ссылок
INVITE_LINK_EXPIRE_TIME = 24 * 60 * 60  # 24 часа в секундах
MEMBER_LIMIT = 1

# Настройки базы данных
DB_PATH = os.path.join(os.path.dirname(__file__), 'users.db')

# Сообщения бота
WELCOME_MESSAGE = '''
Привет! 👋

Чтобы получить документ и доступ к моему закрытому каналу, подпишись на канал {channel} и нажми кнопку "Проверить подписку"
'''

NOT_SUBSCRIBED_MESSAGE = "Похоже, ты ещё не подписался. Подпишись на канал и попробуй снова"
ALREADY_RECEIVED_MESSAGE = "Вы уже получили материалы и доступ к каналу ✅"
SUCCESS_MESSAGE = '''
Отлично! Вот ваши материалы:
1. PDF-документ "Структура высококонверсионных объявлений на Авито"
2. Ссылка для доступа к закрытому каналу (действительна 24 часа): {invite_link}
'''
