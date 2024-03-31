import argparse
from openai import OpenAI

client = OpenAI()

# Memory buffer to store conversation history
conversation_history = []


def chat_with_gpt(user_query,conversation):

    global conversation_history

    if conversation == 1:
        context = " ".join(conversation_history)  # Use conversation history as context
    else:
        context = " "

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
    if conversation == 1:
        conversation_history.append(user_query)
        conversation_history.append(response.choices[0].message.content)

    return response.choices[0].message.content


def main():

    global conversation_history

    # Argument parsing for conversation mode
    # This line creates an ArgumentParser object,
    # which is used to define what command-line arguments the script should accept.
    parser = argparse.ArgumentParser(description="ChatGPT Conversational Mode")

    # Flag. When this flag is provided in the command line, it sets the value of args.convers
    # to True. The action="store_true" parameter indicates that if the --convers flag is present, the value stored for this argument will be True
    parser.add_argument("--convers", action="store_true", help="Activate conversation mode")

    # This line parses the command-line arguments provided by the user using the parser defined above
    args = parser.parse_args()

    if args.convers:
        print("Modo de conversación activado.")

        while True:
            try:
                user_query = input("Ingrese su consulta: ")

                if user_query.strip() == "":
                    print("Por favor, ingrese una consulta válida.")
                    continue

                print("You:", user_query)

                response = chat_with_gpt(user_query,1)
                if response is not None:
                    print("chatGPT:", response)
            except KeyboardInterrupt:
                print("\nSaliendo del programa.")
                break
            except Exception as e:
                print("Error:", e)
    else:
        print("No se ha activado el modo de conversación.")
        while True:
            try:
                user_query = input("Ingrese su consulta: ")

                if user_query.strip() == "":
                    print("Por favor, ingrese una consulta válida.")
                    continue

                print("You:", user_query)

                response = chat_with_gpt(user_query,0)
                if response is not None:
                    print("chatGPT:", response)
            except KeyboardInterrupt:
                print("\nSaliendo del programa.")
                break
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    main()
