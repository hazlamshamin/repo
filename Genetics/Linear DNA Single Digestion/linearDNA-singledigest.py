import re

enzymes=('HindIII','BamHI','EcoRI','BstI','BgIII','ClaI','PstI')
rec_dict= {'HindIII': 'AAGCTT', 'BamHI':'GGATCC','EcoRI':'GAATTC','BstI':'GGATCC','BgIII':'AGATCT','ClaI':'ATCGAT','PstI':'CTGCAG'} #recongnition site
cut_dict={'HindIII': 1, 'BamHI': 1, 'EcoRI':1,'BstI':1,'BgIII':1,'ClaI':2,'PstI':5} #restriction sites (cut after how many nucleotide)

class Enzyme:
    def __init__(self,name):
        self.name=name
        self.recognition=rec_dict[self.name]
        self.cut=cut_dict[self.name]

class Sequences:
    def __init__(self,sequences):
        self.sequences=sequences
        self.length=len(self.sequences)
    def __str__(self):
        return f"A DNA sequence of {self.length} base pairs."
    def find_recsites(self,recognition,sequences,cut):
        
        #Find how many restriction sites and at which positions
        cut_sites_list=[0]
        print(f"Sequences have {len(re.findall(recognition,sequences))} restriction sites.")
        print("The restriction site(s) is/are after the nucluetide(s) at position:")
        for match in re.finditer(recognition,self.sequences):
            cut_sites_list.append(match.start()+cut)
        print(cut_sites_list[1:])
        
        #Find the length of the DNA sequences after digestion
        
        restricted = [sequences[i:j] for i,j in zip(cut_sites_list, cut_sites_list[1:]+[None])]
        #print(restricted) 
        length=[]
        for product in restricted:
            length.append(len(product))
        print(f"\nAfter digestion, the length in bp of the products is as follows:\n{length}")
        print(f"Total length: {sum(length)} base pairs.")
        

def ask_for_seq():
    nucleotides={'A','T','C','G'}
    sequences='wrong'
    
    while set(sequences).issubset(nucleotides)==False:
        try:
            sequences=input("What is the DNA sequences?").replace(" ","").upper()
        except:
            print("Please give DNA sequences of ATCG nucleotides only.")
        else:
            if set(sequences).issubset(nucleotides)==False:
                print("Please give DNA sequences of ATCG nucleotides only.")
    return sequences


def ask_for_enzyme():
    enzyme='wrong'
    while enzyme not in enzymes:
        try:
            enzyme=input("What is the restriction enzyme to be used (eg. HindIII, BamHI)?")
        except:
            print("Invalid.")
        else:
            if enzyme not in enzymes:
                print("Sorry, it seems like it is not in our restriction enzymes dictionary. Try using different enzyme.")
    return enzyme

def single_digest():
    #prompt for sequences and restriction ezymes from user
    sequences=ask_for_seq()
    enzyme=ask_for_enzyme()
    
    #set Enzymes and Sequences class from user's inputs
    enzyme_obj=Enzyme(enzyme)
    sequences_obj=Sequences(sequences)
    print(" ---------------------------------------\n|               RESULTS:                |\n ---------------------------------------")
    #pdb.set_trace()
    #print length of DNA sequences
    print(sequences_obj)
    #find restriction sites and count digested lengths
    sequences_obj.find_recsites(enzyme_obj.recognition, sequences_obj.sequences, enzyme_obj.cut)
    

if __name__ == '__main__':
	single_digest()