import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for different topics
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking!"]
    ],
    [
        r"what's your name?",
        ["I'm Kemins, a Student Of Computer Engineering.", "You can call me Kems."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye! Take care."]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1!"]
    ],
    [
        r"do you like (.*)",
        ["I'm just a chatbot, I don't have preferences."]
    ],
    [
        r"(.*) (like|love|hate) (.*)",
        ["I'm not capable of feelings, but I can understand why you might %2 %3."]
    ],
    [
        r"how (can|do) I (.*)",
        ["You can %2 by doing X or Y."]
    ],
    [
        r"what (is|are) (.*)",
        ["%2 is something like this or that."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you please repeat that?"]
    ]
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Welcome! Let's chat. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
    if user_input.lower() == 'bye':
        break
