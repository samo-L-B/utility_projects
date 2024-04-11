from TTS.api import TTS
import os

DEFAULT_PATH = r"C:\Users\Leon\Documents\coding\python\project-tts\0.2-cd-to-speech\output_command"

def greet():
    print("\n oie dipshit - hope u had a great day so far! how can I help you? please input the text you'd like to convert to speech.\n")

def main():
    greet()
    user_input = input("enter your text:\n")
    
    tts = TTS(model_name="tts_models/de/thorsten/vits")
    file_name = input("enter the file name for saving the speech output (without extension):\n")
    if not file_name:
        file_name = "wtf_01"
    path = input("enter the path where you want to save the file (press Enter for current directory):\n")
    if not path:
        # path = os.getcwd()
        path = DEFAULT_PATH
    file_path = os.path.join(path, file_name + ".wav")
    
    tts.tts_to_file(text=user_input, file_path=file_path)

    user_input = input("Do you want to open the file directly? (yes/no): ")
    if user_input.lower() in ["yes", "y", "ja", "j"]:
        if os.name == 'nt':  # For Windows
            print("Enjoy!")
            os.system(f'start {file_path}')
        else:
            print("Enjoy!")
            os.system(f'open {file_path}')
        print(f"Opening {file_path}...")
    else:
        print("File not opened.")


if __name__ == "__main__":
    print("top of the morning - hope you had a great start in your day!")
    main()
    print("enjoy ur day dipshit")