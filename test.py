# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style
from midiutil import MIDIFile
from tool.miditool import is_odd

track = 0
time = 0
tempo =140

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


from tool.collection import *
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)


royal_chord = copy(royal_chord(8, 'c'))
for c in royal_chord:
    c.play_style.beat_count = 8
    c.play_style.interval = 1
    c.duration = 4

canon_bass = tp.transpose_chords_octave((royal_chord),4)
midi = p.create_chord(canon_bass, midi, track = 1, time = 0)

canon = tp.combo_style_n_pattern(royal_chord, Style.ROYAL_CHORD, Style.ROYAL_CHORD, 8,4)    
midi = p.create_chord(canon, midi, track = 0, time = 0, special= p.SPECIAL.ROYAL_CHORD)

p.play_midi("test.mid", midi)


