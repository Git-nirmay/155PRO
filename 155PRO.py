from tkinter import *

root=Tk()
root.title("Doujusu used by Naruto/Boruto Charecters")
root.geometry("600x400")

labelofMadara=Label(root)
labelofSasuke=Label(root)
labelofObito=Label(root)
dictionary={"Madara":"1 Tomoe Sharingan,3 Tomoe Sharigan,Magekyo Sharingan,Eternal Magekyo Sharingan,Rinnegan,RinneSharingan",
            "Sasuke":"1 Tomoe Sharingan,2 Tomoe Sharingan,3 Tomoe Sharigan,Magekyo Sharingan,Eternal Magekyo Sharingan,One 6 Tomoe Rinnegan",
            "Obito":"2 Tomoe Sharingan,3 Tomoe Sharigan,One Magekyo Sharingan,One Rinnegan"}
def Madara():
    labelofMadara["text"]=dictionary["Madara"]
  
def Sasuke():
    labelofSasuke["text"]=dictionary["Sasuke"]
        
def Obito():
    labelofObito["text"]=dictionary["Obito"]
    
btnMadara=Button(root,text="Madara",command=Madara)    
labelofMadara.place(relx = 0.5, rely =0.3, anchor = CENTER)
btnMadara.place(relx=0.5,rely=0.2,anchor=CENTER)

btnSasuke=Button(root,text="Sasuke",command=Sasuke)    
labelofSasuke.place(relx = 0.5, rely =0.5, anchor = CENTER)
btnSasuke.place(relx=0.5,rely=0.4,anchor=CENTER)

btnObito=Button(root,text="Obito",command=Obito)    
labelofObito.place(relx = 0.5, rely =0.7, anchor = CENTER)
btnObito.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()