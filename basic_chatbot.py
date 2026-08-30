# Task 4: Basic Chatbot
# A simple rule based chatbot

def get_response(message):
    message = message.lower()

    if message == "hello" or message == "hi":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I did not understand that."


def chat():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to end the chat.")

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


chat()
