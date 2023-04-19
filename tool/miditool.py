from mingus.core import chords
from midiutil import MIDIFile





def k(int_note:int):
    note = int_note % 12
    key = ""
    if(note == 1):
        key = "C"
    elif(note == 2):
        key = "C#"
    elif(note == 3):
        key = "D"
    elif(note == 4):
        key = "D#"
    elif(note == 5):
        key = "E"
    elif(note == 6):
        key = "F"
    elif(note == 7):
        key = "F#"
    elif(note == 8):
        key = "G"
    elif(note == 9):
        key = "G#"
    elif(note == 10):
        key = "A"
    elif(note == 11):
        key = "A#"
    elif(note == 0):
        key = "B"

    return key

# Fungsi utk membuat note dr string
def n(note :str, octave=4):
    note_number = 0

    if note == 'C':
        note_number = 1
    if note == 'C#':
        note_number = 2
    if note == 'D':
        note_number = 3
    if note == 'D#':
        note_number = 4
    if note == 'E':
        note_number = 5
    if note == 'F':
        note_number = 6
    if note == 'F#':
        note_number = 7
    if note == 'G':
        note_number = 8
    if note == 'G#':
        note_number = 9
    if note == 'A':
        note_number = 10
    if note == 'A#':
        note_number = 11
    if note == 'B':
        note_number = 12
    
    if note == 'do':
        note_number = 1
    if note == 'dis':
        note_number = 2
    if note == 're':
        note_number = 3
    if note == 'ris':
        note_number = 4
    if note == 'mi':
        note_number = 5
    if note == 'fa':
        note_number = 6
    if note == 'fis':
        note_number = 7
    if note == 'sol':
        note_number = 8
    if note == 'sis':
        note_number = 9
    if note == 'la':
        note_number = 10
    if note == 'lis':
        note_number = 11
    if note == 'si':
        note_number = 12

    if note == '1':
        note_number = 1
    if note == '1#':
        note_number = 2
    if note == '2':
        note_number = 3
    if note == '2#':
        note_number = 4
    if note == '3':
        note_number = 5
    if note == '4':
        note_number = 6
    if note == '4#':
        note_number = 7
    if note == '5':
        note_number = 8
    if note == '5#':
        note_number = 9
    if note == '6':
        note_number = 10
    if note == '6#':
        note_number = 11
    if note == '7':
        note_number = 12
    
    note_number += octave * 12
    return note_number



def is_odd(n):
    """
    Fungsi untuk memeriksa apakah suatu bilangan bulat adalah bilangan ganjil atau tidak.
    Mengembalikan nilai True jika bilangan ganjil, dan False jika sebaliknya.
    """
    return n % 2 != 0
