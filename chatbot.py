#CHATBOT
import os
print("WELCOME TO CHATBOT")
print("You can talk to me")


#user questions
m1 = "hello"
m2 = "how are you"
m3 = "what is your name"
m4 = "bye"

while(True):
    a = input("enter your message:\n").lower()

      
    if(a== m1):
           
           command= f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{"hi"}')\""
           os.system(command) 
    elif(a==m2):
           command= f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{"i am fine"}')\""
           os.system(command)        
    elif(a==m3):
            command= f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{"my name is chatbot"}')\""
            os.system(command)  
    elif(a == m4):
           command= f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{"bye"}')\""
           os.system(command)  
           break
    else:
    
     command = f"powershell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('sorry i can not answer')\""
    os.system(command)
                 
                          
