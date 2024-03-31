from openai import OpenAI
# pip install pyreadline, guarda un historial de los inputs anteriores
import sys

client = OpenAI()

# Memory buffer to store conversation history
conversation_history = []


def chat_with_gpt(user_query):

    global conversation_history

    context = " ".join(conversation_history)  # Use conversation history as context
    usertask = " "
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": usertask},
            {"role": "user", "content": user_query},
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Append the user query and GPT response to conversation history
    conversation_history.append(user_query)
    conversation_history.append(response.choices[0].message.content)

    return response.choices[0].message.content


def main():

    global conversation_history

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
