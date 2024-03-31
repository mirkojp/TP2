from openai import OpenAI
#pip install pyreadline, guarda un historial de los inputs anteriores


client = OpenAI()
def chat_with_gpt(user_query):

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
        try:
            user_query = input("Ingrese su consulta: ")

            if user_query.strip() == "":
                print("Por favor, ingrese una consulta válida.")
                continue

            print("You:", user_query)

            response = chat_with_gpt(user_query)
            if response is not None:
                print("chatGPT:", response)
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
