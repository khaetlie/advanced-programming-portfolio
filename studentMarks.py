from tkinter import *
from tkinter import messagebox

class StudentMarks:
    def __init__(self, root):
        self.root = root

        self.student_records = []

        self.name_l1 = Label(root, text="Student Manager", font=("Helvetica", 18), bg="#E7759A", fg="white", bd=5)
        self.name_l1.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        self.records_b1 = Button(root, text="View All Student Records", bg="#FFA35F", width=20, height=2, command=self.view_all_records)
        self.records_b1.grid(row=1, column=0, padx=5, pady=15)

        self.highest_b1 = Button(root, text="Show Highest Score", bg="#FFA35F", width=20, height=2, command=self.show_highest_score)
        self.highest_b1.grid(row=1, column=1, padx=10, pady=15)

        self.lowest_b1 = Button(root, text="Show Lowest Score", bg="#FFA35F", width=20, height=2, command=self.show_lowest_score)
        self.lowest_b1.grid(row=1, column=2, padx=15, pady=15)

        self.view_l1 = Label(root, text="View Individual Student Record: ", bg="#E7759A", font=("Helvetica", 10))
        self.view_l1.grid(row=2, column=0, padx=8, pady=(15, 15))

        self.search_name_entry = Entry(root, width=30)
        self.search_name_entry.grid(row=2, column=1, padx=5, pady=(15, 15))

        self.view_btn = Button(root, text="View Record", bg="#BA78CD", fg="white", width=18, height=1, font=("Helvetica", 10), command=self.view_individual_record)
        self.view_btn.grid(row=2, column=2, padx=10, pady=(15, 15))

        self.list = Listbox(root, height=15, width=100)
        self.list.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

        self.pre_records()  # Preload student records from the text file

    def pre_records(self):
        with open("studentMarks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, scores = line.split(', ', 1)
                    cw1 = int(scores.split(', ')[0].split(': ')[1])
                    cw2 = int(scores.split(', ')[1].split(': ')[1])
                    cw3 = int(scores.split(', ')[2].split(': ')[1])
                    exam = int(scores.split(', ')[3].split(': ')[1])

                    total_marks = cw1 + cw2 + cw3 + exam
                    percentage = (total_marks / 160) * 100
                    grade = self.calculate_grade(percentage)

                    # Append the record to the student_records list
                    self.student_records.append({
                        "name": name,
                        "cw1": cw1,
                        "cw2": cw2,
                        "cw3": cw3,
                        "exam": exam,
                        "marks": total_marks,
                        "percentage": percentage,
                        "grade": grade
                    })
                except (ValueError, IndexError):
                    continue

    def view_all_records(self):
        self.list.delete(0, END)

        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        for record in self.student_records:
            formatted_line = (f"Name: {record['name']}\n"
                              f"Coursework1: {record['cw1']}\n"
                              f"Coursework2: {record['cw2']}\n"
                              f"Coursework3: {record['cw3']}\n"
                              f"Exam: {record['exam']}\n"
                              f"Total Marks: {record['marks']} / 160\n"
                              f"Percentage: {record['percentage']:.2f}%\n"
                              f"Grade: {record['grade']}\n")
            self.list.insert(END, formatted_line)
            self.list.insert(END, "")  # Blank line for spacing between records

    def view_individual_record(self):
        self.list.delete(0, END)

        name = self.search_name_entry.get().strip()
        found = False
        
        for record in self.student_records:
            if record['name'].lower() == name.lower():
                formatted_line = (f"Name: {record['name']}\n"
                                  f"Coursework1: {record['cw1']}\n"
                                  f"Coursework2: {record['cw2']}\n"
                                  f"Coursework3: {record['cw3']}\n"
                                  f"Exam: {record['exam']}\n"
                                  f"Total Marks: {record['marks']} / 160\n"
                                  f"Percentage: {record['percentage']:.2f}%\n"
                                  f"Grade: {record['grade']}\n")
                self.list.insert(END, formatted_line)
                found = True
                break

        if not found:
            messagebox.showerror("Error!", f"No record was found for student: {name}")

    def calculate_grade(self, percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def show_highest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        highest_record = max(self.student_records, key=lambda x: x['marks'])
        messagebox.showinfo("Highest Score", 
            f"Highest Score:\n"
            f"Name: {highest_record['name']}\n"
            f"Coursework1: {highest_record['cw1']}\n"
            f"Coursework2: {highest_record['cw2']}\n"
            f"Coursework3: {highest_record['cw3']}\n"
            f"Exam: {highest_record['exam']}\n"
            f"Total Marks: {highest_record['marks']} / 160\n"
            f"Percentage: {highest_record['percentage']:.2f}%\n"
            f"Grade: {highest_record['grade']}")

    def show_lowest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        lowest_record = min(self.student_records, key=lambda x: x['marks'])
        messagebox.showinfo("Lowest Score", 
            f"Lowest Score:\n"
            f"Name: {lowest_record['name']}\n"
            f"Coursework1: {lowest_record['cw1']}\n"
            f"Coursework2: {lowest_record['cw2']}\n"
            f"Coursework3: {lowest_record['cw3']}\n"
            f"Exam: {lowest_record['exam']}\n"
            f"Total Marks: {lowest_record['marks']} / 160\n"
            f"Percentage: {lowest_record['percentage']:.2f}%\n"
            f"Grade: {lowest_record['grade']}")

root = Tk()
root.title("Student Manager")
root.geometry("700x500")
root.configure(bg="#E7759A")

app = StudentMarks(root)

root.mainloop()
