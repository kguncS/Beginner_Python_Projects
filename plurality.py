        
#global değişkenler
dict_of_candidates = {}
MAX = 10

def vote():
    #Seçmen adaylardan herhangi birine oy vermiyorsa tekrar seçim yapması istenir.
    #sonrasında seçtiği adayın oy sayımı 1 arttırılır
    candidate_name = input("Vote: ")

    while candidate_name not in dict_of_candidates:
        print("Invalid vote.")
        candidate_name = input("Vote: ")
    
    dict_of_candidates[candidate_name] += 1
    return 

#kazananın yazdırılması için oluşturulmuş bu fonksiyonda,
#oy sayılarında eşitlik olması durumunda birden çok galip oluşabilir.

def print_winner():
    highest_vote = max(dict_of_candidates.values())
    for candidate in dict_of_candidates.items():     
        if candidate[1] == highest_vote:
            print(candidate[0])
    return
    

#aday listesi max aşılmayacak şekilde doldurulur.
candidate_count = 0
print("Please enter the names of the candidates.")

while candidate_count < MAX:

    buffer = input("Candidate: ")
    
    if buffer == 'Q' or buffer == 'q': #quit 
        break
    
    else:
        dict_of_candidates[buffer] = 0
        candidate_count += 1

number_of_voters = int(input("Number of voters: "))

for voter in range(number_of_voters):
    vote()
    
print_winner()
