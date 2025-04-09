import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_task_description(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты — помощник по проектному менеджменту."},
            {"role": "user", "content": f"Сгенерируй подробное описание задачи: {prompt}"},
        ],
        max_tokens=150,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
