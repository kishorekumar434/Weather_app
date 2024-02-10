# RESTAURANT MANAGEMENT SYSTEM...,,,
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from price import *
import random, math #mysql.connector


win = Tk()
w = 1300
h = 700
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
x = (sw / 2) - (w / 2)
y = (sh / 2) - (h / 2)
win.geometry('%dx%d+%d+%d' % (w, h, x, y))

win.title("Bairava 3in1")
#win.iconbitmap(r"C:\Users\Kishore\Desktop\PROJECT\htl.ico")


# main fram
frmcov = Frame(win)
frmcov.pack(fill=BOTH, expand=1)
# canvas
canvas = Canvas(frmcov)
canvas.pack(side=LEFT, fill=BOTH, expand=1)
# scrollbar
scrollbary = Scrollbar(frmcov, orient=VERTICAL, command=canvas.yview)
scrollbary.pack(side=RIGHT, fill=Y)
# configure canvas
canvas.configure(yscrollcommand=scrollbary.set, bg='#0B0C10')
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# Anotherr frm inside the canvas
overfrm = Frame(canvas, bg='#0B0C10')
# new frm to a window in the canvas
canvas.create_window((0, 0), window=overfrm, anchor=NW)
# overfrm.config(bg="#3500D3")

# dbc = mysql.connector.connect(host="localhost", user="root", passwd="", db="project")


def delete_frm():
    for frame in mfrm.winfo_children():
        frame.destroy()


