def speech_recogniser():
    import speech_recognition as speech_recog

    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()


    with mic as audio_file:
        print('Говорите')
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language='ru-RU')