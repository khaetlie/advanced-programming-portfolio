from tkinter import *
from tkinter import messagebox, simpledialog  

#create class called StudentMarks
class StudentMarks:
    def __init__ (self, root):
        self.root=root

        self.student_records = []
        
        #creating a label with font and text colors
        self.name_l1=Label(root, text="Student Manager",font=("Helvetica", 18), bg="#E7759A", fg="white", bd=5)
        self.name_l1.grid(row=0, column=0, padx=20, pady=20, columnspan=4)
        
        #resizing the columns
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        
        #creating a button and use command to connect a function to widget 
        #creating the grid sizes to have properly aligned grids
        self.records_b1=Button(root, text="View All Student Records", bg="#FFA35F", width=20, height=2, command=self.view_all_records)
        self.records_b1.grid(row=1, column=0, padx=5, pady=15)
        
        self.highest_b1=Button(root, text="Show Highest Score", bg="#FFA35F", width=20, height=2, command=self.show_highest_score)
        self.highest_b1.grid(row=1, column=1, padx=10, pady=15)
        
        self.lowest_b1=Button(root, text="Show Lowest Score", bg="#FFA35F", width=20, height=2, command=self.show_lowest_score)
        self.lowest_b1.grid(row=1, column=2, padx=15, pady=15)
        
        self.delete_b1=Button(root, text="Delete Student Record", bg="#FFA35F", width=20, height=2, command=self.delete_record)
        self.delete_b1.grid(row=2, column=0, padx=15, pady=(15,25))
        
        self.update_b1=Button(root, text="Update Student Record", bg="#FFA35F", width=20, height=2, command=self.update_record)
        self.update_b1.grid(row=2, column=1, padx=15, pady=(15,25))
        
        self.sort_b1=Button(root, text="Sort Student Record", bg="#FFA35F", width=20, height=2, command=self.sort_records)
        self.sort_b1.grid(row=2, column=2, padx=15, pady=(15,25))
        
        self.add_name_btn=Button(root,text="Add New Student Record", bg="#BA78CD", fg="white", width=18, height=1, font=("Helvetica", 10), command=self.add_record)
        self.add_name_btn.grid(row=3, column=1, padx=5, pady=(15,15))
        
        #creating a label for the students to be guided
        self.view_l1=Label(root, text="Enter Student Name to view: ", bg="#E7759A", font=("Helvetica", 10))
        self.view_l1.grid(row=4, column=0, padx=8,pady=(15,15))
        
        #creating an entry for the student to type if they want to view their records
        self.search_name_entry=Entry(root, width=30)
        self.search_name_entry.grid(row=4, column=1, padx=5, pady=(15,15))
        
        self.view_btn=Button(root, text="View Record", bg="#BA78CD", fg="white", width=18, height=1, font=("Helvetica", 10), command=self.view_individual_record)
        self.view_btn.grid(row=4, column=2, padx=10, pady=(15,15))
        
        #creating a listbox to list and show all student records
        self.list=Listbox(root, height=10,width=100)
        self.list.grid(row=5, column=0, columnspan=4, padx=10,pady=5)
        
        #creating a scrollbar
        self.scrollbar = Scrollbar(root)
        self.scrollbar.grid(row=5, column=3) 
        
        self.list.config(yscrollcommand=self.scrollbar.set) #The scrollbar is on the listbox
        self.scrollbar.config(command=self.list.yview)  #Scrollbar is scrollable
        self.pre_records()
        
    #this function gets a txt file to be used to display records
    def pre_records(self):
        with open("studentMarks.txt", "r") as file: #reads the studentmarks.txt file
            for line in file: #reads each line #remove whitespace from the line
                line = line.strip()
                #if the line is not empty, 
                if line:
                    try:
                        name, scores = line.split(', ', 1) #split line into name and scores using ','
                        cw1 = int(scores.split(', ')[0].split(': ')[1]) #coursework 1
                        cw2 = int(scores.split(', ')[1].split(': ')[1]) #coursework 2
                        cw3 = int(scores.split(', ')[2].split(': ')[1]) #coursework 3
                        exam = int(scores.split(', ')[3].split(': ')[1]) #exam score

                        total_marks = cw1 + cw2 + cw3 + exam #get the total marks by adding all scores
                        percentage = (total_marks / 160) * 100 #get the percentage based on total marks
                        grade = self.calculate_grade(percentage) #get the grade based on the calculated percentage

                        #append the student record using dictionary to the student_records list
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

    #a function to allow users to add their records
    def add_record(self):
        name = simpledialog.askstring("Student Name", "Enter student name:")
        if not name:
            return
        
        try:
            #ask the user to enter coursework 1 mark
            cw1 = int(simpledialog.askstring("Coursework 1", "Enter Coursework 1 mark(0-20):")) 
            #ask the user to enter coursework 2 mark
            cw2 = int(simpledialog.askstring("Coursework 2", "Enter Coursework 2 mark(0-20):"))
            #ask the user to enter coursework 3 mark
            cw3 = int(simpledialog.askstring("Coursework 3", "Enter Coursework 3 mark(0-20):"))
            #ask the user to enter exam marks
            exam = int(simpledialog.askstring("Exam", "Enter exam mark (0-100): "))

            #check if there is any mark less than 0
            if any(mark < 0 for mark in [cw1, cw2, cw3, exam]):
                raise ValueError("Marks should be non-negative.") #if any mark is negative, it raises a ValueError
           
            total_marks = cw1 + cw2 + cw3 + exam #get the total marks by adding all the scores
            percentage = (total_marks / 160) * 100 #get the percentage based on total marks
            grade = self.calculate_grade(percentage) #get the grade based on the calculated percentage

            #new dictionary created
            new_record = {
               "name": name,
               "cw1": cw1,
               "cw2": cw2,
               "cw3": cw3,
               "exam": exam,
               "marks": total_marks,
               "percentage": percentage,
               "grade": grade
            } 
            self.student_records.append(new_record)

            #create a messagebox for the student information added
            messagebox.showinfo("Student Record Added", 
                        f"Name: {name}\n" #displays student name
                        f"Coursework1: {cw1}\n" #displays score for coursework 1
                        f"Coursework2: {cw2}\n" #displays score for coursework 2
                        f"Coursework3: {cw3}\n" #displays score for coursework 3
                        f"Exam: {exam}\n" #displays score for exam
                        f"Total Marks: {total_marks}\n" #displays score for total marks
                        f"Percentage: {percentage:.2f}%\n" #displays score for percentage
                        f"Grade: {grade}") #displays student;s grade

            with open("studentMarks.txt", "a") as file:
                file.write(f"{name}, Coursework1: {cw1}, Coursework2: {cw2}, Coursework3: {cw3}, Exam: {exam}\n")

            self.view_all_records()
            
                
        except (TypeError, ValueError):
            messagebox.showerror("Invalid input", "Please enter valid number for marks.")
            
    #a function that allows user to delete their records
    def delete_record(self):
        delete_name = simpledialog.askstring("Delete Student's Record", "Enter student's name (delete): ")

        #if the delete_name variable is empty, exit the function
        if not delete_name:
            return 

        record_found = False
        for record in self.student_records: #loops through the student record list
            if record['name'].lower() == delete_name.lower(): #check if the current name matches the name to be deleted
                self.student_records.remove(record)
                record_found = True
                break

        #sif there is record found, show a message that the student's record was deleted
        if record_found: 
            messagebox.showinfo("Record Deleted", f"Record for {delete_name} has been deleted.")
        #if no record was found, a message will appear saying no record was found
        else:
            messagebox.showerror("Error", f"No record found for student: {delete_name}") 

        self.view_all_records()
        
    #a function that allows user to update their records
    def update_record(self):
        update_name = simpledialog.askstring("Update Student's Record", "Enter student's name (update): ")

        #if the update_name variable is empty, exit the function
        if not update_name:
            return 
        
        record_found = False
        for record in self.student_records: #loop through the student record list
            if record['name'].lower() == update_name.lower(): #check if the current name matches the name to be updated
                record_found = True
                
                try:
                    #tells the user to enter a new mark for coursework 1
                    cw1 = int(simpledialog.askstring("Coursework 1", "Enter new Coursework 1 mark (0-20):", initialvalue=record['cw1']))
                    #tells the user to enter a new mark for coursework 2
                    cw2 = int(simpledialog.askstring("Coursework 2", "Enter new Coursework 2 mark (0-20):", initialvalue=record['cw2']))
                    #tells the user to enter a new mark for coursework 3
                    cw3 = int(simpledialog.askstring("Coursework 3", "Enter new Coursework 3 mark (0-20):", initialvalue=record['cw3']))
                    #tells the user to enter a new mark for exam
                    exam = int(simpledialog.askstring("Exam", "Enter new exam mark (0-100):", initialvalue=record['exam']))

                    if any(mark < 0 for mark in [cw1, cw2, cw3, exam]): #checks if there are any marks less than 0
                       raise ValueError("Marks should be non-negative.") #if there is any mark with a negative, it raises a ValueError
                   
                    total_marks = cw1 + cw2 + cw3 + exam #get the total marks by adding all the scores
                    percentage = (total_marks / 160) * 100 #get the percentage based on the total marks
                    grade = self.calculate_grade(percentage) #get the grade based on the calculated percentage

                    #update the student record with the new scores
                    record.update({
                      "cw1": cw1,
                      "cw2": cw2,
                      "cw3": cw3,
                      "exam": exam,
                      "marks": total_marks,
                      "percentage": percentage,
                      "grade": grade
                  })

                    #shows that the input has been updated
                    messagebox.showerror("Success!", f"Record for {update_name} has been updated.")
                    #shows that there is no number entered
                except (ValueError, TypeError):
                    messagebox.showerror("Invalid input", "Please enter number for marks.")
                break

        #shows if there are any records found for a student you want to update
        if not record_found:
           messagebox.showerror("Error", f"No record found for this student: {update_name}")
            

        self.view_all_records()

    #a function that shows users the records alphabetically
    def sort_records(self):
        self.student_records.sort(key=lambda x: x['name'].lower())
        
        self.view_all_records()
        
    #a function that shows the equivalent of each percentage to the grade
    def calculate_grade(self, percentage):
        #the grade for the student is 'A' if the percentage is greater or equal to 70
        if percentage >=70:
            return 'A'     
        #the grade is 'B' if the percentage is greater or equal to 60
        elif percentage >=60:
            return 'B'
        #the grade is 'C' if the percentage is greater or equal to 50
        elif percentage >=50:
            return 'C'
        #the grade is 'D' if the percentage is greater or equal to 40
        elif percentage >=40:
            return 'D'
        #if none of the grades are met, the student fails or the grade is 'F'
        else:
            return 'F'

    #a function that allows users to view all records available
    def view_all_records(self):
        self.list.delete(0, END)

        #shows a message that says no records are available for the student
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        for record in self.student_records:
            formatted_line = (f"Name: {record['name']}\n" #display student name
                              f"Coursework1: {record['cw1']}\n" #display score for coursework 1
                              f"Coursework2: {record['cw2']}\n" #display score for coursework 2
                              f"Coursework3: {record['cw3']}\n" #display score for coursework 3
                              f"Exam: {record['exam']}\n"  #display exam score
                              f"Total Marks: {record['marks']} / 160\n"  #display the total marks
                              f"Percentage: {record['percentage']:.2f}%\n"  #display the percentage
                              f"Grade: {record['grade']}\n")  #display the grade
            
            self.list.insert(END, formatted_line) #inserts the formatted information for the student into the listbox
            self.list.insert(END, "") #inserts empty line after each record
            
            
    #this shows each individual student record
    def view_individual_record(self):
        self.list.delete(0, END) #clear all items from the list 

        name = self.search_name_entry.get().strip() #get the text entered in the search entry field
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

        #shows the user that no record was found
        if not found:
            messagebox.showerror("Error!", f"No record was found for student: {name}")
    
    #this shows the student with the highest score 
    def show_highest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        #this will show the student with the highest score in the messagebox
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

    #this shows the student with the lowest score
    def show_lowest_score(self):
        if not self.student_records:
            messagebox.showinfo("Records", "No student records available.")
            return

        #this will show the student with the lowest score in the messagebox
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
 
            
root=Tk()      
root.title("Student Manager") #window title
root.geometry("700x500") #window size
root.configure(bg="#E7759A") #background color of the window


app=StudentMarks(root)

root.mainloop() #runs the application


