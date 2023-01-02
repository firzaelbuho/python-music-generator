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
        if(chordBase == "maj"):
            self.notes = [ note, note + 4, note + 7 ]
        else:
            self.notes = [ note, note + 3, note + 7 ]
        self.duration = duration
# Kelas Note
class MyNote:
    def __init__(self, note_str:str, duration:float, octave = 4):
        self.note = n(note_str, octave)
        self.duration = duration


        


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
           
           
     

        time += chord.duration
        print(time)
        print("beat") 
    
    return midi

track = 0
time = 0
tempo = 140


MyMIDI = MIDIFile(4)  # One track, defaults to format 1 (tempo track is created  automatically)
MyMIDI.addTempo(track, time, tempo)
midi = MyMIDI

# midi = create_melody(notes_coll,midi, track = 0, time = 0)
midi = create_chord(canon_d,midi, track= 1, time = 0, style = 1, style_attr = 1)



with open("test.mid", "wb") as output_file:
    midi.writeFile(output_file)




# for i, pitch in enumerate(my_notes):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)




from music21 import midi
def playMidi(path):
  mf = midi.MidiFile()
  mf.open(path) # path='abc.midi'
  mf.read()
  mf.close()
  s = midi.translate.midiFileToStream(mf)
  s.show('midi')

playMidi('test.mid')