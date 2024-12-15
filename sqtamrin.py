from tkinter import *
from tkinter import messagebox
from sqt import *

class Gui:
    def __init__(self,win):
        
        self.win = win
        self.win.title('Library Management')
        self.win.geometry('600x400')
        
#first_frame
        self.frame_label = Frame(self.win)
        self.frame_label.pack()
        
        self.title_label = Label(self.frame_label, text='Welcome To Our Library', font=('arial',18), foreground='red')
        self.title_label.pack(pady=18,side=LEFT)
        
        self.pic = PhotoImage(file ='aaa_11zon.png')
        self.pic_label = Label(self.frame_label,image=self.pic)
        self.pic_label.pack(side=LEFT)

#line1
    

        self.frame_line1 = Frame(self.win)
        self.frame_line1.pack()

        self.frame1 = LabelFrame(self.frame_line1, text='Search Books', font=(8), foreground='#757575', width=100)
        self.frame1.pack()

        self.title_label = Label(self.frame1, text='Which data do you want to know?', font=('arial',14), foreground='#303F9F')
        self.title_label.pack(padx=15, pady=17)

        self.book_id = Label(self.frame1,text='Book ID :', font=('tahoma',12), foreground='#283593')
        self.book_id.pack(side=LEFT, pady=17)

        self.book_id = Entry(self.frame1, width=25)
        self.book_id.pack(pady=17,side=LEFT, padx = 10)

        self.btn1 = Button(self.frame1, text='Search',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12, bd=1,command=self.def_show_data)
        self.btn1.pack(side=TOP, padx=5,pady= 5)

    
