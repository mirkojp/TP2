from openai import OpenAI



client = OpenAI()
def chat_with_gpt(user_query):
    # context = "Este es el contexto que deseas proporcionar al modelo."  # Puedes personalizar el contexto según tus necesidades
    # usertask = ("Aquí puedes proporcionar una tarea adicional del usuario si es relevante.")
    context = " "  # Puedes personalizar el contexto según tus necesidades
    usertask = " "   
    response = client.chat.completions.create(
        
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": usertask},
            {"role": "user", "content": user_query},
        ],
        temperature=1,
        max_tokens=10,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content


def main():
    while True:
        user_query = input("Ingrese su consulta: ")
        if user_query.strip() == "":
            print("Por favor, ingrese una consulta válida.")
            continue

        print("You:", user_query)

        response = chat_with_gpt(user_query)
        print("chatGPT:", response)


if __name__ == "__main__":
    main()