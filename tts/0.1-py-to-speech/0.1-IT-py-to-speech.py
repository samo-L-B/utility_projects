from TTS.api  import TTS
import os
import platform


def main():
    text1 = "biongiorno cocksucker!"
    text2 = "Un'altra serata no per Gigio Donnarumma. Sempre con il Psg, di nuovo in Champions, stavolta nell'andata dei quarti di finale contro il Barcellona. Il portiere azzurro, titolare come sempre, è entrato in negativo in due dei tre gol dei blaugrana, contribuendo in modo netto alla sconfitta del Psg. Un'altra notte negativa nella grande coppa per l'ex Milan, reo di aver collezionato errori anche durante la fase a gironi contro il Newcastle, il 4 ottobre. In quell'occasione gli inglesi vinsero 4-1."
    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/it"
    os.chdir(desired_directory)
    tts = TTS(model_name="tts_models/it/mai_female/vits")
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
