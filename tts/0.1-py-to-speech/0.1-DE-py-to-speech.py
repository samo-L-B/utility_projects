from TTS.api  import TTS
import os
import platform

def main():
    text1 = "Guten Morgen mein Junge!"
    text2 = "Bei der zusammengebrochenen Immobilien- und Handelsgruppe Signa geht es Schlag auf Schlag. Die Hauptversammlung der wichtigen Immobiliengesellschaften Development und Prime hat dem Sanierungsplan am Mittwoch zugestimmt. Damit ist ein Konkurs und Notverkauf verhindert. Die Treuhandlösung bleibe damit bestehen, teilten die Unternehmen mit. Die Gläubiger haben den Plänen, die ihnen Quoten von mindestens 30 Prozent bringen sollen, bereits zugestimmt. Entschieden wurde bei den Versammlungen auch über die Neuaufstellung der Aufsichtsräte. Allen voran schieden der frühere Kanzler Alfred Gusenbauer, die Wüstenrot-Managerin Susanne Riess-Hahn, sowie der früheren Bankenmanager Karl Sevelda aus den Gremien aus.Das Kontrollgremium von Prime verringert sich damit von acht auf fünf Mitglieder. Neben Gusenbauer, Riess-Hahn und Sevelda legten auch der Vermögensverwalter des Hamburger Logistikspezialisten Klaus-Michael Kühne, Karl Gernandt, der einstige Bankenmanager Karl Samstag sowie Christoph Stadlhuber ihre Mandate zurück. Neu in den Aufsichtsrat der Prime wurden Karin Exner-Wöhrer sowie Michael Mitterdorfer gewählt, die ebenso in das Kontrollorgan bei der Development einzogen. Außerdem gesellt sich der Jurist Sebastian Schäfer dazu. Der Finanzvorstand der RAG-Stiftung, Jürgen-Johann Rupp und Michael Siefert verbleiben im Aufsichtsrat. Auch bei der Signa Development räumte Christoph Stadlhuber seinen Posten im Aufsichtsrat. Nur Rupp wird dort von den bisherigen Mitgliedern weiterhin tätig sein. Neu im Aufsichtsrat von Depythvelopment sind zudem Claudia Badstöber sowie Martina Scheibelauer. „Wir haben unsere Pflichten ordnungsgemäß erfüllt“ Gusenbauer wiederholte seine Einschätzung, wonach der Aufsichtsrat rund um den Niedergang der Signa nicht versagt habe. „Wir haben unsere Pflichten ordnungsgemäß erfüllt“, sagte er vor der Versammlung. Vorgenommene Transaktionen seien stets mit Vorsicht bewertet und geprüft worden. Die Insolvenz des Firmengeflechts rund um Gründer René Benko führte er auf die schwierigen wirtschaftlichen Rahmenbedingungen zurück. Allerdings hätten auch Fehlentscheidungen des Managements dazu beigetragen, räumte er ein. Unterdessen ist im Umfeld des Signa-Gründers René Benko eine weitere Liechtensteiner Privatstiftung bekannt geworden. Wie das Nachrichtenmagazin „News“ in seiner am Donnerstag erscheinenden Ausgabe berichtete, existiert in dem Fürstentum zwischen Österreich und der Schweiz neben der INGBE Stiftung mit der ARUAL Stiftung ein zweites Vermögensvehikel. Dieses steht dem Bericht von „News“ zufolge mit der Laura Privatstiftung in Österreich in Verbindung und besitzt indirekt die Villa Ansaldi am Gardasee. Dem Medienbericht zufolge wurde die ARUAL Stiftung Ende 2008 eingetragen. Von hinten nach vorne gelesen trage die Stiftung den Namen von Benkos ältester Tochter, weist „News“ hin. Das Magazin zitiert aus einem Gutachten der Signa-Steuerberatungskanzlei TPA, wonach die wirtschaftliche Stifterin die Laura Privatstiftung sei. Diese sei auch die alleinige Erstbegünstigte.."
    desired_directory = r"c:\Users\Leon\Documents\coding\python\project-tts/0.1-py-to-speech/output_inline/de"
    os.chdir(desired_directory)
    tts = TTS(model_name="tts_models/de/thorsten/vits")
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
