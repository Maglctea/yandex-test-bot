"""
Bot messages
"""

# ---------HELP---------
BOT_COMMANDS_INFO = (
    ("start",
     "Начало работы с ботом",
     "При отправке этой команды происходит начало взаимодействие с ботом"
     ),
    ("help",
     "Помощь и справка",
     "При отправке этой команды бот покажет, какие команды доступны для взаимодействия с ним",
     ),
    ("links",
     "Контакты и ссылки",
     "При отправке этой команды, бот даст ссылку на репозиторий проекта, а также поделится контактами создателя этого бота"),
)

TEXT_HELP = ("Помощь и справка о боте\n\n"
             "Для того, чтобы отписаться, отправь сообщение 'Отписаться' в чат\n\n"
             "Доступные команды:\n"
             "- /start\n"
             "- /help\n"
             "- /links\n")

# ---------MIDDLEWARES---------
PERMISSION_DENIED_MESSAGE = "У вас нет прав для доступа к этому боту :("

# ---------START---------
GREETING_TEXT = "Привет, это бот, созданный специально для яндекс практикума!"

# ---------LINKS---------
LINKS_TEXT = ("Ссылка на проект: https://github.com/Maglctea/yandex-test-bot\n"
              "Telegram: https://t.me/maglctea\n"
              "VK: https://vk.com/maglctea\n"
              "Github: https://github.com/maglctea\n")

# --------PICTURES---------
PICTURE_SELECTION = "Выберите картинку, которую хотите увидеть"
SCHOOL_PHOTO_DESCRIPTION = "Фото из школы у меня нет, поэтому вот фото, сделанное во время учёбы"
