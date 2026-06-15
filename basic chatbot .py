def get_bot_response(user_input):
    # Convert input to lowercase to make matching case-insensitive
    user_input = user_input.lower().strip()
    
    # Rule-based conditional logic (if-elif-else)
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I didn't quite understand that. Could you try saying hello, how are you, or bye?"

def start_chatbot():
    print("🤖 Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    # Infinite loop to keep the conversation going until the user says bye
    while True:
        # Taking input from the user
        user_message = input("You: ")
        
        # Getting the predefined reply from the function
        bot_reply = get_bot_response(user_message)
        
        # Printing the output response
        print(f"Chatbot: {bot_reply}")
        
        # Breaking the loop if the predefined goodbye reply is triggered
        if bot_reply == "Goodbye!":
            break

# Run the chatbot program
if __name__ == "__main__":
    start_chatbot()