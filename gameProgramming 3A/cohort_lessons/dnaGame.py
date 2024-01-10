# DNA replication Gavin Kloeckner, v0.3a

import time, datetime # Bring the whole tool box


# Import specific method from a module
from random import choice # Bring just the tool needed

dnaBase = ["A", "T", "G", "C"] # Adnine, Thymine, Guanine, Cytosine

def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer value for the number of bases you want generated.\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBase)
        basesGenerated += 1
    return dnaSequence

def genRNA(dnaSequence: str) -> tuple:
    print(f"Your DNA sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA Sequence based on this DNA Sequence.\n")
    print("Remember, the RNA base will match U with A.\n")
    # Start Timer
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return(rnaSequence, rnaTime) # Tuples are ordered (index), unchangeable, allows duplicates

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)