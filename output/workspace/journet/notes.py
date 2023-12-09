# from tool.helo import hello_world
import tool.player as p
from tool.my_note import MyNote
from tool.my_chord import MyChord, ChordType, Style, PlayStyle
from midiutil import MIDIFile
from tool.miditool import is_odd



melody_bait_1 = [
    MyNote("E", 1),
    MyNote("F", 1),
    MyNote("C", 0.5), # harmony
    MyNote("E", 0.5), # harmony
    MyNote("G", 2),


    MyNote("G", 0.5),
    MyNote("G", 0.5),
    MyNote("C", 3, 6),

    MyNote("B", 0.5),
    MyNote("B", 0.5),
    MyNote("B", 2),


    MyNote("D", 0.5), # harmony
    MyNote("F", 0.5), # harmony
    MyNote("A", 3),

    
]

melody_bait_1_v2 = [
    MyNote("E", 1),
    MyNote("F", 1),
    MyNote("C", 0.5), # harmony
    MyNote("E", 0.5), # harmony
    MyNote("G", 2),


    MyNote("G", 0.5),
    MyNote("G", 0.5),
    MyNote("C", 3, 6),

    MyNote("B", 0.5),
    MyNote("B", 0.5),
    MyNote("B", 3),


   
    MyNote("C", 1, 6),
    MyNote("A", 2),

    

    
]
melody_bait_2 = [
    MyNote("G", 1),
    MyNote("F", 0.5),
    MyNote("E", 0.5),
    MyNote("G", 0.5,4), # harmony
    MyNote("B", 0.5,4), # harmony
    MyNote("D", 2),


    MyNote("D", 0.5),
    MyNote("D", 0.5),
    MyNote("B", 3),

    MyNote("A", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 2),


    MyNote("C", 0.5), # harmony
    MyNote("E", 0.5), # harmony
    MyNote("G", 3),   
]

melody_bait_2_v2 = [
    MyNote("G", 1),
    MyNote("F", 0.5),
    MyNote("E", 0.5),
    MyNote("G", 0.5,4), # harmony
    MyNote("B", 0.5,4), # harmony
    MyNote("D", 2),


    MyNote("D", 0.5),
    MyNote("D", 0.5),
    MyNote("B", 3),

    MyNote("A", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 3),


   
    MyNote("B", 1),   
    MyNote("G", 2),   
]

melody_bait_3 = [
    MyNote("D", 1),
    MyNote("E", 0.5),
    MyNote("D", 0.5),
    MyNote("E", 0.5,4), # harmony
    MyNote("G", 0.5,4), # harmony
    MyNote("C", 2),


    MyNote("C", 0.5),
    MyNote("C", 0.5),
    MyNote("B", 3),

    MyNote("B", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 1.5),
    MyNote("A", 0.5),

    MyNote("F", 0.5), # harmony
    MyNote("A", 0.5, 5), # harmony
    MyNote("D", 3, 6),   
]
melody_bait_3_v2 = [
    MyNote("D", 1),
    MyNote("E", 0.5),
    MyNote("D", 0.5),
    MyNote("E", 0.5,4), # harmony
    MyNote("G", 0.5,4), # harmony
    MyNote("C", 2),


    MyNote("C", 0.5),
    MyNote("C", 0.5),
    MyNote("B", 3),

    MyNote("B", 0.5),
    MyNote("A", 0.5),
    MyNote("A", 1.5),
    MyNote("D", 0.5,6),

    MyNote("C", 4, 6),    
]

melody_bait_4 = [
    MyNote("delay", 1, 6),
    MyNote("C", 1, 6),
    MyNote("C", 2, 6),
    MyNote("B", 2),
    MyNote("A", 2), 
    MyNote("B", 2), 

    MyNote("E", 0.5), # harmony
    MyNote("G", 0.5), # harmony
    MyNote("C", 5,6),  
]

melody_bridge = [
    MyNote("mi", 1),
    MyNote("mi", 1),
    MyNote("mi", 1),
    MyNote("fa", 0.5),
    MyNote("sol", 1.5),

    MyNote("sol", 1),
    MyNote("fa", 1),
    MyNote("mi", 1),
    MyNote("re", 1),
    MyNote("re", 1),

    MyNote("re", 0.5),
    MyNote("re", 0.5),
    MyNote("mi", 0.5),
    MyNote("re", 4),

    ###########

    MyNote("re", 0.5),
    MyNote("do", 1),
    MyNote("do", 1),
    MyNote("do", 1),
    MyNote("re", 0.5),
    MyNote("mi", 1.5),

    MyNote("mi", 1),
    MyNote("re", 1),
    MyNote("do", 1),
    MyNote("si", 1, 4),
    MyNote("si", 1,4),

    MyNote("si", 0.5,4),
    MyNote("si", 0.5,4),
    MyNote("do", 0.5),
    MyNote("si", 4.5 ,4),


]

