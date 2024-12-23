import tkinter as tk
from tkinter import messagebox, filedialog
import re
import pyperclip
import numpy as np

def validate_sequence(seq):
    pattern = r'^[ATCG]+$'
    if re.match(pattern, seq.upper()):
        return True
    else:
        return False

def gc_content(seq):
    try:
        seq = seq.upper()
        if not validate_sequence(seq):
            raise ValueError("Invalid DNA sequence")
        if len(seq) == 0:
            return 0
        return (seq.count("G") + seq.count("C")) / len(seq)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def complement(seq):
    try:
        seq = seq.upper()
        if not validate_sequence(seq):
            raise ValueError("Invalid DNA sequence")
        dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
        return "".join(dic[base] for base in seq)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def reverse(seq):
    try:
        return seq[::-1]
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def reverse_complement(seq):
    try:
        return complement(reverse(seq))
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

def translation_table(seq):
    try:
        seq = seq.upper()
        if not validate_sequence(seq):
            raise ValueError("Invalid DNA sequence")
        if len(seq) % 3 != 0:
            raise ValueError("Sequence length must be divisible by 3")
        dic = {
            "TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
            "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
            "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
            "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
            "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
            "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
            "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
            "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
            "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
            "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
            "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
        }
        protein_seq = ""
        for i in range(0, len(seq), 3):
            protein_seq += dic[seq[i:i+3]]
        return protein_seq
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None


