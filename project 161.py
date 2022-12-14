root = Tk()
root.title("File Handling")
root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))
exit_image = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_filename = Label(root,text="File Name")
label_filename.place(relx=0.28,rely=0.03,anchor=CENTER)

input_filename = Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""

def openfile():
    global name 
    my_text.delete(1.0,END)
    input_filename.delete(0,END)
    text_file = filedialog.askopenfilename(title = "Open Text File",filetypes = (("Text Files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    input_filename.insert(END,formatted_name)
    root.title(formatted_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    

open_button = Button(root,image=open_image,text="Open File",command=openfile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)


.
root.mainloop().