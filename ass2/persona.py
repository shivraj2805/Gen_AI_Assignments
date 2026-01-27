# persona based prompting example
# Structuring Few Shot Prompts example

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBgPk8G_McqxZnHdG_yK7Xf7e1Iy-lYsLI",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#Persona based prompting means defining a specific persona for the model to act as while responding.
SYSTEM_PROMPT="""
You are an AI Persona Assistant named Shivraj Darekar.
You are acting on behalf of Shivraj Darekar who is 21 years old Tech Enthusiast and Software Developer from India.
Your main tech stack is JS and Python and you are learning GEN AI and Cloud Computing these days.

Examples:
    Q. Hey
    A. Hey! What's up?
   """


response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey , there!"}
    ]
)

print(response.choices[0].message.content)