class DNASequenceAnalyzer:
    def __init__(self, root):
        self.root = root
        self.result_history = []

        self.background_color = "#222222"
        self.root.configure(bg=self.background_color)

        self.header_label = tk.Label(self.root, text="DNA Sequence Analyzer", font=("Arial", 24, "bold"), bg=self.background_color, fg="#00FF00")
        self.header_label.pack(pady=20)

        self.input_frame = tk.Frame(self.root, bg=self.background_color)
        self.input_frame.pack(padx=20, pady=20)

        tk.Label(self.input_frame, text="DNA Sequence:", font=("Arial", 14), bg=self.background_color, fg="#FFFFFF").pack(side=tk.LEFT)
        self.dna_sequence = tk.Entry(self.input_frame, width=50, font=("Arial", 14), bg="#333333", fg="#FFFFFF")
        self.dna_sequence.pack(side=tk.LEFT)
        # Buttons
        self.button_frame1 = tk.Frame(self.root, bg=self.background_color)
        self.button_frame1.pack(padx=20, pady=10)
        tk.Button(self.button_frame1, text="Calculate GC Content", command=self.calculate_gc_content, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame1, text="Calculate Reverse Complement", command=self.calculate_reverse_complement, font=("Arial", 12), bg="#FF4400", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        self.button_frame2 = tk.Frame(self.root, bg=self.background_color)
        self.button_frame2.pack(padx=20, pady=10)
        tk.Button(self.button_frame2, text="Calculate Translation Table", command=self.calculate_translation_table, font=("Arial", 12), bg="#00FF44", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame2, text="Reset", command=self.reset, font=("Arial", 12), bg="#FF0000", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame2, text="Copy Result", command=self.copy_result, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame2, text="Help/About", command=self.help_about, font=("Arial", 12), bg="#44FF44", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)
        tk.Button(self.button_frame2, text="Select File", command=self.select_file, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        self.button_frame3 = tk.Frame(self.root, bg=self.background_color)
        self.button_frame3.pack(padx=20, pady=10)
        tk.Button(self.button_frame3, text="Match Bad Character", command=self.match_bad_character, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        # Result Frame
        self.result_frame = tk.Frame(self.root, bg=self.background_color)
        self.result_frame.pack(padx=20, pady=20)
        self.result_label = tk.Label(self.result_frame, text="Result:", font=("Arial", 14), bg=self.background_color, fg="#00FF00")
        self.result_label.pack()
        self.result_text = tk.Text(self.result_frame, height=10, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.result_text.pack()

        # Result History Frame
        self.history_frame = tk.Frame(self.root, bg=self.background_color)
        self.history_frame.pack(padx=20, pady=20)
        self.history_label = tk.Label(self.history_frame, text="Result History:", font=("Arial", 14), bg=self.background_color, fg="#00FF00")
        self.history_label.pack()
        self.history_text = tk.Text(self.history_frame, height=10, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
        self.history_text.pack()
        tk.Button(self.button_frame2, text="Reset History", command=self.reset_History, font=("Arial", 12), bg="#FF0000", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2).pack(side=tk.LEFT, padx=10)

        # Theme Selection
        self.theme_frame = tk.Frame(self.root, bg=self.background_color)
        self.theme_frame.pack(padx=20, pady=20, fill=tk.X)

        self.theme_label = tk.Label(self.theme_frame, text="Theme:", font=("Arial", 14), bg=self.background_color, fg="#00FF00")
        self.theme_label.pack(side=tk.LEFT, padx=10)

        self.theme_var = tk.StringVar()
        self.theme_var.set("Dark")
        self.theme_option = tk.OptionMenu(self.theme_frame, self.theme_var, "Dark", "Light")
        self.theme_option.pack(side=tk.LEFT, padx=10)
        self.theme_button = tk.Button(self.theme_frame, text="Apply Theme", command=self.apply_theme, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2)
        self.theme_button.pack(side=tk.LEFT, padx=10)
    def apply_theme(self):
            theme = self.theme_var.get()
            if theme == "Dark":
                    self.background_color = "#222222"
                    self.root.configure(bg=self.background_color)
                    self.header_label.configure(bg=self.background_color)
                    self.input_frame.configure(bg=self.background_color)
                    self.button_frame1.configure(bg=self.background_color)
                    self.button_frame2.configure(bg=self.background_color)
                    self.button_frame3.configure(bg=self.background_color)
                    self.result_frame.configure(bg=self.background_color)
                    self.history_frame.configure(bg=self.background_color)
                    self.theme_frame.configure(bg=self.background_color)
                    self.dna_sequence.configure(bg="#333333", fg="#FFFFFF")
                    self.result_text.configure(bg="#333333", fg="#FFFFFF")
                    self.history_text.configure(bg="#333333", fg="#FFFFFF")
            elif theme == "Light":
                self.background_color = "#FFFFFF"
                self.root.configure(bg=self.background_color)
                self.header_label.configure(bg=self.background_color)
                self.input_frame.configure(bg=self.background_color)
                self.button_frame1.configure(bg=self.background_color)
                self.button_frame2.configure(bg=self.background_color)
                self.button_frame3.configure(bg=self.background_color)
                self.result_frame.configure(bg=self.background_color)
                self.history_frame.configure(bg=self.background_color)
                self.theme_frame.configure(bg=self.background_color)
                self.dna_sequence.configure(bg="#FFFFCC", fg="#000000")
                self.result_text.configure(bg="#FFFFCC", fg="#000000")
                self.history_text.configure(bg="#FFFFCC", fg="#000000")        
    def calculate_gc_content(self):
        seq = self.dna_sequence.get()
        gc = gc_content(seq)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"GC Content: {gc * 100}%")
        self.history_text.insert(tk.END, self.result_text.get("1.0", tk.END) + "\n\n")
        self.result_history.append(self.result_text.get("1.0", tk.END))

    def calculate_reverse_complement(self):
        seq = self.dna_sequence.get()
        rev_comp = reverse_complement(seq)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Reverse Complement: {rev_comp}")
        self.history_text.insert(tk.END, self.result_text.get("1.0", tk.END) + "\n\n")
        self.result_history.append(self.result_text.get("1.0", tk.END))

    def calculate_translation_table(self):
        seq = self.dna_sequence.get()
        trans_table = translation_table(seq)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Translation Table: {trans_table}")
        self.history_text.insert(tk.END, self.result_text.get("1.0", tk.END) + "\n\n")
        self.result_history.append(self.result_text.get("1.0", tk.END))

    def match_bad_character(self):
            self.pattern_label = tk.Label(self.button_frame3, text="Pattern:", font=("Arial", 12), bg=self.background_color, fg="#FFFFFF")
            self.pattern_label.pack(side=tk.LEFT, padx=10)
            
            self.pattern_entry = tk.Entry(self.button_frame3, width=20, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
            self.pattern_entry.pack(side=tk.LEFT, padx=10)
            
            self.match_button = tk.Button(self.button_frame3, text="Match", command=self.match_pattern, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2)
            self.match_button.pack(side=tk.LEFT, padx=10)
    def match_pattern(self):
        seq = self.dna_sequence.get()
        pattern = self.pattern_entry.get()
        print("Sequence:", seq)
        print("Pattern:", pattern)

        match_result = self.match(seq, pattern)
        print("Match Index:", match_result)

        badchars_result = self.Badchars(seq, pattern)
        print("Badchars Index:", badchars_result)

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END,  {match_result})
        self.result_text.insert(tk.END,  {badchars_result})
        self.result_text.insert(tk.END, f"Match Index: {match_result}\n")
        self.result_text.insert(tk.END, f"Badchars Index: {badchars_result}\n")

        self.history_text.insert(tk.END, self.result_text.get("1.0", tk.END) + "\n\n")
        self.result_history.append(self.result_text.get("1.0", tk.END))
            
    def match(self, seq, sub_seq):
        print("Matching...")
        x = -1
        for i in range(len(seq) - len(sub_seq) + 1):
            if sub_seq == seq[i:i + len(sub_seq)]:
                x = i
                print("Match found at index", x)
                break
        return x

    def Badchars(self, seq, sub_seq):
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
                # break
            else:
                for j in range(len(sub_seq) - 1, -1, -1):
                    if seq[i + j] != sub_seq[j]:
                        k = row.index(seq[i + j])
                        i += table[k, j]
                        break
            i = int(i)
        return x        
    def reset(self):
        self.dna_sequence.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.history_text.delete(1.0, tk.END)
        self.result_history.clear()

    def copy_result(self):
        pyperclip.copy(self.result_text.get("1.0", tk.END))

    def help_about(self):
        messagebox.showinfo("About", "DNA Sequence Analyzer\nVersion 1.0\nDeveloped by [Your Name]")

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select DNA Sequence File",  filetypes=[("FASTA Files", "*.fasta"), ("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                lines = file.readlines()
                seq = "".join([line.strip() for line in lines[1:]])  # skip header, join DNA lines
                self.dna_sequence.delete(0, tk.END)
                self.dna_sequence.insert(0, seq)

    def reset_History(self):
        self.history_text.delete(1.0, tk.END)
        self.result_history.clear()

root = tk.Tk()
root.title("DNA Sequence Analyzer")
app = DNASequenceAnalyzer(root)
root.mainloop()

