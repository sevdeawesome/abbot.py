def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hello!"
    
    if p_message == "hi":
        return "Hi!"
    