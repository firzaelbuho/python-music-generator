from mingus.core import chords
from midiutil import MIDIFile





# Fungsi utk membuat note dr string
def n(note :str, octave=4):
    note_number = 0

    if note == 'C':
        note_number = 1
    if note == 'C#':
        note_number = 2
    if note == 'D':
        note_number = 3
    if note == 'D#':
        note_number = 4
    if note == 'E':
        note_number = 5
    if note == 'F':
        note_number = 6
    if note == 'F#':
        note_number = 7
    if note == 'G':
        note_number = 8
    if note == 'G#':
        note_number = 9
    if note == 'A':
        note_number = 10
    if note == 'A#':
        note_number = 11
    if note == 'B':
        note_number = 12
    
    if note == 'do':
        note_number = 1
    if note == 'dis':
        note_number = 2
    if note == 're':
        note_number = 3
    if note == 'ris':
        note_number = 4
    if note == 'mi':
        note_number = 5
    if note == 'fa':
        note_number = 6
    if note == 'fis':
        note_number = 7
    if note == 'sol':
        note_number = 8
    if note == 'sis':
        note_number = 9
    if note == 'la':
        note_number = 10
    if note == 'lis':
        note_number = 11
    if note == 'si':
        note_number = 12

    if note == '1':
        note_number = 1
    if note == '1#':
        note_number = 2
    if note == '2':
        note_number = 3
    if note == '2#':
        note_number = 4
    if note == '3':
        note_number = 5
    if note == '4':
        note_number = 6
    if note == '4#':
        note_number = 7
    if note == '5':
        note_number = 8
    if note == '5#':
        note_number = 9
    if note == '6':
        note_number = 10
    if note == '6#':
        note_number = 11
    if note == '7':
        note_number = 12
    
    note_number += octave * 12
    return note_number

# Kelas Chord
class MyChord:
    def __init__(self, str_note:str,  chordBase:str, duration:float, octave = 4):
        note = n(str_note, octave)
        self.duration = duration
        self.str_note = str_note + chordBase
        self.isDelay = False
        if(chordBase == "delay"):
            self.isDelay = True
        elif(chordBase == "maj"):
            self.notes = [ note, note + 4, note + 7 ]
        elif(chordBase == "min"):
            self.notes = [ note, note + 3, note + 7 ]
        else:
            self.notes = [ note, note + 3, note + 6 ]
        self.duration = duration
        self.str_note = str_note + chordBase
# Kelas Note
class MyNote:
    def __init__(self, note_str:str, duration:float, octave = 4):
        self.str_note = note_str
        self.note = n(note_str, octave)
        self.duration = duration


# Chord Family

