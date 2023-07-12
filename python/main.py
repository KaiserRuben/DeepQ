import json
from pathlib import Path
import requests
import openai
from tqdm import trange, tqdm

from config import openai_api_key, deepL_api_key

openai.api_key = openai_api_key
gpt_model = "gpt-3.5-turbo-16k"
gpt_model_4 = "gpt-4-32k"
messages = [
    {"role": "system",
     "content": "Du generierst Fragen für ein Spiel. Die Fragen sind persönlich, tiefgründig und kontrovers."
                "Die Idee ist, dass man über die Fragen diskutieren kann."
                "Beispiele sind: 'Was macht dir aktuell im Leben am meisten Sorgen?' oder "
                "'Auf welche Errungenschaft bist du in den letzten Monaten besonders stolz?'"
                "Immer wenn ich 'w' schreibe, generierst du eine neue Frage."
     }
]
questions_de = []


def main(append=True, generate=True, translate=True):
    global questions_de
    if append:
        init_messanges_with_json()

    if generate:
        questions_de = get_questions(gpt_model, 50)
        array_to_json(questions_de, Path("../src/data/questions_de.json"))

    if translate:
        if len(questions_de) == 0:
            with open(Path("../src/data/questions_de.json"), "r") as file:
                questions_de = json.load(file)

        questions_en = translate_questions(questions_de)
        array_to_json(questions_en, Path("../src/data/questions_en.json"))


def init_messanges_with_json():
    # check if json file exists
    if Path("../src/data/questions_de.json").exists():
        with open(Path("../src/data/questions_de.json"), "r") as file:
            for question in json.load(file):
                messages.append({"role": "assistant", "content": question})
                messages.append({"role": "user", "content": "w"})


def translate_questions(questions_de):
    """
    translates questions using https://api-free.deepl.com/v2/translate
    :param questions_de: List of questions in german
    :return: List of questions in english
    """
    print("\n", "Translating questions...")
    questions_en = []
    for question_de in tqdm(questions_de):
        response = requests.post(
            "https://api-free.deepl.com/v2/translate",
            headers={
                'Authorization': deepL_api_key
            },
            data={
                "text": question_de,
                "source_lang": "DE",
                "target_lang": "EN"
            }
        )
        questions_en.append(response.json()["translations"][0]["text"])
    return questions_en


def array_to_json(array, path):
    """
    appends array to already existing array in json file
    :param array: array to append
    :param path: path to json file
    :return: None
    """
    if path.exists():
        with open(path, "r", encoding="utf-8") as file:
            json_array = json.load(file)
        json_array.extend(array)
    else:
        json_array = array
    with open(path, "w", encoding="utf-8") as file:
        json.dump(json_array, file, indent=4, ensure_ascii=False)


def get_questions(model, i):
    print("\n", "Generating questions...")
    questions = []
    for _ in trange(i):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        gpt_answer = response.choices[0].message.content
        messages.append({"role": "assistant", "content": gpt_answer})
        messages.append({"role": "user", "content": "w"})
        questions.append(gpt_answer)

    return questions


if __name__ == "__main__":
    main()
