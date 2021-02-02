import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from naoqi import ALProxy

# from naoqi import A
tts = ALProxy("ALTextToSpeech", "155.245.22.39", 9559)
web = ALProxy("ALTabletService", "155.245.22.39", 9559)
import subprocess

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/penny/Desktop/Belia/final/abcassistant-etxg-f65be2e48a1c.json"
audioFile = "/home/penny/Desktop/Belia/vishuu3.wav"  # it needs to be mono wav file
projectID = 'abcassistant-etxg'
languageCode = 'en'
sessionID = 'second'
web.hideWebview()
# user input itneraction

tts.say("Hi, what can I do for you?")
tts.say("I can answer question about COVID-19 and any relevant information about any patient on the system")
tts.say("What would be your question?")

textToAnalyze = raw_input("Insert Question")
while True:
    if audioFile != "":
        def detectAudioIntent(projectID, sessionID, audioFile, languageCode):
            # Returns the result of detect intent with an audio file as input.

            import dialogflow_v2 as dialogflow

	
            session_client = dialogflow.SessionsClient()

            audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
            # sample_rate_hertz = 44100

            session = session_client.session_path(projectID, sessionID)
            print('Session path: {}\n'.format(session))

            with open(audioFile, 'rb') as audio_file:
                input_audio = audio_file.read()

            audio_config = dialogflow.types.InputAudioConfig(
                audio_encoding=audio_encoding, language_code=languageCode)  # add sample_rate_hertz=sample_rate_hertz
            query_input = dialogflow.types.QueryInput(audio_config=audio_config)

            response = session_client.detect_intent(
                session=session, query_input=query_input,
                input_audio=input_audio)

            # print('*' * 20)
            # print('Query text: {}'.format(response.query_result.query_text))
            # print('Detected intent: {} (confidence: {})\n'.format(
            #    response.query_result.intent.display_name,
            #    response.query_result.intent_detection_confidence))
            # print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))

            if response.query_result.fulfillment_text == "Please provide your full name":
                patient = str(response.query_result.fulfillment_text)
                tts.say(patient)
                # print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
                patientName = raw_input("Insert Name: ")
                detectTextIntent(projectID, sessionID, languageCode, patientName)
            elif response.query_result.fulfillment_text == "Please  provide the patient ID to get the medicine information":
                medicine = str(response.query_result.fulfillment_text)
                # print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
                tts.say(medicine)
                medicineName = raw_input("Insert ID: ")
                detectTextIntent(projectID, sessionID, languageCode, medicineName)
            elif response.query_result.fulfillment_text == "Please provie the patient ID for Appointment Information":
                appoint = str(response.query_result.fulfillment_text)
                # print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
                tts.say(appoint)
                appointment = raw_input("Insert ID: ")
                detectTextIntent(projectID, sessionID, languageCode, appointment)
            else:
                # print(response.query_result.fulfillment_text)
                chat = str(response.query_result.fulfillment_text)
                tts.say(chat)

        detectAudioIntent(projectID, sessionID, audioFile, languageCode)
	web.showWebview("https://www.nhs.uk/conditions/coronavirus-covid-19/")

    else:

       def detectTextIntent(projectID, sessionID, languageCode, textToAnalyze):

        # returns result of detect intent with an text file as input

        sessionClient = dialogflow.SessionsClient()
        session = sessionClient.session_path(projectID, sessionID)
        textInput = dialogflow.types.TextInput(text=textToAnalyze, language_code=languageCode)
        queryInput = dialogflow.types.QueryInput(text=textInput)

        try:
            response = sessionClient.detect_intent(session=session, query_input=queryInput)
        except InvalidArgument:
            raise
        # print("Query text:", response.query_result.query_text) #User's text input
        # print("Detected intent:", response.query_result.intent.display_name) #The name of this intent
        # print("Detected intent confidence:", response.query_result.intent_detection_confidence) #help match the best intent within the classification threshold.

        if response.query_result.fulfillment_text == "Please provide your full name":
            patient = str(response.query_result.fulfillment_text)
            tts.say(patient)
            #print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
            patientName = raw_input("Insert Name: ")
            detectTextIntent(projectID, sessionID, languageCode, patientName)
        elif response.query_result.fulfillment_text == "Please  provide the patient ID to get the medicine information":
            medicine = str(response.query_result.fulfillment_text)
            #print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
            tts.say(medicine)
            medicineName = raw_input("Insert ID: ")
            detectTextIntent(projectID, sessionID, languageCode, medicineName)
        elif response.query_result.fulfillment_text == "Please provie the patient ID for Appointment Information":
            appoint = str(response.query_result.fulfillment_text)
            #print(response.query_result.fulfillment_text)  # The text to be pronounced to the user or shown on the screen
            tts.say(appoint)
            appointment = raw_input("Insert ID: ")
            detectTextIntent(projectID, sessionID, languageCode, appointment)
        else:
            #print(response.query_result.fulfillment_text)
            chat = str(response.query_result.fulfillment_text)
            tts.say(chat)


        detectTextIntent(projectID, sessionID, languageCode, textToAnalyze)


    audioFile = None
    answer = raw_input("Would you like to ask another question? yes or no")
    if "no" in answer:
        print ("It was a pleasure")
        break
    else:
        textToAnalyze = raw_input("What would be your question?")

