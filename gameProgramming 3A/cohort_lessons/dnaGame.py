# DNA replication Gavin Kloeckner, v0.2a

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

# dna = genDNA()
# print(dna)