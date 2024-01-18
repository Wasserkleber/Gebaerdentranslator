import customtkinter
from main import main, playRecording

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

    
def textInput():
    text = entry1.get()
    print(text)
    main(text)

root = customtkinter.CTk()
root.geometry("500x370")
root.title("Gebärdentranslator")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame,text="Gebärdentranslator", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button1 = customtkinter.CTkButton(master=frame, width=200, text="Spracherkennung", text_color="black", command=main)
button1.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, width=200, placeholder_text="Schreib!", text_color="black")
entry1.pack(pady=12, padx=10)

button2 = customtkinter.CTkButton(master=frame, width=150, height=21, text="Bestätige Eingabe", text_color="black", command=textInput)
button2.pack(pady=12, padx=10)

button3 = customtkinter.CTkButton(master=frame, width=200, text_color="black", text="Untertietel? (not working)")
button3.pack(pady=12, padx=10)

button4 = customtkinter.CTkButton(master=frame, width=200, text_color="black", text="Spiele letzte Übersetztung ab", command=playRecording)
button4.pack(pady=12, padx=10)

root.mainloop()
