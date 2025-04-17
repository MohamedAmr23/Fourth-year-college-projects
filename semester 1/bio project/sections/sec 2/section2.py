
import pandas as pd
#========================== example 1 =========================================
#  processing protein sequence data in FASTA format, specifically extracting sequences and their corresponding labels (0 or 1) based on the presence of "non-hemolytic" in the metadata
infile = open('HAPPENN_dataset.fasta')
flag=0
tb=[]
for line in infile:
    if flag==0:
        s=line.split("|lcl|")
        print(s[3])
        flag=1
    else:
        print(line[:-1])
        flag=0
        if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
            tb.append([line[:-1],0])
        else:
            tb.append([line[:-1],1])
    print("--------------")

print(tb)
head=['Sequence','y']
df=pd.DataFrame(tb,columns=head)
df.to_csv("HAPPENN.csv")

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import pandas as pd

# class FastaToCSVGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("FASTA to CSV Converter")
#         self.root.configure(bg="#222222")

#         # Input Frame
#         input_frame = tk.Frame(self.root, bg="#222222")
#         input_frame.pack(padx=20, pady=20)

#         tk.Label(input_frame, text="Select FASTA File:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.file_path_entry = tk.Entry(input_frame, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.file_path_entry.pack()
#         tk.Button(input_frame, text="Browse", command=self.browse_file, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF").pack(pady=(10, 0))

#         # Output Frame
#         output_frame = tk.Frame(self.root, bg="#222222")
#         output_frame.pack(padx=20, pady=20)

#         tk.Label(output_frame, text="Output CSV File:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.output_path_entry = tk.Entry(output_frame, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.output_path_entry.pack()

#         # Convert Button
#         tk.Button(output_frame, text="Convert to CSV", command=self.convert_fasta_to_csv, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF").pack(pady=(10, 0))

#     def browse_file(self):
#         file_path = filedialog.askopenfilename(title="Select FASTA File", filetypes=[("FASTA Files", "*.fasta")])
#         self.file_path_entry.delete(0, tk.END)
#         self.file_path_entry.insert(tk.END, file_path)

#     def convert_fasta_to_csv(self):
#         file_path = self.file_path_entry.get()
#         output_path = self.output_path_entry.get()
#         if not file_path or not output_path:
#             messagebox.showerror("Error", "Please select input and output files")
#             return

#         tb = []
#         with open(file_path, 'r') as infile:
#             flag = 0
#             s = []
#             for line in infile:
#                 if flag == 0:
#                     s = line.split("|lcl|")
#                     flag = 1
#                 else:
#                     if len(s) > 3 and (s[3] == 'non-hemolytic' or s[3] == 'non-hemolytic\n'):
#                         tb.append([line[:-1], 0])
#                     elif len(s) > 3:
#                         tb.append([line[:-1], 1])
#                     flag = 0

#         head = ['Sequence', 'y']
#         df = pd.DataFrame(tb, columns=head)
#         df.to_csv(output_path, index=False)
#         messagebox.showinfo("Success", "Conversion completed successfully")


# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = FastaToCSVGUI(root)
#     root.mainloop()
    