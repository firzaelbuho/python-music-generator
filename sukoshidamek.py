# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style
from midiutil import MIDIFile
from tool.miditool import is_odd

track = 0
time = 0
tempo =180

midi = MIDIFile(4)  # 4 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)


from tool.collection import *
import tool.transposer as tp
from copy import copy

# high = tp.transpose_notes(blue_bird_melody, 12)

durr = 8
sukoshidamek = [
    MyChord("C",ChordType.MAJ, durr),
    MyChord("F",ChordType.MAJ, durr),
    MyChord("G",ChordType.MAJ, durr),
    MyChord("C",ChordType.MAJ, durr),  
    MyChord("C",ChordType.MAJ, durr),
    MyChord("F",ChordType.MAJ, durr),
    MyChord("G",ChordType.MAJ, durr),
    MyChord("C",ChordType.MAJ, durr),  
]

for chord in sukoshidamek:
    chord.play_style.style = Style.REPEAT
    chord.play_style.beat_count = 4




# canon = tp.combo_style_n_pattern(royal_chord, Style.REPEAT, Style.REPEAT, durr,4)    
midi = p.create_chord(sukoshidamek, midi, track = 0, time = 0)

p.play_midi("sukoshi.mid", midi)


