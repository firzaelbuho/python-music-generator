
# Chord Family

from tool.my_chord import MyChord, ChordType

chord_family = {
    "major" : {
        "c" : [ MyChord("demo", ChordType.MAJ, 4), MyChord("C", ChordType.MAJ, 4),  MyChord("D", ChordType.MIN, 4), MyChord("E", ChordType.MIN, 4), MyChord("F", ChordType.MAJ, 4), 
                 MyChord("G", ChordType.MAJ, 4),MyChord("A", ChordType.MIN, 4),MyChord("B", ChordType.DIM, 4)],

        "d" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("D", ChordType.MAJ, 4),  MyChord("E", ChordType.MIN, 4), MyChord("F#", ChordType.MIN, 4), MyChord("G", ChordType.MAJ, 4), 
                 MyChord("A", ChordType.MAJ, 4),MyChord("B", ChordType.MIN, 4),MyChord("C#", ChordType.DIM, 4)],

        "e" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("E", ChordType.MAJ, 4),  MyChord("F#", ChordType.MIN, 4), MyChord("G#", ChordType.MIN, 4), MyChord("A", ChordType.MAJ, 4), 
                 MyChord("B", ChordType.MAJ, 4),MyChord("C#", ChordType.MIN, 4),MyChord("D#", ChordType.DIM, 4)],

        "f" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("F", ChordType.MAJ, 4),  MyChord("G", ChordType.MIN, 4), MyChord("A", ChordType.MIN, 4), MyChord("B#", ChordType.MAJ, 4), 
                 MyChord("C", ChordType.MAJ, 4),MyChord("D", ChordType.MIN, 4),MyChord("E", ChordType.DIM, 4)],

        "g" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("G", ChordType.MAJ, 4),  MyChord("A", ChordType.MIN, 4), MyChord("B", ChordType.MIN, 4), MyChord("C", ChordType.MAJ, 4), 
                 MyChord("D", ChordType.MAJ, 4),MyChord("E", ChordType.MIN, 4),MyChord("F#", ChordType.DIM, 4)],

        "a" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("A", ChordType.MAJ, 4),  MyChord("B", ChordType.MIN, 4), MyChord("C#", ChordType.MIN, 4), MyChord("D", ChordType.MAJ, 4), 
                 MyChord("E", ChordType.MAJ, 4),MyChord("F#", ChordType.MIN, 4),MyChord("G#", ChordType.DIM, 4)],

        "b" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("B", ChordType.MAJ, 4),  MyChord("C#", ChordType.MIN, 4), MyChord("D", ChordType.MIN, 4), MyChord("E", ChordType.MAJ, 4), 
                 MyChord("F#", ChordType.MAJ, 4),MyChord("G#", ChordType.MIN, 4),MyChord("A#", ChordType.DIM, 4)],
    },
     "minor" : {
        "c" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("C", ChordType.MIN, 4),  MyChord("D", ChordType.DIM, 4), MyChord("D#", ChordType.MAJ, 4), MyChord("F", ChordType.MIN, 4), 
                 MyChord("G", ChordType.MIN, 4),MyChord("G#", ChordType.MAJ, 4),MyChord("A#", ChordType.MAJ, 4)],

      

        "d" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("D", ChordType.MIN, 4),  MyChord("E", ChordType.DIM, 4), MyChord("F", ChordType.MAJ, 4), MyChord("G", ChordType.MIN, 4), 
                 MyChord("A", ChordType.MIN, 4),MyChord("A#", ChordType.MAJ, 4),MyChord("C", ChordType.MAJ, 4)],

        "e" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("E", ChordType.MIN, 4),  MyChord("F#", ChordType.DIM, 4), MyChord("G", ChordType.MAJ, 4), MyChord("A", ChordType.MIN, 4), 
                 MyChord("B", ChordType.MIN, 4),MyChord("C", ChordType.MAJ, 4),MyChord("D", ChordType.MAJ, 4)],

        "f" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("F", ChordType.MIN, 4),  MyChord("G", ChordType.DIM, 4), MyChord("G#", ChordType.MAJ, 4), MyChord("A#", ChordType.MIN, 4), 
                 MyChord("C", ChordType.MIN, 4),MyChord("C#", ChordType.MAJ, 4),MyChord("D#", ChordType.MAJ, 4)],

        "g" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("G", ChordType.MIN, 4),  MyChord("A", ChordType.DIM, 4), MyChord("A#", ChordType.MAJ, 4), MyChord("C", ChordType.MIN, 4), 
                 MyChord("D", ChordType.MIN, 4),MyChord("D#", ChordType.MAJ, 4),MyChord("F", ChordType.MAJ, 4)],

        "a" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("A", ChordType.MIN, 4),  MyChord("B", ChordType.DIM, 4), MyChord("C", ChordType.MAJ, 4), MyChord("D", ChordType.MIN, 4), 
                 MyChord("E", ChordType.MIN, 4),MyChord("F", ChordType.MAJ, 4),MyChord("G", ChordType.MAJ, 4)],

        "b" : [ MyChord("demo", ChordType.MAJ, 4),MyChord("B", ChordType.MIN, 4),  MyChord("C#", ChordType.DIM, 4), MyChord("D", ChordType.MAJ, 4), MyChord("E", ChordType.MIN, 4), 
                 MyChord("F#", ChordType.MIN, 4),MyChord("G", ChordType.MAJ, 4),MyChord("A", ChordType.MAJ, 4)],
    },

       
    
}