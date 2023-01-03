from midithon import *
from music21 import midi

from midiutil import MIDIFile

def showNotes(notes):
    for note in notes:
        print (note.str_note + ", ") 


track = 0
time = 0
tempo = 140


midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


mychord = chord_family['major']['f']
canon_f = transpose(canon_d,"major","d","major","d")



# midi = create_melody(notes_coll,midi, track = 0, time = 0)
midi = create_chord(canon_d ,midi, track= 1, time = 0, style = 1, style_attr = 0.5)



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