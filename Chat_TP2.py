import argparse
from openai import OpenAI
# pip install pyreadline(windows), readline(Others OS), saves an history orfprevious inputs

# Gets the apikey as an environment variable
client = OpenAI()

# Memory buffer to store conversation history
conversation_history = []


def chat_with_gpt(user_query,conversation):#Conversation boolean
    # Global variable declaration to access the conversation history

    global conversation_history

    # Conditional working, or not, on conversation mode
    if conversation == 1:
        context = " ".join(conversation_history)  # Use conversation history as context
    else:
        context = " "

    # Define a placeholder for user's task (if applicable)
    usertask = " "

    # Generate response from the GPT-3 model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": context},  # System context/message
            {"role": "user", "content": usertask},  # User task (if applicable)
            {"role": "user", "content": user_query},  # User query
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Append the user query and GPT response to conversation history
    # Conditional working, or not, on conversation mode
    if conversation == 1:
        conversation_history.append(user_query)
        conversation_history.append(response.choices[0].message.content)

    # Return the response from the GPT-3 model
    return response.choices[0].message.content


def main():

    # Global variable declaration to access the conversation history
    global conversation_history

    # Argument parsing for conversation mode
    # This line creates an ArgumentParser object,
    # which is used to define what command-line arguments the script should accept.
    parser = argparse.ArgumentParser(description="ChatGPT Conversational Mode")

    # Flag. When this flag is provided in the command line, it sets the value of args.convers
    # to True. The action="store_true" parameter indicates that if the --convers flag is present
    # , the value stored for this argument will be True
    parser.add_argument("--convers", action="store_true", help="Activate conversation mode")

    # This line parses the command-line arguments provided by the user using the parser defined above
    args = parser.parse_args()

    # Check if conversation mode is activated
    if args.convers:
        print("Modo de conversación activado.")

        # Conversation mode loop
        while True:
            try:
                # Prompt user for input
                user_query = input("Ingrese su consulta: ")

                # Check if user input is empty
                if user_query.strip() == "":
                    print("Por favor, ingrese una consulta válida.")
                    continue

                print("You:", user_query)

                # Call chat_with_gpt function with conversation mode activated
                response = chat_with_gpt(user_query,1)
                if response is not None:
                    print("chatGPT:", response)
            except KeyboardInterrupt:
                print("\nSaliendo del programa.")
                break
            except Exception as e:
                print("Error:", e)

    else:
        # If conversation mode is not activated
        print("No se ha activado el modo de conversación.")

        # Non-conversation mode loop
        while True:
            try:
                # Prompt user for input
                user_query = input("Ingrese su consulta: ")

                # Check if user input is empty
                if user_query.strip() == "":
                    print("Por favor, ingrese una consulta válida.")
                    continue

                print("You:", user_query)

                # Call chat_with_gpt function with conversation mode deactivated
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