chord_family = {
    "major" : {
        "c" : [ MyChord("C", "maj", 4),  MyChord("D", "min", 4), MyChord("E", "min", 4), MyChord("F", "maj", 4), 
                 MyChord("G", "maj", 4),MyChord("A", "min", 4),MyChord("B", "dim", 4)],

        "d" : [ MyChord("D", "maj", 4),  MyChord("E", "min", 4), MyChord("F#", "min", 4), MyChord("G", "maj", 4), 
                 MyChord("A", "maj", 4),MyChord("B", "min", 4),MyChord("C#", "dim", 4)],

        "e" : [ MyChord("E", "maj", 4),  MyChord("F#", "min", 4), MyChord("G#", "min", 4), MyChord("A", "maj", 4), 
                 MyChord("B", "maj", 4),MyChord("C#", "min", 4),MyChord("D#", "dim", 4)],

        "f" : [ MyChord("F", "maj", 4),  MyChord("G", "min", 4), MyChord("A", "min", 4), MyChord("B#", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("D", "min", 4),MyChord("E", "dim", 4)],

        "g" : [ MyChord("G", "maj", 4),  MyChord("A", "min", 4), MyChord("B", "min", 4), MyChord("C", "maj", 4), 
                 MyChord("D", "maj", 4),MyChord("E", "min", 4),MyChord("F#", "dim", 4)],

        "a" : [ MyChord("A", "maj", 4),  MyChord("B", "min", 4), MyChord("C#", "min", 4), MyChord("D", "maj", 4), 
                 MyChord("E", "maj", 4),MyChord("F#", "min", 4),MyChord("G#", "dim", 4)],

        "b" : [ MyChord("B", "maj", 4),  MyChord("C#", "min", 4), MyChord("D", "min", 4), MyChord("E", "maj", 4), 
                 MyChord("F#", "maj", 4),MyChord("G#", "min", 4),MyChord("A#", "dim", 4)],
    },
     "minor" : {
        "c" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "d" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "e" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "f" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "g" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "a" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
        "b" : [ MyChord("C", "maj", 4),  MyChord("C", "maj", 4), MyChord("C", "maj", 4), MyChord("C", "maj", 4), 
                 MyChord("C", "maj", 4),MyChord("C", "maj", 4),MyChord("C", "maj", 4)],
    },

       
    
}


notes_coll = [
     MyNote('do', 1.25),
     MyNote('re', 0.5),
     MyNote('mi', 0.75),
     MyNote('fa', 0.75),
     MyNote('sol', 1.25),
     MyNote('mi', 0.5),
     MyNote('do', 3),
]

chord_dur = 4
canon_d = [
    MyChord('D', "maj", chord_dur),
    MyChord('A', "maj", chord_dur),
    MyChord('B', "min", chord_dur),
    MyChord('F#', "min", chord_dur),
    MyChord('G', "maj", chord_dur),
    MyChord('D', "maj", chord_dur),
    MyChord('G', "maj", chord_dur),
    MyChord('A', "maj", chord_dur),

    MyChord('D', "maj", chord_dur),
    MyChord('A', "maj", chord_dur),
    MyChord('B', "min", chord_dur),
    MyChord('F#', "min", chord_dur),
    MyChord('G', "maj", chord_dur),
    MyChord('D', "maj", chord_dur),
    MyChord('G', "maj", chord_dur),
    MyChord('A', "maj", chord_dur)

   
]


def create_melody(notes, midi, track = 0, time = 0):
   
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard
   
   
    for note in notes:
        midi.addNote(track, channel, note.note, time, note.duration, volume)
        time += note.duration
        print(time)
        print("beat")
    
    
    return midi


def create_chord(chords:list  , midi, track = 0, time = 0, style = 0, style_attr = 0):
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard
   
    
   
    for chord in chords:

        if not chord.isDelay:

            if(style == 0):
                for note in chord.notes:
                    midi.addNote(track, channel, note, time, chord.duration, volume)

            if(style == 1):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[0], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[2], time + (interval * 2), chord.duration - (interval * 2), volume)
    
            if(style == 2):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[2], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[0], time + (interval * 2), chord.duration - (interval * 2), volume)

            if(style == 3):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[0], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[2], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 2), chord.duration - (interval * 2), volume)
            
            if(style == 4):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[1], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[2], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[0], time + (interval * 2), chord.duration - (interval * 2), volume)
            if(style == 5):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[1], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[0], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[2], time + (interval * 2), chord.duration - (interval * 2), volume)
            
            if(style == 6):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[2], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[0], time + interval, chord.duration - interval, volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 2), chord.duration - (interval * 2), volume)
            
            if(style == 11):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[0], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + interval * 2, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[0], time + (interval * 3), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 4), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + (interval * 5), chord.duration - (interval * 5), volume)
            
            if(style == 12):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[0], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + interval * 2, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[0], time + (interval * 3), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + (interval * 4), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 5), chord.duration - (interval * 5), volume)
            
            if(style == 13):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[0], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + interval * 2, chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 3), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[2], time + (interval * 4), chord.duration - (interval * 5), volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 5), chord.duration - (interval * 5), volume)

            if(style == 14):
                interval = style_attr
                midi.addNote(track, channel, chord.notes[2], time + 0, chord.duration - 0, volume)
                midi.addNote(track, channel, chord.notes[1], time + interval, chord.duration - (interval * 4), volume)
                midi.addNote(track, channel, chord.notes[2], time + interval * 2, chord.duration - (interval * 4), volume)
                midi.addNote(track, channel, chord.notes[1], time + (interval * 3), chord.duration - (interval * 4), volume)
                midi.addNote(track, channel, chord.notes[0], time + (interval * 4), chord.duration - (interval * 4), volume)
          
        time += chord.duration
       
    
    return midi

def transpose(chords, curr_type:str, curr_key:str, target_type:str, targer_key:str):
    target_chords = chord_family[target_type][targer_key]
    current_chords = chord_family[curr_type][curr_key]

    for i, chord in enumerate(chords):
        if(not chord.isDelay):
            for j, current in enumerate(current_chords):
                if(chord.notes[0] == current.notes[0]):
                    chords[i] = target_chords[j]
                    
                    break
    return chords




def showNotes(notes):
    for note in notes:
        print (note.str_note + ", ") 


from music21 import midi as mp
def playMidi(path:str, midi:MIDIFile):

    with open(path, "wb") as output_file:
        midi.writeFile(output_file)
    mf = mp.MidiFile()
    mf.open(path) # path='abc.midi'
    mf.read()
    mf.close()
    s = mp.translate.midiFileToStream(mf)
    s.show('midi')


def showNotes(notes):
    str = "\n  "
    for i,note in enumerate(notes):
        str += note.str_note +"  "
        if( (i+1) %4 == 0 ):
            str+= "\n  "
    str += "  \n\n"
    print(str)
