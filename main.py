from speech_recognition import recognize_speech
from nlp_processor import process_command
from response_generator import generate_response

def main():
    print("AI Personal Assistant Initialized...")
    while True:
        command = recognize_speech()
        if command.lower() == "exit":
            print("Goodbye!")
            break
        processed_command = process_command(command)
        response = generate_response(processed_command)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
