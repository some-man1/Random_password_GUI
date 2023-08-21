import tkinter , random , string, os

windo = tkinter.Tk()
windo.geometry("600x650")
windo.title("password genrater")

def words(length):
    """"This function just make a random word """
    x = string.ascii_letters + string.punctuation + string.digits
    word = ''.join(random.choice(x)for i in range(length))
    return word


def genrate():
    """This function is the main function """
    leng = int(length1.get())
    length1.delete(0,tkinter.END)
    password = words(length=leng)
    path = os.getcwd() + "/password.txt"
    label2.config(text=f"The password has been saved in {path}")
    with open("passwords.txt", "a") as file:
        file.write(f"A passwrod with {leng} length: {password}\n")

label1 = tkinter.Label(windo, text="Just write the length of the password you want to genrate", font=('Arial Bold', 15))
label1.pack()
length1 = tkinter.Entry(windo, width=40)
length1.pack()
bottn = tkinter.Button(windo, text="Genrate", command=genrate)
bottn.pack()
label2 = tkinter.Label(windo, text="", font=('Arial Bold', 15))
label2.pack()
""""Plase man don't delete this"""
libel3 = tkinter.Label(windo, text="Github: https://github.com/some-man1", font=('Arial Bold', 10), fg="red")
libel3.pack(side=tkinter.BOTTOM, anchor=tkinter.SW) 
libel4 = tkinter.Label(windo, text="Telegram: @RD515Y", font=('Arial Bold', 10), fg="blue")
libel4.pack(side=tkinter.BOTTOM, anchor=tkinter.SW) 


#Just the main loop 
windo.mainloop()
