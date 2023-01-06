from midithon import *

from midiutil import MIDIFile

track = 0
time = 0
tempo =140

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)

mychord = chord_family['major']['f']
canon_f = transpose(canon_d,"major","d","major","d")
showNotes(canon_f)

dur = 4
hikaru_nara = [
   
    MyChord('D', "maj", dur ),
    MyChord('E', "maj", dur ),
    MyChord('F#', "min", dur ),
    MyChord('C#', "min", dur ),

    MyChord('D', "maj", 4 ),
    MyChord('A', "maj", 4 ),
   
]

blue_bird = [
   
    MyChord('F', "delay", 2),
    MyChord('F', "maj", 2),
    MyChord('E', "min", 1.5),
    MyChord('A', "min", 2.5),

    MyChord('F', "delay", 2),
    MyChord('D', "min", 2),
    MyChord('G', "maj", 1.5),
    MyChord('C', "maj", 3.5),

    
    MyChord('F', "delay", 2),
    MyChord('F', "maj", 2),
    MyChord('E', "min", 1.5),
    MyChord('A', "min", 2.5),

    MyChord('F', "delay", 2),
    MyChord('D', "min", 2),
    MyChord('G', "maj", 1.5),
    MyChord('A', "min", 2.5),

   
]
x = transpose(blue_bird, "major", "f", "major", "c")
# midi = create_melody(notes_coll,midi, track = 0, time = 0)
midi = create_chord(x ,midi, track= 1, time = 0, style = 0, style_attr = 0.5)


playMidi("test.mid", midi)