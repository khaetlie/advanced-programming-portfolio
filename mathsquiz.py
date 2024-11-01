from tkinter import *
import random

class MathsQuiz: #create a class for Math Quiz
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x500")
        self.root.configure(bg="#2E86AB")
        self.question_count = 0
        self.score = 0
        self.start()
    
    def start(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        first_l1=Label(self.root,text="WELCOME TO MATHS QUIZ!",bg="#F24236",fg="white",font=('arial', 20)) #shows the main text or title
        first_l1.place(x=60,y=180) 
        first_b1=Button(self.root,text="Start",bg="#F5F749",fg="black",font=('arial', 10), command=self.displayMenu) #will show the start button to go to the second page  
        first_b1.pack(pady=240)
            
    def displayMenu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        second_l1=Label(self.root, text = "Please choose the difficulty:",bg="#F49D40",fg="black",bd=5,font=('arial', 12))
        second_l1.pack(padx=10,pady=(150,20))
        
        b2=Button(self.root,text="Easy", bg="#F6F5AE",command=lambda: self.start_quiz('easy'))  #easy difficulty button
        b2.pack(pady=5)
        b3=Button(self.root,text="Moderate", bg="#F6F5AE", command = lambda:self.start_quiz('moderate')) #moderate difficulty button
        b3.pack(pady=5)
        b4=Button(self.root,text="Hard", bg="#F6F5AE", command=lambda: self.start_quiz('hard')) #hard difficulty button
        b4.pack(pady=5)
        
    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.question_count = 0
        self.score = 0
        self.next_question()
    
    def next_question(self):
        if self.question_count < 10:
            self.question_count += 1
            self.num1, self.num2 = self.random_numbers()
            self.operation = random.choice(['+', '-'])
            self.displayProblem()
        else:
            self.displayResults()
            
    def random_numbers(self):
        if self.difficulty == 'easy':
            return random.randint(1,10), random.randint(1,10)
        elif self.difficulty == 'moderate':
            return random.randint(1,90), random.randint(1,90)
        elif self.difficulty == 'hard':
            return random.randint(1,200), random.randint(1,200)


    def displayProblem(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        question_l1=Label(self.root, text= f"Question {self.question_count}: What is {self.num1} {self.operation} {self.num2}?", font=('arial', 15), bg="#F49D40",bd=5)     
        question_l1.pack(pady=(150,20))  
    
        self.answer_e1 = Entry(self.root, font=('arial', 12))
        self.answer_e1.pack(pady=5)
        self.answer_e1.focus()
        
        submit_btn = Button(self.root, text="Submit", bg="#92BEAD",font=('arial', 10), command=self.isCorrect)
        submit_btn.pack(pady=(20,5))
        
        self.result_l1=Label(self.root, text="", font=('arial', 12))
        self.result_l1.pack(pady=5)
        
    def isCorrect(self):
        try:
            your_answer = int(self.answer_e1.get())
            correct_answer = eval(f"{self.num1} {self.operation} {self.num2}")
            if your_answer == correct_answer:
                self.result_l1.config(text="Your answer is correct!", fg="green")
                self.score += 1
            else:
                self.result_l1.config(text=f"Sorry, your answer is wrong. The correct one is {correct_answer}.")
        except ValueError:
            self.result_l1.config(text="Pleases enter a valid number", fg="red")
            
        self.root.after(1000, self.next_question)
        
    def displayResults(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
            score_l1=Label(self.root, text=f"The quiz is over! Your score is: {self.score}/10", font=('arial', 20))
            score_l1.pack(pady=20)

root=Tk()
root.title("Maths Quiz")
quiz=MathsQuiz(root)
root.mainloop()