from tkinter import *
from tkinter import colorchooser
from random import randint
import random

root=Tk()
root.title("Flash Card!!")
root.geometry("500x400")

global score
score = 0
global essais 
essais = 0


# ------------------------------FONCTIONS-------------------------------------------
def reset():
    global score
    score = 0
    global essais 
    essais = 0
    global score_label
    score_label.pack_forget()  
    score_label = Label(add_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
    score_label.pack()    

# ---------------------------------------------ADDITIONS--------------------------------------------------------------------------------------------------

# 1 ADDITION de 0 à 10
# Verification de l'addition
def add_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct = num1 + num2

    global score
    global essais 
    global score_label
    score_label.pack_forget()   

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " + " + str(num2) + " = " + str(correct) + ", et pas " + str(add_answer.get()))

    if int(add_answer.get()) == correct:                          
        add_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(add_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()                      
    elif int(add_answer.get()) != correct:
        add_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        score = score
        essais +=1
        score_label = Label(add_frame, text = "Ton score : " +  str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()   
    
    # on nettoie l'ntry box reponse
    add_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))
    add_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))

# addition
def add():    
    hide_menu_frame()
    root.geometry("500x400")
    add_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()    
    num_1.set(randint(0,10))
    num_2.set(randint(0,10)) 

    # afficher les nombres a l'écran
    global add_flash
    add_flash = Label(add_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))
    add_flash.pack(pady=10)

    # Entry box pour la réponse
    global add_answer
    add_answer = Entry(add_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    add_answer.pack(pady=10)

    # bouton réponse
    add_button = Button(add_frame, text="OK", command=lambda: add_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    add_button.pack(pady=5)

    # Message juste ou faux
    global add_correct_label
    add_correct_label = Label(add_frame, text="Juste ou faux", font=("Arial",20))
    add_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(add_frame, text="SCORE", font=("Arial",20))
    score_label.pack(pady=5)

# 2 ADDITION de 0 à 50
# Verification de l'addition
def add050_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct = num1 + num2

    global score
    global essais 
    global score_label
    score_label.pack_forget()  

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " + " + str(num2) + " = " + str(correct) + ", et pas " + str(add050_answer.get()))

    if int(add050_answer.get()) == correct:
        add050_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(add050_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()     

    else:
        add050_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1
        score_label = Label(add050_frame, text = "Ton score : " +  str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    
    # on nettoie l'entry box reponse
    add050_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,50))
    num_2.set(randint(0,50))
    add050_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))

# addition050
def add050():
    hide_menu_frame()
    root.geometry("500x400")
    add050_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,50))
    num_2.set(randint(0,50))    
   
    # afficher les nombres a l'écran
    global add050_flash
    add050_flash = Label(add050_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))
    add050_flash.pack(pady=10)

    # Entry box pour la réponse
    global add050_answer
    add050_answer = Entry(add050_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    add050_answer.pack(pady=10)

    # bouton réponse
    add050_button = Button(add050_frame, text="OK", command=lambda: add050_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    add050_button.pack(pady=5)

    # Message juste ou faux
    global add050_correct_label
    add050_correct_label = Label(add050_frame, text="Juste ou faux", font=("Arial",20))
    add050_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(add050_frame, text="SCORE", font=("Arial",20))
    score_label.pack(pady=5)
 
# 3 ADDITION de 0 à 1000
# Verification de l'addition de 0 à 1000
def add01000_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct = num1 + num2

    global score
    global essais 
    global score_label
    score_label.pack_forget()   

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " + " + str(num2) + " = " + str(correct) + ", et pas " + str(add01000_answer.get()))

    if int(add01000_answer.get()) == correct:
        add01000_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(add01000_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack() 
    else:
        add01000_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1
        score_label = Label(add01000_frame, text = "Ton score : " +  str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()  
    
    # on nettoie l'entry box reponse
    add01000_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,1000))
    num_2.set(randint(0,1000))
    add01000_flash.config(text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))

