from openai import OpenAI
from helper.mongo import insert, dinsert
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY")
)

options = ["ISL English to Standard English"]

prompt = """1.eg : tom helped her with the project

noun + pronoun + object + verb

tom her project help.

2.eg : john gave her a book

noun + pronoun + obj + verb

john her book gave

3.eg : sarah gave her friend a gift

noun + pronoun + noun + obj + verb

sarah her friend gift give

4.eg : she is beautiful

noun + adjective

she beautiful

5. eg : Disha is a sweet girl

noun + noun + adjective

if the next word of the adjective a Noun or object or subject, then adjective comes after that word

6. eg: mary told him the truth

Noun Phrase + Pronoun Phrase + Subject/Noun/Object  + Verb Phrase

mary him truth tell

7. eg: What is your favorite colour?

Noun Phrase + Pronoun Phrase + Subject/Noun/Object + Verb Phrase + Question words(wh words)/ Numbers

colour you favorite what
"""


def response(text):

    # if option == options[0]:
    #     respon = client.chat.completions.create(
    #         model="gpt-4o-mini",
    #         messages=[
    #             {
    #                 "role": "system",
    #                 "content": f"Your work is to translate grammatically correct English to deaf person's English. you'll use the formula and give answer as a response\n {prompt} \n only return answer dont return any formula or unnecessary content",
    #             },
    #             {"role": "user", "content": f"{text}"},
    #         ],
    #     )

    # if option == options[0]:
    respon = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Your work is to translate deaf person's babble English to grammatically correct English.",
            },
            {"role": "user", "content": f"{text}"},
        ],
    )
        # Accessing the content of the response
    content = respon.choices[0].message.content
    prompt_tokens = respon.usage.prompt_tokens
    completion_tokens = respon.usage.completion_tokens
    total_tokens = respon.usage.total_tokens

    # if option == options[0]:
    #     insert(
    #         text,
    #         content,
    #         prompt_tokens,
    #         completion_tokens,
    #         total_tokens,
    #     )
    # if option == options[0]:
    dinsert(
        text,
        content,
        prompt_tokens,
        completion_tokens,
        total_tokens,
    )
    return respon
