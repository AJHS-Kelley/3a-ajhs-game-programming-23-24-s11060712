# DNA replication Gavin Kloeckner, v0.8a

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

def doTrnascript(dnaSequence: str) -> tuple:
    print(f"Your DNA sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA Sequence based on this DNA Sequence.\n")
    print("Remember, the RNA base will match U with A.\n")
    # Start Timer
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return(rnaSequence, rnaTime) # Tuples are ordered (index), unchangeable, allows duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "A":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "A" and dnaBase != "T":
            break
        else:
            isMatch = True
    return isMatch


def calcScore(rnaTime: float, dnaSequence: str) -> float:
    score = 0
    if rnaTime < 2.0:
        score += 20000
    elif rnaTime < 4.0:
        score += 2000
    elif rnaTime < 6.0:
        score += 200
    elif rnaTime < 8.0:
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

def saveScore(rna: str, dna: str, rnaTime: float, score: float) -> None:
    firstName = input("what is your first name?\n")
    lastName = input("what is your last name?\n")
    fullname = firstName + " " + lastName
    
    fileName = "dnaReplicatedScore" + fullname + ".txt"
    # My example: dnaReplicatedScoreGavinKloeckner.txt
    # Step 2: open the file
    saveData = open(fileName, "a") # First parameter = file name, second parameter = file mode
    # Three main file modes
    # "w" -- create the file. if it already exists, it will overwrite it
    # "a" -- create the file. If the file already exists, it will add on to the file.
    # "x" -- create a file. If file already exists, will exit with an error message.

    # Step 3: Write the data to the file.
    saveData.write("Test Message.\n")
    # Step 4: Close the file.
    saveData.close


dna = genDNA()
rna = doTrnascript(dna)


if checkSequence(dna, rna[0]):
    score = calcScore(rna[1], dna)
    saveScore( dna, rna[0], rna[0], score)
else:
    print("The sequences did not match. Please try again.\n")
