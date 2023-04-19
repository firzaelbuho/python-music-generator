from tool.my_note import MyNote
from tool.my_chord import MyChord, Style
# from tool.my_chord import MyChord

def transpose_notes(notes:list[MyNote], step:int):
    new_notes = []
    for i, note in enumerate(notes):
        new_note = note
        new_note.note += step
        new_notes.append(new_note)
    
    return new_notes

def transpose_chords_octave(chords:list[MyChord], octave:int):
    new_chords = []
    for i, chord in enumerate(chords):
        new_chord = chord
        new_chord.octave = octave
        new_chords.append(new_chord)
    
    return new_chords

from tool.chord_family import chord_family
def transpose_chords_family(chords:list[MyChord], curr_base:str, curr_key:str, target_base:str, targer_key:str):
    target_chords_family = chord_family[target_base][targer_key]
    current_chords_family = chord_family[curr_base][curr_key]
    new_chords = []

    for i, chord in enumerate(chords):
        if(chord.is_delay):
            new_chord = chord
            new_chords.append(new_chord)
        else:
            for j, current in enumerate(current_chords_family):
                if(chord.str_note == current.str_note and chord.chord_type == current.chord_type):
                    duration = (chord.duration)
                    new_chord = target_chords_family[j]
                    new_chord.duration = duration
                    new_chords.append(new_chord)
                  
                    
                   
    return new_chords

from tool.miditool import is_odd

def combo_style_zigzag(chords:list[MyChord],style_1:Style, style_2:Style):
    new_chords : list[MyChord] = []
    for i,chord in enumerate(chords):
        new_chord = chord
        if(is_odd(i)):
            new_chord.play_style.style = style_2
        else:
            new_chord.play_style.style = style_1
        new_chords.append(new_chord)
    return new_chords

from more_itertools import chunked

def combo_style_n_pattern(chords:list[MyChord],style_1:Style, style_2:Style, n_pattern:int, n_first_count:int = 2):
    token = n_pattern
    new_chords : list[MyChord] = []
    for i,chord in enumerate(chords):
        new_chord = chord
        if(token > (n_pattern - n_first_count)):
            new_chord.play_style.style = style_1
        else:
            new_chord.play_style.style = style_2
        new_chords.append(new_chord)

        token -= 1
        if(token == 0):
            token = n_pattern

    return new_chords

