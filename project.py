from tkinter import *
from tkinter import messagebox
from sqt import *

win = Tk()
win.title('Library Management')
win.geometry('600x400')

    
    
def new_data():
    second=Toplevel(win)
    second.title('New Data')
    second.geometry('350x280')
    
    def def_btn_insert_data():
        str1=book1_entry.get()
        str2=subject1_entry.get()
        str3=author1_entry.get()
        str4=publish1_entry.get()
        insert_data(str1,str2,str3,str4)
        messagebox.showinfo('Data','your information saved!')
    
    labelframe = LabelFrame(second, text='New Data', foreground='#455A64')
    labelframe.pack(pady=15, padx=15)
    
    #line1
    second1 = Frame(labelframe)
    second1.pack(padx=15)
    book1_label = Label(second1,text='Book Ttitle :',font=('arial',12), foreground='#283593')
    book1_label.pack(side=LEFT)
    book1_entry = Entry(second1, width=17)
    book1_entry.pack(pady=10,side=LEFT)

    #line2
    second2 = Frame(labelframe)
    second2.pack(padx=15)
    publish1_label = Label(second2,text='Publish Year :',font=('arial',12), foreground='#283593')
    publish1_label.pack(side=LEFT)
    publish1_entry = Entry(second2, width=17)
    publish1_entry.pack(pady=10,side=LEFT)


    #line3
    second3 = Frame(labelframe)
    second3.pack(padx=15)
    author1_label = Label(second3,text='Author :',font=('arial',12), foreground='#283593')
    author1_label.pack(side=LEFT)
    author1_entry = Entry(second3, width=17)
    author1_entry.pack(pady=10,side=LEFT)

    #line4
    second4 = Frame(labelframe)
    second4.pack(padx=15)
    subject1_label = Label(second4,text='Subject :',font=('arial',12), foreground='#283593')
    subject1_label.pack(side=LEFT)
    subject1_entry = Entry(second4, width=17,)
    subject1_entry.pack(pady=10,side=LEFT)
    
    #line5
    second5 = Frame(labelframe)
    second5.pack(padx=15)
    second_btn = Button(second5,text='Submit information',font=('arial',12),foreground='#004D40', bg='#E0F2F1', bd=1,command=def_btn_insert_data)
    second_btn.pack(pady=10)


def delete_data():
    third=Toplevel(win)
    third.title('Delete Data')
    third.geometry('350x200')

    def def_btn_delete_data():
        str5=delete_third_entry.get()
        deletee_data(str5)
        messagebox.showinfo('Data','your information deleted!')
    
    delete_label = Label(third, text='Which data do you want to delete?', font=('arial',14), foreground='red')
    delete_label.pack()

    #line1
    third1 = Frame(third)
    third1.pack()
    delete_third_label = Label(third1,text='Book ID:',font=('arial',12), foreground='#283593')
    delete_third_label.pack(side=LEFT,pady=15)
    delete_third_entry = Entry(third1, width=17)
    delete_third_entry.pack(pady=10,side=LEFT)

    #line2
    third2 = Frame(third)
    third2.pack()
    third_btn = Button(third2,text='Delete',font=('arial',12),foreground='#004D40', bg='#E0F2F1', bd=1,command=def_btn_delete_data)
    third_btn.pack(pady=8)

def update_data():
    forth=Toplevel(win)
    forth.title('Update Data')
    forth.geometry('350x280')

    def def_btn_update_data():
        str6=field_entry.get()
        str7=new_value_entry.get()
        str8=book_id_entry.get()
        updatee_data(str6,str7,str8)
        messagebox.showinfo('Data','your information saved!')
    
    update_label = Label(forth, text='Which data do you want to update?', font=('arial',14), foreground='red')
    update_label.pack()
    update_label = Label(forth, text='(title,subject,author,pub_year)', font=('arial',11), foreground='#455A64')
    update_label.pack()

    labelframe_update = LabelFrame(forth, text='Upadte Data', foreground='#455A64')
    labelframe_update.pack(pady=15, padx=15)
    
    #line1
    forth1 = Frame(labelframe_update)
    forth1.pack(padx=15)

    book_id_label = Label(forth1,text='Book ID:',font=('arial',12), foreground='#283593')
    book_id_label.pack(side=LEFT)
    book_id_entry = Entry(forth1, width=14)
    book_id_entry.pack(pady=10,side=LEFT)
    
    forth2 = Frame(labelframe_update)
    forth2.pack(padx=15)
    
    field_label = Label(forth2,text='Field:',font=('arial',12), foreground='#283593')
    field_label.pack(side=LEFT)
    field_entry = Entry(forth2, width=14)
    field_entry.pack(pady=10,side=LEFT)
    
    forth3 = Frame(labelframe_update)
    forth3.pack(padx=15)
    
    new_value_label = Label(forth3,text='New Value:',font=('arial',12), foreground='#283593')
    new_value_label.pack(side=LEFT)
    new_value_entry = Entry(forth3, width=14)
    new_value_entry.pack(pady=10,side=LEFT)

    forth4 = Frame(labelframe_update)
    forth4.pack(padx=15)

    btn_update = Button(forth4, text='Submit',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=8,height=1, bd=1,command=def_btn_update_data)
    btn_update.pack(side=LEFT, padx=5,pady= 5)

#first_frame
frame_label = Frame(win)
frame_label.pack()

title_label = Label(frame_label, text='Welcome To Our Library', font=('arial',18), foreground='red')
title_label.pack(pady=18,side=LEFT)

pic = PhotoImage(file ='aaa_11zon.png')
pic_label = Label(frame_label,image=pic)
pic_label.pack(side=LEFT)


#line1
def def_show_data():
    str9=book_id_entry.get()
    messagebox.showinfo('Information', show_data(str9))

frame1 = LabelFrame(win, text='Search Books', font=(8), foreground='#757575', width=100)
frame1.pack()

title_label = Label(frame1, text='Which data do you want to know?', font=('arial',14), foreground='#303F9F')
title_label.pack(padx=15, pady=17)

book_id = Label(frame1,text='Book ID :', font=('tahoma',12), foreground='#283593')
book_id.pack(side=LEFT, pady=17)

book_id_entry = Entry(frame1, width=25)
book_id_entry.pack(pady=17,side=LEFT, padx = 10)


btn1 = Button(frame1, text='Search',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12, bd=1,command=def_show_data)
btn1.pack(side=TOP, padx=5,pady= 5)

#line2
frame2 = Frame(win)
frame2.pack()


label_label = Label(frame2, text='What do you want to do?', font=('arial',14), foreground='#F44336')
label_label.pack(side=TOP,pady=17)
    
btn2 = Button(frame2, text='Insert Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=new_data)
btn2.pack(side=LEFT, padx=5,pady= 5)

btn3 = Button(frame2, text='Update Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=update_data)
btn3.pack(side=LEFT, padx=5,pady= 5)

btn3 = Button(frame2, text='Delete Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=delete_data)
btn3.pack(side=LEFT, padx=5,pady= 5)

btn4 = Button(frame2, text='Exit',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1, command=exit_data)
btn4.pack(side=LEFT, padx=5,pady= 5)



win.mainloop()