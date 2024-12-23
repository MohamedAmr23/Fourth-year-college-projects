
import numpy as np
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
    l=[h[1] for h in hits ]
    offsets=[]
    for i in l:
        if t[i:i+len(p)]==p:
            offsets.append(i)
    return offsets
        
file=open("dna1.fasta")
l=[i for i in file]
t=l[1][0:-1]
index=IndexSorted(t,3)
p="GCGTCGCTGTGGAG"
print(query(t,p,index))

















# import tkinter as tk
# from tkinter import messagebox, filedialog
# import numpy as np
# import bisect

# def index_sorted(seq, ln):
#     index = []
#     for i in range(len(seq) - ln + 1):
#         index.append((seq[i:i+ln], i))
#     index.sort()
#     return index

# def query(t, p, index):
#     keys = [r[0] for r in index]
#     st = bisect.bisect_left(keys, p[:len(keys[0])])
#     en = bisect.bisect(keys, p[:len(keys[0])])
#     hits = index[st:en]
#     l = [h[1] for h in hits]
#     offsets = []
#     for i in l:
#         if t[i:i+len(p)] == p:
#             offsets.append(i)
#     return offsets

# class DNAQueryGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DNA Query")

#         # Input Frame
#         input_frame = tk.Frame(self.root)
#         input_frame.pack(padx=20, pady=20)

#         tk.Label(input_frame, text="DNA Sequence (FASTA format):").pack()
#         self.dna_sequence = tk.Text(input_frame, height=10, width=60)
#         self.dna_sequence.pack()

#         tk.Button(input_frame, text="Upload File", command=self.upload_file).pack()

#         tk.Label(input_frame, text="Pattern:").pack()
#         self.pattern = tk.Entry(input_frame, width=20)
#         self.pattern.pack()

#         tk.Label(input_frame, text="Subsequence Length:").pack()
#         self.subsequence_length = tk.Entry(input_frame, width=5)
#         self.subsequence_length.pack()

#         # Button Frame
#         button_frame = tk.Frame(self.root)
#         button_frame.pack(padx=20, pady=10)

#         tk.Button(button_frame, text="Query", command=self.query_dna).pack(side=tk.LEFT, padx=10)
#         tk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=10)

#         # Result Frame
#         result_frame = tk.Frame(self.root)
#         result_frame.pack(padx=20, pady=20)

#         tk.Label(result_frame, text="Offsets:").pack()
#         self.result_text = tk.Text(result_frame, height=5, width=60)
#         self.result_text.pack()

#     def upload_file(self):
#         file_path = filedialog.askopenfilename(title="Select DNA Sequence File", 
#                                             filetypes=[("FASTA Files", "*.fasta"), 
#                                                         ("Text Files", "*.txt")])
        
#         if file_path:
#             with open(file_path, "r") as file:
#                 lines = file.readlines()
#                 dna_sequence = "".join([line.strip() for line in lines[1:]])  # skip header, join DNA lines
                
#                 if self.validate_dna(dna_sequence):
#                     self.dna_sequence.delete("1.0", tk.END)
#                     self.dna_sequence.insert("1.0", dna_sequence)
#                 else:
#                     messagebox.showerror("Invalid DNA Sequence", "Please upload a valid DNA sequence file.")
                
#     def validate_dna(self, sequence):
#         valid_chars = set("ATCGatcg")
#         return set(sequence).issubset(valid_chars)
#     def query_dna(self):
#         dna_sequence = self.dna_sequence.get("1.0", tk.END).strip()
#         pattern = self.pattern.get()
#         subsequence_length = int(self.subsequence_length.get())

#         index = index_sorted(dna_sequence, subsequence_length)
#         offsets = query(dna_sequence, pattern, index)

#         result = "Offsets: " + ", ".join(map(str, offsets))
#         self.result_text.delete("1.0", tk.END)
#         self.result_text.insert("1.0", result)

#     def reset(self):
#         self.dna_sequence.delete("1.0", tk.END)
#         self.pattern.delete(0, tk.END)
#         self.subsequence_length.delete(0, tk.END)
#         self.result_text.delete("1.0", tk.END)

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = DNAQueryGUI(root)
#     root.mainloop()