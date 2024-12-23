
############################## Section1 ###############################
import pandas as pd

def hemolytic():
    infile = open('HAPPENN_dataset.fasta')
    tb=[]
    for line in infile:
        if line[0]==">":
            s=line.split("|lcl|")
        else:
            # hemolytic=1, non-hemolytic=0
            if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
                tb.append([line[:-1],0])
            else:
                tb.append([line[:-1],1])

    head=['Sequence','y']
    df=pd.DataFrame(tb,columns=head)
    dd=df.head(1)
    return dd

def split_sequence():
    infile = open('seq.fasta')
    tb=[]
    l=[]
    for line in infile:
        if line[0]==">":
            l.append(line[1:-1])
        else:
            seq=line[:-1]
            tb.append(seq)

    df=pd.DataFrame({"ID":l,"Sequence":tb})
    dd=df.head(1)
    return dd

############################## Section2 ###############################
def GC_Content():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    l=len(seq)
    num_G=seq.count("G")
    num_C=seq.count("C")
    total=num_C+num_G
    return str(total/l)

def Complement():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    dic={"G":"C","C":"G","A":"T","T":"A"}
    s=list(seq)
    for i in range(len(seq)):
        s[i]=str(dic[s[i]])
    s="".join(s)
    return str(s)

def Reverse():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    s=list(seq)
    s=reversed(s)
    s="".join(s)
    return str(s)

def Reverse_Complement():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    seq=Reverse()
    seq=Complement()
    return str(seq)

############################## Section3 ###############################
# Translate DNA to Protiens

def Translation_Table():
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
    sf=""
    flag=0
    
    file=open("dna2.fna")
    l=[i for i in file]
    seq=l[1][0:-1]
    
    for i in range(0,len(seq)-2,3):
        if dic[seq[i:i+3]]=="M":
            flag=1
        elif (dic[seq[i:i+3]]=="*"):
            flag=0
        if flag==1:
            s+=dic[seq[i:i+3]]
        sf+=dic[seq[i:i+3]]
    return f"Translation of DNA from dna2.fna to protien: \n{sf}\nString between 'M' and '*' are: \n{s}"      


############################## Section4 ###############################
import numpy as np

def match():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    sub_seq= 'GCGTCGCTGTGGAG'
    
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
    return f"Native Matching of pattern 'GCGTCGCTGTGGAG' at offset: {x}"


def Badchars():
    file=open("dna1.fasta")
    l=[i for i in file]
    seq=l[1][0:-1]
    sub_seq= 'GCGTCGCTGTGGAG'
    
    table=np.zeros([4,len(sub_seq)])     
    row=["C","G","A","T"]
    for i in range (4):
        num=-1
        for j in range (len(sub_seq)):
            if row[i]==sub_seq[j]:
                table[i,j]=-1
                num=-1
            else:
                num+=1
                table[i,j]=num
    x=-1
    i=0
    while(i<len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
        else:
            for j in range(i+len(sub_seq)-1,i-1,-1):
                if seq[j] != sub_seq[int(j-i)]:
                    k=row.index(seq[j])
                    i+=table[k,j-i]
                    break
        i=int(i+1)
    return f"Bad Character Matching of pattern 'GCGTCGCTGTGGAG' at offset: {x}"

############################## Section5 ###############################
import bisect

def IndexSorted(seq,ln):
    index = []
    for i in range(len(seq)-ln+1):
        index.append((seq[i:i+ln], i))
    index.sort() 
    return index

def query(t,p,index):
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys,p[:len(keys[0])])
    
    en = bisect.bisect(keys,p[:len(keys[0])])
    hits = index[st:en] 
    print(hits)
    l=[h[1] for h in hits ]
    offsets=[]
    for i in l:
        if t[i:i+len(p)]==p:
            offsets.append(i)
    return offsets


def offsets(pattern,ln):
    file=open("dna1.fasta")
    l=[i for i in file]
    t=l[1][0:-1]
    index=IndexSorted(t,ln)
    return f"The offsets of the pattern 'AACGG' with 4 in the sequence: {query(t,pattern,index)}"


#offsets("AACGG",4)

############################## Section6 ###############################
def overlap(a,b,min_length=3):
    start=0
    while True:
        start=a.find(b[:min_length],start)
        if start==-1:
            return 0
        if b.startswith(a[start:]):
            return f"Overlap between Two Sequences 'ACGGTAGGT', 'GGTAGGTCC':\n{len(a[start:])}, {a[start:]}"
        start+=1
        
#print(overlap("ACGGTAGGT", "GGTAGGTCC",3))

############################## Section7 ###############################
def suffix_array(t):
    l=[]
    for i in range(len(t)):
        l.append(t[i:])
    l2=l.copy()
    l.sort()
    dec={}
    for i in range(len(l)):
        dec[l[i]]=i
    table=[]
    for i in range(len(l)):
        table.append([l2[i],i,dec[l2[i]]])
    return f"The index of the text'ACGACTACGATAAC$':\n{dec}\nThe Suffix Array:\n{table}"



############################## Gui ###############################
from tkinter import *
root =Tk()
root.title("Bioinformatics Project")


### sec1
hemo=hemolytic()
var_hemo = StringVar()
var_hemo.set(hemo)
def hemo_func():    
    label1.config(textvariable=var_hemo)


label1 = Label(root,text="result 1", justify="left", bg="#5c6bc0", width=50, wraplength=300)
label1.pack()
label1.place(x=150,y=10)

button1_1 = Button(root, text="1. Show Hemolytic", activebackground="#FFFF9E",
                   command=hemo_func, bg="#ea80fc", font="helvetica 9 bold")
button1_1.pack()
button1_1.place(x=10,y=0)

