from tool.my_chord import MyChord, ChordType
from tool.my_note import MyNote

def blue_bird_melody():
    return  [
    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('B', 1.5),
    MyNote('A', 3),

  
    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('D', 1, 5),
    MyNote('C', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('E', 2, 5),

    MyNote('E', 2/4),
    MyNote('A', 2/4),
    MyNote('B', 2/4),
    MyNote('C', 2, 5),
    MyNote('B', 1.5),
    MyNote('A', 3),

    MyNote('A', 0.5),
    MyNote('E', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('A', 0.5),
    MyNote('E', 0.5, 5),
    MyNote('D', 1, 5),
    MyNote('G', 1),
    MyNote('G', 1),
    MyNote('A', 0.5),
    MyNote('A', 1.5),
    
]

def canon_in_d(chord_dur:float = 4):
    return  [
        MyChord('D', ChordType.MAJ, chord_dur),
        MyChord('A', ChordType.MAJ, chord_dur),
        MyChord('B', ChordType.MIN, chord_dur),
        MyChord('F#', ChordType.MIN, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('D', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('A', ChordType.MAJ, chord_dur),

        MyChord('D', ChordType.MAJ, chord_dur),
        MyChord('A', ChordType.MAJ, chord_dur),
        MyChord('B', ChordType.MIN, chord_dur),
        MyChord('F#', ChordType.MIN, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('D', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('A', ChordType.MAJ, chord_dur) 
    ]


def lotus_on_river_chord_intro(chord_dur:float = 8):
    return  [

        # intro

        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
    ]

from tool.chord_family import  chord_family
def royal_chord(chord_dur:float = 8, key = "c", base = "major"):
    return  [

        # intro

       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],

       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
       
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
      
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
      
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
       chord_family[base][key][4],
       chord_family[base][key][5],
       chord_family[base][key][3],
       chord_family[base][key][6],
       chord_family[base][key][2],
       chord_family[base][key][5],
       chord_family[base][key][1],
       chord_family[base][key][1],
       
      
      
    ]

def lotus_on_river_chord(chord_dur:float = 8):
    return  [

        # # intro

        # MyChord('C', ChordType.MAJ, chord_dur),
        # MyChord('F', ChordType.MAJ, chord_dur),
        # MyChord('G', ChordType.MAJ, chord_dur),
        # MyChord('E', ChordType.MIN, chord_dur),
        # MyChord('A', ChordType.MIN, chord_dur),
        # MyChord('F', ChordType.MAJ, chord_dur),
        # MyChord('G', ChordType.MAJ, chord_dur),
        # MyChord('G', ChordType.MAJ, chord_dur),
        # MyChord('G', ChordType.MAJ, chord_dur),

        # Bait
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
     
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),

        # Bridge
        
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
      

        # REFF
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
     
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),

        # Bridge
        
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),

        # Bait
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
        
         # Bridge
        
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),

        
        # REFF
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
     
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),

        
         # Bridge
        
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),

        # Bait
        MyChord('C', ChordType.MAJ, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('E', ChordType.MIN, chord_dur),
        MyChord('A', ChordType.MIN, chord_dur),
        MyChord('F', ChordType.MAJ, chord_dur),
        MyChord('G', ChordType.MAJ, chord_dur),
        MyChord('C', ChordType.MAJ, chord_dur),

       
    ]