# function for home---------------------------------------------------------------------------------------
def home():
    delete_frm()

    lbl_room = Label(mfrm, text="♛ HOME", fg="orange", bg='#0B0c10', font=("times", 25, "bold"))
    lbl_room.pack(padx=0, pady=0, fill=X)
    wcm_lbl = Label(mfrm, text="Welcome to our 3 in 1 site", bg="#0B0c10", fg="#3500D3", font=("broadway 25 bold"))
    wcm_lbl.pack(padx=0, pady=1, fill=X)

    lbl_eat = Label(mfrm, text="🍴 Eat", fg="#8EE4AF", bg='#0B0c10', font=("times",20 , "bold"))
    lbl_eat.pack(padx=0, pady=0, fill=X)
    lbl_sleep = Label(mfrm, text="🛌 Sleep", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_sleep.pack(padx=0, pady=0, fill=X)
    lbl_party = Label(mfrm, text="🎼 Party", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_party.pack(padx=0, pady=0, fill=X)
    wcm_lbl = Label(mfrm, text='"you Don\'t Need A Silver Fork to Eat Good food"', bg="#0B0c10", fg="#C3073F", font=("times 18 bold"))
    wcm_lbl.pack(padx=0, pady=1)




def restaurant():
    def myspinbox():
        def back():
            restaurant()

        tea = 10 * (int(stea.get()))
        cof = 15 * (int(scof.get()))
        mil = 20 * (int(smil.get()))
        mws = 35 * (int(smws.get()))
        idl = 25 * (int(sidl.get()))
        sd = 30 * (int(ssd.get()))
        pd = 50 * (int(spd.get()))
        md = 40 * (int(smd.get()))
        ou = 40 * (int(sou.get()))
        pon = 40 * (int(spon.get()))
        poo = 30 * (int(spoo.get()))
        vs = 35 * (int(svs.get()))
        cs = 50 * (int(scs.get()))
        bt = 40 * (int(sbt.get()))
        ps = 60 * (int(sps.get()))
        vp = 70 * (int(svp.get()))
        vcp = 80 * (int(svcp.get()))
        mp = 80 * (int(smp.get()))
        pp = 90 * (int(spp.get()))
        ppz = 80 * (int(sppz.get()))
        ctp = 100 * (int(sctp.get()))
        crp = 110 * (int(scrp.get()))
        ts = 40 * (int(sts.get()))
        ns = 50 * (int(sns.get()))
        cso = 65 * (int(scso.get()))
        ms = 70 * (int(sms.get()))
        ff = 50 * (int(sff.get()))
        mc = 90 * (int(smc.get()))
        cc = 90 * (int(scc.get()))
        p65 = 120 * (int(sp65.get()))
        cg = 130 * (int(scg.get()))
        c65 = 140 * (int(sc65.get()))
        cl = 110 * (int(scl.get()))
        ffy = 120 * (int(sffy.get()))
        cfr = 100 * (int(scfr.get()))
        efr = 90 * (int(sefr.get()))
        mfr = 180 * (int(smfr.get()))
        pr = 70 * (int(spr.get()))
        cr = 40 * (int(scr.get()))
        vb = 80 * (int(svb.get()))
        cb = 120 * (int(scb.get()))
        eb = 100 * (int(seb.get()))
        mb = 130 * (int(smb.get()))
        oj = 30 * (int(soj.get()))
        aj = 40 * (int(saj.get()))
        mfj = 60 * (int(smfj.get()))
        flw = 15 * (int(sflw.get()))
        ss = 30 * (int(sss.get()))
        ven = 20 * (int(sven.get()))
        sb = 25 * (int(ssb.get()))
        chc = 30 * (int(schc.get()))
        bs = 30 * (int(sbs.get()))
        kp = 45 * (int(skp.get()))
        fc = 40 * (int(sfc.get()))
        bc = 30 * (int(sbc.get()))
        cost = (
                tea + cof + mil + mws + idl + sd + pd + md + ou + pon + poo + vs + cs + bt + ps + vp + vcp + mp +
                pp + ppz + ctp + crp + ts + ns + cso + ms + ff + mc + cc + p65 + cg + c65 + cl + ffy + cfr + efr +
                mfr + pr + cr + vb + cb + eb + mb + oj + aj + mfj + flw + ss + ven + sb + chc + bs + kp + fc + bc)

        if cost != "" and cost == 0:
            messagebox.showinfo("Bairava restaurant", "Order something")
        elif cost > 0:
            cost = cost
            sercrgbef = float(cost / 44)
            taxbef = float(cost / 32)
            randbill = random.randint(1234, 9999)
            randbill_str = str(randbill)
            cost_str = ("Rs. " + str(cost))
            totalbef = float(cost + sercrgbef + taxbef)
            print("Cost:", cost)
            print("service Charge: Rs. ", sercrgbef)
            # print("Tax: RS. ",tax)
            print("Taxs:", "Rs. ", str("%.2f" % taxbef))
            sercrgaft = str("%.2f" % sercrgbef)
            sercrg = ("Rs. " + str(sercrgaft))
            tax = ("Rs. " + str("%.2f" % taxbef))
            totals = math.ceil(totalbef)
            total = ("Rs. " + str("%.2f" % totals))
            print("Total: Rs.", total)
            messagebox.showinfo("Your Total cost", total)

            delete_frm()
            frmord = Frame(mfrm)
            frmord.pack()
            frmord1 = Frame(mfrm, bg="#5cdb95")
            frmord1.pack()

            lbl_resh = Label(frmord, text="🍜 Restaurant", fg="orange", bg='#0B0c10', font=('times 30 bold'))
            lbl_resh.pack(padx=0, pady=2, fill=X)
            lbl_ord = Label(frmord, text="ORDER RECEIPT", fg="orange", bg='#0B0c10', font=('times 20 bold'))
            lbl_ord.pack(padx=0, pady=2, fill=X)

            lbl_obill = Label(frmord1, text="Bill NO", width=20, fg="white", bg='#0B0c10', font=('times 15 bold'))
            lbl_obill.grid(row=0, column=0, padx=2, pady=2)
            lbl_ocost = Label(frmord1, text="Cost", width=20, fg="white", bg='#0B0c10', font=('times 15 bold'))
            lbl_ocost.grid(row=1, column=0, padx=2, pady=2)
            lbl_osc = Label(frmord1, text="Service charge", width=20, fg="white", bg='#0B0c10', font=('times 15 bold'))
            lbl_osc.grid(row=2, column=0, padx=2, pady=2)
            lbl_otax = Label(frmord1, text="Tax", width=20, fg="white", bg='#0B0c10', font=('times 15 bold'))
            lbl_otax.grid(row=3, column=0, padx=2, pady=2)
            lbl_ototal = Label(frmord1, text="total", width=20, fg="white", bg='#0B0c10', font=('times 15 bold'))
            lbl_ototal.grid(row=4, column=0, padx=2, pady=2)

            btn_b = Button(frmord1, text="BACK", fg="orange", activebackground="#4056A1",
                           activeforeground="white", width=7, padx=2, pady=2, bg='#802BB1',
                           font=('times 18 bold'),
                           command=back)
            btn_b.grid(row=5, column=0, columnspan=2, padx=2, pady=2)
            # btn_r = Button(frmord1, text="RECORD", fg="orange", activebackground="#4056A1",
            #                    activeforeground="white", width=7, padx=2, pady=2, bg='#802BB1',
            #                    font=('times 18 bold'),
            #                    command=record)
            # btn_r.grid(row=5, column=1, padx=2, pady=2)

            txt_obill = Entry(frmord1, width=20, bg="#C96567", font=('times 15 bold'))
            txt_obill.grid(row=0, column=1)
            txt_obill.insert(0, "%s" % randbill)
            txt_ocost = Entry(frmord1, width=20, bg="#C96567", font=('times 15 bold'))
            txt_ocost.grid(row=1, column=1)
            txt_ocost.insert(0, "Rs. %s" % cost)
            txt_osc = Entry(frmord1, width=20, bg="#C96567", font=('times 15 bold'))
            txt_osc.grid(row=2, column=1)
            txt_osc.insert(0, "Rs. %s" % sercrg)
            txt_otax = Entry(frmord1, width=20, bg="#C96567", font=('times 15 bold'))
            txt_otax.grid(row=3, column=1)
            txt_otax.insert(0, "Rs. %s" % tax)
            txt_ototal = Entry(frmord1, width=20, bg="#C96567", font=('times 15 bold'))
            txt_ototal.grid(row=4, column=1)
            txt_ototal.insert(0, "Rs. %s" % total)

            c = dbc.cursor()
            qry = "INSERT INTO restaurant (Bill_no,Cost,Service_Charge, Tax, Total) VALUES (%s, %s, %s, %s,%s)"
            val = (randbill_str, cost_str, sercrg, tax, total)
            c.execute(qry, val)
            dbc.commit()
            dbc.close()


    def reset():
        restaurant()

    delete_frm()
    frmr = Frame(mfrm)
    frmr.grid(row=0, column=0, columnspan=2)

    listfrm = Frame(mfrm, bg='#5CDB95')
    listfrm.grid(row=1, column=1)
    frmr0 = Frame(listfrm, bg='#5CDB95')
    frmr0.grid(row=0, column=0)
    frmr1 = Frame(listfrm, bg='#5CDB95')
    frmr1.grid(row=0, column=1)
    frmr2 = Frame(listfrm, bg='#5CDB95')
    frmr2.grid(row=0, column=2)
    frmr3 = Frame(listfrm, bg='#5CDB95')
    frmr3.grid(row=0, column=3)

    lbl_resh = Label(frmr, text="🍜 Restaurant", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_resh.pack(padx=0, pady=0, fill=X)
    # menu selection label------------------------------------------------
    lfav = Label(frmr1, text="Your Favourite", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lfav.grid(row=0, column=0, columnspan=2, pady=1)
    ltea = Label(frmr1, text="Tea", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    ltea.grid(row=1, column=0, pady=1)
    lcof = Label(frmr1, text="Coffee", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcof.grid(row=2, column=0, pady=1)
    lmil = Label(frmr1, text="Milk", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmil.grid(row=3, column=0, pady=1)
    # Break fast ---------------------------------------------------------------------
    lbf = Label(frmr1, text="South Indian Breakfast", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lbf.grid(row=4, column=0, columnspan=2, pady=1)
    lmws = Label(frmr1, text="Medu Wada Sambhar", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmws.grid(row=5, column=0, pady=1)
    lidl = Label(frmr1, text="Idli", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lidl.grid(row=6, column=0, pady=1)
    lsd = Label(frmr1, text="Sada Dosa", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lsd.grid(row=7, column=0, pady=1)
    lpd = Label(frmr1, text="Paper Dosa", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lpd.grid(row=8, column=0, pady=1)
    lmd = Label(frmr1, text="Masal Dosa", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmd.grid(row=9, column=0, pady=1)
    lou = Label(frmr1, text="Onion Uttapam", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lou.grid(row=10, column=0, pady=1)
    lpon = Label(frmr1, text="Pongal", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lpon.grid(row=11, column=0, pady=1)
    lpoo = Label(frmr1, text="Poori", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lpoo.grid(row=12, column=0, pady=1)

    # start new label---------------------------------------------------------------------------------------
    lsn = Label(frmr1, text="Start New", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lsn.grid(row=13, column=0, columnspan=2, pady=1)
    lvs = Label(frmr1, text="Veg Sandwich", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lvs.grid(row=14, column=0, pady=1)
    lcs = Label(frmr1, text="Cheese Sandwich", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcs.grid(row=15, column=0, pady=1)
    lbt = Label(frmr1, text="Butter Sandwich", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lbt.grid(row=16, column=0, pady=1)
    lps = Label(frmr1, text="Paneer Sandwich", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lps.grid(row=17, column=0, pady=1)
    # pizza label-------------------------------------------
    lpiz = Label(frmr1, text="Pizza", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lpiz.grid(row=18, column=0, columnspan=2, pady=1)
    lvp = Label(frmr1, text="Veg Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lvp.grid(row=19, column=0, pady=1)
    lvcp = Label(frmr1, text="Veg Cheese Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lvcp.grid(row=20, column=0, pady=1)
    lmp = Label(frmr1, text="Mushroom Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmp.grid(row=21, column=0, pady=1)
    lpp = Label(frmr2, text="Paneer Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lpp.grid(row=0, column=0, pady=1)
    lvpp = Label(frmr2, text="Veg Plain Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lvpp.grid(row=1, column=0, pady=1)
    lctp = Label(frmr2, text="Chicken Tikka Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lctp.grid(row=2, column=0, pady=1)
    lcrp = Label(frmr2, text="Chicken Roast Pizza", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcrp.grid(row=3, column=0, pady=1)
    # soup-------------------------------------------------------------------------------------------
    lsou = Label(frmr2, text="Soup", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lsou.grid(row=4, column=0, columnspan=2, pady=1)
    ltu = Label(frmr2, text="Tomato Soup", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    ltu.grid(row=5, column=0, pady=1)
    lns = Label(frmr2, text="Noodle Soup", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lns.grid(row=6, column=0, pady=1)
    lcso = Label(frmr2, text="Chicken Soup", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcso.grid(row=7, column=0, pady=1)
    lms = Label(frmr2, text="Mutton Soup", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lms.grid(row=8, column=0, pady=1)
    # Veg non-----------------------------------------------------------------
    lveg = Label(frmr2, text="VEG", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lveg.grid(row=9, column=0, columnspan=2, pady=1)
    lff = Label(frmr2, text="French Fries", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lff.grid(row=10, column=0, pady=1)
    lmc = Label(frmr2, text="Mashroom Chilly", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmc.grid(row=11, column=0, pady=1)
    lcc = Label(frmr2, text="Califlower Chilly", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcc.grid(row=12, column=0, pady=1)
    lp65 = Label(frmr2, text="Paneer 65", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lp65.grid(row=13, column=0, pady=1)
    # Nnveg----------------------------------------------------------------------
    lnon = Label(frmr2, text="Non-Veg", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lnon.grid(row=14, column=0, columnspan=2, pady=1)
    lcg = Label(frmr2, text="Chicken Gravy", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcg.grid(row=15, column=0, pady=1)
    lc65 = Label(frmr2, text="Chicken 65", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lc65.grid(row=16, column=0, pady=1)
    lcl = Label(frmr2, text="Chicken Lollypop", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcl.grid(row=17, column=0, pady=1)
    lffy = Label(frmr2, text="Fish Fry", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lffy.grid(row=18, column=0, pady=1)

    # china special-------------------------------------------------------------------------------------------
    lcnr = Label(frmr2, text="Chinies Noodles & Rice", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lcnr.grid(row=19, column=0, columnspan=2, pady=1)
    lcfr = Label(frmr2, text="Chicken Fried N/R", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcfr.grid(row=20, column=0, pady=1)
    lcfr = Label(frmr2, text="Egg Fried N/R", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcfr.grid(row=21, column=0, pady=1)
    lcfr = Label(frmr3, text="Mix Fried N/R", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcfr.grid(row=0, column=0, pady=1)
    # Rice/Briyani-----------------------------------------------------------------------------------------------
    lrb = Label(frmr3, text="Rice/Briyani", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lrb.grid(row=1, column=0, columnspan=2, pady=1)
    lpr = Label(frmr3, text="Plain Rice", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lpr.grid(row=2, column=0, pady=1)
    lcr = Label(frmr3, text="Curd Rice", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcr.grid(row=3, column=0, pady=1)

    lvb = Label(frmr3, text="Veg Briyani", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lvb.grid(row=4, column=0, pady=1)
    lcb = Label(frmr3, text="Chicken Briyani", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lcb.grid(row=5, column=0, pady=1)
    leb = Label(frmr3, text="Egg Briyani", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    leb.grid(row=6, column=0, pady=1)
    lmb = Label(frmr3, text="Mutton Briyani", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmb.grid(row=7, column=0, pady=1)

    # Juices-----------------------------------------------------------------------------------------------
    ljui = Label(frmr3, text="Juices", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    ljui.grid(row=8, column=0, columnspan=2, pady=1)
    loj = Label(frmr3, text="Orange Juice", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    loj.grid(row=9, column=0, pady=1)
    laj = Label(frmr3, text="Apple Juice", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    laj.grid(row=10, column=0, pady=1)
    lmfj = Label(frmr3, text="Mix Fresh Juice", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lmfj.grid(row=11, column=0, pady=1)
    lflw = Label(frmr3, text="Fresh Lime Water", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lflw.grid(row=12, column=0, pady=1)
    lss = Label(frmr3, text="Straberry Shake", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lss.grid(row=13, column=0, pady=1)
    # Ice Cream-----------------------------------------------------------------------------------------------
    lic = Label(frmr3, text="Ice Creams", width=17, bg="#0074E1", fg="white", font=('times 20 bold'))
    lic.grid(row=14, column=0, columnspan=2, pady=1)
    lven = Label(frmr3, text="Venilla", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lven.grid(row=15, column=0, pady=1)
    lsb = Label(frmr3, text="Straw Berry", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lsb.grid(row=16, column=0, pady=1)
    lchc = Label(frmr3, text="Chocolate", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lchc.grid(row=17, column=0, pady=1)
    lbs = Label(frmr3, text="Butter Scotch", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lbs.grid(row=18, column=0, pady=1)
    lkp = Label(frmr3, text="Kesar Pista", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lkp.grid(row=19, column=0, pady=1)
    lfc = Label(frmr3, text="Fruit Cocktail", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lfc.grid(row=20, column=0, pady=1)
    lbc = Label(frmr3, text="Black Cureent", width=17, bg="#F79E02", fg="white", font=('times 20 bold'))
    lbc.grid(row=21, column=0, pady=1)

    # count of mvppu spinbox----------------------------------------------------------------------
    stea = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)  # your favorite
    stea.grid(row=1, column=1, pady=1)
    scof = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scof.grid(row=2, column=1, pady=1)
    smil = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smil.grid(row=3, column=1, pady=1)

    smws = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)  # breakfast
    smws.grid(row=5, column=1, pady=1)
    sidl = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sidl.grid(row=6, column=1, pady=1)
    ssd = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    ssd.grid(row=7, column=1, pady=1)
    spd = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    spd.grid(row=8, column=1, pady=1)
    smd = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smd.grid(row=9, column=1, pady=1)
    sou = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sou.grid(row=10, column=1, pady=1)
    spon = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    spon.grid(row=11, column=1, pady=1)
    spoo = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    spoo.grid(row=12, column=1, pady=1)

    svs = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)  # start new
    svs.grid(row=14, column=1, pady=1)
    scs = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scs.grid(row=15, column=1, pady=1)
    sbt = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sbt.grid(row=16, column=1, pady=1)
    sps = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sps.grid(row=17, column=1, pady=1)

    svp = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)  # pizza
    svp.grid(row=19, column=1, pady=1)
    svcp = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    svcp.grid(row=20, column=1, pady=1)
    smp = Spinbox(frmr1, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smp.grid(row=21, column=1, pady=1)

    # ======================
    spp = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    spp.grid(row=0, column=1, pady=1)
    sppz = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sppz.grid(row=1, column=1, pady=1)
    sctp = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sctp.grid(row=2, column=1, pady=1)
    scrp = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scrp.grid(row=3, column=1, pady=1)

    sts = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)  # soup
    sts.grid(row=5, column=1, pady=1)
    sns = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sns.grid(row=6, column=1, pady=1)
    scso = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scso.grid(row=7, column=1, pady=1)
    sms = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sms.grid(row=8, column=1, pady=1)

    sff = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)  # veg
    sff.grid(row=10, column=1, pady=1)
    smc = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smc.grid(row=11, column=1, pady=1)
    scc = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scc.grid(row=12, column=1, pady=1)
    sp65 = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sp65.grid(row=13, column=1, pady=1)

    scg = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)  # non-veg
    scg.grid(row=15, column=1, pady=1)
    sc65 = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sc65.grid(row=16, column=1, pady=1)
    scl = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scl.grid(row=17, column=1, pady=1)
    sffy = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sffy.grid(row=18, column=1, pady=1)

    scfr = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)  # Chinies Special
    scfr.grid(row=20, column=1, pady=1)
    sefr = Spinbox(frmr2, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sefr.grid(row=21, column=1, pady=1)
    # =======================================
    smfr = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smfr.grid(row=0, column=1, pady=1)

    spr = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)  # rice /briyaini
    spr.grid(row=2, column=1, pady=1)
    scr = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scr.grid(row=3, column=1, pady=1)
    svb = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    svb.grid(row=4, column=1, pady=1)
    scb = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    scb.grid(row=5, column=1, pady=1)
    seb = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    seb.grid(row=6, column=1, pady=1)
    smb = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smb.grid(row=7, column=1, pady=1)

    soj = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)  # juices
    soj.grid(row=9, column=1, pady=1)
    saj = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    saj.grid(row=10, column=1, pady=1)
    smfj = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    smfj.grid(row=11, column=1, pady=1)
    sflw = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sflw.grid(row=12, column=1, pady=1)
    sss = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sss.grid(row=13, column=1, pady=1)

    sven = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)  # ice cream
    sven.grid(row=15, column=1, pady=1)
    ssb = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    ssb.grid(row=16, column=1, pady=1)
    schc = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    schc.grid(row=17, column=1, pady=1)
    sbs = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sbs.grid(row=18, column=1, pady=1)
    skp = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    skp.grid(row=19, column=1, pady=1)
    sfc = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sfc.grid(row=20, column=1, pady=1)
    sbc = Spinbox(frmr3, from_=0, to=20, font=("times", 20, "bold"), width=2)
    sbc.grid(row=21, column=1, pady=1)

    # button for Restaurant---------------------------------------------------------------------------
    btn_price = Button(frmr0, text="PRICE", fg="#0B0C10", activebackground="#4056A1", activeforeground="white", width=7,
                       padx=2, pady=2, bg='#802BB1', font=('times 18 bold'),
                       command=prices)
    btn_price.grid(row=0, column=0)
    btn_reset = Button(frmr0, text="RESET", fg="#0B0C10", activebackground="#4056A1", activeforeground="white", width=7,
                       padx=2, pady=2, bg='#802BB1', font=('times 18 bold'), command=reset)
    btn_reset.grid(row=1, column=0)
    # btn_reset = Button(frmr0, text="RECORD", fg="#0B0C10", activebackground="#4056A1",activeforeground="white",width=7, padx=2, pady=2, bg='#802BB1', font=('times 18 bold'),command=record)
    # btn_reset.grid(row=2, column=0)
    btn_total = Button(frmr0, text="TOTAL", fg="#0B0C10", activebackground="#4056A1", activeforeground="white", width=7,
                       padx=2, pady=2, bg='#802BB1', font=('times 18 bold'),
                       command=myspinbox)
    btn_total.grid(row=2, column=0)


def rooms():
    delete_frm()

    lbl_room = Label(mfrm, text="✭ ROOMS", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_room.pack(padx=0, pady=0, fill=X)


def partyhall():
    delete_frm()

    lbl_par = Label(mfrm, text="〠 PARTY HALL", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_par.pack(padx=0, pady=0, fill=X)

    frmimg = Frame(mfrm, bg="red")
    frmimg.pack()

    imagee = Image.open("C:/Users/Kishore/Desktop/PROJECT/OO5.jpg")
    re_size = imagee.resize((300, 150))
    cnvrt_imag = ImageTk.PhotoImage(re_size)
    lbl_img = Label(frmimg, image=cnvrt_imag, width=300, height=150)
    lbl_img.pack()


def emi():
    delete_frm()

    lbl_emi = Label(mfrm, text="∓ EMI", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_emi.pack(padx=0, pady=0, fill=X)


def about():
    delete_frm()

    lbl_abo = Label(mfrm, text="☃ ABOUT", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_abo.pack(padx=0, pady=0, fill=X)

    wcm_lbl = Label(mfrm, text="Our Special Services", bg="#0B0c10", fg="#3500D3", font=("broadway 25 bold"))
    wcm_lbl.pack(padx=0, pady=1, fill=X)

    lbl_eat = Label(mfrm, text="🍴 Eat - Order Health | We Cook 24/7 ", fg="#8EE4AF", bg='#0B0c10', font=("times",20 , "bold"))
    lbl_eat.pack(padx=0, pady=0, fill=X)
    lbl_sleep = Label(mfrm, text="🛌 Sleep - Sleep Peace | Room Delivery Food ", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_sleep.pack(padx=0, pady=0, fill=X)
    lbl_party = Label(mfrm, text="🎼 Party - Room Capacity of 150 | With Dj", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_party.pack(padx=0, pady=0, fill=X)
    wcm_lbl = Label(mfrm, text='“There is no love sincerer than the love of food, sleep and music”', bg="#0B0c10", fg="#C3073F", font=("times 18 bold"))
    wcm_lbl.pack(padx=0, pady=1, fill=X)


def contact():
    delete_frm()
    lbl_con = Label(mfrm, text="⇲ CONTACT", fg="orange", bg='#0B0c10', font=('times 30 bold'))
    lbl_con.pack(padx=0, pady=0, fill=X)

    wcm_lbl = Label(mfrm, text="Reach here for Food, Rest, Music", bg="#0B0c10", fg="#3500D3", font=("broadway 21 bold"))
    wcm_lbl.pack(padx=0, pady=1, fill=X)

    lbl_eat = Label(mfrm, text="P.T Rajan Salai,", fg="#8EE4AF", bg='#0B0c10', font=("times",20 , "bold"))
    lbl_eat.pack(padx=0, pady=0, fill=X)
    lbl_sleep = Label(mfrm, text="K.K Nagar", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_sleep.pack(padx=0, pady=0, fill=X)
    lbl_party = Label(mfrm, text="Chennai- 600 078", fg="#8EE4AF", bg='#0B0c10', font=("times", 20, "bold"))
    lbl_party.pack(padx=0, pady=0, fill=X)
    wcm_lbl = Label(mfrm, text='📱: +91 89406 55130', bg="#0B0c10", fg="#C3073F", font=("times 18 bold"))
    wcm_lbl.pack(padx=0, pady=1, fill=X)


# frames-----------------------------------------------------------------------------------------------------
frm0 = Frame(overfrm, bg="#C5C6C7")
frm0.pack(padx=15, pady=20, fill=X)
frm1 = Frame(overfrm, bg="#0B0c10")
frm1.pack(padx=20, pady=20, fill=X)
mfrm = Frame(overfrm, highlightcolor='black', highlightthickness=2, bg="#5cdb95")
mfrm.pack(pady=50)
# Heading label--------------------------------------------------------------------------------------------
lbl_bairava = Label(frm0, text="BAIRAVA RESTAURANT", fg="#66FCF1", bg='#0B0C10', font=('times 30 bold'),
                    bd=10)
lbl_bairava.pack(padx=1, pady=5, fill=X)
# first view------------------------------------------------------------------------------------------
wcm_lbl = Label(mfrm, text="Taste\n            your\n          Toungh",
                bg="#66FCF1", fg="#0B0C10", font=("broadway 40 bold"))
wcm_lbl.grid(row=0, column=0, sticky=E)
wcm_lbl1 = Label(mfrm, text="௹..", bg="#66FCF1", fg="#0B0C10", font=("broadway 60 bold"))
wcm_lbl1.grid(row=0, column=0, sticky=W)
# button font-----------------------------------------------------------------------------------------
btn_font = Font(family="Helvetica", size=12, weight="bold")
# buttons in frame (frm1)------------------------------------------------------------------------------
btn_res = Button(frm1, text="HOME", padx=5, pady=5, width=15, bg='#5CDB95', fg="#05386B", bd=0,
                 activebackground="#379683", font=btn_font, command=home)
btn_res.grid(row=0, column=0, padx=5)
btn_res = Button(frm1, text="RESTAURANT", padx=5, pady=5, width=15, bg='#5CDB95', fg="#05386B", bd=0,
                 activebackground="#379683", font=btn_font, command=restaurant)
btn_res.grid(row=0, column=1, padx=15)
btn_roo = Button(frm1, text="MENU", padx=5, pady=5, width=15, bg='#5CDB95', fg="#05386B", bd=0,
                 activebackground="#379683", font=btn_font, command=prices)
btn_roo.grid(row=0, column=2, padx=15)


btn_abo = Button(frm1, text="ABOUT", padx=5, pady=5, width=15, bg='#5CDB95', fg="#05386B", bd=0,
                 activebackground="#379683", font=btn_font, command=about)
btn_abo.grid(row=0, column=5, padx=15)
btncon = Button(frm1, text="CONTACT", padx=5, pady=5, width=15, bg='#5CDB95', fg="#05386B", bd=0,
                activebackground="#379683", font=btn_font, command=contact)
btncon.grid(row=0, column=6, padx=15)

win.mainloop()
