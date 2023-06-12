import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "Not too bad, thanks for asking.", "I'm doing great!"],
    "what's your name": ["My name is ChatBot.", "I'm ChatBot!", "You can call me ChatBot."],
    "default": ["I'm sorry, I didn't understand. Can you please rephrase that?", "I'm not sure what you mean. Can you please clarify?"]
}


def respond(message):
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        return random.choice(responses["default"])


print("Hi, I'm ChatBot! How can I help you today?")
while True:
    message = input("You: ")
    print("ChatBot:", respond(message))