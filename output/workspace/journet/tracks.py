# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style, PlayStyle
from tool.miditool import is_odd
from chords import *
from notes import *

vocal_melody = []
# vocal_melody.extend(intro_1)
vocal_melody.append(MyNote("delay", 72))
vocal_melody.extend(melody_bait_1)
vocal_melody.extend(melody_bait_2)
vocal_melody.extend(melody_bait_3)
vocal_melody.extend(melody_bait_4)
vocal_melody.append(MyNote("delay", 8))
vocal_melody.extend(melody_bait_1_v2)
vocal_melody.extend(melody_bait_2_v2)
vocal_melody.extend(melody_bait_3_v2)
vocal_melody.extend(melody_bait_4_v2)
vocal_melody.append(MyNote("delay", 9))
vocal_melody.extend(reff_1)
vocal_melody.extend(reff_2)

piano_chord =[]
piano_chord.append(MyChord("delay",ChordType.DELAY, (58)))
# chord.append( MyChord("C",ChordType.MAJ, durr, octave, play_style))
# kasih jeda
piano_chord.append( MyChord("C",ChordType.MAJ, durr, chord_octave, play_style))
piano_chord.append( MyChord("C",ChordType.MAJ, durr, chord_octave, play_style))
piano_chord.extend(chord_1)
piano_chord.append( MyChord("C",ChordType.MAJ, durr, chord_octave, play_style))
piano_chord.extend(chord_1)
# bridge
piano_chord.append( MyChord("C",ChordType.MAJ, durr, chord_octave, play_style))
piano_chord.extend(chord_reff_1)
piano_chord.extend(chord_reff_2)

solo_piano = []
solo_piano.extend(intro_1)
solo_piano.extend(intro_2)

violin = []
violin.append(MyNote("delay", 32))
violin.extend(intro_2_violin)
