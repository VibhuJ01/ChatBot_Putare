import openai
import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)

def Query(data):
    
##    l = ['bye', 'goodbye', 'see you soon', 'later', 'see you later']
##    if(data.lower() in l):
##            speech.say('Have a nice day, Goodbye!!!!')
##            speech.runAndWait()
##            return 'Have a nice day, Goodbye!!!!'

    openai.api_key = "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"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": data}])
    ans = completion.choices[0].message.content
    return ans
        
        
    

