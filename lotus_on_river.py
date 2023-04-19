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


from tool.collection import lotus_on_river_chord, lotus_on_river_melody, lotus_on_river_chord_intro
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)


lotus_chord = copy(lotus_on_river_chord())
lotus_melody = copy(lotus_on_river_melody())
for c in lotus_chord:
    c.play_style.beat_count = 2
    c.play_style.interval = 1
    c.play_style.duration_scale = 1

# canon_bass = tp.transpose_chords_octave((canon),3)
# midi = p.create_chord(canon_bass, midi, track = 1, time = 0)

lotus_chord = tp.combo_style_n_pattern(lotus_chord, Style.PROGRESSIVE_FULL, Style.PROGRESSIVE_FULL_REVERSE, 8,4)    
midi = p.create_chord(lotus_chord, midi, track = 2, time = 0)
# midi = p.create_melody(lotus_melody, midi, track = 1, time = 0)

p.play_midi("lotus_on_the_river.mid", midi)


