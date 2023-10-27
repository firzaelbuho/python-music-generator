from midithon import *
from tool.my_chord import *
from tool.chord_family import *
from tool.my_note import *
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

    MyChord('B', "min", dur ),
    MyChord('E', "maj", dur ),
    MyChord('D', "maj", dur ),
    MyChord('D', "maj", dur )
]

hikaru_nara_chord_2 = [
   
    MyChord('C', "maj", dur ,5),
    MyChord('D', "maj", dur ,5),
    MyChord('E', "min", dur ,5),
    MyChord('B', "min", dur, 4 ),

    MyChord('A', "min", dur, 4 ),
    MyChord('D', "maj", dur , 5),
    MyChord('C', "maj", dur , 5),
    MyChord('C', "maj", dur , 5)
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


# x = transpose_notes(hikaru_nara, 12)

twinkle = [
     MyNote('C',2),
     MyNote('C',2),
     MyNote('G',2),
     MyNote('G',2),
     MyNote('A',2),
     MyNote('A',2),
     MyNote('G',4),
     MyNote('F',2),
     MyNote('F',2),
     MyNote('E',2),
     MyNote('E',2),
     MyNote('D',2),
     MyNote('D',2),
     MyNote('C',4),
]

twinkle_chord = [
    MyChord('C', "maj", 2),
    MyChord('C', "maj", 2),
    MyChord('E', "min", 2),
    MyChord('E', "min", 2),
    MyChord('F', "maj", 2),
    MyChord('F', "maj", 2),
    MyChord('E', "min", 4),
    MyChord('F', "min", 2),
    MyChord('F', "min", 2),
    MyChord('E', "min", 2),
    MyChord('E', "min", 2),
    MyChord('D', "min", 2),
    MyChord('D', "min", 2),
    MyChord('C', "min", 4),
]


cb =   chord_family["major"]["c"]
royal= [
  cb[4],
  cb[5],
  cb[3],
  cb[6],
  

  ]


mc = [
 cb[1],
 cb[4],
 cb[5],
 cb[1]
  ]



melodi = [
    MyNote("do", 1.5),
    MyNote("do", 1.5),
    MyNote("re", 1),
    MyNote("mi", 1.5),
    MyNote("do", 1),
    MyNote("mi", 1.5),
    MyNote("sol", 1),
    MyNote("do", 2, 6),
    MyNote("si", 1),
    MyNote("la", 2),


]


# showNotes(ibkk)
# royal = transpose_chords(royal, "major", "c", "major", "a")


# midi = create_melody(twinkle, midi, track = 0, time = 0)
# midi = create_melody(melodi, midi, track = 0, time = 0)
# mc = change_durations(mc, 8)
# midi = create_chord(mc ,midi, track= 1, time = 0, style = 0, style_attr = 0 )



# playMidi("test.mid", midi)
# showChords(royal)

# for i in range(0,256):
#     create_note(i)
#     print(i)

print(cb[6].get_str_notes())
