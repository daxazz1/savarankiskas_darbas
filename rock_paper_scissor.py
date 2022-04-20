import random, time
import tkinter as tk

window = tk.Tk()
window.minsize(320, 250)
window.maxsize(320, 250)
window.title("Akmuo_Popierius_Žirklės žaidimas")

h_score = 0
c_score = 0
t_score = 0
h_choice = ""
c_choice = ""


def ChoiceToNr(choice):     # pasirinkimas priskiriamas skaičiui
    nr = {'akmuo': 0, 'popierius': 1, 'zirkles': 2}
    return nr[choice]


def RCC():                   # kompiuterio random'as
    return random.choice(['akmuo', 'popierius', 'zirkles'])


def result(hc, cc):         #nustatom rezultatą
    global h_score
    global c_score
    global t_score
    human = ChoiceToNr(hc)
    PC = ChoiceToNr(cc)

    if human == PC:         # tikrinam ar PC ir žmogaus pasirinkimai sutampa
        time.sleep(0.2)
        t_score += 1        # pridedam +1 prie Tie Score jeigu sutampa
        print('Lygiosios')

    elif (human - PC) % 3 == 1:
        time.sleep(0.2)
        h_score += 1        # pridedam +1 prie Human score jeigu liekana yra 1
        print('Žaidėjas laimėjo')

    else:
        time.sleep(0.2)
        c_score += 1        #visais kitais atvejais +1 prie Computer score
        print('Kompiuteris laimėjo')


    text_area = tk.Text(height=15, width=35, bg="lightgrey", font="Arial")
    text_area.grid(columnspan=9, row=2)
    answer = "\nTavo pasirinkimas: {hc} \n\nKompiuterio pasirinkimas : {cc} \n\nTavo rezultatas: {h} \n\nKompiuterio rezultatas : {c} \n\nLygiosios: {t}".format(hc = h_choice, cc = c_choice, h = h_score, c = c_score, t = t_score)
    text_area.insert(tk.END, answer)


def akmuo():
    global h_choice
    global c_choice
    h_choice = 'akmuo'
    c_choice = RCC()
    result(h_choice, c_choice)


def popierius():
    global h_choice
    global c_choice
    h_choice = 'popierius'
    c_choice = RCC()
    result(h_choice, c_choice)


def zirkles():
    global h_choice
    global c_choice
    h_choice = 'zirkles'
    c_choice = RCC()
    result(h_choice, c_choice)


button1 = tk.Button(text="Akmuo", bg="yellow", command=akmuo)
button1.grid(column=3, row=1)
button2 = tk.Button(text="Popierius", bg="green", command=popierius)
button2.grid(column=4, row=1)
button3 = tk.Button(text="Žirklės", bg="red", command=zirkles)
button3.grid(column=5, row=1)

window.mainloop()


