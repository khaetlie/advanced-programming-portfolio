from tkinter import *
from tkinter import messagebox 

#create a class called StudentMarks
class StudentMarks:
    def __init__(self, root):
        self.root = root

        self.student_records = []

        #creating the title 
        self.name_l1 = Label(root, text="Student Manager", font=("Helvetica", 18), bg="#E7759A", fg="white", bd=5)
        self.name_l1.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

        #resizing the columns
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        #creating buttons and using command to connect the function to a widget
        self.records_b1 = Button(root, text="View All Student Records", bg="#FFA35F", width=20, height=2, command=self.view_all_records)
        self.records_b1.grid(row=1, column=0, padx=5, pady=15)

        self.highest_b1 = Button(root, text="Show Highest Score", bg="#FFA35F", width=20, height=2, command=self.show_highest_score)
        self.highest_b1.grid(row=1, column=1, padx=10, pady=15)

        self.lowest_b1 = Button(root, text="Show Lowest Score", bg="#FFA35F", width=20, height=2, command=self.show_lowest_score)
        self.lowest_b1.grid(row=1, column=2, padx=15, pady=15)

        #creating a label to guide the user
        self.view_l1 = Label(root, text="View Individual Student Record: ", bg="#E7759A", font=("Helvetica", 10))
        self.view_l1.grid(row=2, column=0, padx=8, pady=(15, 15))

        #creating an entry where the user can type their information
        self.search_name_entry = Entry(root, width=30)
        self.search_name_entry.grid(row=2, column=1, padx=5, pady=(15, 15))

        self.view_btn = Button(root, text="View Record", bg="#BA78CD", fg="white", width=18, height=1, font=("Helvetica", 10), command=self.view_individual_record)
        self.view_btn.grid(row=2, column=2, padx=10, pady=(15, 15))

        #the listbox lists all student records
        self.list = Listbox(root, height=15, width=100)
        self.list.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

        self.pre_records()  # preload student records from the text file

    #a saved txt file to display records
    def pre_records(self):
        with open("studentMarks.txt", "r") as file:  #opens the studentMarks.txt file
            for line in file:  #every line in the file is read 
                line = line.strip()
                if not line:
                    continue  

                
                try:
                    name, scores = line.split(', ', 1)
                    cw1 = int(scores.split(', ')[0].split(': ')[1])
                    cw2 = int(scores.split(', ')[1].split(': ')[1])
                    cw3 = int(scores.split(', ')[2].split(': ')[1])
                    exam = int(scores.split(', ')[3].split(': ')[1])

                    total_marks = cw1 + cw2 + cw3 + exam #get the total marks by adding all the scores
                    percentage = (total_marks / 160) * 100 #get the percentage based on the total marks
                    grade = self.calculate_grade(percentage) #get the grade based on the calculated grade

                    # append the record to the student_records list
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
                except (ValueError, IndexError): #handling errors
                    continue

    #a function that allows user to see all student records
    def view_all_records(self):
        self.list.delete(0, END)

        #a message will show if there are no information provided
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
            self.list.insert(END, "")  # blank line to make spaces between records

    #a function that allows user to see each student individual record
    def view_individual_record(self):
        self.list.delete(0, END) 

        name = self.search_name_entry.get().strip()
        found = False
        
        for record in self.student_records:
            #check if the name in the record matches
            if record['name'].lower() == name.lower():
                #each information is formatted on a new line
                formatted_line = (f"Name: {record['name']}\n"
                                  f"Coursework1: {record['cw1']}\n"
                                  f"Coursework2: {record['cw2']}\n"
                                  f"Coursework3: {record['cw3']}\n"
                                  f"Exam: {record['exam']}\n"
                                  f"Total Marks: {record['marks']} / 160\n"
                                  f"Percentage: {record['percentage']:.2f}%\n"
                                  f"Grade: {record['grade']}\n")
                self.list.insert(END, formatted_line)
                found = True #used if there is a matching record
                break #exit the loop

        #a message will appear if there were no record found
        if not found:
            messagebox.showerror("Error!", f"No record was found for student: {name}")

    #shows the equivalent of the percentage to grade
    def calculate_grade(self, percentage):
        #the grade is 'A' if the percentage is greater or equal to 70
        if percentage >= 70: 
            return 'A'
        #the grade is 'B' if the percentage is greater or equal to 60
        elif percentage >= 60:
            return 'B'
        #the grade is 'C' if the percentage is greater or equal to 50
        elif percentage >= 50:
            return 'C'
        #the grade is 'D' if the percentage is greater or equal to 40
        elif percentage >= 40:
            return 'D'
        #if the percentage is not met, the grade is 'F'
        else:
            return 'F'

    #show the student with the highest score
    def show_highest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        #this will show the student with the highest score in teh messagebox
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

    #show the student with the lowest score
    def show_lowest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        #this will show the student with the lowest score in teh messagebox
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
root.title("Student Manager") #window title
root.geometry("700x500") #window size
root.configure(bg="#E7759A") #background color of the window

app = StudentMarks(root)

root.mainloop() #runs the application
