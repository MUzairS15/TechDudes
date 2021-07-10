from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from tkinter.font import BOLD
from PIL import Image, ImageTk
from numpy import nextafter, pad
import pytesseract as suraj
suraj.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


a = Tk()
a.title("Smart Evaluation System")
a.geometry('+%d+%d'%(200,100))

main_frame = Frame(a , width=900, height=500  )
main_frame.grid(columnspan=4 ,rowspan=12 , row=0)





def cwin():
    z = Tk()
    z.geometry("500x400")



    def ppp():
        f = str(que_no_entry.get())
        print("No of Question selected", f)
        g = str(ans_no_entry.get())
        print("No of Answers selected", g)

    def qqq():
        m = str(your_ans_box.get("1.0","end-1c"))
        print("Entered Keywords are : ", m)



    p = StringVar()
    q = StringVar(  )

    que_no = Label(z ,text="Enter no of Questions")
    que_no.pack()
    que_no_entry = Entry(z , textvariable=p)
    que_no_entry.pack()

    # que_no_button = Button(text="Save" , command=ppp)
    # que_no_button.pack()


    ans_no = Label(z , text="Enter No of Keywords")
    ans_no.pack()
    ans_no_entry = Entry(z , textvariable=q )
    ans_no_entry.pack()

    ans_no_button = Button(z , text="Save" , command=ppp)
    ans_no_button.pack()

    your_ans = Label(z ,text="Enter your List of Keywords")
    your_ans.pack()
    your_ans_box = Text(z ,width=50 , height=10 ,bg="#c8c8c8")
    your_ans_box.pack()
    your_ans_box_button = Button(z , text="Save" , command=qqq)
    your_ans_box_button.pack()








    z.mainloop()



def showimage():
    fln = filedialog.askopenfilename(initialdir = "/", title ="Select a file", filetype = (("jpeg", "*.jpg"),  ("All FIles", "*.*")))
    img = Image.open(fln)
    img.thumbnail((200,250))
    img = ImageTk.PhotoImage(img)
#     label.configure(image=img)
    label.image = img
    p = Label(frame2 , image=img)
    p.grid(rowspan=6, row=2, column=0 )



label = Label(a)
label.grid()



heading = Label(text="Smart Evaluation System", font=("Arial", 20), pady=10)
heading.grid(columnspan=3,column=1 , row=0)

frame2 = Frame(a )
frame2.grid( row=0 , column=0 , rowspan=12 , sticky=E )

canvs3 = Canvas(frame2 , bg="grey" , height=358 , width=200)
canvs3.grid(row=0 , rowspan=12 )

select_assgn = Label(frame2 , text="Select Assignment", bg="grey" , fg="white" , font=("default" , 14 , BOLD))
select_assgn.grid(column=0 , row=0 )

browser_btn = Button(frame2 ,text="Browse" , command=showimage)
browser_btn.grid(column=0 , row=1 ,sticky= N)



page_no = Label(frame2,text="Page No : " , bg="grey" , fg="white")
page_no.grid(column=0 , row=9)

Pp = Frame(frame2 , bg="grey")
Pp.grid(row=10, column=0, columnspan=1)
previous_page = Button(Pp, text="Previous Page")
previous_page.grid(column=0,row=0)
gap = Label(Pp, text="  ", bg="grey" , fg="white")
gap.grid(column=1 , row=0)
next_page = Button(Pp, text="Next Page")
next_page.grid(column=2 ,row=0)



frame1 = Frame(a,  highlightbackground="black", highlightthickness=3 )
frame1.grid(column=1 , row=0 , columnspan=3 , rowspan=12 )

canvs = Canvas(frame1 ,width=500 )
canvs.grid(column=0 , row=1 , columnspan=3 , rowspan=12 , ipadx=40 , ipady=30 )

canvs.create_line(0 ,100 , 800 , 100 , width=3  )

canvs2 = Canvas(frame1 , width=500 )
canvs2.grid(column=0 , row=1 , columnspan=3 , rowspan=12 , ipadx=40 , ipady=30)
canvs2.create_line(0 ,100 , 800 , 100 , width=3  )


canvs2.create_line(300 ,100 , 300 , 500 , width=3 )



col_gap = Label(a ,text="                     ")
col_gap.grid(column=10 )





lbl = Label(frame1 , text="Now you can Create your custom Answer sheet"  , font=("default" , 12))
lbl.grid(row=0 ,column=0, sticky=W )
lbl2 = Label(frame1 , text="by providing your keywords data here" , font=("default" , 12))
lbl2.grid(row=1 , column=0 , sticky=W )

gap2 = Label(frame1, text="          ")
gap2.grid(row=2 ,column=0)

add_data_btn = Button(frame1, text="Click here to Add new Data" , command=cwin , font=("default" , 10 , BOLD), bg="sky blue")
add_data_btn.grid(row=3 , column=0)

save_data_btn = Button(frame1, text="Save Data", font=("default" , 10 , BOLD), bg="sky blue")
save_data_btn.grid(row=3 , column=1)



gap3 = Label(frame1, text="          ")
gap3.grid(row=6 ,column=0)





check_page = Label(frame1 , text="Check Pages for ,", font=("default" , 12))
check_page.grid(row=6  , sticky=W)

student_name = Label(frame1, text="Student Name", font=("default" , 10 , BOLD))
student_name.grid(row=7 )
name_entry = Entry(frame1)
name_entry.grid(row=8 , sticky=N)
student_roll = Label(frame1 , text="Student Roll no ", font=("default" , 10 , BOLD))
student_roll.grid(row=9 )
roll_entry = Entry(frame1)
roll_entry.grid(row=10 , sticky=N)
save_btn = Button(frame1 , text="Save", font=("default" , 10 , BOLD) , bg="sky blue")
save_btn.grid(row=11 )



total_pages = Label(frame1 , text="Total Pages : ", font=("default" , 12))
total_pages.grid(row=6 , sticky=W ,  column=1)

scan_pages_btn = Button(frame1 , text="Scan Pages", font=("default" , 10 , BOLD) , bg="orange")
scan_pages_btn.grid(row=7 , sticky=W , column=1)

total_keywords = Label(frame1 , text="Total Keywords detected : ", font=("default" , 12))
total_keywords.grid(row=8 , column=1 , sticky=W)

find_score = Button(frame1 , text="Find Score", font=("default" , 10 , BOLD) , bg="orange")
find_score.grid(row=9 , column=1, sticky=W)

save_txt = Button(frame1 , text="Save ", font=("default" , 10 , BOLD) , bg="grey" ,fg="white")
save_txt.grid(row=10 , column=1 )







a.mainloop()