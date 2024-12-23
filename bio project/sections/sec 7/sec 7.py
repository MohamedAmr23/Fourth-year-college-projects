dec = {
    '$' : 0,
    'A' : 1,
    'C' : 2,
    'G' : 3,
    'T' : 4
}
T = 'ACGGTTAACAGT$'
table=[]
i=2**0
n=0
while True:    
    l=[]
    dec2={}
    if i>1:
        for j in range(len(T)):
            if not(table[n-1][j:j+i] in l):
                l.append(table[n-1][j:j+i])
        l.sort()
        l
        for j in range(len(l)):
            dec2[tuple(l[j])]=j
    row=[]
    for j in range (len(T)):
        if i==1:
            row.append(dec[T[j]])
        else:
            row.append(dec2[tuple(table[n-1][j:j+i])])
    table.append(row)
    flag=0
    for j in range(len(row)):
        c=0
        c=row.count(j)
        if c>1:
            flag=1
            break
    print(row)
    if flag==0:
        break
    n+=1
    i=2**n





















# import tkinter as tk
# from tkinter import messagebox

# class DNAGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("DNA Suffix Array Construction")
#         self.root.configure(bg="#222222")

#         # Input Frame
#         input_frame = tk.Frame(self.root, bg="#222222")
#         input_frame.pack(padx=20, pady=20)

#         tk.Label(input_frame, text="DNA Sequence:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.sequence_entry = tk.Entry(input_frame, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.sequence_entry.pack()

#         tk.Button(input_frame, text="Construct Suffix Array", command=self.construct_suffix_array, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF").pack(pady=(10, 0))

#         # Output Frame
#         output_frame = tk.Frame(self.root, bg="#222222")
#         output_frame.pack(padx=20, pady=20)

#         tk.Label(output_frame, text="Suffix Array:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.output_text = tk.Text(output_frame, height=10, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.output_text.pack()

#     def construct_suffix_array(self):
#         sequence = self.sequence_entry.get() + '$'
#         dec = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
#         table = []
#         i = 2**0
#         n = 0

#         while True:
#             l = []
#             dec2 = {}
#             if i > 1:
#                 for j in range(len(sequence)):
#                     if sequence[j:j+i] not in l:
#                         l.append(sequence[j:j+i])
#                 l.sort()
#                 for j in range(len(l)):
#                     dec2[tuple(l[j])] = j
#             row = []
#             for j in range(len(sequence)):
#                 if i == 1:
#                     row.append(dec[sequence[j]])
#                 else:
#                     row.append(dec2[tuple(table[n-1][j:j+i])])
#             table.append(row)
#             flag = 0
#             for j in range(len(row)):
#                 c = row.count(j)
#                 if c > 1:
#                     flag = 1
#                     break
#             self.output_text.insert(tk.END, str(row) + "\n")
#             if flag == 0:
#                 break
#             n += 1
#             i = 2**n

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = DNAGUI(root)
#     root.mainloop()