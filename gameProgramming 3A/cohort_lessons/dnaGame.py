# DNA replication Gavin Kloeckner, v0.6aWIP

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
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "T" and dnaBase != "A":
            break
        else:
            isMatch = True
            break
    return isMatch


def calcScore(time: float, dnaSequence: str) -> float:
    score = 0
    if time < 2.0:
        score += 20000
    elif time < 4.0:
        score += 2000
    elif time < 6.0:
        score += 200
    elif time < 8.0:
        score += 20
    else:
        score += 10
    
    if len(dnaSequence) >= 25:
        score *= 4.0
    elif len(dnaSequence) >= 15:
        score *= 3.0
    elif len(dnaSequence) >= 10:
        score *= 2.0
    elif len(dnaSequence) >= 5:
        score *= 1.5
    else:
        score *= 1.0

    return score

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)

print(checkSequence(dna, rna[0]))

print(calcScore)