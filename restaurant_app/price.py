from tkinter import *
#from Bairavaa import *



def prices():
    def back():
        top.destroy()
    top=Toplevel()
    w = 900
    h = 600
    sw = top.winfo_screenwidth()
    sh = top.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))
    top.config(bg='#0B0c10')
    top.title("Price Menu")

    # main fram
    frmcov = Frame(top)
    frmcov.pack(fill=BOTH, expand=1)
    # canvas
    canvas = Canvas(frmcov, bg='#0B0C10')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # scrollbar
    scrollbary = Scrollbar(frmcov, orient=VERTICAL, command=canvas.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    # configure canvas
    canvas.configure(yscrollcommand=scrollbary.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # Anotherr frm inside the canvas
    frmt0 = Frame(canvas, bg='#0B0C10')
    # new frm to a window in the canvas
    canvas.create_window((5, 5), window=frmt0, anchor=NE)



#frames---------------------------------------------------------------------------------------
    frmth=Frame(frmt0)
    frmth.pack()
    frmtm=Frame(frmt0 , bg='#0B0C10')
    frmtm.pack()
    frmt1=Frame(frmtm, bg='#0B0C10')
    frmt1.grid(row=0, column=0 , padx=25)
    frmt2=Frame(frmtm, bg='#0B0C10')
    frmt2.grid(row=0, column=1, padx=25)
    frmt3 = Frame(frmtm, bg='#0B0C10')
    frmt3.grid(row=0, column=2, padx=25)
    btn_price = Button(frmt0, text="BACK", fg="orange", width=5, padx=2, pady=2, bg='#802BB1', font=('times 18 bold'),
                       activebackground="#4056A1",activeforeground="white",command=back)
    btn_price.pack(padx=2, pady=2, )
    lbl_resh = Label(frmth, text="🍜 Restaurant Menu", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_resh.pack(padx=0, pady=0, )
#label menu-------------------------------------------------------------------------------------------------

    fav=Label(frmt1, text="Your Favorite", bg='#802BB1', width=25, font=('times 15 bold'))     #1
    fav.grid(row=0, column=0,columnspan=2, pady=1)
    tea= Label(frmt1, text="Tea",bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    tea.grid(row=1, column=0, pady=1)
    cof = Label(frmt1, text="Coffee",bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    cof.grid(row=2, column=0, pady=1)
    mil = Label(frmt1, text="Milk",bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=3, column=0, pady=1)

    fav=Label(frmt1, text="South Indian Breakfast", bg='#802BB1', width=25, font=('times 15 bold'))        #2
    fav.grid(row=4, column=0,columnspan=2, pady=1)
    mil = Label(frmt1, text="Medu Wada Sambhar", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=5, column=0, pady=1)
    mil = Label(frmt1, text="Idli", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=6, column=0, pady=1)
    mil = Label(frmt1, text="Sada Dosa", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=7, column=0, pady=1)
    mil = Label(frmt1, text="Paper Dosa", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=8, column=0, pady=1)
    mil = Label(frmt1, text="Mashal Dosa", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=9, column=0, pady=1)
    mil = Label(frmt1, text="Onion Uttspam", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=10, column=0, pady=1)
    mil = Label(frmt1, text="Pongal", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=11, column=0, pady=1)
    mil = Label(frmt1, text="Poori", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=12, column=0, pady=1)

    fav=Label(frmt1, text="Start New", bg='#802BB1', width=25, font=('times 15 bold'))       #3
    fav.grid(row=13, column=0,columnspan=2, pady=1)
    mil = Label(frmt1, text="Veg Sandwich", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=14, column=0, pady=1)
    mil = Label(frmt1, text="Cheese Sandwich", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=15, column=0, pady=1)
    mil = Label(frmt1, text="Butter Toast", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=16, column=0, pady=1)
    mil = Label(frmt1, text="Paneer Sandwich", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=17, column=0, pady=1)

    fav=Label(frmt1, text="Pizza", bg='#802BB1', width=25, font=('times 15 bold'))      #4
    fav.grid(row=18, column=0,columnspan=2, pady=1)
    mil = Label(frmt1, text="Veg Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=19, column=0, pady=1)
    mil = Label(frmt1, text="Veg Cheese Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=20, column=0, pady=1)
    mil = Label(frmt1, text="Mushrooom Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=21, column=0, pady=1)
    mil = Label(frmt2, text="Paneer Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=0, column=0, pady=1)
    mil = Label(frmt2, text="Plain Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=1, column=0, pady=1)
    mil = Label(frmt2, text="Chicken Tikka Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=2, column=0, pady=1)
    mil = Label(frmt2, text="Chicken Roast Pizza", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=3, column=0, pady=1)

    fav=Label(frmt2, text="Soup", bg='#802BB1', width=25, font=('times 15 bold'))      #5
    fav.grid(row=4, column=0,columnspan=2, pady=1)
    mil = Label(frmt2, text="Tomato Soup", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=5, column=0, pady=1)
    mil = Label(frmt2, text="Noodle Soup", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=6, column=0, pady=1)
    mil = Label(frmt2, text="Chicken Soup", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=7, column=0, pady=1)
    mil = Label(frmt2, text="Mutton Soup", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=8, column=0, pady=1)

    fav=Label(frmt2, text="Veg", bg='#802BB1', width=25, font=('times 15 bold'))        #6
    fav.grid(row=9, column=0,columnspan=2, pady=1)
    mil = Label(frmt2, text="French Fries", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=10, column=0, pady=1)
    mil = Label(frmt2, text="Mashroom Chilly", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=11, column=0, pady=1)
    mil = Label(frmt2, text="Calliflower Chilly", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=12, column=0, pady=1)
    mil = Label(frmt2, text="Paneer 65", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=13, column=0, pady=1)

    fav=Label(frmt2, text="Non-Veg", bg='#802BB1', width=25, font=('times 15 bold'))     #7
    fav.grid(row=14, column=0,columnspan=2, pady=1)
    mil = Label(frmt2, text="Chicken Grevy", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=15, column=0, pady=1)
    mil = Label(frmt2, text="Chicken 65", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=16, column=0, pady=1)
    mil = Label(frmt2, text="Chicken Lollypop", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=17, column=0, pady=1)
    mil = Label(frmt2, text="Fish Fry", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=18, column=0, pady=1)

    fav=Label(frmt2, text="Chinies Noodle & Rice", bg='#802BB1', width=25, font=('times 15 bold'))    #8
    fav.grid(row=19, column=0,columnspan=2, pady=1)
    mil = Label(frmt2, text="Chicken Fried N/R ", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=20, column=0, pady=1)
    mil = Label(frmt2, text="Egg Fried N/R", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=21, column=0, pady=1)
    mil = Label(frmt3, text="Mix Fried N/R", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=0, column=0, pady=1)



    fav=Label(frmt3, text="Rice / Briyani", bg='#802BB1', width=25, font=('times 15 bold'))      #9
    fav.grid(row=1, column=0,columnspan=2, pady=1)
    mil = Label(frmt3, text="Plain Rice", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=2, column=0, pady=1)
    mil = Label(frmt3, text="Curd Rice", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=3, column=0, pady=1)
    mil = Label(frmt3, text="Veg Briyani", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=4, column=0, pady=1)
    mil = Label(frmt3, text="Chicken Briyani", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=5, column=0, pady=1)
    mil = Label(frmt3, text="Egg Briyani", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=6, column=0, pady=1)
    mil = Label(frmt3, text="Mutton Briyani", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=7, column=0, pady=1)

    fav=Label(frmt3, text="Juices", bg='#802BB1', width=25, font=('times 15 bold'))             #10
    fav.grid(row=8, column=0,columnspan=2, pady=1)
    mil = Label(frmt3, text="Orange Juice", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=9, column=0, pady=1)
    mil = Label(frmt3, text="Apple Juice", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=10, column=0, pady=1)
    mil = Label(frmt3, text="Mix Fresh Juice", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=11, column=0, pady=1)
    mil = Label(frmt3, text="Fresh Lime Water", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=12, column=0, pady=1)
    mil = Label(frmt3, text="Strawberry Shake", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=13, column=0, pady=1)

    fav=Label(frmt3, text="Ice Creams", bg='#802BB1', width=25, font=('times 15 bold'))             #11
    fav.grid(row=14, column=0,columnspan=2, pady=1)
    mil = Label(frmt3, text="Venilla", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=15, column=0, pady=1)
    mil = Label(frmt3, text="Straw Berry", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=16, column=0, pady=1)
    mil = Label(frmt3, text="Chocolate", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=17, column=0, pady=1)
    mil = Label(frmt3, text="Kesar Pista", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=18, column=0, pady=1)
    mil = Label(frmt3, text="Fruit Cocktail", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=19, column=0, pady=1)
    mil = Label(frmt3, text="Black Current", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=20, column=0, pady=1)
    mil = Label(frmt3, text="Milk", bg="#F79E02", fg="white", width=25, font=('times 15 bold'))
    mil.grid(row=21, column=0, pady=1)





#price of favorit
    tea = Label(frmt1, text="RS. 10",bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))    #1
    tea.grid(row=1, column=1)
    cof = Label(frmt1, text="Rs. 15",bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    cof.grid(row=2, column=1)
    mil = Label(frmt1, text="Rs . 20",bg="#1B9CE5", fg="white",  width=7, font=('times 15 bold'))
    mil.grid(row=3, column=1)

    mil = Label(frmt1, text="Rs . 35",bg="#1B9CE5", fg="white",  width=7, font=('times 15 bold'))      #2
    mil.grid(row=5, column=1)
    mil = Label(frmt1, text="Rs . 25",bg="#1B9CE5", fg="white",  width=7, font=('times 15 bold'))
    mil.grid(row=6, column=1)
    mil = Label(frmt1, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=7, column=1)
    mil = Label(frmt1, text="Rs . 50", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=8, column=1)
    mil = Label(frmt1, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=9, column=1)
    mil = Label(frmt1, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=10, column=1)
    mil = Label(frmt1, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=11, column=1)
    mil = Label(frmt1, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=12, column=1)

    mil = Label(frmt1, text="Rs . 35", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))      #3
    mil.grid(row=14, column=1)
    mil = Label(frmt1, text="Rs . 50", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=15, column=1)
    mil = Label(frmt1, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=16, column=1)
    mil = Label(frmt1, text="Rs . 60", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=17, column=1)

    mil = Label(frmt1, text="Rs . 70", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))     #4
    mil.grid(row=19, column=1)
    mil = Label(frmt1, text="Rs . 80", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=20, column=1)
    mil = Label(frmt1, text="Rs . 80", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=21, column=1)
    mil = Label(frmt2, text="Rs . 90", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=0, column=1)
    mil = Label(frmt2, text="Rs . 80", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=1, column=1)
    mil = Label(frmt2, text="Rs . 100", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=2, column=1)
    mil = Label(frmt2, text="Rs . 110", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=3, column=1)

    mil = Label(frmt2, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))    #5
    mil.grid(row=5, column=1)
    mil = Label(frmt2, text="Rs . 50", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=6, column=1)
    mil = Label(frmt2, text="Rs . 65", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=7, column=1)
    mil = Label(frmt2, text="Rs . 70", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=8, column=1)

    mil = Label(frmt2, text="Rs . 50", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))     #6
    mil.grid(row=10, column=1)
    mil = Label(frmt2, text="Rs . 90", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=11, column=1)
    mil = Label(frmt2, text="Rs . 90", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=12, column=1)
    mil = Label(frmt2, text="Rs . 120", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=13, column=1)

    mil = Label(frmt2, text="Rs . 130", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))     #7
    mil.grid(row=15, column=1)
    mil = Label(frmt2, text="Rs . 140", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=16, column=1)
    mil = Label(frmt2, text="Rs . 110", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=17, column=1)
    mil = Label(frmt2, text="Rs . 120", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=18, column=1)

    mil = Label(frmt2, text="Rs . 100", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))     #8
    mil.grid(row=20, column=1)
    mil = Label(frmt2, text="Rs . 90", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=21, column=1)
    mil = Label(frmt3, text="Rs . 180", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=0, column=1)

    mil = Label(frmt3, text="Rs . 70", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))     #9
    mil.grid(row=2, column=1)
    mil = Label(frmt3, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=3, column=1)
    mil = Label(frmt3, text="Rs . 80", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=4, column=1)
    mil = Label(frmt3, text="Rs . 120", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=5, column=1)
    mil = Label(frmt3, text="Rs . 100", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=6, column=1)
    mil = Label(frmt3, text="Rs . 130", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=7, column=1)

    mil = Label(frmt3, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))   #10
    mil.grid(row=9, column=1)
    mil = Label(frmt3, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=10, column=1)
    mil = Label(frmt3, text="Rs . 60", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=11, column=1)
    mil = Label(frmt3, text="Rs . 15", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=12, column=1)
    mil = Label(frmt3, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=13, column=1)

    mil = Label(frmt3, text="Rs . 10", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))    #11
    mil.grid(row=15, column=1)
    mil = Label(frmt3, text="Rs . 25", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=16, column=1)
    mil = Label(frmt3, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=17, column=1)
    mil = Label(frmt3, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=18, column=1)
    mil = Label(frmt3, text="Rs . 45", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=19, column=1)
    mil = Label(frmt3, text="Rs . 40", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=20, column=1)
    mil = Label(frmt3, text="Rs . 30", bg="#1B9CE5", fg="white", width=7, font=('times 15 bold'))
    mil.grid(row=21, column=1)






