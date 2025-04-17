from itertools import permutations

def overlap(a, b, min_length=3):
    start=0
    while True:
        start=a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1
            
               
def native_overlap(reads, k):
    olap={}
    for a,b in permutations(reads, 2):
        olen=overlap(a, b, k)
        if olen > 0:
            olap[(a, b)]=olen
    return olap

print(native_overlap(["ACGGTA", "GGTACC","GCATACG"], 3))


# import tkinter as tk
# from tkinter import messagebox
# from itertools import permutations

# class NativeOverlapGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Native Overlap")
#         self.root.configure(bg="#222222")

#         # Input Frame
#         input_frame = tk.Frame(self.root, bg="#222222")
#         input_frame.pack(padx=20, pady=20)

#         tk.Label(input_frame, text="Enter DNA Reads (comma-separated):", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.reads_entry = tk.Entry(input_frame, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.reads_entry.pack()

#         tk.Label(input_frame, text="Minimum Overlap Length:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.min_length_entry = tk.Entry(input_frame, width=5, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.min_length_entry.pack()

#         tk.Button(input_frame, text="Calculate Overlap", command=self.calculate_overlap, font=("Arial", 12), bg="#0044FF", fg="#FFFFFF").pack(pady=(10, 0))

#         # Output Frame
#         output_frame = tk.Frame(self.root, bg="#222222")
#         output_frame.pack(padx=20, pady=20)

#         tk.Label(output_frame, text="Overlap Results:", font=("Arial", 14), bg="#222222", fg="#FFFFFF").pack()
#         self.output_text = tk.Text(output_frame, height=10, width=50, font=("Arial", 12), bg="#333333", fg="#FFFFFF")
#         self.output_text.pack()

#     def overlap(self, a, b, min_length):
#         start = 0
#         while True:
#             start = a.find(b[:min_length], start)
#             if start == -1:
#                 return 0
#             if b.startswith(a[start:]):
#                 return len(a) - start
#             start += 1

#     def native_overlap(self, reads, k):
#         olap = {}
#         for a, b in permutations(reads, 2):
#             olen = self.overlap(a, b, k)
#             if olen > 0:
#                 olap[(a, b)] = olen
#         return olap

#     def calculate_overlap(self):
#         reads = self.reads_entry.get().split(',')
#         reads = [r.strip() for r in reads]
#         k = int(self.min_length_entry.get())
#         result = self.native_overlap(reads, k)
#         self.output_text.delete(1.0, tk.END)
#         for key, value in result.items():
#             self.output_text.insert(tk.END, f"{key}: {value}\n")


# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = NativeOverlapGUI(root)
#     root.mainloop()