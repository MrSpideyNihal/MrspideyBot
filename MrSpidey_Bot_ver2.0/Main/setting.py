import pygame
import tkinter as tk
from game import main
import random
from define import languages

def Setting(query,results):
                
                print("Setting...   ")
                tkinter_root = tk.Tk()
                check_btn_var = tk.IntVar()


                def add_app():
                    def open_app():
                         address =  entry.get()
                         Title =  title.get()
                   
                         data = open('data\\addresses.txt', 'a')
                         Data = f"\n Title: open {Title} \n address : {address} \n"
                         data.write(Data)
                         data.close()
                         tkinter_root.destroy()
                   
                    tkinter_root = tk.Tk()
                    tkinter_root.title("Add app")
                    tkinter_root.geometry("300x200")
                    var = tk.StringVar()
                    entry = tk.Entry(tkinter_root)
                    title = tk.Entry(tkinter_root)
                   
                    entry.place(x=50,y=50)
                    title.place(x=50,y=10)
                    Title = tk.Label(tkinter_root, text="Title ")
                    Title.place(x=10,y=10)
                    Address = tk.Label(tkinter_root, text="Address")
                    Address.place(x=10,y=50)
                   
                    Note = tk.Label(tkinter_root, text="Add open at start of title ex: open chrome")
                    Note.place(x=10,y=130)
                    Note = tk.Label(tkinter_root, text="Title must be lowercase!")
                    Note.place(x=10,y=150)
                    Note = tk.Label(tkinter_root, text="Changes will applied after restarting software !")
                    Note.place(x=10,y=170)
                    add_app = tk.Button(tkinter_root, text="Add app", command=open_app)
                    add_app.place(x=100,y=100)
                   
                    tkinter_root.mainloop()
                   
                def show_popup_list():
                    def on_select(event):
                        selected = listbox.get(listbox.curselection())
                        print("Selected language:", selected)
                        lang_code = selected.split(': ')[1]  # Extracting the language code part
                        print("Language code to store:", lang_code)
                        myfile = open('data\\language.txt', 'w')
                        myfile.write(lang_code)
                        myfile.close()
                        popup.destroy()
               
                    popup = tk.Toplevel(tkinter_root)
                    popup.title("Language List")
               
                    listbox = tk.Listbox(popup)
                    for lang in languages:
                        listbox.insert(tk.END, lang)
                    listbox.pack(padx=10, pady=10)
               
                    listbox.bind("<<ListboxSelect>>", on_select)
                   


                def download_data():
                     try :
                          data = open('userdata.txt', 'a')
                          MainData = f"\n User : {query} \n Bot : {results} \n"
                          data.write(MainData)
                          data.close()
                     except FileNotFoundError:
                          with open('file.txt', 'w') as file:
                               file.write(MainData)


                def setVoice():
                    selection = choice1()
                    myfile = open('data\\voice.txt', 'w')
                    myfile.write(selection)
                    myfile.close()
                    write_status()
                    tkinter_root.destroy()
               
                def choice1():
                    selection = var.get()
                    if selection == "male":
                        return "male"
                    elif selection == 'female':
                        return "female"
                    else:
                        return "male"
               
                def initialize_selection():
                   
                        myfile = open('data\\voice.txt', 'r')
                        content = myfile.read()
                        if content == 'male':
                            var.set('male')
                           
                        elif content == 'female':
                            var.set('female')
                           
                        myfile.close()
                 
                def write_status():
                    with open("data\\startup.txt", "w") as file:
                        if check_btn_var.get() == 1:
                            file.write("Checked")
                        else:
                            file.write("Unchecked")
                def check_startup_file():
                     with open("data\\startup.txt", "r") as file:
                         status = file.read().strip()
                         if status == "Checked":
                             check_btn_var.set(1)
                         else:
                             check_btn_var.set(0)
             
                               
                tkinter_root.title("Settings")
                tkinter_root.geometry("300x200")
                var = tk.StringVar()
               
                initialize_selection()  # Set initial selection based on file content
                Note = tk.Label(tkinter_root, text="VOICE ")
                Note.place(x=10,y=12)
                male = tk.Radiobutton(tkinter_root, text="Male", value='male', variable=var)
                male.place(x=70,y=12)
                female = tk.Radiobutton(tkinter_root, text="Female", value='female', variable=var)
                female.place(x=120,y=12)
               
                apply = tk.Button(tkinter_root, text="Apply", command=setVoice)
                apply.place(x=170,y=135)
                Note = tk.Label(tkinter_root, text="Changes will applied after restarting software !")
                Note.place(x=10,y=170)
                download = tk.Button(tkinter_root, text="Download data", command=download_data)
                download.place(x=20,y=90)
                addApp = tk.Button(tkinter_root, text="Add App", command=add_app)
                addApp.place(x=20,y=45)
                popup_button = tk.Button(tkinter_root, text="Select Language", command=show_popup_list)
                popup_button.place(x=20,y=135)
                check_startup_file()
                check_btn = tk.Checkbutton(tkinter_root,text="Wish me on startup!" ,variable=check_btn_var)
                check_btn.place(x=130,y=50)
                offline_btn = tk.Button(tkinter_root,text="Offline Click here!",command=main)
                offline_btn.place(x=140,y=90)
                tkinter_root.mainloop()

