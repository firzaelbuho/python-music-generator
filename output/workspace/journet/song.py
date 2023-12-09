# from tool.helo import hello_world
from midiutil import MIDIFile
from tracks import *

track = 0
time = 0
tempo = 130

midi = MIDIFile(10)  # 10 track, defaults to format 1 (tempo track is created  automatically)
midi.addTempo(track, time, tempo)







# melody vocal 
midi = p.create_melody(vocal_melody, midi, track = 0, time = 0)

# main chord
midi = p.create_chord(piano_chord, midi, track = 1, time = 0)

# solo piano
midi = p.create_melody(solo_piano, midi, track = 3, time = 0)

# bass
midi = p.create_melody(bass_intro, midi, track = 2, time = 0)

# violin
midi = p.create_melody(violin, midi, track = 5, time = 0)

# bass chord
midi = p.create_chord(chord_bass_intro, midi, track = 4, time = 0)


# # testing
# midi = p.create_melody(melody_bridge, midi, track = 5, time = 0)


p.play_midi("journey.mid", midi)