split_seq=split_sequence()
var_split_seq = StringVar()
var_split_seq.set(split_seq)
def split_seq_func():    
    label1.config(textvariable=var_split_seq)

button1_2 = Button(root, text="1. Split The Sequence", activebackground="#FFFF9E",
                   command=split_seq_func, bg="#ea80fc", font="helvetica 9 bold")
button1_2.pack()
button1_2.place(x=10,y=30)

##################################################################


##################################################################
### Sec 2

gc= GC_Content()
var_gc = StringVar()
var_gc.set(gc)
def gc_func():    
    label2.config(textvariable=var_gc)


label2 = Label(root,text="result 2", justify="left", width=50, wraplength=300, bg="#5c6bc0")
label2.pack()
label2.place(x=150,y=100)

button2_1 = Button(root, text="2. Show GC Content", activebackground="#FFFF9E",
                   command=gc_func, bg="#ea80fc", font="helvetica 9 bold")
button2_1.pack()
button2_1.place(x=20,y=80)


comp=Complement()
var_comp = StringVar()
var_comp.set(comp)
def comp_func():    
    label2.config(textvariable=var_comp)

button2_2 = Button(root, text="2. Complement", activebackground="#FFFF9E",
                   command=comp_func, bg="#ea80fc", font="helvetica 9 bold")
button2_2.pack()
button2_2.place(x=20,y=110)


rev=Reverse()
var_rev = StringVar()
var_rev.set(rev)
def rev_func():    
    label2.config(textvariable=var_rev)

button2_3 = Button(root, text="2. Reverse", activebackground="#FFFF9E", 
                   command=rev_func, bg="#ea80fc", font="helvetica 9 bold")
button2_3.pack()
button2_3.place(x=20,y=140)


rev_comp=Reverse_Complement()
var_rev_comp = StringVar()
var_rev_comp.set(rev_comp)
def rev_comp_func():    
    label2.config(textvariable=var_rev_comp)

button2_4 = Button(root, text="2. Reverse Complement", activebackground="#FFFF9E",
                   command=rev_comp_func, bg="#ea80fc", font="helvetica 9 bold")
button2_4.pack()
button2_4.place(x=20,y=170)

##################################################################

##################################################################
### sec3
trans=Translation_Table()
var_trans = StringVar()
var_trans.set(trans)
def trans_func():    
    label3.config(textvariable=var_trans)


label3 = Label(root,text="result 3", justify="left", bg="#5c6bc0", wraplength=300, width=50)
label3.pack()
label3.place(x=180,y=300)

button3 = Button(root, text="3. Translation Table", activebackground="#FFFF9E", 
                 command=trans_func, bg="#ea80fc", font="helvetica 9 bold")
button3.pack()
button3.place(x=20,y=300)
##################################################################

##################################################################
### sec4
match1=match()
var_match1 = StringVar()
var_match1.set(match1)
def match1_func():    
    label4.config(textvariable=var_match1)


label4 = Label(root,text="result 4",justify="left", wraplength=300, bg="#5c6bc0", width=50)
label4.pack()
label4.place(x=200,y=550)

button4_1 = Button(root, text="4. Native Matching", activebackground="#FFFF9E", 
                   command=match1_func, bg="#ea80fc", font="helvetica 9 bold")
button4_1.pack()
button4_1.place(x=20,y=530)

match2=Badchars()
var_match2 = StringVar()
var_match2.set(match2)
def match2_func():    
    label4.config(textvariable=var_match2)


button4_2 = Button(root, text="4. Bad Character Matching", activebackground="#FFFF9E", 
                   command=match2_func, bg="#ea80fc", font="helvetica 9 bold")
button4_2.pack()
button4_2.place(x=20,y=560)
##################################################################


##################################################################
### sec5
dna_index=offsets("AACGG",4)
var_dna_index = StringVar()
var_dna_index.set(dna_index)
def dna_index_func():    
    label5.config(textvariable=var_dna_index)


label5 = Label(root,text="result 5",justify="left", bg="#5c6bc0", wraplength=300, width=50)
label5.pack()
label5.place(x=820,y=0)

button5 = Button(root, text="5. Index Of Sequence", activebackground="#FFFF9E", 
                 command=dna_index_func, bg="#ea80fc", font="helvetica 9 bold")
button5.pack()
button5.place(x=600,y=0)
##################################################################

##################################################################
### sec6
seq_overlap=overlap("ACGGTAGGT", "GGTAGGTCC",3)
var_seq_overlap = StringVar()
var_seq_overlap.set(seq_overlap)
def seq_overlap_func():    
    label6.config(textvariable=var_seq_overlap)


label6 = Label(root,text="result 6",justify="left", bg="#5c6bc0", wraplength=300, width=50)
label6.pack()
label6.place(x=820,y=120)
button6 = Button(root, text="6. Sequence Overlap", activebackground="#FFFF9E",
                 command=seq_overlap_func, bg="#ea80fc", font="helvetica 9 bold")
button6.pack()
button6.place(x=600,y=120)
##################################################################


##################################################################
### sec7
suffix_array=suffix_array('ACGACTACGATAAC$')
var_suffix_array = StringVar()
var_suffix_array.set(suffix_array)
def dna_dist_func():    
    label7.config(textvariable=var_suffix_array)


label7 = Label(root,text="result 7",justify="left", width=50, wraplength=300, bg="#5c6bc0")
label7.pack()
label7.place(x=820,y=300)
button7 = Button(root, text="7. Suffix Array", activebackground="#FFFF9E", 
                 command=dna_dist_func, bg="#ea80fc", font="helvetica 9 bold")
button7.pack()
button7.place(x=600,y=300)
##################################################################


##################################################################


root.configure(bg='#e0f2f1')
root.geometry("1200x700")
root.mainloop()
