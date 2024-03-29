

# class style
from enum import Enum

class ChordType(Enum):
    MAJ = "M"
    MIN = "min"
    DIM = "dim"
    DELAY = "delay"

class Style(Enum):

    """
    Enum class to represent gender.

    Values:
    - `STANDARD`: the notes of chord played once at same times.
    - `REPEAT`: the notes of chord played X times repeatly.
    - `REPEAT_INVERSION`: the notes of chord played X times repeatly with change inversion 1 and 2 each beat.
    """

    def __str__(self):
        return str(self.value)

    # @property
    # def description(self):
    #     """
    #     Get a detailed description of the gender.

    #     Returns:
    #     - str: Description of the gender.
    #     """
    #     if self == Style.STANDARD:
    #         return "the notes of chord played once at same times."
    #     elif self == Style.REPEAT:
    #         return "the notes of chord played X times repeatly"
    #     else:
    #         return "Unknown gender."

    STANDARD = "standard" #
    REVERSE = "reverse"

    # beat count_based
    REPEAT = "repeat" #
    REPEAT_INVERSION_12 = "repeat_inversion_12"
    REPEAT_INVERSION_13 = "repeat_inversion_13"
    REPEAT_INVERSION_12_ONCE = "repeat_inversion_12_once"
    REPEAT_INVERSION_13_ONCE = "repeat_inversion_13_once"


    # interval_based
    PROGRESSIVE = "progessive"
    PROGRESSIVE_REVERSE = "progressive reverse"
    PROGRESSIVE_FULL = "progressive full"
    PROGRESSIVE_FULL_REVERSE = "progressive full reverse"
    PROGRESSIVE_REPEAT = "pr"
    PROGRESSIVE_REPEAT_REVERSE = "prr"
    ROYAL_CHORD = "rc"
    ROYAL_CHORD_2 = "rc1"
    ROYAL_CHORD_3 = "rc2"
    ROYAL_CHORD_4 = "rc3"
    ROYAL_CHORD_5 = "rc4"
    ROYAL_CHORD_6 = "rc5"





# kelas play style
class PlayStyle:
    def __init__(self, style:Style = Style.STANDARD, beat_count:int = 1, interval:float = 1, duration_scale:float = 1):
        self.style = style
        self.beat_count = beat_count
        self.interval = interval
        self.duration_scale = duration_scale

    def copy(self):
        return PlayStyle(self.style, self.beat_count, self.interval)
        
       
       


from tool.miditool import k, n

# Kelas Chord
class MyChord:
    def __init__(self, str_note:str ="", chord_type:ChordType = ChordType.MAJ, duration:float = 8, octave = 4, play_style:PlayStyle = PlayStyle(), inversion:int = 1):
        self.duration = duration
        self.is_delay = False
        self.chord_type = chord_type
        self.inversion = inversion
        import copy
        self.play_style = copy.copy(play_style)
        self.str_note = str_note
        self.octave = octave
        if(chord_type == ChordType.DELAY):
            self.str_note = " | "


      
       
    def get_notes(self):
        if(self.chord_type == ChordType.DELAY):
            self.is_delay = True
            return [ 0, 0, 0 ]
        else:
            if self.inversion == 1:
                note =  n(self.str_note, self.octave)
                if(self.chord_type == ChordType.MAJ):
                    return [ note, note + 4, note + 7 ]
                elif(self.chord_type == ChordType.MIN):
                    return [ note, note + 3, note + 7 ]
                elif(self.chord_type == ChordType.DIM):
                    return [ note, note + 3, note + 6 ]
                
            elif self.inversion == 2:
                note =  n(self.str_note, self.octave)
                if(self.chord_type == ChordType.MAJ):
                    return [ note + 7 - 12, note, note + 4 ]
                elif(self.chord_type == ChordType.MIN):
                    return [ note + 7 - 12, note, note + 3 ]
                elif(self.chord_type == ChordType.DIM):
                    return [ note + 6 - 12, note, note + 3 ]
                
            elif self.inversion == 3:
                note =  n(self.str_note, self.octave)
                if(self.chord_type == ChordType.MAJ):
                    return [ note + 4 - 12, note + 7 - 12, note  ]
                elif(self.chord_type == ChordType.MIN):
                    return [ note + 3 - 12, note + 7 - 12, note ]
                elif(self.chord_type == ChordType.DIM):
                    return [ note + 3 - 12, note + 6 - 12, note ]
       
    def get_str(self):
        str = ""
        if(self.is_delay):
            str =   "|"
        else:
            str = k(self.get_notes()[0]) + self.chord_type.value
        return str
    
        
    def get_str_note(self):
        str = ""
        for note in self.get_notes():
            str += k(note)
            str += " "
        return str





