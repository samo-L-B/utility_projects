from TTS.api  import TTS
import os
import platform


def main():
    text1 = "buenia dias cocksucker!"
    text2 = "Ismail Haniya, exiliado en Qatar, afirma que la muerte de sus familiares no hará variar la postura del grupo en las negociaciones. Biden considera “un error” la gestión de Netanyahu"
    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/es"
    os.chdir(desired_directory)
    tts = TTS(model_name="tts_models/es/css10/vits")
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
