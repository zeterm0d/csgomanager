from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
import re
from ttkthemes import ThemedTk
import time
from tkinter import filedialog
import shutil
import random
import os
import logging
import webbrowser

logging.basicConfig(filename='logs.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)



try:
    ggtime, cctime, bks, stater  = 0, 0, 0, ""
    
    #Panorama Switcher
    def panoraman():
        flag = ''
        try:
            if eget:
                pass
        except:
            NameError
            if NameError:
                messagebox.showerror("CSGO Manager", "CSGO folder not found. Check the path and try again.")
                flag = 'no'
        if flag != 'no': 
            print("Panoraman:")
            global A, B, C
            A, B, C = '', '', ''
            k = '''
            Some help...
            '''
            def opnr1():
                global checkform, A, flag2
                try:
                    flag2 = True
                    print("Function: opnr1...")
                    A = root.directory = filedialog.askopenfilename()
                    checkform = re.findall(r"\.\S*", A)
                    if checkform[0] != '.webm':
                        messagebox.showerror("Panorama switcher","Invalid file type. Please chooose .webm file.")
                        flag2 = False
                        A = ''
                except:
                    pass

            def opnr2():
                print("Function: opnr2...")
                global checkform, B, flag3
                try:
                    flag3 = True
                    B = root.directory = filedialog.askopenfilename()
                    checkform = re.findall(r"\.\S*", B)
                    if checkform[0] != '.webm':
                        messagebox.showerror("Panorama switcher","Invalid file type. Please chooose .webm file.")
                        flag3 = False
                        B = ''
                except:
                    pass

            def opnr3():
                print("Function: opnr3...")
                global checkform, C, flag4
                try:
                    flag4 = True
                    C = root.directory = filedialog.askopenfilename()
                    checkform = re.findall(r"\.\S*", C)
                    if checkform[0] != '.webm':
                        messagebox.showerror("Panorama switcher","Invalid file type. Please chooose .webm file.")
                        flag4 = False
                        C = ''
                except:
                    pass

            def changer():
                try:
                    if flag2 == True and flag3 == True and flag4 == True:
                        print("Function: changer...")
                        global A,B,C, egetp
                        if A != '' and B != '' and C != '':
                            egetp = eget + r'\panorama\videos'

                            shutil.copy2(A, egetp)
                            nameA = re.findall("/\S*\.webm", A)
                            nameA = nameA[0]
                            nameA.replace('/', '\\')
                            os.remove(egetp + r'\sirocco_night.webm')
                            os.rename(egetp+nameA, egetp + r'\sirocco_night.webm')

                            shutil.copy2(B, egetp)
                            nameB = re.findall("/\S*\.webm", B)
                            nameB = nameB[0]
                            nameB.replace('/', '\\')
                            os.remove(egetp + r'\sirocco_night540p.webm')
                            os.rename(egetp+nameB, egetp + r'\sirocco_night540p.webm')

                            shutil.copy2(C, egetp)
                            nameC = re.findall("/\S*\.webm", C)
                            nameC = nameC[0]
                            nameC.replace('/', '\\')
                            os.remove(egetp + r'\sirocco_night720p.webm')
                            os.rename(egetp+nameC, egetp + r'\sirocco_night720p.webm')

                            messagebox.showinfo("Panorama switcher","Successfully!")
                        else:
                            messagebox.showerror("Panorama switcher", "Please select all three panorama files of correct file type.")
                    else:
                        messagebox.showerror("Panorama switcher", "Please select all three panorama files of .webm file type.")
                except:
                    messagebox.showerror("Panorama switcher", "Please select all three panorama files of correct file type.")
            def helper():
                print("Function: helper...")
                messagebox.showinfo("Panorama switcher",k)

            def restores():
                print("Function: restores...")
                try:
                    egetp = eget + r'\panorama\videos'
                    shutil.copy2("files/sirocco_night.webm", egetp)
                    shutil.copy2("files/sirocco_night540p.webm",egetp)
                    shutil.copy2("files/sirocco_night720p.webm",egetp)
                    messagebox.showinfo("Panorama switcher","Successfully restored!")
                except:
                    FileNotFoundError
                    if FileNotFoundError:
                        messagebox.showerror("Panorama switcher", "I can't find some files... Please try to open me in default folder.(You need to use the last release of CSGO Manager.)")
            for widget in root.winfo_children():
                widget.destroy()

            def bef():
                print("Function: bef...")
                global e
                bt1 = ttk.Button(root, text='1 File', command=opnr1)
                bt1.place(x=312, y=27)
                bt2 = ttk.Button(root, text='2 File',command=opnr2)
                bt2.place(x=312, y=67)
                bt3 = ttk.Button(root, text='3 File',command=opnr3)
                bt3.place(x=312, y=107)
                bt4 = ttk.Button(root, text='Change', command=changer)
                bt4.place(x=230, y=180)
                bt5 = ttk.Button(root, text='Restore to default', command=restores)
                bt5.place(x=80, y=180)
                bt6 = ttk.Button(root, text='Help',command=helper)
                bt6.place(x=10, y=220)
                btback = ttk.Button(root, text="<", command=back, width=2)
                btback.place(x=0, y=0)
                #e = ttk.Entry(root, width=12)
                #.place(x=312, y=120)
                #thetext= r"C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\panorama\videos"
                #e.insert(END, thetext)
                textp = Text(root, width=31, height=7, relief="flat")
                textp.place(x=45, y=30)
                textp.insert(END, "This is csgo panorama manager. It might help you to set wallpaper of csgo.")
                textp.insert(END, " Choose 3 files of panorama, and the path of your panorama files.")
                textp.insert(END, "(You can try to launch with default.)")
                textp.config(state=DISABLED)
            bef()

            
    def seteget():
        print("Function seteget...")
        global eget, flag, ggtime
        flag =  'yes'
        try:
            open(e2.get() + r'\scripts\items\items_game.txt')
        except:
            FileNotFoundError
            if FileNotFoundError:
                messagebox.showerror("CSGO Manager", "Maybe some files of your csgo are broken. Try to restore your csgo files or check the path to your csgo and try again.")
                flag = 'no'
        if flag != 'no':
            messagebox.showinfo("CSGO Manager", "Path has been set.")
            eget = e2.get()
            copypath = eget + r'\scripts\items\items_game.txt'
            if ggtime == 0:
                shutil.copy2(copypath, r"files/")
                ggtime +=1
            

#Widget manager
    def widgetman():
        global onetime
        onetime = 0
        def sete3get():
            global ec3get, flagr
            flagr = ''
            try:
                ec3get = ec3.get()
            except:
                NameError
                if NameError:
                    messagebox.showerror("Widget manager", "Please enter what you want to search.")
                    flagr = 'no'
            if flagr != 'no':
                if ec3get != '':
                    if len(ec3get) >=3:
                        try:
                            gtext.delete('1.0', END)
                        except:
                            pass
                        widshow()
                    else:
                        messagebox.showerror("Widget manager", "The argument is too short. Try word at least with 3 characters.")
                else:
                    messagebox.showerror("Widget manager", "You didn't write anything.")
            
            
        def widshow():
            global dictiong, keys2, valuess2, btc7, allstrokes, keys2def, valuess2def, combb, cctime,  plus, bks, cs
            allstrokes = []
            print("Function widshow..")

            plus =  eget + r"\resource" + "\\"
            plus = plus + "csgo_" + lang + '.txt'

            plus2 = "files/" + "csgo_" + lang + '.txt'
            try:
                open(plus2, "r")
                print("Widget backup had been already created.")
                cctime = 1
            except:
                pass

            if cctime == 0:
                shutil.copy2(plus, "files/")
                print("Widget backup created.")
                cctime +=1
            
                
            with open(plus, "r", encoding="utf-16") as c:
                cs = c.readlines()
                dictiong = {}
                for i in cs:
                    if ec3get in i:
                            keyg = re.search('"\S*"', i)
                            if keyg:
                                keyg = keyg[0]
                                changeg = i[len(keyg)+1:]
                                mentiong = re.search('"\D*"', changeg)
                                if mentiong:
                                    mentiong = mentiong[0]
                                    allstrokes.append(i)
                            if mentiong and keyg:
                                dictiong[keyg] = mentiong
                if dictiong:
                    pass
                else:
                    messagebox.showerror("Widget manager", "I didn't find anything :(")
                
                keys2, valuess2 = [], []
                for key in dictiong.keys():
                    keys2.append(key)
                for value in dictiong.values():
                    valuess2.append(value)

                    btc7 = ttk.Button(root, text="Choose: ", width=8, command=showpar)
                    btc7.place(x=42, y=48)
                    combbs.destroy()
                    combb = ttk.Combobox(root, width=50, values=keys2)
                    combb.place(x=120,y=50)
                
                
        def widchange():
            print("Function widchange...")
            global whrepl, wiwhrepl, realwhrepl, x, creadl, xstr, gkav, valuess2, keys2,cs85, dictiong
            for i in allstrokes:
                if keys2[mainnum] in i and valuess2[mainnum] in i:
                    whrepl = i
                    
            otst = re.search('"\S*"', whrepl)
            otst = otst[0]

            wiwhrepl = re.search('"\D*"', whrepl[len(otst):])
            wiwhrepl = wiwhrepl[0]

            gkav = gtext.get("1.0", END).replace("\t", "").replace("\n", "")
            gkav  = '"' + gkav + '"'
            realwhrepl = whrepl.replace(wiwhrepl, gkav)


            with open(plus, "r", encoding="utf16") as c1:
                creadl = c1.readlines()
                for i in creadl:
                    if whrepl in i:
                        xstr = i.replace("\n", "")

            with open(plus, "w", encoding="utf16") as c2:
                    for i in creadl:
                        global valforval
                        if xstr in i:  
                            i = realwhrepl
                            valforval = i
                        c2.write(i)
                    messagebox.showinfo("Widget manager", "Sucessfully changed!")
            
            with open(plus, "r", encoding="utf-16") as c:
                cs85 = c.readlines()
                dictiong = {}
                for i in cs85:
                    if ec3get in i:
                            keyg = re.search('"\S*"', i)
                            if keyg:
                                keyg = keyg[0]
                                changeg = i[len(keyg)+1:]
                                mentiong = re.search('"\D*"', changeg)
                                if mentiong:
                                    mentiong = mentiong[0]
                                    allstrokes.append(i)
                            if mentiong and keyg:
                                dictiong[keyg] = mentiong
                
                keys2, valuess2 = [], []
                for key in dictiong.keys():
                    keys2.append(key)
                for value in dictiong.values():
                    valuess2.append(value)


        def showpar():
            global mainnum, gtext, cmb, mainstr
            if combb.get != '':
                print("Function: showpar...")
                flagg = 'no'
                inum = 0
                cmb = combb.get()
                for i in keys2:
                    if cmb == i:
                        mainnum = inum
                        flagg = 'yes'
                    inum +=1
                if flagg == 'yes':
                    gtext.delete(1.0,END)
                    mainstr = valuess2[mainnum].replace('"','')
                    #mainstr.replace('\n', '')
                    gtext.insert(END, mainstr)
                    
                else:
                    messagebox.showerror("Widget manager", "You didn't choose what you want to change.")
            else:
                messagebox.showerror("Widget manager", "You didn't write anything.")
            
        def befwidgetman():
            print("Function widgetman...")
            global cctime, plus
            flag = ''
            try:
                if eget:
                    pass    
            except:
                NameError
                if NameError:
                    messagebox.showerror("CSGO Manager", "CSGO folder not found. Check the path and try again.")
                    flag = 'no'
            if flag != 'no':
                global Languages, photogit, photovk, photoyoutube, photoweap, photowallp, photowidg
                for widget in root.winfo_children():
                    widget.destroy()
                photoweap = PhotoImage(file = r"files\photoweap.png")
                photowallp = PhotoImage(file = r"files\photowallp.png")
                photowidg = PhotoImage(file = r"files\photowidg.png")
                

                #bta =  ttk.Button(root, text='Weapon manager', command=beforehand)
                #bta.place(x=0, y=0)
                bta =  ttk.Button(root, image=photoweap, command=beforehand)
                bta.place(x=0, y=0, width=60, height=35)
                btb =  ttk.Button(root, image=photowallp, command=panoraman)
                btb.place(x=65, y=0,width=46, height=35)
                btc =  ttk.Button(root, image=photowidg, command=widgetman)
                btc.place(x=115, y=0,width=46, height=35)
        
               
                btc1 = ttk.Button(root, text='OK',  command=widgetmain)
                btc1.place(x=450, y=46)
                btc2 = ttk.Button(root, text='Help', command=infowid)
                btc2.place(x=10, y=46)
                Languages = ttk.Combobox(root, values=['english', 'russian'], width=10)
                Languages.place(x=350,y=47)
            


        def infowid():
            pass


        
        def restwid():
            print("Function restwid...")
            global dictiong, valuess2, keys2
            try:
                dictiong = {}
                for i in cs:
                    if ec3get in i:
                        keyg = re.search('"\S*"', i)
                        if keyg:
                            keyg = keyg[0]
                            changeg = i[len(keyg)+1:]
                            mentiong = re.search('"\D*"', changeg)
                            if mentiong:
                                mentiong = mentiong[0]
                                allstrokes.append(i)
                                if mentiong and keyg:
                                    dictiong[keyg] = mentiong

                keys2, valuess2 = [], []
                for key in dictiong.keys():
                    keys2.append(key)
                for value in dictiong.values():
                    valuess2.append(value)
                namt = 'files/csgo_' + lang + '.txt'

                shutil.copy2(namt, plus)
                messagebox.showinfo("Widget manager", "Successfully restored.")
            except:
                messagebox.showinfo("Widget manager.", "Nothing to restore.")
            


        def widgetmain():
            print("Function widgetmain...")
            global allnice, lang, plus, ec3, gtext, onetime, combbs, cctime
            lang = Languages.get()
            
            allnice = ''
            valoflan = ['english', 'russian']
            for i in valoflan:
                if lang in valoflan:
                    allnice = 'ok'
            if allnice == 'ok':
                for widget in root.winfo_children():
                    widget.destroy() 
                #→
                btc3 = ttk.Button(root, text="Find:", width=5, command=sete3get)
                btc3.place(x=40, y=228)
                btc4 = ttk.Button(root, text="Change", command=widchange)
                btc4.place(x=390, y=230)
                btc5 = ttk.Button(root, text="Restore to default", command=restwid)
                btc5.place(x=240, y=230)
                btc6 = ttk.Button(root, text="<", command=back, width=2)
                btc6.place(x=0, y=0)
                ec3 = ttk.Entry(root, width=12)
                ec3.place(x=100, y=230)
                gtext = Text(root, width=50, height=7, relief="flat")
                gtext.place(x=50, y=90)
                combbs = ttk.Combobox(root, width=50)
                combbs.place(x=120,y=50)
            else:
                messagebox.showerror("Widget manager", "You didn't choose the language.")
        befwidgetman()
        

    def redirectgit():
        webbrowser.open('https://github.com/zeterm0d/csgomanager') 

    def redirectvk():
        webbrowser.open('https://vk.com/sointerestingperson') 

    def redirectyoutube():
        webbrowser.open('https://www.youtube.com/channel/UCzt_LknuF3hdIDmE7sg8MjA')
    
    def hellowind():
        print("Function: hellowind...")

        
        global texter, bta, btb, yp, e2, text5, egetm,  eget, btok, timert, photogit, photovk, photoyoutube,  photoweap, photowallp, photowidg

        photogit = PhotoImage(file = r"files\githublog.png")
        photovk = PhotoImage(file = r"files\vklog.png")
        photoyoutube = PhotoImage(file = r"files\youtubelog.png")
        photoweap = PhotoImage(file = r"files\photoweap.png")
        photowallp = PhotoImage(file = r"files\photowallp.png")
        photowidg = PhotoImage(file = r"files\photowidg.png")

        timert = 0
        texter = Text(root, width=52, height=9, relief="flat")
        texter.place(x=50, y=50)
        texter.insert("1.0","Hey! ⚙This is csgo manager.                       This programm help you to manage your csgo.\n")
        texter.insert(END,"Choose the option what you want, in buttons bellow.\n")
        texter.insert(END,"\n1. Weapon manager can change the damage, range,\nspread and many others specifications of guns. \n")
        texter.insert(END,"2. Panorama switcher, switch the wallpaper of csgo.\n")
        texter.insert(END,"3. Widget manager can change the names of different game modes and many other interesting labels.")
        

        #bta =  ttk.Button(root, text='Weapon manager', command=beforehand)
        #bta.place(x=0, y=0)
        bta =  ttk.Button(root, image=photoweap, command=beforehand)
        bta.place(x=0, y=0, width=60, height=35)
        btb =  ttk.Button(root, image=photowallp, command=panoraman)
        btb.place(x=65, y=0,width=46, height=35)
        btc =  ttk.Button(root, image=photowidg, command=widgetman)
        btc.place(x=115, y=0,width=46, height=35)
        
        btgit = Button(root, text="", command=redirectgit, image=photogit, width=16, relief="flat", height=16, bg="white")
        btgit.place(x=525, y=275)
        btvk = Button(root, text="", command=redirectvk, image=photovk, width=16, relief="flat", height=16, bg="white")
        btvk.place(x=500, y=275)
        btyt = Button(root, text="git", command=redirectyoutube, image=photoyoutube, width=16, relief="flat", height=16, bg="white")
        btyt.place(x=475, y=275)

        yp = ''
        e2 = ttk.Entry(root, width=12)
        e2.place(x=340, y=211)
        e2.insert(END, 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo')
        btok =  ttk.Button(root, text='OK', command=seteget, width=3)
        btok.place(x=430, y=210)
        text5 = Text(root, width=25, height=1, relief="flat")
        text5.place(x=50, y=210)
        text5.insert("1.0","Path to your csgo files.")
        




 #Weapon manager
    def info():
        print("Function: info...")
        helptext = '''
        Some helptext......
        '''
        messagebox.showinfo("Weapon Manager", helptext)



    def main():
        print("Function: main...")
        global CE, CEI, diction, keys, bt3, bt4, bt5, bt6, yptext, yp, valuess, witp, valofyp, alright, ggtime5, descnum, valuess, b

        alright = ''
        yp = CE.get()
        valofyp=['Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'CZ75', 'P250', 'P2000', 'Revolver R8', 'Tec-9', 'USP-S',
            'MP5-SD', 'MAC-10', 'P90', 'UMP-45', 'MP7', 'MP9', 'PP-19 Bison', 'XM1014', 'MAG-7', 'Nova', 'Sawed-Off', 'AUG', 'SG 556',
            'AK-47', 'M4A4', 'M4A1', 'FAMAS', 'Galil AR',
            'AWP', 'SCAR-20', 'G3SG1', 'SSG 08', 'M249', 'Negev', 'Hegrenade', 'Molotov', 'Incendiary grenade', 'Fake grenade', 'Snowball', 'Smoke grenade',
            'Zeus',  'C4', 'Knife','Tablet', 'Fists', 'Healthshot', 'Bumpine', 'Breachcharge', 'Shield', 'Cutters', 'Defuser']
        for i in valofyp:
            if yp != '':
                if yp in i:
                    alright = 'ok'
        if alright != 'ok':
            messagebox.showerror("Weapon manager", "You didn't choose the weapon.")
        else:
            for widget in root.winfo_children():
                widget.destroy()    
            with open(witp, "r", encoding="utf8") as f:
                b = f.readlines()
                diction = {}
                for i in b:
                    if yp in i:
                        key = re.search('"\D*"', i)
                        if key:
                            key = key[0]
                            change = i[len(key)+1:]
                            mention = re.search('"\S*"', change)
                        if mention and key:
                            mention = mention[0]
                            key = key.replace("\t", "").replace('"', "")
                            mention = mention.replace("\t", "").replace('"', "")
                            diction[key] = mention

                keys, valuess = [], []
                for key in diction.keys():
                    keys.append(key)
                for value in diction.values():
                    valuess.append(value)

            
                
                CEI = ttk.Combobox(root, values=keys, width=25)
                CEI.place(x=90,y=55)

                bt3 = ttk.Button(root, text="→", command=launchsearch, width=2)
                bt3.place(x=45, y=53)

                bt4 = ttk.Button(root, text="Change", command=changing)
                bt4.place(x=195, y=100)

                bt5 = ttk.Button(root, text="Restore to default", command=restore)
                bt5.place(x=35, y=100)

                bt6 = ttk.Button(root, text="<", command=back, width=2)
                bt6.place(x=0, y=0)

                yptext = Text(root, width=21, height=1, relief="flat")
                yptext.place(x=45, y=10)
                ypvar = yp + " options:"
                yptext.insert('1.0', ypvar)
                yptext.config(state=DISABLED)

        
        

    def launchsearch():
        print("Function: launchsearch...")
        global text
        try:
            text.delete(0, END)
        except:
            NameError
        text = Text(root, width=4, height=1, relief="flat")
        text.place(x=280, y=57)
        for i in range(len(keys)):
            if re.fullmatch(CEI.get(), keys[i]) !=  None:
                text.insert('1.0', valuess[i])
                
            
                
    def restore():
        global diction, keys, valuess
        print("Function: restore...")
        diction = {}
        for i in b:
            if yp in i:
                key = re.search('"\D*"', i)
                if key:
                    key = key[0]
                    change = i[len(key)+1:]
                    mention = re.search('"\S*"', change)
                    if mention and key:
                        mention = mention[0]
                        key = key.replace("\t", "").replace('"', "")
                        mention = mention.replace("\t", "").replace('"', "")
                        diction[key] = mention
        shutil.copy2('files/items_game.txt',  witp)
        messagebox.showinfo("Weapon manager", "Sucessfully restored.")

        keys, valuess = [], []
        for key in diction.keys():
            keys.append(key)
        for value in diction.values():
            valuess.append(value)


    def changing():
        print("Function: changing...")
        trigger, trigger2 = 'no', 'no'

        for i in keys:
            if i in CEI.get():
                trigger = 'yes'
        if trigger == 'no':
            messagebox.showerror("Weapon manager", "You didn't choose the parameter what you want to change.")
        try:
            if text:
                trigger2 = 'yes'
        except:
            NameError
            if NameError:
                trigger2 = 'no'

        if trigger == 'yes' and trigger2 == 'yes':
            global repl_stroke, new_repl_stroke, b, getin, tim 
            tim = 0
            with open(witp, "r", encoding="utf8") as f1:
                b = f1.readlines()
                for i in b:
                    getin = '"' + CEI.get() + '"'
                    if getin in i:
                        if yp in i:
                            repl_stroke = i

                ots = re.findall('"\S*"', repl_stroke)
                whatreaplce = re.findall('"\S*"', repl_stroke[len(ots[0])+1:])
                whatreaplce = whatreaplce[0]


                textget = text.get(1.0,END)
                ntextget = re.findall('\S*', textget)
                ntextget = ntextget[0]
                ntextget = '"' + ntextget + '"'


                new_repl_stroke = repl_stroke.replace(whatreaplce, ntextget)
            
            with open(witp, "w", encoding="utf8") as f2:
                for i in b:
                    if repl_stroke in i:
                        i = new_repl_stroke
                    f2.write(i) 
                messagebox.showinfo("Weapon manager", "Sucessfully changed!")
                
                for i in keys:
                    i = '"' + i + '"'
                    if getin in i:
                        ntextget = ntextget[1:len(ntextget)-1]
                        valuess[tim] = ntextget
                        
                    tim +=1
        elif trigger == 'yes' and trigger2 == 'no':
            messagebox.showerror("Weapon manager", "You didn't choose the number to what you want to change. Put → and write mention what you want.")


    def back():
        print("Function: back...")
        global texter, photo1, text5, e2, btok, eget, photogit, photovk, photoyoutube, photoweap, photowallp, photowidg

        for widget in root.winfo_children():
            widget.destroy()
        photogit = PhotoImage(file = r"files\githublog.png")
        photovk = PhotoImage(file = r"files\vklog.png")
        photoyoutube = PhotoImage(file = r"files\youtubelog.png")
        photoweap = PhotoImage(file = r"files\photoweap.png")
        photowallp = PhotoImage(file = r"files\photowallp.png")
        photowidg = PhotoImage(file = r"files\photowidg.png")

        timert = 0
        texter = Text(root, width=52, height=9, relief="flat")
        texter.place(x=50, y=50)
        texter.insert("1.0","Hey! ⚙This is csgo manager.                       This programm help you to manage your csgo.\n")
        texter.insert(END,"Choose the option what you want, in buttons bellow.\n")
        texter.insert(END,"\n1. Weapon manager can change the damage, range,\nspread and many others specifications of guns. \n")
        texter.insert(END,"2. Panorama switcher, switch the wallpaper of csgo.\n")
        texter.insert(END,"3. Widget manager can change the names of different game modes and many other interesting labels.")
        

        #bta =  ttk.Button(root, text='Weapon manager', command=beforehand)
        #bta.place(x=0, y=0)
        bta =  ttk.Button(root, image=photoweap, command=beforehand)
        bta.place(x=0, y=0, width=60, height=35)
        btb =  ttk.Button(root, image=photowallp, command=panoraman)
        btb.place(x=65, y=0,width=46, height=35)
        btc =  ttk.Button(root, image=photowidg, command=widgetman)
        btc.place(x=115, y=0,width=46, height=35)
        
        btgit = Button(root, text="", command=redirectgit, image=photogit, width=16, relief="flat", height=16, bg="white")
        btgit.place(x=525, y=275)
        btvk = Button(root, text="", command=redirectvk, image=photovk, width=16, relief="flat", height=16, bg="white")
        btvk.place(x=500, y=275)
        btyt = Button(root, text="git", command=redirectyoutube, image=photoyoutube, width=16, relief="flat", height=16, bg="white")
        btyt.place(x=475, y=275)

        yp = ''
        e2 = ttk.Entry(root, width=12)
        e2.place(x=340, y=211)
        e2.insert(END, 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo')
        btok =  ttk.Button(root, text='OK', command=seteget, width=3)
        btok.place(x=430, y=210)
        text5 = Text(root, width=25, height=1, relief="flat")
        text5.place(x=50, y=210)
        text5.insert("1.0","Path to your csgo files.")
        try:
            e2.insert(0, eget)
        except:
            NameError
            if NameError:
                e2.insert(0, 'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo')

    def beforehand():
        global flag
        flag = ''
        try:
            if eget:
                pass
        except:
            NameError
            if NameError:
                messagebox.showerror("CSGO Manager", "CSGO folder not found. Check the path and try again.")
                flag = 'no'
        if flag != 'no': 
            print("Function: beforehand...")
            for widget in root.winfo_children():
                widget.destroy()
            global bt1, bt2, CE, witp, photowidg, photoweap, photowallp
            witp = eget + '\scripts\items\items_game.txt'
            

            bta =  ttk.Button(root, image=photoweap, command=beforehand)
            bta.place(x=0, y=0, width=60, height=35)
            btb =  ttk.Button(root, image=photowallp, command=panoraman)
            btb.place(x=65, y=0,width=46, height=35)
            btc =  ttk.Button(root, image=photowidg, command=widgetman)
            btc.place(x=115, y=0,width=46, height=35)
            bt1 = ttk.Button(root, text='OK',  command=main)
            bt1.place(x=450, y=46)
            bt2 = ttk.Button(root, text='Help', command=info)
            bt2.place(x=10, y=46)
            CE = ttk.Combobox(root, values=['Desert Eagle', 'Dual Berettas', 'Five-SeveN', 'Glock-18', 'CZ75', 'P250', 'P2000', 'Revolver R8', 'Tec-9', 'USP-S',
            'MP5-SD', 'MAC-10', 'P90', 'UMP-45', 'MP7', 'MP9', 'PP-19 Bison', 'XM1014', 'MAG-7', 'Nova', 'Sawed-Off', 'AUG', 'SG 556',
            'AK-47', 'M4A4', 'M4A1', 'FAMAS', 'Galil AR',
            'AWP', 'SCAR-20', 'G3SG1', 'SSG 08', 'M249', 'Negev', 'Hegrenade', 'Molotov', 'Incendiary grenade', 'Fake grenade', 'Snowball', 'Smoke grenade',
            'Zeus',  'C4', 'Knife','Tablet', 'Fists', 'Healthshot', 'Bumpine', 'Breachcharge', 'Shield', 'Cutters', 'Defuser'])
            CE.place(x=300,y=47)
            os.remove(witp)
            witp2 = eget + '\scripts\items'
            shutil.copy2('files\items_modiflied.txt',  witp2)
            witp3 = eget + '\scripts\items\items_modiflied.txt'
            os.rename(witp3, witp)
            print("File copied.")
              
        
    root = ThemedTk(theme="arc")
    root.title("CSGO Manager")
    root.resizable(False, False)
    root.geometry("550x300")
    root.iconbitmap('files/ks.ico')
    hellowind()




    root.mainloop()

except Exception as err:
    messagebox.showerror("CSGO Manager", "Something went wrong... Try to reinstall the program. If it anyway doesn't work  write message with your logs file.")
    logger.error(err)