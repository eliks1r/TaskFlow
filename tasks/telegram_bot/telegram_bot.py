import telebot
import openai
import django
import sys
import os

# Указываем путь к Django-проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow_backend.settings')
django.setup()

from tasks.models import Task, List  # Импорт моделей
from users.models import CustomUser  # Импорт кастомного пользователя (если нужен)


# Токен Telegram-бота
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

# Ключ OpenAI
openai.api_key = "sk-..."  # 🔒 сюда вставь свой OpenAI ключ (временно)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я бот TaskFlow.\nОтправь мне название задачи, и я сгенерирую описание 📌"
    )

# Ответ на любой текст
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    task_title = message.text
    description = generate_ai_description(task_title)

    # Найдём список и пользователя (пока тестовые значения)
    try:
        task_list = List.objects.first()
        user = CustomUser.objects.first()

        Task.objects.create(
            title=task_title,
            description=description,
            list=task_list,
            created_by=user  # если у тебя есть такое поле
        )
        bot.send_message(message.chat.id, f"✅ Задача сохранена!\n📌 {task_title}\n📝 {description}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при сохранении задачи: {e}")


# AI генерация
def generate_ai_description(title):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты помощник по проектному менеджменту."},
            {"role": "user", "content": f"Сгенерируй описание задачи: {title}"}
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# Запуск бота
if __name__ == '__main__':
    print("🤖 Бот запущен")
    bot.polling()


