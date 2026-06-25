dna_sequence = input("Enter the DNA Sequence: ")
dna_sequence = dna_sequence.upper().strip()
adenosine = "A"
thymine = "T"
guanine = "G"
cytosine = "C"
countA = 0
countT = 0
countG = 0
countC = 0

def validate_dna(dna_sequence):
    valid_bases = set('ATGC')
    if len(dna_sequence) == 0:
        print("The sequence cannot be empty.")
        return False
    invalid = set(dna_sequence) - valid_bases
    if invalid:
        print("Invalid sequence! Only A, T, G, C allowed.")
        return False
    return True

if not validate_dna(dna_sequence):
    exit()

countA = dna_sequence.count(adenosine)

print("The number of A Nitrogenous base is: " , countA)

countT = dna_sequence.count(thymine)
		
print("The number of T Nitrogenous base is: " , countT)	

countG = dna_sequence.count(guanine)		
		
print("The number of G Nitrogenous base is: " , countG)

countC = dna_sequence.count(cytosine)
length_string = len(dna_sequence)
print("The length of the given DNA Sequence is: " , length_string)

calc = (countG + countC) / length_string 
gc = float(calc)
print("The GC content of DNA Sequence is: " , f"{gc:.2%}")	

base_pair = { "A":"T" , "T":"A" , "G":"C" , "C":"G" }
compliment = "".join(base_pair[x] for x in dna_sequence)
print("The compliment strand of DNA Sequence is: " , compliment)
stringrev_og = dna_sequence[::-1]
reverse_compliment = "".join(base_pair[y] for y in stringrev_og)
print("The reverse compliment strand of DNA Sequence is: " , reverse_compliment)