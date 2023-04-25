# fire_detection
Detects fire and makes a phone call to the given number


**Fire Detection and Alarm System**

This project is a fire detection and alarm system that uses computer vision to detect fire in real-time and raise an alarm. The system can also make a phone call to a configured phone number using Twilio's API to notify users about the fire.


**How it works**

The system uses a pre-trained Haar Cascade classifier model to detect fire from a video stream. Once a fire is detected, the system starts a timer and waits for 4 seconds to confirm if the fire is sustained. If the fire is sustained for 4 seconds, the system raises an alarm by playing a sound and initiates a phone call to the configured number using Twilio's API.

**Installation**

To use this project, follow these steps:

1. Clone the repository to your local machine.

2. Install the necessary libraries using the command pip install -r requirements.txt.

3. Create a .env file in the project root directory and add your Twilio    account SID, auth token, to and from phone numbers as environment      variables. The .env file should look like this:

`account_sid=<your_account_sid>
auth_token=<your_auth_token>
to=<your_phone_number>
from_=<twilio_phone_number>`

4. Run the fire_detection.py script using the command python              fire_detection.py.

5. The system will use the computer's camera to capture video, detect      fire and raise an alarm if necessary.

**Dependencies**

This project depends on the following libraries:

- cv2
- threading
- time
- playsound
- twilio
- decouple
