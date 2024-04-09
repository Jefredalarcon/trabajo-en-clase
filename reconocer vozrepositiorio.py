import speech_recognition as sr

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Utilizar el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

    try:
        # Reconocer el texto del audio
        text = r.recognize_google(audio, language="es-ES")
        print("Has dicho: " + text)
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))