melody_bait_4_v2 = [
    MyNote("delay", 1, 6),
    MyNote("C", 1, 6),
    MyNote("C", 2, 6),
    MyNote("B", 2),
    MyNote("A", 2), 
    MyNote("D",2,  6), 

    MyNote("E", 0.5), # harmony
    MyNote("G", 0.5), # harmony
    MyNote("C", 5,6),  
]

bass_intro = [
    MyNote("delay", 1.5),
    MyNote("la", 2.5, 8),

    MyNote("delay", 1.5),
    MyNote("re", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("sol", 2.5, 8),

    MyNote("delay", 1.5),
    MyNote("do", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("fa", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("fa", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("mi", 2.5, 7),

    MyNote("delay", 1.5),
    MyNote("sol", 2.5, 7),


]
intro_octave = 6
intro_1 = [
    MyNote("do", 1,intro_octave),


    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 0.25,intro_octave),
    MyNote("la", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave-1),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 2.5,intro_octave),

    MyNote("si", 1,intro_octave),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave),
    MyNote("la", 0.25,intro_octave),
    MyNote("do", 2.5,intro_octave),

    MyNote("sol", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("re", 1,intro_octave),
    MyNote("la", 0.25,intro_octave-1),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 2.5,intro_octave),

    MyNote("la", 1,intro_octave),

    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    #################
   
]

intro_2 = [
    MyNote("do", 1),
    MyNote("re", 0.25),
    MyNote("fa", 0.25),
    MyNote("la", 2.5),

    MyNote("la", 1),
    MyNote("sol", 0.25),
    MyNote("si", 0.25),
    MyNote("re", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),
    MyNote("sol", 2.5),

    MyNote("si", 1),
    MyNote("fa", 0.25),
    MyNote("la", 0.25),
    MyNote("do", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),   
    MyNote("sol", 2.5),

    MyNote("mi", 1),
    MyNote("si", 0.25, 4),
    MyNote("re", 0.25),
    MyNote("fa", 2.5),

    MyNote("re", 2),
    MyNote("do", 6)
]

intro_2_violin = [
    # MyNote("do", 1),

    MyNote("delay", 1),
    MyNote("la", 4),


    MyNote("re", 4, 6),


    MyNote("sol", 4),


    MyNote("do", 4, 6),


    MyNote("sol", 4),


    MyNote("fa", 6),


    MyNote("do", 4)
]

reff_1 = [
    MyNote("do", 1,intro_octave),


    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 0.25,intro_octave),
    MyNote("la", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave-1),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 2.5,intro_octave),

    MyNote("si", 1,intro_octave),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("sol", 0.25,intro_octave),
    MyNote("la", 0.25,intro_octave),
    MyNote("do", 2.5,intro_octave),

    MyNote("sol", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("mi", 1,intro_octave),
    MyNote("si", 0.25,intro_octave-1),
    MyNote("re", 0.25,intro_octave),
    MyNote("fa", 2.5,intro_octave),

    MyNote("re", 1,intro_octave),
    MyNote("la", 0.25,intro_octave-1),
    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 2.5,intro_octave),

    MyNote("la", 1,intro_octave),

    MyNote("do", 0.25,intro_octave),
    MyNote("mi", 0.25,intro_octave),
    MyNote("sol", 2.5,intro_octave),

    #################
   
]

reff_2 = [
    MyNote("do", 1),
    MyNote("re", 0.25),
    MyNote("fa", 0.25),
    MyNote("la", 2.5),

    MyNote("la", 1),
    MyNote("sol", 0.25),
    MyNote("si", 0.25),
    MyNote("re", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),
    MyNote("sol", 2.5),

    MyNote("si", 1),
    MyNote("fa", 0.25),
    MyNote("la", 0.25),
    MyNote("do", 2.5, 6),

    MyNote("la", 1),
    MyNote("do", 0.25),
    MyNote("mi", 0.25),   
    MyNote("sol", 2.5),

    MyNote("mi", 1),
    MyNote("si", 0.25, 4),
    MyNote("re", 0.25),
    MyNote("fa", 2.5),

    MyNote("re", 2),
    MyNote("do", 6)
]

