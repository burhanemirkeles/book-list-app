import tkinter

root = tkinter.Tk()
root.geometry("720x370")
root.title("Book List Project")

# creating labels
lbl_name = tkinter.Label(root, text="Name of Book:")
lbl_name_of_author = tkinter.Label(root, text="Name of Author:")
lbl_genre = tkinter.Label(root, text="Genre:")
lbl_date = tkinter.Label(root, text="Date Between(MM/YYYY):")
lbl_view = tkinter.Label(root, text="View On Book:")
lbl_books_read = tkinter.Label(root, text="Books read:")

#creating listbox of books
listbox_book = tkinter.Listbox(root)

#creating button
btn_add = tkinter.Button(root, text="ADD")

#creating txt areas
txt_name = tkinter.Entry(root)
txt_nofa = tkinter.Entry(root)
txt_genre = tkinter.Entry(root)
txt_start_date = tkinter.Entry(root, width=7) #restrict character number with 7 !!!
txt_finish_date = tkinter.Entry(root, width=7)
txt_view = tkinter.Entry(root)

#positioning labels
lbl_name.grid(row=0, column=0)
lbl_name_of_author.grid(row=1, column=0)
lbl_genre.grid(row=2, column=0)
lbl_date.grid(row=3, column=0)
lbl_view.grid(row=4, column=0)
lbl_books_read.grid(row=0, column=3)

#positioning txt areas
txt_name.grid(row=0, column=1)
txt_nofa.grid(row=1, column=1)
txt_genre.grid(row=2, column=1)
txt_start_date.grid(row=3, column=1)
txt_view.grid(row=4, column=1) #convert it to rich text box

#positioning button
btn_add.grid(row=5, column=2)

#positioning listbox
listbox_book.grid(row=1, column=3)


txt_finish_date.grid(row=3, column=2)


root.mainloop()
