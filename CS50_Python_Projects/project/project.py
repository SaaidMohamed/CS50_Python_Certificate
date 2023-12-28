from pocketsphinx import LiveSpeech
import speech_recognition as sr
from AppOpener import (
    open as opener_open_app,
    close as opener_close_app,
)
from gtts import gTTS
from playsound import playsound
import webbrowser
import os


r = sr.Recognizer()
m = sr.Microphone()


def main():
    Listen_to_wakeup_word()


def record_command():
    """
    this function plays an audio file to let user know recording has started,
    uses sr.Microphone() to get audio data from devices default Microphone for 5sec,
    then uses google recognizer to transcribe audio to text, finally pass result to check_condition(text) function.

    """
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            playsound(r"C:\Path\to\audio\file\listen-start-sound.mp3")
        except:
            speak(f"recording")
        audio = r.record(source, duration=5)

    try:
        text = r.recognize_google(audio).lower()
        check_condition(text)

    except sr.UnknownValueError:
        speak(f"could not understand audio")
    except sr.RequestError as e:
        speak(f"error; {0}".format(e))
    Listen_to_wakeup_word()


def Listen_to_wakeup_word():
    """
    Listen_to_wakeup_word() uses pocketsphinx's LiveSpeech to listen in the background for a wakeup word.
    when wake up word is detected calls record_command()

    """
    wakeup_word = "sesame"

    speech = LiveSpeech(keyphrase=wakeup_word, kws_threshold=1e-20)

    # an for in loop to iterate in speech
    for phrase in speech:
        # printing if the keyword is spoken with segments along side.
        if "sesame" in phrase.segments():
            record_command()
            break


def speak(text):
    """
    text to speech.

    function takes a str as a param, change to audio then use playsound to read audio file.

    Parameters
    ----------
    text : str
        string to change to audio.

    Returns
    -------
    audio
        plays audio of a text.

    """
    tts = gTTS(text=text, lang="en")
    filename = r"./audio.mp3"
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


def check_condition(spocken_text):
    """
    check param's condition.

    function takes param spocken_text as a str, check condition then call a function based on truthy condition.

    Parameters
    ----------
    spocken_text : str
        string condition to check.

    Returns
    -------
    calls a different function.

    """
    if "open" in spocken_text:
        spocken_text = spocken_text.strip()
        app = spocken_text[4:]
        open_app(app)

    if "close" in spocken_text:
        spocken_text = spocken_text.strip()
        app = spocken_text[5:]
        close_app(app)

    if "create" in spocken_text and "file" in spocken_text and "named" in spocken_text:
        spocken_text = spocken_text.strip()
        _, new_file_name = spocken_text.split("named")
        new_file_name = new_file_name.strip()
        create_file(new_file_name)

    if "delete" in spocken_text and "file" in spocken_text and "named" in spocken_text:
        spocken_text = spocken_text.strip()
        _, new_file_name = spocken_text.split("named")
        new_file_name = new_file_name.strip()
        delete_file(new_file_name)

    if (
        "create" in spocken_text
        and "folder" in spocken_text
        and "named" in spocken_text
    ):
        spocken_text = spocken_text.strip()
        _, new_file_name = spocken_text.split("named")
        new_file_name = new_file_name.strip()
        create_folder(new_file_name)

    if (
        "delete" in spocken_text
        and "folder" in spocken_text
        and "named" in spocken_text
    ):
        spocken_text = spocken_text.strip()
        _, new_file_name = spocken_text.split("named")
        new_file_name = new_file_name.strip()
        delete_folder(new_file_name)

    if "search google" in spocken_text:
        spocken_text = spocken_text.strip()
        Query = spocken_text[13:]
        search_google(Query)

    if "search youtube" in spocken_text:
        spocken_text = spocken_text.strip()
        Query = spocken_text[14:]
        search_youtube(Query)

    if "shutdown computer" in spocken_text:
        shutdown_computer()

    if "restart computer" in spocken_text:
        restart_computer()

    if "sign out" in spocken_text:
        logout()


def open_app(app_name):
    opener_open_app(app_name, output=False, match_closest=True, throw_error=False)
    speak(f"{app_name} is started")


def close_app(app_name):
    opener_close_app(app_name, output=False, match_closest=True, throw_error=False)
    speak(f"{app_name} is terminated")


def create_file(file_name):
    parent_directory = os.path.expanduser(r"~\oneDrive\Desktop")
    absolute_path = os.path.join(parent_directory, file_name)
    check_file_exist = os.path.exists(absolute_path)

    if check_file_exist:
        speak(f"file named {absolute_path} already exists")

    else:
        try:
            with open(absolute_path, "a") as file:
                file.write("Text appended")
            speak(f"file named {file_name} was created")

        except FileNotFoundError:
            speak(f"directory does not exist")
    return 0




def delete_file(file_name):
    parent_directory = os.path.expanduser(r"~\oneDrive\Desktop")
    absolute_path = os.path.join(parent_directory, file_name)
    check_file_exist = os.path.exists(absolute_path)

    if check_file_exist and parent_directory != absolute_path:
        os.remove(absolute_path)
        speak(f"file {absolute_path} is deleted")

    else:
        speak(
            f"couldn't locate file {absolute_path}, are you sure it was created?"
        )
    return 0



def create_folder(folder_name_to_create):
    parent_directory = os.path.expanduser(r"~\oneDrive\Desktop")
    folder_name = folder_name_to_create
    path = os.path.join(parent_directory, folder_name)
    check_folder_exist = os.path.exists(path)

    if check_folder_exist:
        speak(f"Folder named {folder_name_to_create} already exists")

    else:
        os.mkdir(path)
        speak(f"folder named {folder_name_to_create} is created")
    return 0


def delete_folder(file_name):
    parent_directory = os.path.expanduser(r"~\oneDrive\Desktop")
    absolute_path = os.path.join(parent_directory, file_name)
    check_folder_exist = os.path.exists(absolute_path)

    if check_folder_exist and absolute_path != parent_directory:
        os.rmdir(absolute_path)
        speak(f"folder {absolute_path} is deleted")

    else:
        speak(
            f"couldn't locate folder {absolute_path}, are you sure it was created?"
        )
    return 0


def shutdown_computer():
    speak(f"computer is shutting down")
    return os.system("shutdown /s /t 1")


def restart_computer():
    speak(f"computer is restarting")
    return os.system("shutdown /r /t 1")


def logout():
    speak(f"signing out of your account")
    return os.system("shutdown -l")


def search_google(Query):
    URL = r"www.google.com/search?q=" + Query
    webbrowser.open_new(URL)


def search_youtube(Query):
    URL = r"www.youtube.com/results?search_query=" + Query
    webbrowser.open_new(URL)


if __name__ == "__main__":
    main()
