import cv2
import threading
import time
import playsound
from twilio.rest import Client
from decouple import config

# Training model based on fire and non-fire data
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')
vid = cv2.VideoCapture(0) 
runOnce = False 
fire_detected_time = 0

def play_alarm_sound_function(): 
    """ Plays an alarm """

    playsound.playsound('Alarm_Sound.mp3', True) 
    print("Fire alarm end")


def make_phone_call():
    """ Makes a phone call with Twilio based on the information provided """

    account_sid = config("account_sid")
    auth_token = config("auth_token") 
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                               twiml="<Response><Say>Fire detected at [address]</Say></Response>", # Pronounces the given text
                               to=config("to"),
                               from_=config("from_")
                            )
    
    print("Call initiated. SID:", call.sid)


# Initialize the timer
fire_detected_time = 0

while True:
    Alarm_Status = False
    ret, frame = vid.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    fire = fire_cascade.detectMultiScale(frame, 1.5, 3) # Parameters are small enough to detect the fire from a lighter

    # Draw rectangle around detected fire
    for (x,y,w,h) in fire:
        cv2.rectangle(frame, (x-20,y-20), (x+w+20,y+h+20), (255,0,0), 2)

        # Start the timer if fire is detected for the first time
        if fire_detected_time == 0:
            fire_detected_time = time.time()

        # Check if fire has been detected for 4 seconds
        if time.time() - fire_detected_time >= 4:

            # Start alarm sound and phone call
            print("Fire alarm initiated")
            threading.Thread(target=play_alarm_sound_function).start()

            if not runOnce:
                print("Phone call initiated")
                threading.Thread(target=make_phone_call).start()
                runOnce = True


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
