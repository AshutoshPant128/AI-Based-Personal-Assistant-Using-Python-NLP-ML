import json

def save_interaction(user_input, response):
    data = {"user": user_input, "assistant": response}
    with open("interaction_log.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
