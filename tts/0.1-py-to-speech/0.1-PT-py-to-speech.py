from TTS.api  import TTS
import os
import platform


def main():
    text2 = "Caralho - A pauta dos biocombustíveis se tornou ponto de convergência de interesses entre o agronegócio e o governo Lula (PT), protagonistas de uma relação com mais conflitos que momentos amistosos.O projeto de lei que trata dos combustíveis de base orgânica foi aprovado na Câmara em março, onde recebeu apoio da principal bancada no momento, a ruralista. O texto contou com apoio de 429 deputados, do PT ao PL. O motivo disso, em grande medida, é o fato de que o agro tem grande interesse na regulamentação do setor, uma vez que os biocombustíveis são feitos a partir de plantações como cana ou soja. Filho da puta"

    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/pt"
    os.chdir(desired_directory)
    tts = TTS(model_name="tts_models/pt/cv/vits")
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
