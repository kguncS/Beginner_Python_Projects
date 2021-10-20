import sys
import csv

def max_repetiton(dna, sequence):
    
    max_num = 0
    ctr = 0
    index = dna.find(sequence)

    while index != -1 and index + len(sequence) <= len(dna):

        if dna[index : index + len(sequence)] == sequence:
            ctr += 1
            index += len(sequence) #consecutive

        else:
            if max_num < ctr:
                max_num = ctr
            ctr = 0
            index = dna.find(sequence, index, len(dna))

    return max_num


if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    quit()

counts = []
with open(sys.argv[1]) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        counts.append(row)
        
person_dna = ""

with open(sys.argv[2], "r") as dna_file:
    person_dna = dna_file.readline()


for row in counts:
    breaked = False
    
    for key in row.keys():
        if(key == "name"):
            continue

        repetition = max_repetiton(person_dna, key)
        if repetition != int(row[key]):
            breaked = True
            break

    if not breaked:
        print(row["name"])
        quit()


print("No match")