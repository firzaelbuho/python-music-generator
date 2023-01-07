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
   
    MyChord('D', "delay", 2),
    MyChord('E', "maj", 2),
    MyChord('F#', "min", 1.5),
    MyChord('B', "min", 2.5),
]

bb = [
     MyNote('do', 1.25),
     MyNote('re', 0.5),
     MyNote('mi', 0.75),
     MyNote('fa', 0.75),
     MyNote('sol', 1.25),
     MyNote('mi', 0.5),
     MyNote('do', 3),
]

x = transpose(blue_bird, "major", "d", "major", "c")
midi = create_melody(bb, midi, track = 0, time = 0)
# midi = create_chord(x ,midi, track= 1, time = 0, style = 0, style_attr = 0.5)




playMidi("test.mid", midi)