import os
import platform
from TTS.api import TTS
DEFAULT_PATH = r"C:\Users\Leon\Documents\coding\python\project-tts\0.3-txt-to-speech\output_txt"


def greet():
    print("\n oie dipshit - hope u had a great day so far! how can I help you? please input the text you'd like to convert to speech.\n")

def read_text_from_file(file_path):
    """Reads text content from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_text_as_audio(text, file_path):
    """Saves text content as an audio file. """
    file_name = input("enter the file name for saving the speech output (without extension):\n")
    if not file_name:
        file_name = "wtf_01"
    path = input("enter the path where you want to save the file (press Enter for current directory):\n")
    if not path:
        path = DEFAULT_PATH
    file_path = os.path.join(path, file_name + ".wav")
    """ Converts text to speech and saves it as an audio file."""
    tts = TTS(model_name="tts_models/de/thorsten/vits")
    tts.tts_to_file(text=text, file_path=file_path)
    """ Ask user if file should be opened. """
    user_input = input("Do you want to open the file directly? (yes/no): ")
    if user_input.lower() in ["yes", "y", "ja", "j"]:
        if platform.system() == 'Windows':
            print("Enjoy!")
            os.system(f'start {file_path}')
        else:
            os.system(f'open {file_path}')
        print(f"Opening {file_path}...")
    else:
        print("File not opened.")

def main():
    user_file_path = input("Enter the path to the text file (leave blank to use the default path): ")
    if not user_file_path:
        file_path = r"c:\Users\Leon\Documents\coding\python\project-tts\0.3-txt-to-speech\txt_input\nzz_afghanistan.txt"
    else:
        file_path = user_file_path
    text = read_text_from_file(file_path)
    save_text_as_audio(text, file_path)

if __name__ == "__main__":
    print("willkommen willi - enjoy ur listening session!")
    main()
