from midithon import *

from midiutil import MIDIFile

track = 0
time = 0
tempo =140

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)

mychord = chord_family['major']['f']


dur = 4
hikaru_nara = [
   
    MyChord('D', "maj", dur ),
    MyChord('E', "maj", dur ),
    MyChord('F#', "min", dur ),
    MyChord('C#', "min", dur ),

    MyChord('D', "maj", 4 ),
    MyChord('B', "min", 4 ),
   
]

blue_bird = [
   
    MyChord('delay', "", 2),
    MyChord('E', "maj", 2),
    MyChord('F#', "min", 1.5),
    MyChord('B', "min", 2.5),
   
   
]

ibkk = [
    MyNote('delay', 1.25),
    MyNote('do', 1.25),
    MyNote('re', 0.5),
    MyNote('mi', 0.75),
    MyNote('fa', 0.75),
    MyNote('sol', 1.25),
    MyNote('mi', 0.5),
    MyNote('do', 1.5),
    MyNote('la', 1),
    MyNote('do', 0.5, 5),
    MyNote('si', 0.75),
    MyNote('la', 0.75),
    MyNote('sol', 3),
]


x = transpose_chords(blue_bird, "major", "d", "major", "d")
showChords(blue_bird)
showNotes(ibkk)


# y = transpose_notes(bb, 4)
# midi = create_melody(x, midi, track = 0, time = 0)
# midi = create_chord(x ,midi, track= 1, time = 0, style = 0, style_attr = 0.5)




# playMidi("test.mid", midi)