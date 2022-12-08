from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','#','$','%','&','*','(',')','+']


    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_list=password_letters+password_symbols+password_numbers

    print(password_list)
    random.shuffle(password_list)   # this will print the list item in random order
    # print(password_list)

    # password=" "
    # for char in password_list:
    #     password +=char
    password="".join(password_list)
    # print(f"Your password is {password}")
    password_entry.insert(0,  password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_file():
    website=website_name_entry.get()
    email=user_name_email.get()
    pass_word=password_entry.get()

    if len(website)==0 or len(pass_word)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!") 

    else:  
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {pass_word} \nIs it ok to save?" )
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}: {email} -> password={pass_word}\n")
                website_name_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_image=PhotoImage(file="logo.png")
my_canva=Canvas(width=200, height=200)
my_canva.create_image(100,100,image=logo_image)
my_canva.grid(row=0, column=1)

###labels###
website_label=Label(text="Website:", font="bold")
website_label.grid(row=1, column=0)
userName_email_label=Label(text="Email/Username:", font="bold")
userName_email_label.grid(row=2, column=0)
password_label=Label(text="Password:", font="bold")
password_label.grid(row=3, column=0)

###entries###
website_name_entry=Entry(width=35)
website_name_entry.grid(row=1, column=1, columnspan=2)
website_name_entry.focus()  # firstly typing cursor will go to website entry automatically
# website_name.get()

user_name_email=Entry(width=35)
user_name_email.grid(row=2, column=1, columnspan=2)
user_name_email.insert(0, "sy640952@gmail.com")  # this email will alrealdy be in the email entry box
# user_name_email.get()

password_entry=Entry(width=21)
password_entry.grid(row=3, column=1)
# password.get()

###buttons###
generate_button=Button(text="Generate Password", font="bold", command=generate_password)
generate_button.grid(row=3, column=2)
add_button=Button(text="Add", font="bold",width=10, command=password_file)
add_button.grid(row=4, column=1)


window.mainloop()