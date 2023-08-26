from tkinter import *
from tkinter import messagebox


tasks_list = []


counter = 1


def inputError() :
    if enterTaskField.get() == "" :
        messagebox.showerror(" Input Error       ")
        return 0
	
    return 1


def clear_taskNumberField() :
    taskNumberField.delete(0.0, END)


def clear_taskField() :
    enterTaskField.delete(0, END)
	

def insertTask():

	global counter
	

	value = inputError()
	if value == 0 :
		return

	
	content = enterTaskField.get() + "\n"
	tasks_list.append(content)
	TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
	counter += 1
	clear_taskField()


def delete() :
	
	global counter
	
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	number = taskNumberField.get(1.0, END)

	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		task_no = int(number)

	clear_taskNumberField()
	
	tasks_list.pop(task_no - 1)

	counter -= 1
	TextArea.delete(1.0, END)

	for i in range(len(tasks_list)) :
		TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
	

if __name__ == "__main__" :

	gui = Tk()

	gui.configure(background = "light blue")

	gui.title("ToDo App")

	gui.geometry("500x600")
	
	enterTask = Label(gui, text = "Enter Your Task")
	enterTaskField = Entry(gui)

	Submit = Button(gui, text = "Submit", fg = "Black", command = insertTask,height=2,width=20)

	TextArea = Text(gui, height = 10, width = 50, font = "lucida 13")

	taskNumber = Label(gui, text = "Delete Task Number")
						
	taskNumberField = Text(gui, height = 2, width = 5, font = "lucida 13")

	delete = Button(gui, text = "Delete", fg = "Black", command = delete,height=2,width=20)
	Exit = Button(gui, text = "Exit", fg = "Black", command = exit,height=2,width=20)

	enterTask.grid(row = 0, column = 2,pady=8)
		
	enterTaskField.grid(row = 1, column = 2, ipadx = 50,padx=100,pady=8)
	Submit.grid(row = 2, column = 2)
	TextArea.grid(row = 3, column = 2, padx = 10, sticky = W,pady=8)						
	taskNumber.grid(row = 4, column = 2, pady = 8)						
	taskNumberField.grid(row = 5, column = 2,pady=8)				
	delete.grid(row = 6, column = 2, pady = 8)						
	Exit.grid(row = 7, column = 2,pady=8)

	
	gui.mainloop()
