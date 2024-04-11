from TTS.api  import TTS
import os
import platform


def main():
    text1 = "fuck you bitch this is baby keem!"
    text2 = "What's the deal with airline peanuts? Are they trying to feed the passengers or stock their bird feeders? Why is there a light switch on the refrigerator? Like I need to see if it's cold in there.You know what's messed up? The fact that they call it an ATM machine. Isn't that redundant?"    
    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/en"
    os.chdir(desired_directory)
    tts = TTS(model_name="tts_models/en/ljspeech/speedy-speech")
    tts.tts_to_file(text=text2)
    user_input = input("Do you want to open the file directly? (yes/no): ")
    if user_input.lower() in ["yes", "y", "ja", "j"]:
        if platform.system() == 'Windows':
            print("Enjoy!")
            file_path = tts.tts_to_file(text=text2)
            os.system(f'start {file_path}')
        else:
            file_path = tts.tts_to_file(text=text2)
            os.system(f'open {file_path}')
        print(f"Opening {file_path}...")
    else:
        print("File not opened.")


if __name__ == "__main__":
    print("oie fuckhead - hope u are having a great day beleza!")
    main()
