
# Basic Rule-Based Chatbot

def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I am a Python chatbot."

    elif message == "help":
        return "You can say hello, ask how I am, or say bye."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that message."


def main():
    print("===== Basic Chatbot =====")
    print("Type 'hello', 'how are you', 'help', or 'bye'.")

    while True:
        user_message = input("\nYou: ")

        response = chatbot_response(user_message)
        print("Bot:", response)

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()
