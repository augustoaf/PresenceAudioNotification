import time
import datetime
import threading
from gpiozero import MotionSensor
import gtts
import pygame
import paho.mqtt.client as mqtt

def play_text(message):
    # you can specify the language as a second argument like: lang="pt-br" for Portuguese Brazil
    # to get all available languages along with their IETF tag, use: print(gtts.lang.tts_langs())
    tts = gtts.gTTS(message, lang="pt-br")
    
    # save the audio file
    audio_file_name = "speech.mp3"
    tts.save(audio_file_name)
    
    # play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
    print("notification done!")

def send_notification(payload):

    broker_address="192.168.86.42"     
    topic = "house/presencedetected"
    
    client = mqtt.Client("ID222") 
    client.connect(broker_address, port=1883, keepalive=10)
    client.publish(topic,payload)
    
    print("message sent on topic ", topic, " = ", payload)


def motion_listener():

    try:

        # gpio pin 27
        pir = MotionSensor(27)
        presence_detected = 0

        while True:

            pir.wait_for_motion()
            
            presence_detected = presence_detected + 1
            current_date_and_time = datetime.datetime.now()
            detected_message = 'presença detectada: ' + str(presence_detected) + '  |  ' + str(current_date_and_time)
            notification_to_environment = "a acesso apartir daqui é restrito, por favor se identifique!"

            # print(detected_message)
            play_text(notification_to_environment)
            send_notification(detected_message)

    except RuntimeError:
        print('runtime error')

def main():

    try:

        # Start a thread to listen motion sensor and play a notification
        motion_thread = threading.Thread(target=motion_listener, args=())
        motion_thread.daemon = True
        motion_thread.start()

        while True:
            time.sleep(10)
            print(".")

    except KeyboardInterrupt:
        print ( "App stopped" )

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    main()