# addition01000
def add01000():
    hide_menu_frame()
    root.geometry("500x400")
    add01000_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,1000))
    num_2.set(randint(0,1000))    
   
    # afficher les nombres a l'écran
    global add01000_flash
    add01000_flash = Label(add01000_frame, text=str(num_1.get()) + " + " + str(num_2.get()), font=("Arial",72))
    add01000_flash.pack(pady=10)

    # Entry box pour la réponse
    global add01000_answer
    add01000_answer = Entry(add01000_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    add01000_answer.pack(pady=10)

    # bouton réponse
    add01000_button = Button(add01000_frame, text="OK", command=lambda: add01000_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    add01000_button.pack(pady=5)

    # Message juste ou faux
    global add01000_correct_label
    add01000_correct_label = Label(add01000_frame, text="Juste ou faux", font=("Arial",20))
    add01000_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(add01000_frame, text="SCORE", font=("Arial",20))
    score_label.pack(pady=5)

# ---------------------------------------------------------SOUSTRACTIONS----------------------------------------------------------------------------------
# 4 SOUSTRACTION de 0 à 10
# Verification de la soustraction de 0 à10
def subtract_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    if num1 > num2:
        correct = num1 - num2
    else:
        correct = num2 - num1

    global score
    global essais 
    global score_label
    score_label.pack_forget() 

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    if num1 > num2:
        output_answer_incorrect.set("Faux, " + str(num1) + " - " + str(num2) + " = " + str(correct) + ", et pas " + str(subtract_answer.get()))
    else:
        output_answer_incorrect.set("Faux, " + str(num2) + " - " + str(num1) + " = " + str(correct) + ", et pas " + str(subtract_answer.get()))

    if int(subtract_answer.get()) == correct:                         
        subtract_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1         
        subtract_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score_label = Label(subtract_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()   
    else:        
        subtract_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1
        subtract_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        score_label = Label(subtract_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    
    # on nettoiel'entry box reponse
    subtract_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))
    if num_1.get() > num_2.get():
        subtract_flash.config(text=str(num_1.get()) + " - " + str(num_2.get()), font=("Arial",72))
    else:
        subtract_flash.config(text=str(num_2.get()) + " - " + str(num_1.get()), font=("Arial",72))
    

# soustraction
def subtract():
    hide_menu_frame()
    root.geometry("500x400")
    subtract_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))    
   
    # afficher les nombres a l'écran
    global subtract_flash
    if num_1.get() > num_2.get():
        subtract_flash = Label(subtract_frame, text=str(num_1.get()) + " - " + str(num_2.get()), font=("Arial",72))
        subtract_flash.pack(pady=10)
    else:
        subtract_flash = Label(subtract_frame, text=str(num_2.get()) + " - " + str(num_2.get()), font=("Arial",72))
        subtract_flash.pack(pady=10)

    # Entry box pour la réponse
    global subtract_answer
    subtract_answer = Entry(subtract_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    subtract_answer.pack(pady=10)

    # bouton réponse
    subtract_button = Button(subtract_frame, text="OK", command=lambda: subtract_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    subtract_button.pack(pady=5)

    # Message juste ou faux
    global subtract_correct_label
    subtract_correct_label = Label(subtract_frame, text="Juste ou faux", font=("Arial",20))
    subtract_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(subtract_frame, text="SCORE", font=("Arial",20))
    score_label.pack(pady=5)

# 5 SOUSTRACTION de 0 à 100
# Verification de la soustraction de 0 à 100
def subtract0100_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    if num1 > num2:
        correct = num1 - num2
    else:
        correct = num2 - num1

    global score
    global essais 
    global score_label
    score_label.pack_forget() 

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    if num1 > num2:
        output_answer_incorrect.set("Faux, " + str(num1) + " - " + str(num2) + " = " + str(correct) + ", et pas " + str(subtract0100_answer.get()))
    else:
        output_answer_incorrect.set("Faux, " + str(num2) + " - " + str(num1) + " = " + str(correct) + ", et pas " + str(subtract0100_answer.get()))

    if int(subtract0100_answer.get()) == correct:
        subtract0100_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(subtract0100_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()  
    else:
        subtract0100_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1
        subtract0100_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        score_label = Label(subtract0100_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    
    
    # on nettoie l'entry box reponse
    subtract0100_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))
    if num_1.get() > num_2.get():
        subtract0100_flash.config(text=str(num_1.get()) + " - " + str(num_2.get()), font=("Arial",72))
    else:
        subtract0100_flash.config(text=str(num_2.get()) + " - " + str(num_1.get()), font=("Arial",72))
    

# soustraction de 0 à 100
def subtract0100():
    hide_menu_frame()
    root.geometry("500x400")
    subtract0100_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,100))
    num_2.set(randint(0,100))    
   
    # afficher les nombres a l'écran
    global subtract0100_flash
    if num_1.get() > num_2.get():
        subtract0100_flash = Label(subtract0100_frame, text=str(num_1.get()) + " - " + str(num_2.get()), font=("Arial",72))
        subtract0100_flash.pack(pady=10)
    else:
        subtract0100_flash = Label(subtract0100_frame, text=str(num_2.get()) + " - " + str(num_1.get()), font=("Arial",72))
        subtract0100_flash.pack(pady=10)

    # Entry box pour la réponse
    global subtract0100_answer
    subtract0100_answer = Entry(subtract0100_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    subtract0100_answer.pack(pady=10)

    # bouton réponse
    subtract0100_button = Button(subtract0100_frame, text="OK", command=lambda: subtract0100_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    subtract0100_button.pack(pady=5)

    # Message juste ou faux
    global subtract0100_correct_label
    subtract0100_correct_label = Label(subtract0100_frame, text="Juste ou faux",font=("Arial",20))
    subtract0100_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(subtract0100_frame, text="SCORE",font=("Arial",20))
    score_label.pack(pady=5)

# -------------------------------------------------------------MULTIPLICATIONS----------------------------------------------------------------------------
# MULTIPLICATION de 0 à 5 et 10
# Verification de la Multiplication 0510
def multiply0510_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct = num1 * num2

    global score
    global essais 
    global score_label
    score_label.pack_forget() 
 
    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " x " + str(num2) + " = " + str(correct) + ", et pas " + str(multiply0510_answer.get()))

    if int(multiply0510_answer.get()) == correct:
        multiply0510_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(multiply0510_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()     

    else:
        multiply0510_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1              
        score_label = Label(multiply0510_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()     

    
    # on nettoie l'entry box reponse
    multiply0510_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    liste = [0, 1, 2, 3, 4, 5, 10]
    num_1.set(random.choice(liste))
    num_2.set(random.choice(liste))  
    multiply0510_flash.config(text=str(num_1.get()) + " x " + str(num_2.get()), font=("Arial",72))

# multiplication
def multiply0510():
    hide_menu_frame()
    root.geometry("500x400")
    multiply0510_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    liste = [0, 1, 2, 3, 4, 5, 10]
    num_1.set(random.choice(liste))
    num_2.set(random.choice(liste))    
   
    # afficher les nombres a l'écran
    global multiply0510_flash
    multiply0510_flash = Label(multiply0510_frame, text=str(num_1.get()) + " x " + str(num_2.get()), font=("Arial",72))
    multiply0510_flash.pack(pady=10)

    # Entry box pour la réponse
    global multiply0510_answer
    multiply0510_answer = Entry(multiply0510_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    multiply0510_answer.pack(pady=10)

    # bouton réponse
    multiply0510_button = Button(multiply0510_frame, text="OK", command=lambda: multiply0510_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    multiply0510_button.pack(pady=5)

    # Message juste ou faux
    global multiply0510_correct_label
    multiply0510_correct_label = Label(multiply0510_frame, text="Just ou faux", font=("Arial", 20))
    multiply0510_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(multiply0510_frame, text="SCORE", font=("Arial", 20))
    score_label.pack(pady=5)

# MULTIPLICATION
# Verification de la Multiplication
def multiply_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct = num1 * num2

    global score
    global essais 
    global score_label
    score_label.pack_forget() 

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar() 
    output_answer_correct.set("Juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " x " + str(num2) + " = " + str(correct) + ", et pas " + str(multiply_answer.get()))

    if int(multiply_answer.get()) == correct:
        multiply_correct_label.config(text=output_answer_correct.get(), font=("Arial",20 ))
        score +=1 
        essais +=1              
        score_label = Label(multiply_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()     

    else:
        multiply_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",20 ))
        essais +=1              
        score_label = Label(multiply_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()     

    
    # on nettoie l'entry box reponse
    multiply_answer.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))
    multiply_flash.config(text=str(num_1.get()) + " x " + str(num_2.get()), font=("Arial",72))

# multiplication
def multiply():
    hide_menu_frame()
    root.geometry("500x400")
    multiply_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0,10))
    num_2.set(randint(0,10))    
   
    # afficher les nombres a l'écran
    global multiply_flash
    multiply_flash = Label(multiply_frame, text=str(num_1.get()) + " x " + str(num_2.get()), font=("Arial",72))
    multiply_flash.pack(pady=10)

    # Entry box pour la réponse
    global multiply_answer
    multiply_answer = Entry(multiply_frame, font=("Arial", 52), width=5, justify="center") # width correspond au nombre de caracteres
    multiply_answer.pack(pady=10)

    # bouton réponse
    multiply_button = Button(multiply_frame, text="OK", command=lambda: multiply_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    multiply_button.pack(pady=5)

    # Message juste ou faux
    global multiply_correct_label
    multiply_correct_label = Label(multiply_frame, text="Just ou faux", font=("Arial", 20))
    multiply_correct_label.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(multiply_frame, text="SCORE", font=("Arial", 20))
    score_label.pack(pady=5)
 
# -------------------------------------------------------------------DIVISIONS-----------------------------------------------------------------------------
# DIVISION
# Verification de la division
def divide_correct(num1, num2):   # num1 et num2 sont de nouvelles variables qu'on utilise pour cette fonction qui correspondent a num_1 et _2
    correct_quotient = num1 // num2
    correct_reste = num1%num2

    global score
    global essais 
    global score_label
    score_label.pack_forget() 

    # on crée 2 variable string qui donneront juste ou faux
    output_answer_correct= StringVar()
    output_answer_incorrect = StringVar()     
    output_answer_correct.set("Le quotient est juste!! Bravo!!")
    output_answer_incorrect.set("Faux, " + str(num1) + " / " + str(num2) + " = " + str(correct_quotient) + ", et pas " + str(divide_answer.get()))
    output_modulo_correct = StringVar()
    output_modulo_incorrect = StringVar()
    output_modulo_correct.set("Le reste est juste!! Bravo!!")
    output_modulo_incorrect.set("Faux, le reste est de " + str(correct_reste))



    if int(divide_answer.get()) == correct_quotient and int(divide_reste.get()) == correct_reste:
        divide_correct_label.config(text=output_answer_correct.get(), font=("Arial",18 ))
        divide_correct_label2.config(text=output_modulo_correct.get(), font=("Arial",18 ))
        score += 1
        essais += 1
        score_label = Label(divide_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    elif int(divide_answer.get()) == correct_quotient and int(divide_reste.get()) != correct_reste:
        divide_correct_label.config(text=output_answer_correct.get(), font=("Arial",18 ))
        divide_correct_label2.config(text=output_modulo_incorrect.get(), font=("Arial",18 ))
        essais += 1
        score_label = Label(divide_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    elif int(divide_answer.get()) != correct_quotient and int(divide_reste.get()) == correct_reste:
        divide_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",18 ))
        divide_correct_label2.config(text=output_modulo_correct.get(), font=("Arial",18 ))
        essais += 1
        score_label = Label(divide_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()
    elif int(divide_answer.get()) != correct_quotient and int(divide_reste.get()) != correct_reste:
        divide_correct_label.config(text=output_answer_incorrect.get(), font=("Arial",18 ))
        divide_correct_label2.config(text=output_modulo_incorrect.get(), font=("Arial",18 ))
        essais += 1
        score_label = Label(divide_frame, text ="Ton score : " + str(score) + " / " + str(essais), font=("Arial",20 ))
        score_label.pack()

    # effacer la entry box reponse
    divide_answer.delete(0, END) 
     # effacer la entry box reste
    divide_reste.delete(0, END) 

    # On crée 2 nouveaux nombres
    num_1.set(randint(20,100))
    num_2.set(randint(1,20))
    divide_flash.config(text=str(num_1.get()) + " / " + str(num_2.get()), font=("Arial",68))
    

# division
def divide():
    hide_menu_frame()
    root.geometry("550x530")
    divide_frame.pack(fill="both", expand=1)

    # creation des variables
    global num_1, num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(20,100))
    num_2.set(randint(1,20))    
   
    # afficher les nombres a l'écran
    global divide_flash
    if num_1.get() > num_2.get():
        divide_flash = Label(divide_frame, text=str(num_1.get()) + " / " + str(num_2.get()), font=("Arial",72))
        divide_flash.pack(pady=10)
    else:
        divide_flash = Label(divide_frame, text=str(num_2.get()) + " / " + str(num_2.get()), font=("Arial",72))
        divide_flash.pack(pady=10)

    # Entry box pour le quotient
    global divide_answer
    divide_answer = Entry(divide_frame, font=("Arial", '40'), width=10,justify="center") # width correspond au nombre de caracteres
    divide_answer.insert(0, "quotient")
    divide_answer.pack(pady=10)

    # Entry box pour le reste
    global divide_reste
    divide_reste = Entry(divide_frame,font=("Arial", 40), width=10, justify="center") # width correspond au nombre de caracteres
    divide_reste.insert(0, "reste")
    divide_reste.pack(pady=10)

    # bouton réponse
    divide_button = Button(divide_frame, text="OK", command=lambda: divide_correct(num_1.get(), num_2.get()), font=("Arial", 20))
    divide_button.pack(pady=5)

    # Message quotient juste ou faux
    global divide_correct_label
    divide_correct_label = Label(divide_frame, text="Quotient juste ou faux", font=("Arial", 20))
    divide_correct_label.pack(pady=5)

    # Message reste juste ou faux
    global divide_correct_label2
    divide_correct_label2 = Label(divide_frame, text="Reste juste ou faux", font=("Arial", 20))
    divide_correct_label2.pack(pady=5)

    # Score label
    global score_label
    score_label = Label(divide_frame, text="SCORE", font=("Arial", 20))
    score_label.pack(pady=5)


# on cache les frame
def hide_menu_frame():
    # destruction du widget enfant
    for widget in add_frame.winfo_children():
        widget.destroy()        
    for widget in add050_frame.winfo_children():
        widget.destroy()
    for widget in add01000_frame.winfo_children():
        widget.destroy()
    for widget in subtract_frame.winfo_children():
        widget.destroy()
    for widget in subtract0100_frame.winfo_children():
        widget.destroy()
    for widget in multiply0510_frame.winfo_children():
        widget.destroy()
    for widget in multiply_frame.winfo_children():
        widget.destroy()
    for widget in divide_frame.winfo_children():
        widget.destroy()
    for widget in start_frame.winfo_children():
        widget.destroy()
    
    add_frame.pack_forget()
    add050_frame.pack_forget()
    add01000_frame.pack_forget()
    subtract_frame.pack_forget()
    subtract0100_frame.pack_forget()
    multiply0510_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()    
       
    # On efface le start_frame
    start_frame.pack_forget()

# -------------------------------MENU------------------------------------------------

# main
my_menu = Menu()
root.config(menu=my_menu)

def home():
    hide_menu_frame()
    score = 0 
    essais = 0
    start_frame.pack(fill="both", expand=1)
    start_label = Label(start_frame, text=" Bienvenu(e) dans ce petit jeu!!", font=("Arial", 20))
    start_label.pack(pady=20)

    # Les boutons de calculs
    add_button = Button(start_frame, text="Addition de 0 à 10", command=add) 
    add_button.pack(pady=5) 
    add050_button = Button(start_frame, text="Addition de 0 à 50", command=add050) 
    add050_button.pack(pady=5)
    add01000_button = Button(start_frame, text="Addition de 0 à 1000", command=add01000) 
    add01000_button.pack(pady=5)
    subtract_button = Button(start_frame, text="Soustraction de 0 à 10", command=subtract) 
    subtract_button.pack(pady=5)
    subtract0100_button = Button(start_frame, text="Soustraction de 0 à 100", command=subtract0100) 
    subtract0100_button.pack(pady=5)
    multiply0510_button = Button(start_frame, text="Multiplication de 0 à 5 et 10", command=multiply0510) 
    multiply0510_button.pack(pady=5)
    multiply_button = Button(start_frame, text="Multiplication de 0 à 10", command=multiply) 
    multiply_button.pack(pady=5)
    divide_button = Button(start_frame, text="Division", command=divide) 
    divide_button.pack(pady=5)  

#menu items
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Mathématiques!!", menu=math_menu)
math_menu.add_command(label="Addition de 0 à 10", command=add)
math_menu.add_command(label="Addition de 0 à 50", command=add050)
math_menu.add_command(label="Addition de 0 à 1000", command=add01000)
math_menu.add_command(label="Soustraction de 0 à 10", command=subtract)
math_menu.add_command(label="Soustraction de 0 à 100", command=subtract0100)
math_menu.add_command(label="Multiplication de 0 à 5 et 10", command=multiply0510)
math_menu.add_command(label="Multiplication de 0 à 10", command=multiply)
math_menu.add_command(label="Division", command=divide)

math_menu.add_separator()
math_menu.add_command(label="Mise à 0", command=reset)
math_menu.add_separator()
math_menu.add_command(label="Menu principal", command=home)
math_menu.add_separator()
math_menu.add_command(label="Quitter", command=root.quit)


# ----------------------FRAMES--------------------------------------------------

# Frame de calcul
add_frame = Frame(root, width=400, height=400, bg="blue")
add050_frame = Frame(root, width=400, height=400, bg="blue")
add01000_frame = Frame(root, width=400, height=400, bg="blue")
subtract_frame = Frame(root, width=400, height=400, bg="red")
subtract0100_frame = Frame(root, width=400, height=400, bg="red")
multiply0510_frame = Frame(root, width=400, height=400, bg="yellow")
multiply_frame = Frame(root, width=400, height=400, bg="yellow")
divide_frame = Frame(root, width=400, height=400, bg="green")
score_frame = Frame(root,height=50,width=400, bg="white")
# Frame de l'écran principal
start_frame = Frame(root, height=400, width=400)

# afficher le menu en appelant la fonction dédiée
home()

root.mainloop()
