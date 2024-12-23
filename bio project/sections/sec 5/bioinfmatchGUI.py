import numpy as np

def match(seq,sub_seq):
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
            break
    return x

def Badchars(seq,sub_seq):
    table=np.zeros([4,len(sub_seq)])     
    row=["A","C","G","T"]
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
            #break
        
        else:
            for j in range(len(sub_seq)-1,-1,-1):
                if seq[i+j] != sub_seq[j]:
                    k=row.index(seq[i+j])
                    i+=table[k,j]
                    break
        '''
        else:
            for j in range(i+len(sub_seq)-1,i-1,-1):
                if seq[j] != sub_seq[j-i]:
                    k=row.index(seq[j])
                    i+=table[k,j-i]
                    break
        '''
        i=int(i+1)
    return x

file=open("dna1.fasta")
l=[i for i in file]
t=l[1][0:-1]
p="GCGTCGCTGTGGAG"
# p="G"
print(match(t,p))
print(Badchars(t,p))






# GUI for it
# import tkinter as tk
# from tkinter import messagebox
# import numpy as np
# from tkinter import filedialog

# # Functions
# def match(seq, sub_seq):
#     # Existing implementation
#     x = -1
#     for i in range(len(seq) - len(sub_seq) + 1):
#         if sub_seq == seq[i:i + len(sub_seq)]:
#             x = i
#             break
#     return x

# def Badchars(seq, sub_seq):
#     # Existing implementation
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

# def analyze():
#     seq = sequence_entry.get()
#     sub_seq = substring_entry.get()
#     match_result = match(seq, sub_seq)
#     badchars_result = Badchars(seq, sub_seq)
#     result_text.delete(1.0, tk.END)
#     result_text.insert(tk.END, f"Match Index: {match_result}\n")
#     result_text.insert(tk.END, f"Badchars Index: {badchars_result}\n")

# def clear():
#     sequence_entry.delete(0, tk.END)
#     substring_entry.delete(0, tk.END)
#     result_text.delete(1.0, tk.END)

# def load_file():
#     file_path = filedialog.askopenfilename(title="Select DNA File", filetypes=[("FASTA Files", "*.fasta")])
#     if file_path:
#         with open(file_path, 'r') as file:
#             seq = file.read().splitlines()[1].strip()
#             sequence_entry.insert(tk.END, seq)

# # GUI
# root = tk.Tk()
# root.title("DNA Sequence Analyzer")

# # Background
# root.configure(bg="#222222")

# # Header
# header_label = tk.Label(root, text="DNA Sequence Analyzer", font=("Arial", 24, "bold"), bg="#222222", fg="#00FF00")
# header_label.pack(pady=20)

# # Input Frame
# input_frame = tk.Frame(root, bg="#222222")
# input_frame.pack(padx=20, pady=20)

# sequence_label = tk.Label(input_frame, text="DNA Sequence:", font=("Arial", 14), bg="#222222", fg="#FFFFFF")
# sequence_label.pack(side=tk.LEFT, padx=10)
# sequence_entry = tk.Entry(input_frame, width=50, font=("Arial", 14), bg="#333333", fg="#FFFFFF")
# sequence_entry.pack(side=tk.LEFT, padx=10)

# # Button Frame
# button_frame = tk.Frame(root, bg="#222222")
# button_frame.pack(padx=20, pady=20)

# substring_label = tk.Label(button_frame, text="Substring:", font=("Arial", 12), bg="#222222", fg="#FFFFFF")
# substring_label.pack(side=tk.LEFT, padx=10)
# substring_entry = tk.Entry(button_frame, width=20, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
# substring_entry.pack(side=tk.LEFT, padx=10)

# analyze_button = tk.Button(button_frame, text="Analyze", command=analyze, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2)
# analyze_button.pack(side=tk.LEFT, padx=10, pady=10)
# clear_button = tk.Button(button_frame, text="Clear", command=clear, font=("Arial", 12), bg="#FF0000", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2)
# clear_button.pack(side=tk.LEFT, padx=10, pady=10)
# load_button = tk.Button(button_frame, text="Load File", command=load_file, font=("Arial", 12), bg="#4444FF", fg="#FFFFFF", relief=tk.RAISED, borderwidth=2)
# load_button.pack(side=tk.LEFT, padx=10, pady=10)

# # Result Frame
# result_frame = tk.Frame(root, bg="#222222")
# result_frame.pack(padx=20, pady=20)

# result_text = tk.Text(result_frame, height=10, width=60, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
# result_text.pack()

# root.mainloop()