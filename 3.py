def chatbot(): 
    conversations = {
    "hello": "Hi there! How can I assist you today?",
    "how are you?": "I'm just a program, but I'm doing great! Thanks for asking.",
    "what is your name?": "I'm your friendly chatbot.",
    "what do you do?": "I can help you with simple tasks and answer questions.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "what's the weather like?": "I'm not sure, but you could check a weather app for that!",
    "what is python?": "Python is a versatile programming language used for various  applications.",
    "how old are you?": "Age is just a number, and for a bot like me, it's a non-issue.",
    "goodbye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Let me know if you need anything else."
    }

    print("chatbot: hi i am a simple chatbot ask me something") 
    while True: 
        msg = input("user: ").lower()
        if msg in conversations: 
            replay = conversations[msg] 
            print(f"chatbot:{replay}")
            if msg == "goodbye":
                return 
        else: 
            print("chatbot: i am not sure how to replay to that, try something else")

chatbot()