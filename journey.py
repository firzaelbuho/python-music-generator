# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style, PlayStyle
from midiutil import MIDIFile
from tool.miditool import is_odd

track = 0
time = 0
tempo = 140

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


from tool.collection import *
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)

durr = 8
style = Style.REPEAT
play_style = PlayStyle(style=style, beat_count=4, interval=1.0)
octave = 4
chord_1 = [
   
    # main chord
    MyChord("C",ChordType.MAJ, durr, octave, play_style),
    MyChord("F",ChordType.MAJ, durr, octave, play_style),
    MyChord("G",ChordType.MAJ, durr, octave, play_style),
    MyChord("E",ChordType.MIN, durr, octave, play_style),
    
    MyChord("A",ChordType.MIN, durr, octave, play_style),
    MyChord("F",ChordType.MAJ, durr, octave, play_style),
    MyChord("G",ChordType.MAJ, durr, octave, play_style),
    MyChord("C",ChordType.MAJ, durr, octave, play_style),
    # main chord



]

chord =[]
chord.append(MyChord("delay",ChordType.DELAY, (58)))
# chord.append( MyChord("C",ChordType.MAJ, durr, octave, play_style))
# kasih jeda
chord.append( MyChord("C",ChordType.MAJ, durr, octave, play_style))
chord.append( MyChord("C",ChordType.MAJ, durr, octave, play_style))
chord.extend(chord_1)
chord.append( MyChord("C",ChordType.MAJ, durr, octave, play_style))
chord.extend(chord_1)

melody_bait_1 = [
    MyNote("E", 1),
    MyNote("F", 1),
    MyNote("C", 0.5), # harmony
    MyNote("E", 0.5), # harmony
    MyNote("G", 2),


    MyNote("G", 0.5),
    MyNote("G", 0.5),
    MyNote("C", 3, 6),

    MyNote("B", 0.5),
    MyNote("B", 0.5),
    MyNote("B", 2),


    MyNote("D", 0.5), # harmony
    MyNote("F", 0.5), # harmony
    MyNote("A", 3),

    

    
]
melody_bait_2 = [
    MyNote("G", 1),
    MyNote("F", 0.5),
    MyNote("E", 0.5),
    MyNote("G", 0.5,4), # harmony
    MyNote("B", 0.5,4), # harmony
    MyNote("D", 2),


    MyNote("D", 0.5),
    MyNote("D", 0.5),
    MyNote("B", 3),

    MyNote("A", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 2),


    MyNote("C", 0.5), # harmony
    MyNote("E", 0.5), # harmony
    MyNote("G", 3),   
]

melody_bait_3 = [
    MyNote("D", 1),
    MyNote("E", 0.5),
    MyNote("D", 0.5),
    MyNote("E", 0.5,4), # harmony
    MyNote("G", 0.5,4), # harmony
    MyNote("C", 2),


    MyNote("C", 0.5),
    MyNote("C", 0.5),
    MyNote("B", 3),

    MyNote("B", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 1.5),
    MyNote("A", 0.5),

    MyNote("F", 0.5), # harmony
    MyNote("A", 0.5, 5), # harmony
    MyNote("D", 3, 6),   
]

melody_bait_4 = [
    MyNote("delay", 1, 6),
    MyNote("C", 1, 6),
    MyNote("C", 2, 6),
    MyNote("B", 2),
    MyNote("A", 2), 
    MyNote("B", 2), 

    MyNote("E", 0.5), # harmony
    MyNote("G", 0.5), # harmony
    MyNote("C", 5,6),


   
]

chord_bass_intro = [
    MyChord("delay",ChordType.DELAY, (1.5)),
    MyChord("D",ChordType.MAJ, 2.5, 5)

]

bass_intro = [
    MyNote("delay", 1.5),
    MyNote("la", 2.5, 8),

    MyNote("delay", 1.5),
    MyNote("re", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("sol", 2.5, 8),

    MyNote("delay", 1.5),
    MyNote("do", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("fa", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("fa", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("mi", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("sol", 2.5, 7),


]
intro_octave = 6
intro_1 = [
    MyNote("do", 1,intro_octave),


    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 0.25,intro_octave),
    MyNote("la", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave-1),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 2.5,intro_octave),

    MyNote("si", 1,intro_octave),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave),
    MyNote("la", 0.25,intro_octave),
    MyNote("do", 2.5,intro_octave),

    MyNote("sol", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("re", 1,intro_octave),
    MyNote("la", 0.25,intro_octave-1),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 2.5,intro_octave),

    MyNote("la", 1,intro_octave),

    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    #################

    MyNote("do", 1),
    MyNote("re", 0.25),
    MyNote("fa", 0.25),
    MyNote("la", 2.5),

    MyNote("la", 1),
    MyNote("sol", 0.25),
    MyNote("si", 0.25),
    MyNote("re", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),
    MyNote("sol", 2.5),

    MyNote("si", 1),
    MyNote("fa", 0.25),
    MyNote("la", 0.25),
    MyNote("do", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),   
    MyNote("sol", 2.5),

    MyNote("mi", 1),
    MyNote("si", 0.25, 4),
    MyNote("re", 0.25),
    MyNote("fa", 2.5),

    MyNote("re", 2),
    MyNote("do", 6),
  
   

   
]
melody = []
melody.extend(intro_1)
melody.append(MyNote("delay", 8))
melody.extend(melody_bait_1)
melody.extend(melody_bait_2)
melody.extend(melody_bait_3)
melody.extend(melody_bait_4)
melody.append(MyNote("delay", 8))
melody.extend(melody_bait_1)
melody.extend(melody_bait_2)
melody.extend(melody_bait_3)
melody.extend(melody_bait_4)





# melody  
midi = p.create_melody(melody, midi, track = 0, time = 0)

# main chord
midi = p.create_chord(chord, midi, track = 1, time = 0)

# bass
# midi = p.create_melody(bass_intro, midi, track = 2, time = 0)

# bass chord
midi = p.create_chord(chord_bass_intro, midi, track = 3, time = 0)


p.play_midi("journey.mid", midi)

