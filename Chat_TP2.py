"""
This Python program allows interaction with the chat GPT conversational engine from OpenAI.
The program accepts user queries, invokes the chatGPT API with 
the provided query, and displays the obtained response on the screen.
It also provides additional functionalities such as error handling,
 the ability to retrieve and edit the last query,
and the option to enable a conversation mode.
Furthermore, measures are included to improve the code quality using pylint as a static analyzer.

Instructions:
1. Accepts user queries and sends them to chatGPT.
2. Handles errors using Try/Except structures.
3. Allows retrieval and editing of the last query using the "cursor Up" key.
4. Optionally enables a conversation mode.
5. Performs code quality metrics and proposes improvements.
6. Uses pylint to analyze the code and make necessary corrections.
"""

import argparse
from openai import OpenAI

# Define more specific exceptions to catch
SPECIFIC_EXCEPTIONS = (ConnectionError, TimeoutError, ValueError, TypeError)


# pip install pyreadline(windows), readline(Others OS), saves an history or previous inputs

# Gets the apikey as an environment variable
client = OpenAI()

# Memory buffer to store conversation history
conversation_history = []


def chat_with_gpt(user_query, conversation):  # Conversation boolean
    """
    Generate a response using the GPT-3
    model from OpenAI, based on the user's query.

    Args:
        user_query (str): The user's query.
        conversation (bool): A boolean indicator specifying whether
          the conversation history should be taken into account.

    Returns:
        str: The response generated by the GPT-3 model.
    """

    # Global variable declaration to access the conversation history

    # Conditional working, or not, on conversation mode
    context = " ".join(conversation_history) if conversation else ""

    # Define a placeholder for user's task (if applicable)
    usertask = " "
    try:
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
        if conversation:
            conversation_history.append(user_query)
            conversation_history.append(response.choices[0].message.content)

        # Return the response from the GPT-3 model
        return response.choices[0].message.content
    except SPECIFIC_EXCEPTIONS as e:
        print("Error durante la conversación con GPT:", e)
        return None


def handle_user_interaction(conversation):
    """
    Handles the interaction with the user by
    repeatedly prompting for input and generating responses.

    Args:
        conversation (bool): A boolean indicator
        specifying whether the conversation history should be considered.

    Returns:
        None
    """
    while True:
        try:
            # Prompt user for input
            user_query = input("Ingrese su consulta: ")

            # if empty
            if user_query.strip() == "":
                print("Por favor, ingrese una consulta válida.")
                continue
            print("You:", user_query)

            # Call chat_with_gpt function using the mode
            response = chat_with_gpt(user_query, conversation)
            if response is not None:
                print("chatGPT:", response)

        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            break
        except SPECIFIC_EXCEPTIONS as e:
            print("Error:", e)


def main():
    """
    Main function to handle command-line arguments and start the conversation mode.

    This function parses the command-line arguments
    to determine whether the conversation mode should be activated.
    If the "--convers" flag is provided, conversation
    mode is activated, otherwise, it's not activated.
    It then calls the handle_user_interaction function accordingly.

    Args:
        None

    Returns:
        None
    """
    # Global variable declaration to access the conversation history

    # Argument parsing for conversation mode
    parser = argparse.ArgumentParser(description="ChatGPT Conversational Mode")
    # When this flag is provided in the command line, it sets the value of args.convers to True.
    parser.add_argument(
        "--convers", action="store_true", help="Activate conversation mode"
    )
    # This line parses the command-line arguments provided by the user using the parser
    args = parser.parse_args()

    # Checks COnversation mode
    if args.convers:
        print("Modo de conversación activado.")
        handle_user_interaction(1)
    else:
        print("No se ha activado el modo de conversación.")
        handle_user_interaction(0)


if __name__ == "__main__":
    main()
