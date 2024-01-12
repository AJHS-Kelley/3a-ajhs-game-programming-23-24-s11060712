# DNA replication Gavin Kloeckner, v0.5a

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

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "T":
            print('Both of these sequences do not match.\n')
            break
        elif rnaBase == "C" and dnaBase != "G":
            print('Both of these sequences do not match.\n')
            break
        elif rnaBase == "G" and dnaBase != "C":
            print('Both of these sequences do not match.\n')
            break
        elif rnaBase == "T" and dnaBase != "A":
            print('Both of these sequences do not match.\n')
            break
        else:
            isMatch = True
            print("Both of these sequences match!\n")
            break
    return isMatch


dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)

checkSequence(dna, rna)