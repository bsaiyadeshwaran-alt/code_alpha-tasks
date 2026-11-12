
# Basic Rule-Based Chatbot

# Function to generate chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Welcome to our chatbot."

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input == "what is your name":
        return "I'm Python Chatbot, your virtual assistant."

    elif user_input == "what can you do":
        return "I can respond to greetings and simple questions."

    elif user_input == "thank you":
        return "You're welcome! Happy to help."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that message."


# Main program
print("===================================")
print("       WELCOME TO PYTHON CHATBOT")
print("===================================")

print("Chatbot: Hello! How can I help you?")
print("Chatbot: Type 'bye' to exit the conversation.")

# Conversation loop
while True:

    user_message = input("\nYou: ")

    # Get chatbot response
    response = chatbot_response(user_message)

    print("Chatbot:", response)

    # Exit condition
    if user_message.lower().strip() == "bye":
        break

print("\nChatbot session ended.")
