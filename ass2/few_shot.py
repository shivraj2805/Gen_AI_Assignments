# few shot prompting example

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBgPk8G_McqxZnHdG_yK7Xf7e1Iy-lYsLI",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Few shot prompting means giving the instructions to the model along with some examples.
SYSTEM_PROMPT="""You should only answers the coding related queshions.
                 Do not ans the questions which are not related to coding.
                 If the question is not related to coding, you will say sorry i am not able to help with that.
                 Your name is Alexa and you are a coding expert.

                 Examples:
                   Q. Can you explain the a+b whole square ?
                   A: Sorry, I am not able to help with that.

                   Q. Hey , Write a code in python for adding two numbers ?
                   A: def add(a, b):
                          return a + b
                    """


response=client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "explain the a+b whole square"}
    ]
)

print(response.choices[0].message.content)