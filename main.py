from midithon import *

from midiutil import MIDIFile

track = 0
time = 0
tempo =140

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)

mychord = chord_family['major']['f']


dur = 4



blue_bird_chord = [
   
    MyChord('delay', "", 1.5),
    MyChord('F', "maj", 2),
    MyChord('E', "min", 2),
    MyChord('A', "min", 2.5),
   
    MyChord('delay', "", 1.5),
    MyChord('D', "min", 2),
    MyChord('G', "maj", 2),
    MyChord('C', "maj", 2.5),

    MyChord('delay', "", 1.5),
    MyChord('F', "maj", 2),
    MyChord('E', "min", 2),
    MyChord('A', "min", 2.5),
   
    MyChord('delay', "", 1.5),
    MyChord('D', "min", 2),
    MyChord('G', "maj", 2),
    MyChord('A', "min", 2.5),
      
]

blue_bird_melody = [
    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('B', 1.5),
    MyNote('A', 3),

  
    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('D', 1, 5),
    MyNote('C', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('E', 2, 5),

    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('B', 1.5),
    MyNote('A', 3),

    MyNote('A', 0.5),
    MyNote('E', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('A', 0.5),
    MyNote('E', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('G', 1),
    MyNote('G', 1),
    MyNote('A', 0.5),
    MyNote('A', 1.5),
    
]

hikaru_nara_chord = [
   
    MyChord('D', "maj", dur ),
    MyChord('E', "maj", dur ),
    MyChord('F#', "min", dur ),
    MyChord('C#', "min", dur ),

    MyChord('B', "min", dur, 3 ),
    MyChord('E', "maj", dur ),
    MyChord('D', "maj", dur ),
    MyChord('D', "maj", dur )
]


hikaru_nara = [
    MyNote('do', 0.5, 5),
    MyNote('si', 0.5),
    MyNote('do', 0.5, 5),
    MyNote('re', 1, 5),
    MyNote('do', 1, 5),
    MyNote('do', 1, 5),
    MyNote('si', 0.5),
    MyNote('do', 0.5, 5),
    MyNote('re', 1.5, 5),

    MyNote('do', 1, 5),
    MyNote('mi', 1, 5),
    MyNote('fa', 0.5, 5),
    MyNote('mi', 1.5, 5),
    MyNote('re', 1, 5),
    MyNote('do', 2, 5),

    MyNote('do', 1, 5),
    MyNote('si', 1),
    MyNote('la', 1),
    MyNote('fa', 1),
    MyNote('sol', 1),
    MyNote('la', 1),
    MyNote('do', 1, 5),
    MyNote('si', 0.5),
    MyNote('la', 1),
    MyNote('si', 1),
    MyNote('do', 1, 5),


    
]


x = transpose_notes(hikaru_nara, 12)




# showNotes(ibkk)
hikaru_nara_chord = transpose_chords(hikaru_nara_chord, "major", "d", "major", "c")
showChords(hikaru_nara_chord)
# y = transpose_notes(bb, 4)
midi = create_melody(hikaru_nara, midi, track = 0, time = 0)
midi = create_chord(hikaru_nara_chord ,midi, track= 1, time = 0, style = 0, style_attr = 0.5 )
playMidi("test.mid", midi)