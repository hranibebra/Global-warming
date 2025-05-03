import telebot
import os
import random
from telebot import types

TOKEN = '7186069488:AAEqzkOZJNR8Z9iy_jfzdteeUX7btYq0ocs'

if TOKEN is None:
    print("Ошибка: Не найден токен Telegram бота в переменной окружения TELEGRAM_BOT_TOKEN.")
    exit()

bot = telebot.TeleBot(TOKEN)

def get_climate_news_link():
    return "Последние новости о климате можно найти здесь: https://www.theguardian.com/environment/climate-change"

def get_faq():
    faq_text = """
**Что такое глобальное потепление?**
Глобальное потепление - это долгосрочное повышение средней температуры климатической системы Земли.

**Каковы причины глобального потепления?**
В основном, это увеличение концентрации парниковых газов в атмосфере, вызванное деятельностью человека.

**Какие последствия глобального потепления?**
Повышение уровня моря, экстремальные погодные явления, таяние ледников, изменение экосистем и т.д.

**Что можно сделать для борьбы с глобальным потеплением?**
Переход на возобновляемые источники энергии, повышение энергоэффективности, сокращение потребления, участие в экологических инициативах.
    """
    return faq_text

def get_resources():
    resources_text = """
**Полезные ресурсы о глобальном потепнии:**

*   NASA Climate Change: [https://climate.nasa.gov/](https://climate.nasa.gov/)
*   NOAA Climate.gov: [https://www.climate.gov/](https://climate.nasa.gov/)
*   IPCC (Межправительственная группа экспертов по изменению климата): [https://www.ipcc.ch/](https://www.ipcc.ch/)
    """
    return resources_text

facts = [
    "Средняя температура на Земле повысилась примерно на 1,2°C с конца 19 века, что связано с увеличением концентрации парниковых газов.",
    "Основные парниковые газы — углекислый газ (CO2), метан (CH4) и закись азота (N2O). Их уровень в атмосфере значительно возрос с начала промышленной революции.",
    "Ледники в Гренландии и Антарктиде теряют около 400 миллиардов тонн льда в год, что способствует повышению уровня моря.",
    "Ожидается, что уровень моря может подняться на 1 метр или более к 2100 году, что угрожает прибрежным городам и экосистемам.",
    "Глобальное потепление увеличивает частоту и интенсивность экстремальных погодных явлений, таких как ураганы, засухи и наводнения.",
    "Изменение климата может привести к перемещению миллионов людей, которые будут вынуждены покинуть свои дома из-за повышения уровня моря или ухудшения условий жизни.",
    "Изменение климата влияет на сельское хозяйство, снижая урожайность некоторых культур и увеличивая риск засух и наводнений.",
    "Повышение температуры океанов приводит к обесцвечиванию коралловых рифов, что угрожает морским экосистемам.",
    "В России тайга является одним из крупнейших поглотителей углерода, но изменение климата может привести к ее деградации.",
    "Метан имеет в 25 раз более сильный парниковый эффект по сравнению с углекислым газом за 100-летний период.",
    "Океаны поглощают около 30% углекислого газа, что приводит к их подкислению и негативно сказывается на морской жизни.",
    "Изменение климата увеличивает риск лесных пожаров, которые выделяют большое количество углерода в атмосферу.",
    "Снег и лед отражают солнечные лучи, но их таяние приводит к тому, что больше солнечного света поглощается Землей, усугубляя потепление.",
    "Глобальное потепление может привести к ухудшению здоровья населения из-за увеличения числа заболеваний, связанных с жарой и загрязнением воздуха.",
    "Многие виды животных и растений не успевают адаптироваться к быстрому изменению климата и могут вымирать.",
    "Парижское соглашение по климату было подписано в 2015 году с целью ограничить глобальное потепление до 1,5°C выше доиндустриального уровня.",
    "Переход на возобновляемые источники энергии (солнечную, ветровую) является ключевым шагом в борьбе с глобальным потеплением.",
    "Некоторые страны создают рынки углерода для торговли правами на выбросы CO2 с целью снижения общего уровня выбросов.",
    "Повышение осведомленности о проблемах изменения климата является важным шагом для вовлечения общества в действия по его предотвращению.",
    "Каждый человек может внести свой вклад в борьбу с глобальным потеплением через сокращение потребления энергии, переработку отходов и поддержку устойчивого образа жизни.",
    "Таяние вечной мерзлоты высвобождает метан — мощный парниковый газ — что усугубляет проблему глобального потепления.",
    "Многие виды животных меняют свои миграционные маршруты из-за изменения климата, что влияет на экосистемы и пищевые цепочки."
]

def get_random_fact():
    return random.choice(facts)

MEME_FOLDER = "memes"

def get_meme_file_names():
    try:
        return [f for f in os.listdir(MEME_FOLDER) if os.path.isfile(os.path.join(MEME_FOLDER, f))]
    except FileNotFoundError:
        print(f"Ошибка: Папка '{MEME_FOLDER}' не найдена.")
        return []

meme_files = get_meme_file_names()

