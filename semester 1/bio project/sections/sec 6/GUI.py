# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox, filedialog
# import numpy as np
# import bisect

# # Functions
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

# def match(seq, sub_seq):
#     x = -1
#     for i in range(len(seq) - len(sub_seq) + 1):
#         if sub_seq == seq[i:i + len(sub_seq)]:
#             x = i
#             break
#     return x

# def Badchars(seq, sub_seq):
#     table = np.zeros([4, len(sub_seq)])
#     row = ["A", "C", "G", "T"]
#     for i in range(4):
#         num = -1
#         for j in range(len(sub_seq)):
#             if row[i] == sub_seq[j]:
#                 table[i, j] = -1
#                 num = -1
#             else:
#                 num += 1
#                 table[i, j] = num
#     x = -1
#     i = 0
#     while (i < len(seq) - len(sub_seq) + 1):
#         if sub_seq == seq[i:i + len(sub_seq)]:
#             x = i
#         else:
#             for j in range(len(sub_seq) - 1, -1, -1):
#                 if seq[i + j] != sub_seq[j]:
#                     k = row.index(seq[i + j])
#                     i += table[k, j]
#                     break
#         i = int(i + 1)
#     return x

# class DNAQueryGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DNA Query and Sequence Analyzer")

#         # Input Frame
#         input_frame = tk.Frame(self.root)
#         input_frame.pack(padx=20, pady=20)

#         tk.Label(input_frame, text="DNA Sequence (FASTA format):").pack()
#         self.dna_sequence = tk.Text(input_frame, height=10, width=60)
#         self.dna_sequence.pack()

#         tk.Button(input_frame, text="Upload File", command=self.upload_file).pack()

#         # Tab Control
#         tab_control = ttk.Notebook(self.root)
#         tab_control.pack(padx=20, pady=10)

#         # Query Tab
#         query_tab = tk.Frame(tab_control)
#         tab_control.add(query_tab, text="Query")

#         tk.Label(query_tab, text="Pattern:").pack()
#         self.pattern = tk.Entry(query_tab, width=20)
#         self.pattern.pack()

#         tk.Label(query_tab, text="Subsequence Length:").pack()
#         self.subsequence_length = tk.Entry(query_tab, width=5)
#         self.subsequence_length.pack()

#         tk.Button(query_tab, text="Query", command=self.query_dna).pack()
#         tk.Button(query_tab, text="Reset", command=self.reset_query).pack()

#         tk.Label(query_tab, text="Offsets:").pack()
#         self.result_text_query = tk.Text(query_tab, height=5, width=60)
#         self.result_text_query.pack()

#         # Analyzer Tab
#         analyzer_tab = tk.Frame(tab_control)
#         tab_control.add(analyzer_tab, text="Analyzer")

#         tk.Label(analyzer_tab, text="Substring:").pack()
#         self.substring = tk.Entry(analyzer_tab, width=20)
#         self.substring.pack()

#         tk.Button(analyzer_tab, text="Analyze", command=self.analyze).pack()
#         tk.Button(analyzer_tab, text="Clear", command=self.clear_analyzer).pack()
#         tk.Button(analyzer_tab, text="Load File", command=self.load_file).pack()

#         tk.Label(analyzer_tab, text="Results:").pack()
#         self.result_text_analyzer = tk.Text(analyzer_tab, height=10, width=60)
#         self.result_text_analyzer.pack()

#     def upload_file(self):
#         file_path = filedialog.askopenfilename(title="Select DNA Sequence File", 
#                                             filetypes=[("FASTA Files", "*.fasta"), 
#                                                         ("Text Files", "*.txt")])
        
#         if file_path:
#             with open(file_path, "r") as file:
#                 lines = file.readlines()
#                 dna_sequence = "".join([line.strip() for line in lines[1:]])
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
#         self.result_text_query.delete("1.0", tk.END)
#         self.result_text_query.insert("1.0", result)


