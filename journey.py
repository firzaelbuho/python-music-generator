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
style = Style.PROGRESSIVE_FULL
play_style = PlayStyle(style=style, beat_count=4, interval=1.0)
octave = 4
chord = [
    MyChord("delay",ChordType.DELAY, 58),
    MyChord("C",ChordType.MAJ, durr, octave, play_style),
    MyChord("C",ChordType.MAJ, durr, octave, play_style),

    MyChord("C",ChordType.MAJ, durr, octave, play_style),
    MyChord("F",ChordType.MAJ, durr, octave, play_style),
    MyChord("G",ChordType.MAJ, durr, octave, play_style),
    MyChord("E",ChordType.MIN, durr, octave, play_style),

    MyChord("A",ChordType.MIN, durr, octave, play_style),
    MyChord("F",ChordType.MAJ, durr, octave, play_style),
    MyChord("G",ChordType.MAJ, durr, octave, play_style),
    MyChord("C",ChordType.MAJ, durr, octave, play_style),
]

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

melody = []
melody.extend(melody_bait_1)
melody.extend(melody_bait_2)
melody.extend(melody_bait_3)
melody.extend(melody_bait_4)
melody.append(MyNote("delay", 8))
melody.extend(melody_bait_1)
melody.extend(melody_bait_2)
melody.extend(melody_bait_3)
melody.extend(melody_bait_4)





# canon = tp.combo_style_n_pattern(royal_chord, Style.REPEAT, Style.REPEAT, durr,4)    
midi = p.create_melody(melody, midi, track = 0, time = 0)
midi = p.create_chord(chord, midi, track = 1, time = 0)

p.play_midi("journey.mid", midi)


