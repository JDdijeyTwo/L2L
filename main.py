import os
import sys
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

prompt = """Ты выступаешь в роли конвертера языка в язык. отдавай ящык в чистом виде без ```
Когда тебе говорят конвертируй тот язык в тот ты смотришь на исходный язык и переписываешь его по правилам второго языка.
"""
lang1 = sys.argv[1]
lang2 = sys.argv[2]
original = sys.argv[3]
msg_template = f"Конвертируй язык {lang1} в язык {lang2}. Исходник: {original}"
endpoint = "https://models.github.ai/inference"
model_name = "openai/gpt-4o"
token = "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"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(prompt),
        UserMessage(msg_template),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

answer = response.choices[0].message.content
print(f"""
Исходный язык: {lang1}
Целевой язык: {lang2}
Код:

{answer}
""")
