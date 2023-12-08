from tool.my_note import MyNote
from tool.my_chord import MyChord, PlayStyle, Style
from midiutil import MIDIFile

from enum import Enum

class SPECIAL(Enum):
    NONE = "none"
    ROYAL_CHORD ="roch"


def create_melody(notes:list[MyNote], midi:MIDIFile, track = 0, time = 0):
    
    my_notes = notes.copy()
    my_midi = midi
    
    channel = 0
    volume = 100  # 0-127, as per the MIDI standard
   
   
    for note in my_notes:
        if not note.is_delay:
            my_midi.addNote(track, channel, note.note, time, note.duration, volume)
        
        time += note.duration

           
    
    print("melody play time " , time)
    return midi



def create_chord(chords:list[MyChord]  , midi, track = 0, time = 0, special:SPECIAL = SPECIAL.NONE):

    channel = 0
    volume = 100  # 0-127, as per the MIDI standard
   
    if special == SPECIAL.NONE:
        print(f'chords are : {chords} with length {len(chords)}')
        for i, chord in enumerate(chords):

            print(f'tessss')

            # set play duration scale
            empty_duration = (((1 - chord.play_style.duration_scale) * (chord.duration)))
            play_duration = chord.duration - empty_duration
            time += empty_duration
        
            if not chord.is_delay:
                # STANDARD
                if(chord.play_style.style == Style.STANDARD):
                    print(f'STD now playing chord {chord.get_str()} for {play_duration} at {time} with {chord.play_style.style} from {time} until {time + chord.duration}')
                    for note in chord.get_notes():
                        midi.addNote(track, channel, note, time, play_duration, volume)

                # REPEAT , using beat count
                elif(chord.play_style.style == Style.REPEAT):
                    interval = play_duration / chord.play_style.beat_count
                    for i in range(chord.play_style.beat_count):
                        for note in chord.get_notes():
                            midi.addNote(track, channel, note, time + (interval * i), interval, volume)
                            print(f'now playing chord {chord.get_str()} for {interval} at {time}')
                
                # PROGRESSIVE, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE):
                    interval = chord.play_style.interval
                    elapsed = 0
                    for i, note in enumerate(chord.get_notes()):
                        
                        # if last key played, play until end of durration
                        if(i == 2):
                            interval = play_duration - (2 * interval)
                        midi.addNote(track, channel, note, time + elapsed, interval, volume)
                        elapsed += interval
                        print(f'now playing chord {chord.get_str()} for {interval} at {time}')
                    
                # PROGRESSIVE_REVERSVE, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE_REVERSE):
                    interval = chord.play_style.interval
                    elapsed = 0
                    for i, note in enumerate(chord.get_notes()[::-1]):

                        # if last key played, play until end of durration
                        if(i == 2):
                            interval = play_duration - (2 * interval)
                        midi.addNote(track, channel, note, time + elapsed, interval, volume)
                        elapsed += interval
                        print(f'now playing chord {chord.get_str()} for {interval} at {time}')

                # PROGRESSIVE_FULL, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE_FULL):
                    interval = chord.play_style.interval
                    beat_count = play_duration / interval
                    counter = 0
                    i = 0
                    notes = chord.get_notes()
                    while(counter < beat_count):                  
                        midi.addNote(track, channel, notes[i], time + (interval * counter), interval, volume)
                        print(f'PF now playing chord {chord.get_str()} for {interval} at {time}')
                        i += 1
                        counter += 1
                        if(i == 3):
                            i = 0
                
                # PROGRESSIVE_FULL_REVERSE, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE_FULL_REVERSE):
                    interval = chord.play_style.interval
                    beat_count = play_duration / interval
                    counter = 0
                    i = 0
                    notes = chord.get_notes()[::-1]
                    while(counter < beat_count):                  
                        midi.addNote(track, channel, notes[i], time + (interval * counter), interval, volume)
                        print(f'PF now playing chord {chord.get_str()} for {interval} at {time}')
                        i += 1
                        counter += 1
                        if(i == 3):
                            i = 0

                # PROGRESSIVE_REPEAT, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE_REPEAT):
                    interval = chord.play_style.interval
                    beat_count = play_duration / interval
                
                    counter = 0
                    is_up = True
                    i = 0
                    notes = chord.get_notes()
                    while(counter < beat_count):                  
                        midi.addNote(track, channel, notes[i], time + (interval * counter), interval, volume)
                        print(f'PF now playing chord {chord.get_str()} for {interval} at {time}')
                        if(is_up):
                            i += 1
                            if(i > 2):
                                i = 1
                                is_up = False  
                        else:
                            i -= 1
                            if(i < 0):
                                i = 1
                                is_up = True 
                    
                        counter += 1


                # PROGRESSIVE_REPEAT_REVERSE, using interval 
                elif(chord.play_style.style == Style.PROGRESSIVE_REPEAT_REVERSE):
                    interval = chord.play_style.interval
                    beat_count = play_duration / interval
                    counter = 0
                    is_up = True
                    i = 0
                    notes = chord.get_notes()[::-1]
                    while(counter < beat_count):                  
                        midi.addNote(track, channel, notes[i], time + (interval * counter), interval, volume)
                        print(f'PF now playing chord {chord.get_str()} for {interval} at {time}')
                        if(is_up):
                            i += 1
                            if(i > 2):
                                i = 1
                                is_up = False  
                        else:
                            i -= 1
                            if(i < 0):
                                i = 1
                                is_up = True 
                        counter += 1

                # BROKEN_CHORD
                elif(chord.play_style.style == Style.PROGRESSIVE_REPEAT_REVERSE):
                    interval = chord.play_style.interval
                    beat_count = play_duration / interval
                    counter = 0
                    is_up = True
                    i = 0
                    notes = chord.get_notes()[::-1]
                    while(counter < beat_count):                  
                        midi.addNote(track, channel, notes[i], time + (interval * counter), interval, volume)
                        print(f'PF now playing chord {chord.get_str()} for {interval} at {time}')
                        if(is_up):
                            i += 1
                            if(i > 2):
                                i = 1
                                is_up = False  
                        else:
                            i -= 1
                            if(i < 0):
                                i = 1
                                is_up = True 
                        counter += 1

                # ROYAL_CHORD
                elif(chord.play_style.style == Style.ROYAL_CHORD):
                    interval = chord.play_style.interval
                    notes = chord.get_notes()

                    midi.addNote(track, channel, notes[0], time + (interval * 0), interval, volume)
                    midi.addNote(track, channel, notes[1], time + (interval * 0), interval, volume)
                    midi.addNote(track, channel, notes[2], time + (interval * 0), interval, volume)

                    midi.addNote(track, channel, notes[0], time + (interval * 1), interval, volume)
                    midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
                    midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)

                    midi.addNote(track, channel, (notes[0]) + 12, time + (interval * 4), play_duration - (interval * 4), volume)
                    midi.addNote(track, channel, (notes[1]) + 0, time + (interval * 4), play_duration - (interval * 4), volume)
                    midi.addNote(track, channel, (notes[2]) - 0, time + (interval * 4), play_duration - (interval * 4), volume)

                # ROYAL_CHORD_2
                elif(chord.play_style.style == Style.ROYAL_CHORD_2):
                    interval = chord.play_style.interval
                    notes = chord.get_notes()

                    midi.addNote(track, channel, notes[0], time + (interval * 0), interval, volume)
                    midi.addNote(track, channel, notes[1], time + (interval * 0), interval, volume)
                    midi.addNote(track, channel, notes[2], time + (interval * 0), interval, volume)

                    midi.addNote(track, channel, notes[0], time + (interval * 1), interval, volume)
                    midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
                    midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)

                    midi.addNote(track, channel, (notes[0]) + 0, time + (interval * 4), play_duration - (interval * 4), volume)
                    midi.addNote(track, channel, (notes[1]) + 0, time + (interval * 4), play_duration - (interval * 4), volume)
                    midi.addNote(track, channel, (notes[2]) - 12, time + (interval * 4), play_duration - (interval * 4), volume)
                

                # ROYAL_CHORD 5
                elif(chord.play_style.style == Style.ROYAL_CHORD_5):
                    interval = chord.play_style.interval
                    notes = chord.get_notes()

                    midi.addNote(track, channel, notes[2], time + (interval * 0), interval, volume)
                    midi.addNote(track, channel, notes[0], time + (interval * 1), interval, volume)
                    midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
                    midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)
                    midi.addNote(track, channel, (notes[2]) + 1, time + (interval * 4), play_duration - (interval * 4), volume)
                    # midi.addNote(track, channel, (notes[2]) - 10, time + (interval * 4), play_duration - (interval * 4), volume)

            time += chord.duration  

            print(f"Total Play Time : {time} elapsed")
        return midi    
          

    elif special == SPECIAL.ROYAL_CHORD:

        from more_itertools import chunked


        # Memecah list menjadi sublist dengan panjang maksimal 4
        chunked_chords = list(chunked(chords, 8))

        for c_chords in chunked_chords:
            
            interval = c_chords[0].play_style.interval
            empty_duration = (((1 - c_chords[0].play_style.duration_scale) * (c_chords[0].duration)))
            play_duration = c_chords[0].duration - empty_duration
            
            # play chord 1
            notes = c_chords[0].get_notes()

            midi.addNote(track, channel, notes[0], time + (interval * 0), interval, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 0), interval, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 0), interval, volume)

            midi.addNote(track, channel, notes[0], time + (interval * 1), interval, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)

            time += play_duration

            # play chord 2
            notes = c_chords[1].get_notes()
            midi.addNote(track, channel, (notes[0]) + 12, time, play_duration, volume)
            midi.addNote(track, channel, (notes[1]) + 0, time, play_duration, volume)
            midi.addNote(track, channel, (notes[2]) - 0, time, play_duration, volume)

            time += play_duration

            # play chord 3
            notes = c_chords[2].get_notes()

            midi.addNote(track, channel, notes[0], time + (interval * 0), interval, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 0), interval, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 0), interval, volume)

            midi.addNote(track, channel, notes[0], time + (interval * 1), interval, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)

            time += play_duration

            # play chord 4
            notes = c_chords[3].get_notes()
            midi.addNote(track, channel, (notes[0]) + 12, time, play_duration, volume)
            midi.addNote(track, channel, (notes[1]) + 0, time, play_duration, volume)
            midi.addNote(track, channel, (notes[2]) - 0, time, play_duration, volume)
            
            time += play_duration

            # play chord 5
            notes = c_chords[4].get_notes()

            midi.addNote(track, channel, notes[0] + 12, time + (interval * 0), interval * 3, volume)
            midi.addNote(track, channel, notes[1] + 0, time + (interval * 0), interval * 3, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 0), interval * 3, volume)

            midi.addNote(track, channel, notes[2], time + (interval * 3), interval, volume)
            
            time += play_duration

            # play chord 6
            notes = c_chords[5].get_notes()
        
            midi.addNote(track, channel, notes[0] + 12, time + (interval * 0), interval * 3, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 0), interval * 3, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 0), interval * 3, volume)

            midi.addNote(track, channel, notes[0] + 12, time + (interval * 3), interval, volume)
            
            time += play_duration

            # play chord 7
            notes = c_chords[6].get_notes()
        
            midi.addNote(track, channel, notes[0] + 0, time + (interval * 0), interval * 8, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 0), interval * 8, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 0), interval * 8, volume)

            midi.addNote(track, channel, notes[1], time + (interval * 1), interval, volume)
            midi.addNote(track, channel, notes[1], time + (interval * 2), interval, volume)
            midi.addNote(track, channel, notes[0], time + (interval * 3), interval, volume)

            time += play_duration
            
            # play chord 8
            notes = c_chords[7].get_notes()
        
            midi.addNote(track, channel, notes[0], time + (interval * 0), interval, volume)
        
            midi.addNote(track, channel, notes[1], time + (interval * 1), interval, volume)
            midi.addNote(track, channel, notes[2], time + (interval * 2), interval, volume)
        
            time += play_duration





            
        print(f"Total Play Time : {time} elapsed")
        return midi  




        






from music21 import midi as mp
def play_midi(path:str, midi:MIDIFile):

    with open("output/"+path, "wb") as output_file:
        midi.writeFile(output_file)
    mf = mp.MidiFile()
    mf.open("output/"+path) # path='abc.midi'
    mf.read()
    mf.close()
    s = mp.translate.midiFileToStream(mf)
    s.show('midi')


def hello_world():
    print("hello world")