#     def reset_query(self):
#         self.dna_sequence.delete("1.0", tk.END)
#         self.pattern.delete(0, tk.END)
#         self.subsequence_length.delete(0, tk.END)
#         self.result_text_query.delete("1.0", tk.END)


#     def analyze(self):
#         seq = self.dna_sequence.get("1.0", tk.END).strip()
#         sub_seq = self.substring.get()
#         match_result = match(seq, sub_seq)
#         badchars_result = Badchars(seq, sub_seq)
#         self.result_text_analyzer.delete("1.0", tk.END)
#         self.result_text_analyzer.insert(tk.END, f"Match Index: {match_result}\n")
#         self.result_text_analyzer.insert(tk.END, f"Badchars Index: {badchars_result}\n")


#     def clear_analyzer(self):
#         self.dna_sequence.delete("1.0", tk.END)
#         self.substring.delete(0, tk.END)
#         self.result_text_analyzer.delete("1.0", tk.END)


#     def load_file(self):
#         file_path = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA Files", "*.fasta")])
#         if file_path:
#             with open(file_path, 'r') as file:
#                 seq = file.read().splitlines()[1].strip()
#                 self.dna_sequence.insert(tk.END, seq)

    

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = DNAQueryGUI(root)
#     root.mainloop()            


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import numpy as np
import bisect

class DNAQueryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Query and Sequence Analyzer")
        self.root.configure(bg="#222222")

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#222222")
        input_frame.pack(padx=20, pady=20)

        tk.Label(input_frame, text="DNA Sequence (FASTA format):", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
        self.dna_sequence = tk.Text(input_frame, height=10, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.dna_sequence.pack()

        tk.Button(input_frame, text="Upload File", command=self.upload_file, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF").pack(pady=(10,0))

        # Tab Control
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(padx=20, pady=10)

        # Query Tab
        query_tab = tk.Frame(tab_control, bg="#222222")
        tab_control.add(query_tab, text="Query")

        button_frame_query = tk.Frame(query_tab, bg="#222222")
        button_frame_query.pack(pady=10)

        tk.Label(query_tab, text="Pattern:", font=("Arial", 12), bg="#222222", fg="#FFFFFF").pack()
        self.pattern = tk.Entry(query_tab, width=20, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.pattern.pack()

        tk.Label(query_tab, text="Subsequence Length:", font=("Arial", 12), bg="#222222", fg="#FFFFFF").pack()
        self.subsequence_length = tk.Entry(query_tab, width=5, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.subsequence_length.pack()

        tk.Button(button_frame_query, text="Query", command=self.query_dna, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame_query, text="Reset", command=self.reset_query, font=("Arial", 12), bg="#FF0000", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        tk.Label(query_tab, text="Offsets:", font=("Arial", 12), bg="#222222", fg="#FFFFFF").pack()
        self.result_text_query = tk.Text(query_tab, height=5, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.result_text_query.pack()

        # Analyzer Tab
        analyzer_tab = tk.Frame(tab_control, bg="#222222")
        tab_control.add(analyzer_tab, text="Analyzer")

        tk.Label(analyzer_tab, text="Substring:", font=("Arial", 12), bg="#222222", fg="#FFFFFF").pack()
        self.substring = tk.Entry(analyzer_tab, width=20, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.substring.pack()

        
        button_frame_analyzer = tk.Frame(analyzer_tab, bg="#222222")
        button_frame_analyzer.pack(pady=10)

        tk.Button(button_frame_analyzer, text="Analyze", command=self.analyze, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame_analyzer, text="Clear", command=self.clear_analyzer, font=("Arial", 12), bg="#FF0000", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame_analyzer, text="Load File", command=self.load_file, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        tk.Label(analyzer_tab, text="Results:", font=("Arial", 12), bg="#222222", fg="#FFFFFF").pack()
        self.result_text_analyzer = tk.Text(analyzer_tab, height=10, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.result_text_analyzer.pack()
    def analyze(self):
            seq = self.dna_sequence.get("1.0", tk.END).strip()
            sub_seq = self.substring.get()
            match_result = match(seq, sub_seq)
            badchars_result = Badchars(seq, sub_seq)
            self.result_text_analyzer.delete("1.0", tk.END)
            self.result_text_analyzer.insert(tk.END, f"Match Index: {match_result}\n")
            self.result_text_analyzer.insert(tk.END, f"Badchars Index: {badchars_result}\n")


    def clear_analyzer(self):
        self.dna_sequence.delete("1.0", tk.END)
        self.substring.delete(0, tk.END)
        self.result_text_analyzer.delete("1.0", tk.END)


    def load_file(self):
        file_path = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA Files", "*.fasta")])
        if file_path:
            with open(file_path, 'r') as file:
                seq = file.read().splitlines()[1].strip()
                self.dna_sequence.insert(tk.END, seq)


    def validate_dna(self, sequence):
        valid_chars = set("ATCGatcg")
        return set(sequence).issubset(valid_chars)


    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select DNA Sequence File", 
                                                filetypes=[("FASTA Files", "*.fasta"), 
                                                            ("Text Files", "*.txt")])
        
        if file_path:
            with open(file_path, "r") as file:
                lines = file.readlines()
                dna_sequence = "".join([line.strip() for line in lines[1:]])  
                
                if self.validate_dna(dna_sequence):
                    self.dna_sequence.delete("1.0", tk.END)
                    self.dna_sequence.insert("1.0", dna_sequence)
                else:
                    messagebox.showerror("Invalid DNA Sequence", "Please upload a valid DNA sequence file.")


    def query_dna(self):
        dna_sequence = self.dna_sequence.get("1.0", tk.END).strip()
        pattern = self.pattern.get()
        subsequence_length = int(self.subsequence_length.get())

        index = index_sorted(dna_sequence, subsequence_length)
        offsets = query(dna_sequence, pattern, index)

        result = "Offsets: " + ", ".join(map(str, offsets))
        self.result_text_query.delete("1.0", tk.END)
        self.result_text_query.insert("1.0", result)


    def reset_query(self):
        self.dna_sequence.delete("1.0", tk.END)
        self.pattern.delete(0, tk.END)
        self.subsequence_length.delete(0, tk.END)
        self.result_text_query.delete("1.0", tk.END)


def index_sorted(seq, ln):
        index = []
        for i in range(len(seq) - ln + 1):
            index.append((seq[i:i+ln], i))
        index.sort()
        return index


def query(t, p, index):
        keys = [r[0] for r in index]
        st = bisect.bisect_left(keys, p[:len(keys[0])])
        en = bisect.bisect(keys, p[:len(keys[0])])
        hits = index[st:en]
        l = [h[1] for h in hits]
        offsets = []
        for i in l:
            if t[i:i+len(p)] == p:
                offsets.append(i)
        return offsets


def match(seq, sub_seq):
        x = -1
        for i in range(len(seq) - len(sub_seq) + 1):
            if sub_seq == seq[i:i + len(sub_seq)]:
                x = i
                break
        return x


def Badchars(seq, sub_seq):
    table = np.zeros([4, len(sub_seq)])
    row = ["A", "C", "G", "T"]
    for i in range(4):
        num = -1
        for j in range(len(sub_seq)):
            if row[i] == sub_seq[j]:
                table[i, j] = -1
                num = -1
            else:
                num += 1
                table[i, j] = num
    x = -1
    i = 0
    while (i < len(seq) - len(sub_seq) + 1):
        if sub_seq == seq[i:i + len(sub_seq)]:
            x = i
        else:
            for j in range(len(sub_seq) - 1, -1, -1):
                if seq[i + j] != sub_seq[j]:
                    k = row.index(seq[i + j])
                    i += int(table[k, j])
                    break
        i += 1
    return x

if __name__ == "__main__":
    root = tk.Tk()
    gui = DNAQueryGUI(root)
    root.mainloop()