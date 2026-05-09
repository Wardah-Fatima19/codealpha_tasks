# Basic Chatbot - CodeAlpha Internship
# Coder: Wardah Fatima

import random
import datetime

def chatbot():
    print("My Chatbot activated! Type 'bye' to exit.")

    jokes = [
        "Why do programmers hate nature? Too many bugs.",
        "I would tell you a coding joke, but it is not compiling.",
        "Why was the math book sad? Because it had too many problems.",
        "Why was the computer cold? Because it left its Windows open.",
        "Why do Python programmers wear glasses? Because they cannot C.",
        "Why do programmers prefer dark mode? Because light attracts bugs."
    ]

    while True:
        user = input("\nWardah: ").lower()

        if "hello" in user or "hi" in user:
            print("ChatBot: Hello. How are you?")

        elif "how are you" in user:
            print("ChatBot: I am fine. Thanks for asking.")

        elif "i am fine" in user or "i am good" in user:
            print("ChatBot: Nice to hear that.")

        elif "feeling bad" in user or "feeling sad" in user:
            print("ChatBot: I hope your day gets better.")

        elif "thanks" in user or "thank you" in user:
            print("ChatBot: You are welcome.")

        elif "what is your name?" in user:
            print("ChatBot: I am your chatbot.")

        elif "time" in user:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("ChatBot: Current time is:", current_time)

        elif "date" in user:
            today = datetime.date.today()
            print("ChatBot: Today's date is:", today)

        elif "tell me joke" in user:
            print("ChatBot:", random.choice(jokes))

        elif "help" in user:
            print("ChatBot: You can ask me about:")
            print("hello / hi")
            print("how are you")
            print("time")
            print("date")
            print("joke")
            print("your name")

        elif "bye" in user:
            print("Bot: Goodbye.")
            break

        else:
            print("Bot: I did not understand that.")

chatbot()
