presencenotification app  
This app detect motion and send an audio notification to the environment, also it connect to a Mqtt broker to publish a message about the presence detected. The audio notification is generated from a predefined text using a google service through gtts lib, and then play the audio file generated.  
  
Requirements:  
-pip3 install paho-mqtt  
-pip3 install gTTS  
-pip3 install gpiozero  
apt-get install python-pygame  
The usage of the gtts lib requires internet connection.  
  
References:  
http://www.steves-internet-guide.com/into-mqtt-python-client/  
https://www.thepythoncode.com/article/convert-text-to-speech-in-python  
https://projects.raspberrypi.org/en/projects/parent-detector/  