def get_random_meme():
    if not meme_files:
        return None
    return os.path.join(MEME_FOLDER, random.choice(meme_files))

TEMP_FOLDER = "temp"

def get_temperature():
    temp_change = +0.55
    source_link = "https://climate.nasa.gov/vital-signs/global-temperature/?intent=121"
    text = f"Изменение температуры за последние 14 лет(2010-2024): {temp_change} °C\n\nАктуальная информация и источник - {source_link}"

    try:
        image_files = [f for f in os.listdir(TEMP_FOLDER) if os.path.isfile(os.path.join(TEMP_FOLDER, f))]
        if not image_files:
            return None, text
        image_path = os.path.join(TEMP_FOLDER, random.choice(image_files))
        return image_path, text
    except FileNotFoundError:
        print(f"Ошибка: Папка '{TEMP_FOLDER}' не найдена.")
        return None, text

CO2_FOLDER = "co2"

def get_co2_level():
    co2_ppm = 428
    year = 2025
    source_link = "https://climate.nasa.gov/vital-signs/carbon-dioxide/?intent=121"
    text = f"Актуальный уровень CO2 на {year} год: {co2_ppm} ppm\n\nИсточник - {source_link}"

    try:
        image_files = [f for f in os.listdir(CO2_FOLDER) if os.path.isfile(os.path.join(CO2_FOLDER, f))]
        if not image_files:
            return None, text
        image_path = os.path.join(CO2_FOLDER, random.choice(image_files))
        return image_path, text
    except FileNotFoundError:
        print(f"Ошибка: Папка '{CO2_FOLDER}' не найдена.")
        return None, text

@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    if user_name is None:
        user_name = message.from_user.username
    greeting = f"Привет, {user_name}! Я бот, который предоставляет информацию о глобальном потеплении. Используйте /help или /menu для просмотра списка команд."
    bot.send_message(message.chat.id, greeting)
    show_menu(message)

def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🌡️ Температура")
    btn2 = types.KeyboardButton("💨 Уровень CO2")
    btn3 = types.KeyboardButton("📰 Новости")
    btn4 = types.KeyboardButton("❓ FAQ")
    btn5 = types.KeyboardButton("📚 Ресурсы")
    btn6 = types.KeyboardButton("💡 Факт")
    btn7 = types.KeyboardButton("😄 Мемы")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
    show_menu(message)

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """
**Список команд:**
/start - Запуск бота и приветствие.
/menu - Показать меню с кнопками.
/temp - Получить текущую аномалию глобальной температуры.
/co2 - Получить текущий уровень CO2 в атмосфере.
/news - Получить ссылку на последние новости о глобальном потеплении.
/faq - Получить ответы на часто задаваемые вопросы.
/resources - Получить полезные ресурсы о глобальном потепнии.
/fact - Получить случайный факт о глобальном потепнии.
/meme - Получить случайный мем.
/help - Показать этот список команд.
    """
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text == "🌡️ Температура":
        temp(message)
    elif message.text == "💨 Уровень CO2":
        co2(message)
    elif message.text == "📰 Новости":
        news(message)
    elif message.text == "❓ FAQ":
        faq(message)
    elif message.text == "📚 Ресурсы":
        resources(message)
    elif message.text == "💡 Факт":
        fact(message)
    elif message.text == "😄 Мемы":
        meme(message)
    else:
        bot.send_message(message.chat.id, "Не понимаю. Используйте кнопки или /help для списка команд.")

@bot.message_handler(commands=['temp'])
def temp(message):
    image_path, text = get_temperature()
    if image_path:
        try:
            with open(image_path, "rb") as temperature_file:
                bot.send_photo(message.chat.id, temperature_file, caption=text)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Ошибка: Файл с графиком температуры не найден.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка при отправке данных о температуре: {e}")
    else:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['co2'])
def co2(message):
    image_path, text = get_co2_level()
    if image_path:
        try:
            with open(image_path, "rb") as co2_file:
                bot.send_photo(message.chat.id, co2_file, caption=text)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Ошибка: Файл с графиком CO2 не найден.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка при отправке данных об уровне CO2: {e}")
    else:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['news'])
def news(message):
    climate_news_link = get_climate_news_link()
    bot.send_message(message.chat.id, climate_news_link)

@bot.message_handler(commands=['faq'])
def faq(message):
    faq = get_faq()
    bot.send_message(message.chat.id, faq)

@bot.message_handler(commands=['resources'])
def resources(message):
    resources = get_resources()
    bot.send_message(message.chat.id, resources)

@bot.message_handler(commands=['fact'])
def fact(message):
    random_fact = get_random_fact()
    if random_fact:
        bot.send_message(message.chat.id, random_fact)

@bot.message_handler(commands=['meme'])
def meme(message):
    random_meme_path = get_random_meme()
    if random_meme_path:
        try:
            with open(random_meme_path, "rb") as meme_file:
                bot.send_photo(message.chat.id, meme_file)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Ошибка: Файл мема не найден.")
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка при отправке мема: {e}")

    else:
        bot.send_message(message.chat.id, "Ошибка: Нет доступных мемов.")

if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()