import tkinter as tk
from tkinter import messagebox, filedialog
import re
import pyperclip

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
        self.theme_button.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        # Animation
        self.animate()

    def animate(self):
            self.header_label.config(fg="#FF0000" if self.header_label.cget("fg") == "#00FF00" else "#00FF00")
            self.root.after(2000, self.animate)

    def reset(self):
            self.dna_sequence.delete(0, tk.END)
            self.result_text.delete(1.0, tk.END)

    def reset_History(self):
            self.history_text.delete(1.0, tk.END)
            self.result_history = []

    def calculate_gc_content(self):
            seq = self.dna_sequence.get()
            if validate_sequence(seq):
                gc_content_result = gc_content(seq)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"GC Content: {gc_content_result}")
                self.result_history.append(f"GC Content: {gc_content_result}")
                self.history_text.insert(tk.END, f"GC Content: {gc_content_result}\n")
            else:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "Invalid DNA sequence")

    def calculate_reverse_complement(self):
        seq = self.dna_sequence.get()
        if validate_sequence(seq):
            reverse_complement_result = reverse_complement(seq)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Reverse Complement: {reverse_complement_result}")
            self.result_history.append(f"Reverse Complement: {reverse_complement_result}")
            self.history_text.insert(tk.END, f"Reverse Complement: {reverse_complement_result}\n")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Invalid DNA sequence")

    def calculate_translation_table(self):
        seq = self.dna_sequence.get()
        if validate_sequence(seq):
            translation_table_result = translation_table(seq)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Translation Table: {translation_table_result}")
            self.result_history.append(f"Translation Table: {translation_table_result}")
            self.history_text.insert(tk.END, f"Translation Table: {translation_table_result}\n")
        else:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Invalid DNA sequence")

    def copy_result(self):
        result = self.result_text.get("1.0", tk.END)
        pyperclip.copy(result)
        messagebox.showinfo('Copied successfully', result)

    def help_about(self):
        messagebox.showinfo("Help/About", "DNA Sequence Analyzer\nVersion 1.0\nDeveloped by [Your Name]")

    def apply_theme(self):
        theme = self.theme_var.get()
        if theme == "Dark":
            self.background_color = "#222222"
            self.root.configure(bg=self.background_color)
            self.header_label.configure(bg=self.background_color)
            self.input_frame.configure(bg=self.background_color)
            self.button_frame1.configure(bg=self.background_color)
            self.button_frame2.configure(bg=self.background_color)
            self.result_frame.configure(bg=self.background_color)
            self.history_frame.configure(bg=self.background_color)
            self.theme_frame.configure(bg=self.background_color)
            self.theme_label.configure(bg=self.background_color, fg="#00FF00")
            self.theme_button.configure(bg="#4444FF", fg="#FFFFFF")
            self.header_label.configure(fg="#00FF00")
            self.result_label.configure(bg=self.background_color, fg="#00FF00")
            self.history_label.configure(bg=self.background_color, fg="#00FF00")
        elif theme == "Light":
            self.background_color = "#FFFFFF"
            self.root.configure(bg=self.background_color)
            self.header_label.configure(bg=self.background_color)
            self.input_frame.configure(bg=self.background_color)
            self.button_frame1.configure(bg=self.background_color)
            self.button_frame2.configure(bg=self.background_color)
            self.result_frame.configure(bg=self.background_color)
            self.history_frame.configure(bg=self.background_color)
            self.theme_frame.configure(bg=self.background_color)
            self.theme_label.configure(bg=self.background_color, fg="#000000")
            self.theme_button.configure(bg="#FF4400", fg="#FFFFFF")
            self.header_label.configure(fg="#000000")
            self.result_label.configure(bg=self.background_color, fg="#000000")
            self.history_label.configure(bg=self.background_color, fg="#000000")

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA Files", "*.fasta")])
        if file_path:
            self.dna_sequence.delete(0, tk.END)
            self.dna_sequence.insert(tk.END, file_path)
            self.read_fasta_file(file_path)



    def read_fasta_file(self, file_path):
        with open(file_path, 'r') as file:
            seq = ''
            for line in file:
                if not line.startswith('>'):
                    seq += line.strip()
    
        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        
        # Display current file results
        self.display_results(seq)
        
        # Add previous results to history
        self.history_text.insert(tk.END, self.result_history[-1] + "\n\n")
        
        # Update result history
        self.result_history.append(self.result_text.get("1.0", tk.END))


    def display_results(self, seq):
        self.result_text.insert(tk.END, f"Sequence:\n\n{seq}\n\n")
        gc_content_result = gc_content(seq)
        self.result_text.insert(tk.END, f"----------------------------------------\n")
        self.result_text.insert(tk.END, f"GC Content: {gc_content_result}\n\n")
        reverse_complement_result = reverse_complement(seq)
        self.result_text.insert(tk.END, f"----------------------------------------\n")
        self.result_text.insert(tk.END, f"Reverse Complement:\n\n{reverse_complement_result}\n\n")
        translation_table_result = translation_table(seq)
        self.result_text.insert(tk.END, f"----------------------------------------\n")
        self.result_text.insert(tk.END, f"Translation Table:\n\n{translation_table_result}\n")

    def calculate_gc_content_from_file(self, seq):
        gc_content_result = gc_content(seq)
        self.result_text.insert(tk.END, f"GC Content: {gc_content_result}\n")

    def calculate_reverse_complement_from_file(self, seq):
        reverse_complement_result = reverse_complement(seq)
        self.result_text.insert(tk.END, f"Reverse Complement: {reverse_complement_result}\n")

    def calculate_translation_table_from_file(self, seq):
        translation_table_result = translation_table(seq)
        self.result_text.insert(tk.END, f"Translation Table: {translation_table_result}\n")
root = tk.Tk()
app = DNASequenceAnalyzer(root)
root.mainloop()        