def lotus_on_river_melody():
    return  [

    # intro
    MyNote('C',4),
    MyNote('delay',1),
    MyNote('C',1),
    MyNote('B',1),
    MyNote('C',1),

    MyNote('D',4),
    MyNote('delay',1),
    MyNote('D',1),
    MyNote('C',1),
    MyNote('D',1),

    MyNote('B',4),
    MyNote('delay',1),
    MyNote('D',1),
    MyNote('C',1),
    MyNote('D',1),

    MyNote('E',4),
    MyNote('delay',1),
    MyNote('E',1),
    MyNote('E',1),
    MyNote('D',1),

    MyNote('C',4),
    MyNote('delay',1),
    MyNote('C',1),
    MyNote('B',1),
    MyNote('C',1),

    MyNote('D',4),
    MyNote('delay',1),
    MyNote('E',1),
    MyNote('D',1),
    MyNote('E',1),

    MyNote('C',4),
    MyNote('delay',1),
    MyNote('E',1),
    MyNote('D',1),
    MyNote('E',1),

    MyNote('F',4),
    MyNote('delay',3),
    MyNote('E',1),
    MyNote('D',4),
    MyNote('D',4),
   
    # Bait 1

    # C
    MyNote('C',3),
    MyNote('delay',0.5),
    MyNote('A',0.5),
    MyNote('C',1),
    MyNote('A',0.5),
    MyNote('C',1.5),
    MyNote('D',1),

    # F
    MyNote('C',4),
    MyNote('delay',3),
    MyNote('A',0.5),
    MyNote('A',0.5),

    # G
    MyNote('D',2),
    MyNote('delay',1),
    MyNote('D',0.5),
    MyNote('D',0.5),
    MyNote('D',1),
    MyNote('F',0.5),
    MyNote('E',1.5),
    MyNote('C',1),

    # Em
    MyNote('D',1),
    MyNote('C',1),
    MyNote('delay',0.5 ),
    MyNote('C',1),
    MyNote('D',0.5),
    MyNote('C',1),
    MyNote('delay',2),
    MyNote('C',1),

    # Am
    MyNote('E',2),
    MyNote('delay',1),
    MyNote('E',0.5),
    MyNote('E',0.5),
    MyNote('E',1),
    MyNote('F',0.5),
    MyNote('E',1.5),
    MyNote('D',1),

    # F
    MyNote('C',2),
    MyNote('delay',0.5),
    MyNote('C',1),
    MyNote('D',0.5),
    MyNote('C',2),
    MyNote('delay',1),
    MyNote('C',1),

    # G
    MyNote('D',2),
    MyNote('delay',1),
    MyNote('C',0.5),
    MyNote('C',0.5),
    MyNote('C',1),
    MyNote('B',0.5),
    MyNote('A',1.5),
    MyNote('D',1),

    # C
    MyNote('C',4),
    MyNote('delay',4),

    # Bait 2

    # C
    MyNote('C',3),
    MyNote('delay',0.5),
    MyNote('A',0.5),
    MyNote('C',1),
    MyNote('A',0.5),
    MyNote('C',1.5),
    MyNote('D',1),

    # F
    MyNote('F',4),
    MyNote('delay',3),
    MyNote('E',0.5),
    MyNote('E',0.5),

    # G
    MyNote('D',2),
    MyNote('delay',1),
    MyNote('E',0.5),
    MyNote('D',0.5),
    MyNote('D',1),
    MyNote('G',0.5),
    MyNote('F',1.5),
    MyNote('E',1),

    # Em
    MyNote('D',1),
    MyNote('C',1),
    MyNote('delay',0.5 ),
    MyNote('C',1),
    MyNote('D',0.5),
    MyNote('C',1),
    MyNote('delay',2),
    MyNote('C',1),

    # Am
    MyNote('E',2),
    MyNote('delay',1),
    MyNote('E',0.5),
    MyNote('E',0.5),
    MyNote('E',1),
    MyNote('F',0.5),
    MyNote('E',1.5),
    MyNote('D',1),

    # F
    MyNote('C',2),
    MyNote('delay',0.5),
    MyNote('C',1),
    MyNote('D',0.5),
    MyNote('C',2),
    MyNote('delay',1),
    MyNote('C',1),

    # G
    MyNote('D',2),
    MyNote('delay',1),
    MyNote('C',0.5),
    MyNote('C',0.5),
    MyNote('C',1),
    MyNote('B',0.5),
    MyNote('A',1.5),
    MyNote('B',1),

    # C
    MyNote('C',4),
    MyNote('delay',4),



    # Bridge

    

       
    ]
    

