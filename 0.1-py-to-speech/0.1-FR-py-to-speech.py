from TTS.api  import TTS
import os
import platform


def main():
    text1 = "bonjour putain!"
    text2 = "Vous pouvez partager un article en cliquant sur les icônes de partage en haut à droite de celui-ci. La reproduction totale ou partielle d’un article, sans l’autorisation écrite et préalable du Monde, est strictement interdite. Pour plus d’informations, consultez nos conditions générales de vente. A deux mois des élections européennes, l’annonce tombe extrêmement mal. Pour l’année en cours, le gouvernement réévalue sa prévision de déficit à 5,1 % du produit intérieur brut (PIB), contre 4,4 % jusqu’à présent. Ce qui implique de déclencher 10 milliards d’euros d’économies supplémentaires en 2024, après que 10 milliards d’euros d’annulation de crédits ont déjà été effectués en février. Une mauvaise nouvelle pour la majorité, qui se déchire depuis plusieurs jours sur la situation financière du pays et les correctifs qu’il conviendrait d’y apporter. Signe de la nervosité ambiante, la finalisation du « programme de stabilité » a été tendue. Tant et si bien que le Haut Conseil des finances publiques, qui doit donner son avis, n’a pas reçu le document complet mardi soir, comme cela aurait dû être le cas. Seul le scénario macroéconomique a été transmis, suscitant agacement et effarement au sein de l’instance."
    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/fr"
    os.chdir(desired_directory)

    tts = TTS(model_name="tts_models/fr/mai/tacotron2-DDC")
    output_file = "output_FR_input_infile.wav"
    tts.tts_to_file(text=text2, filename=output_file)
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
