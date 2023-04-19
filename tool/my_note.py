from tool.miditool import k,n

# Kelas Note
class MyNote:
    def __init__(self, note_str:str, duration:float, octave = 5):
        self.duration = duration
        self.is_delay = False
       
        if(note_str == "delay"):
            self.is_delay = True
            self.note = 0
        else:
            self.note = n(note_str, octave)
    
    def get_str(self):
        str = ""
        if(self.is_delay):
            str =   "|"
        else:
            str = k(self.note)
        return str