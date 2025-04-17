
def GC_Content(seq):
    l=len(seq)
    num_G=seq.count("G")
    num_C=seq.count("C")
    total=num_C+num_G
    return total/l
    
def Complement(seq):
    dic={"G":"C","C":"G","A":"T","T":"A"}
    s=list(seq)
    for i in range(len(seq)):
        s[i]=dic[seq[i]]
    s="".join(s)
    return s
def Reverse(seq):
    s=list(seq)
    s=reversed(s)
    s="".join(s)
    return s
def Reverse_Complement(seq):
    seq=Reverse(seq)
    seq=Complement(seq)
    return seq
def Translation_Table(seq):
    dic = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
           "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
           "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
           "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
           "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
           "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
           "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "TAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "TAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
           "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "TGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }
    s=""
    for i in range(0,len(seq)- 2,3):
        s+=dic[seq[i:i+3]]
    return s


file=open("dna1.fasta")
l=[i for i in file]
p=l[1][0:-1]

"""file=open("dna2.fasta")
l=[i for i in file]
p=l[1][0:-1]""" 

#generally:
"""file=open("GCF_002817395.1_ASM281739v1_genomic.fna")
l=[i for i in file]
p=""
for i in range(1,len(l)):
    p = p + l[i][0:-1]   """ 

print(p)
print("GC Content:",GC_Content(p))
print("Reverse Complement:","\n" + Reverse_Complement(p))
print("Translation Table:","\n" + Translation_Table(p))