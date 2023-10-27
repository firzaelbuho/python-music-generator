# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style
from midiutil import MIDIFile
from tool.miditool import is_odd

track = 0
time = 0
tempo =160

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


from tool.collection import *
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)


chords = [
    MyChord("C", ChordType.MAJ),
    MyChord("F", ChordType.MAJ),
    MyChord("G", ChordType.MAJ),
    MyChord("E", ChordType.MIN),
    MyChord("A", ChordType.MIN),
    MyChord("F", ChordType.MAJ),
    MyChord("G", ChordType.MAJ),
    MyChord("C", ChordType.MAJ),

    MyChord("C", ChordType.MAJ),
    MyChord("F", ChordType.MAJ),
    MyChord("G", ChordType.MAJ),
    MyChord("E", ChordType.MIN),
    MyChord("A", ChordType.MIN),
    MyChord("F", ChordType.MAJ),
    MyChord("G", ChordType.MAJ),
    MyChord("C", ChordType.MAJ),
    
]
for c in chords:
    c.play_style.style = Style.REPEAT
    c.play_style.beat_count = 4
    c.play_style.interval = 2
    c.duration = 8

# canon_bass = tp.transpose_chords_octave((royal_chord),4)
# midi = p.create_chord(canon_bass, midi, track = 1, time = 0)

# canon = tp.combo_style_n_pattern(royal_chord, Style.ROYAL_CHORD, Style.ROYAL_CHORD, 8,4)    
midi = p.create_chord(chords, midi, track = 0, time = 0, special= p.SPECIAL.NONE)
# midi = p.create_chord(royal_chord(), midi, track = 1, time = 0, special= p.SPECIAL.NONE)


p.play_midi("mengapa.mid", midi)