#line2
        self.frame2 = Frame(self.win)
        self.frame2.pack()

        self.label_label = Label(self.frame2, text='What do you want to do?', font=('arial',14), foreground='#F44336')
        self.label_label.pack(side=TOP,pady=17)

        self.btn2 = Button(self.frame2, text='Insert Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=self.new_data)
        self.btn2.pack(side=LEFT, padx=5,pady= 5)

        self.btn3 = Button(self.frame2, text='Update Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=self.update_data)
        self.btn3.pack(side=LEFT, padx=5,pady= 5)

        self.btn3 = Button(self.frame2, text='Delete Data',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1,command=self.delete_data)
        self.btn3.pack(side=LEFT, padx=5,pady= 5)

        self.btn4 = Button(self.frame2, text='Exit',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=12,height=1, bd=1, command=exit_data)
        self.btn4.pack(side=LEFT, padx=5,pady= 5)
        
#show
    def def_show_data(self):
        self.str9=self.book_id.get()
        messagebox.showinfo('Information', show_data(self.str9))
    
#insert
    def def_btn_insert_data(self):
            self.str1=self.book1_entry.get()
            self.str2=self.subject1_entry.get()
            self.str3=self.author1_entry.get()
            self.str4=self.publish1_entry.get()
            insert_data(self.str1,self.str2,self.str3,self.str4)
            messagebox.showinfo('Data','your information saved!')
         
    def new_data(self):
        self.second=Toplevel(self.win)
        self.second.title('New Data')
        self.second.geometry('350x280')

        self.labelframe = LabelFrame(self.second, text='New Data', foreground='#455A64')
        self.labelframe.pack(pady=15, padx=15)

        #line1
        self.second1 = Frame(self.labelframe)
        self.second1.pack(padx=15)
        self.book1_label = Label(self.second1,text='Book Ttitle :',font=('arial',12), foreground='#283593')
        self.book1_label.pack(side=LEFT)
        self.book1_entry = Entry(self.second1, width=17)
        self.book1_entry.pack(pady=10,side=LEFT)

        #line2
        self.second2 = Frame(self.labelframe)
        self.second2.pack(padx=15)
        self.publish1_label = Label(self.second2,text='Publish Year :',font=('arial',12), foreground='#283593')
        self.publish1_label.pack(side=LEFT)
        self.publish1_entry = Entry(self.second2, width=17)
        self.publish1_entry.pack(pady=10,side=LEFT)


        #line3
        self.second3 = Frame(self.labelframe)
        self.second3.pack(padx=15)
        self.author1_label = Label(self.second3,text='Author :',font=('arial',12), foreground='#283593')
        self.author1_label.pack(side=LEFT)
        self.author1_entry = Entry(self.second3, width=17)
        self.author1_entry.pack(pady=10,side=LEFT)

        #line4
        self.second4 = Frame(self.labelframe)
        self.second4.pack(padx=15)
        self.subject1_label = Label(self.second4,text='Subject :',font=('arial',12), foreground='#283593')
        self.subject1_label.pack(side=LEFT)
        self.subject1_entry = Entry(self.second4, width=17,)
        self.subject1_entry.pack(pady=10,side=LEFT)

        #line5
        self.second5 = Frame(self.labelframe)
        self.second5.pack(padx=15)
        self.second_btn = Button(self.second5,text='Submit information',font=('arial',12),foreground='#004D40', bg='#E0F2F1', bd=1,command=self.def_btn_insert_data)
        self.second_btn.pack(pady=10)

#delete
    
    def def_btn_delete_data(self):
        self.str5=self.delete_third_entry.get()
        deletee_data(self.str5)
        messagebox.showinfo('Data','your information deleted!')
    
        
    def delete_data(self):
        self.third=Toplevel(self.win)
        self.third.title('Delete Data')
        self.third.geometry('350x200')


        self.delete_label = Label(self.third, text='Which data do you want to delete?', font=('arial',14), foreground='red')
        self.delete_label.pack()

        #line1
        self.third1 = Frame(self.third)
        self.third1.pack()
        self.delete_third_label = Label(self.third1,text='Book ID:',font=('arial',12), foreground='#283593')
        self.delete_third_label.pack(side=LEFT,pady=15)
        self.delete_third_entry = Entry(self.third1, width=17)
        self.delete_third_entry.pack(pady=10,side=LEFT)

        #line2
        self.third2 = Frame(self.third)
        self.third2.pack()
        self.third_btn = Button(self.third2,text='Delete',font=('arial',12),foreground='#004D40', bg='#E0F2F1', bd=1,command=self.def_btn_delete_data)
        self.third_btn.pack(pady=8)
    
#update
    
    def def_btn_update_data(self):
        self.str6=self.field_entry.get()
        self.str7=self.new_value_entry.get()
        self.str8=self.book_id_entry.get()
        updatee_data(self.str6,self.str7,self.str8)
        messagebox.showinfo('Data','your information saved!')
          
            
    def update_data(self):
        self.forth=Toplevel(self.win)
        self.forth.title('Update Data')
        self.forth.geometry('350x280')


        self.update_label = Label(self.forth, text='Which data do you want to update?', font=('arial',14), foreground='red')
        self.update_label.pack()
        self.update_label = Label(self.forth, text='(title,subject,author,pub_year)', font=('arial',11), foreground='#455A64')
        self.update_label.pack()

        self.labelframe_update = LabelFrame(self.forth, text='Upadte Data', foreground='#455A64')
        self.labelframe_update.pack(pady=15, padx=15)

        #line1
        self.forth1 = Frame(self.labelframe_update)
        self.forth1.pack(padx=15)

        self.book_id_label = Label(self.forth1,text='Book ID:',font=('arial',12), foreground='#283593')
        self.book_id_label.pack(side=LEFT)
        self.book_id_entry = Entry(self.forth1, width=14)
        self.book_id_entry.pack(pady=10,side=LEFT)

        self.forth2 = Frame(self.labelframe_update)
        self.forth2.pack(padx=15)

        self.field_label = Label(self.forth2,text='Field:',font=('arial',12), foreground='#283593')
        self.field_label.pack(side=LEFT)
        self.field_entry = Entry(self.forth2, width=14)
        self.field_entry.pack(pady=10,side=LEFT)

        self.forth3 = Frame(self.labelframe_update)
        self.forth3.pack(padx=15)

        self.new_value_label = Label(self.forth3,text='New Value:',font=('arial',12), foreground='#283593')
        self.new_value_label.pack(side=LEFT)
        self.new_value_entry = Entry(self.forth3, width=14)
        self.new_value_entry.pack(pady=10,side=LEFT)

        self.forth4 = Frame(self.labelframe_update)
        self.forth4.pack(padx=15)

        self.btn_update = Button(self.forth4, text='Submit',font=('tahoma',12),foreground='#004D40', bg='#E0F2F1', width=8,height=1, bd=1,command=self.def_btn_update_data)
        self.btn_update.pack(side=LEFT, padx=5,pady= 5)

        
def main():
    win = Tk()
    project = Gui(win)
    win.mainloop()
    
main()

