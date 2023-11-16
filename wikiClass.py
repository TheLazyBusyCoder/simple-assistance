import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

class Wiki:
    def __init__(self):
        pass
    
    def wiki(self , search , oneone):
        try:
            result = wikipedia.summary(search, sentences = 2)
            oneone.speak(result , 185)
            return 1
        except DisambiguationError as e:
            # oneone.speak("Page not found sir")
            oneone.speak(f"No data for {search} You can search for following")
            output = ", ".join(e.options[:3])
            oneone.speak(output , 185)
            return -1
    
    def start(self , oneone):
        while True:
            oneone.speak("what would you like to search?")
            q = oneone.takequery()
            oneone.speak(f"searching for {q}")
            res = self.wiki(q , oneone)
            if res == 1:
                break
            oneone.speak("would you like me to search?")
            oneone.record_audio(3)
            s = oneone.recognize_speech()
            if "no".lower() in s:
                break
            if s == -1:
                break
            
