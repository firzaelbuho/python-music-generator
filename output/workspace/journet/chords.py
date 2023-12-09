# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style, PlayStyle
from midiutil import MIDIFile
from tool.miditool import is_odd

track = 0
time = 0
tempo = 130

midi = MIDIFile(8)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


from tool.collection import *
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)

durr = 8
style = Style.REPEAT_INVERSION_13_ONCE
play_style = PlayStyle(style=style, beat_count=4, interval=1.0)
chord_octave = 3
chord_1 = [
   
    # main chord
    MyChord("C",ChordType.MAJ, durr, chord_octave, play_style),
    MyChord("F",ChordType.MAJ, durr, chord_octave, play_style),
    MyChord("G",ChordType.MAJ, durr, chord_octave, play_style),
    MyChord("E",ChordType.MIN, durr, chord_octave, play_style),
    
    MyChord("A",ChordType.MIN, durr, chord_octave, play_style),
    MyChord("F",ChordType.MAJ, durr, chord_octave, play_style),
    MyChord("G",ChordType.MAJ, durr, chord_octave, play_style),
    MyChord("C",ChordType.MAJ, durr, chord_octave, play_style),
    # main chord



]

chord_reff_1 = [
   
    # main chord
    MyChord("F",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("B",ChordType.DIM, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("G",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("A",ChordType.MIN, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),


    MyChord("F",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("D",ChordType.MIN, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("E",ChordType.MIN, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("G",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
]

chord_reff_2 = [
   
    # main chord
    MyChord("F",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("G",ChordType.DIM, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("E",ChordType.MIN, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("A",ChordType.MIN, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),


    MyChord("F",ChordType.MAJ, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("B",ChordType.DIM, 4, chord_octave, play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_13_ONCE, beat_count=2
    )),
    MyChord("C",ChordType.MAJ, 4, chord_octave , play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_12_ONCE, beat_count=2
    )),
    MyChord("C",ChordType.MAJ, 4, chord_octave , play_style = PlayStyle(
        style=Style.REPEAT_INVERSION_12_ONCE, beat_count=2
    )),
]

chord_bass_intro = [
    MyChord("C",ChordType.DELAY, 1.5, 6),
    MyChord("A",ChordType.MIN, 2.5, 6)

]



