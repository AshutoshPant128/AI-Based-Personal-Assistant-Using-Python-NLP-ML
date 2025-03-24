def generate_response(command):
    if "weather" in command:
        return "Fetching weather details..."
    elif "time" in command:
        return "Checking the current time..."
    elif "news" in command:
        return "Retrieving latest news..."
    else:
        return "I'm not sure how to respond to that."
