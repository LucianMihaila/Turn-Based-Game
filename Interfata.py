import clips
import tkinter as tk

def citeste_hp_super():
  lista = []
  file = open('Output.txt','r')
  while True:
    continut =file.readline()
    #print(continut)
    if not continut:
      break
    if continut == "Player Wins\n" or continut == "CPU Wins\n" or continut == "Draw\n":
      lista.append(continut.strip())
      break
    if continut == "HeavyPunch\n" or continut == "LightPunch\n" or continut == "Block\n" or continut == "Super\n":
      lista.append(continut.strip())
    if len(continut) <= 4:
      lista.append(continut.strip())
      #print(continut)
  file.close()
  #print(lista)

  return lista

def baza_fapte():
  env = clips.Environment() #crearea unei variabile de tip clips
  env.eval('(set-strategy random)')
  env.clear() #clear echivalent celui din Clips
  env.load("Etapa3.clp") #load la fisier (fisierul sa fie mai intai incarcat in colab)
  env.reset() #reset echivalent celui din Clips
  env.run() #run echivalent celui din Clips

  facts = env.eval("(get-fact-list *)") #salvarea bazei de fapte intr-o variabila

  #print('######### Baza de fapte #########')
  #print(facts) #afisarea bazei de fapte
  #print('######### Afisare tip baza de fapte #########')
  #print(type(facts))
  #print('######### Afisarea bazei de fapte #########')
  #for fact in facts:
  #  print(fact)
  return env

def output_reset():
  file = open('Output.txt', 'w')
  file.write('100\n100\n0\n0\n')
  file.close()
  

def check_end_match(resultat):
  if "Player Wins" in resultat:
    update_image("desene pt ui/win.png")
    interfata.update()
    output_reset()
    interfata.after(4000, update_image("desene pt ui/win.png"))
    quit()
  elif "CPU Wins" in resultat:
    update_image("desene pt ui/lose.png")
    interfata.update()
    output_reset()
    interfata.after(4000, update_image("desene pt ui/lose.png"))
    quit()
  elif "Draw" in resultat:
    update_image("desene pt ui/draw.png")
    interfata.update()
    output_reset()
    interfata.after(4000, update_image("desene pt ui/draw.png"))
    quit()
   

def first_move():
  val_hp_super = citeste_hp_super()
  file = open('Input.txt', 'w')
  file.write('Super\n')
  for i in range(0,len(val_hp_super)):
    file.write(val_hp_super[i] + '\n')
  file.close()

#---MISCARI---
def LightPunch():
  print("LightPunch apasat")
  lbl1.config(text="Player Move: Light Punch")

  val_hp_super = citeste_hp_super()
  print(val_hp_super)
  check_end_match(val_hp_super)
  file = open('Input.txt', 'w')
  file.write('LightPunch\n')
  for i in range(1,len(val_hp_super)):
    file.write(val_hp_super[i] + '\n')
  file.close()

  baza_fapte()

  val_hp_super = citeste_hp_super()
  if(val_hp_super[0] == 'Super'):
    update_image("desene pt ui/cpu_super.png")
    lbl2.config(text="Enemy Move: Super")
  elif (val_hp_super[0] == 'HeavyPunch'):
    update_image("desene pt ui/player_lp.png")
    lbl2.config(text="Enemy Move: Heavy Punch")
  elif (val_hp_super[0] == 'LightPunch'):
    update_image("desene pt ui/draw_attack.png")
    lbl2.config(text="Enemy Move: Light Punch")
  elif (val_hp_super[0] == 'Block'):
    update_image("desene pt ui/cpu_bl.png")
    lbl2.config(text="Enemy Move: Block")

  lbl3.config(text=f"HP: {val_hp_super[1]}")
  lbl4.config(text=f"SP: {min(5.0,float(val_hp_super[3]))}")
  lbl5.config(text=f"HP: {val_hp_super[2]}")
  lbl6.config(text=f"SP: {min(5.0,float(val_hp_super[4]))}")
  
  interfata.update()
  interfata.after(1000, update_image('desene pt ui/neutral.png'))

def HeavyPunch():
  print("HeavyPunch apasat")
  lbl1.config(text="Player Move: Heavy Punch")

  val_hp_super = citeste_hp_super()
  print(val_hp_super)
  check_end_match(val_hp_super)
  file = open('Input.txt', 'w')
  file.write('HeavyPunch\n')
  for i in range(1,len(val_hp_super)):
    file.write(val_hp_super[i] + '\n')
  file.close()

  baza_fapte()
  val_hp_super = citeste_hp_super()
  if(val_hp_super[0] == 'Super'):
    update_image("desene pt ui/cpu_super.png")
    lbl2.config(text="Enemy Move: Super")
  elif (val_hp_super[0] == 'HeavyPunch'):
    update_image("desene pt ui/draw_attack.png")
    lbl2.config(text="Enemy Move: Heavy Punch")
  elif (val_hp_super[0] == 'LightPunch'):
    update_image("desene pt ui/cpu_lp.png")
    lbl2.config(text="Enemy Move: Light Punch")
  elif (val_hp_super[0] == 'Block'):
    update_image("desene pt ui/player_hp.png")
    lbl2.config(text="Enemy Move: Block")

  lbl3.config(text=f"HP: {val_hp_super[1]}")
  lbl4.config(text=f"SP: {min(5.0,float(val_hp_super[3]))}")
  lbl5.config(text=f"HP: {val_hp_super[2]}")
  lbl6.config(text=f"SP: {min(5.0,float(val_hp_super[4]))}")

  interfata.update()
  interfata.after(1000, update_image('desene pt ui/neutral.png'))

def Block():
  print("Block apasat")
  lbl1.config(text="Player Move: Block")

  val_hp_super = citeste_hp_super()
  print(val_hp_super)
  check_end_match(val_hp_super)
  file = open('Input.txt', 'w')
  file.write('Block\n')
  for i in range(1,len(val_hp_super)):
    file.write(val_hp_super[i] + '\n')
  file.close()
  
  baza_fapte()
  val_hp_super = citeste_hp_super()
  if(val_hp_super[0] == 'Super'):
    update_image("desene pt ui/cpu_super.png")
    lbl2.config(text="Enemy Move: Super")
  elif (val_hp_super[0] == 'HeavyPunch'):
    update_image("desene pt ui/cpu_hp.png")
    lbl2.config(text="Enemy Move: Heavy Punch")
  elif (val_hp_super[0] == 'LightPunch'):
    update_image("desene pt ui/player_bl.png")
    lbl2.config(text="Enemy Move: Light Punch")
  elif (val_hp_super[0] == 'Block'):
    update_image("desene pt ui/draw_attack.png")
    lbl2.config(text="Enemy Move: Block")

  lbl3.config(text=f"HP: {val_hp_super[1]}")
  lbl4.config(text=f"SP: {min(5.0,float(val_hp_super[3]))}")
  lbl5.config(text=f"HP: {val_hp_super[2]}")
  lbl6.config(text=f"SP: {min(5.0,float(val_hp_super[4]))}")

  interfata.update()
  interfata.after(1000, update_image('desene pt ui/neutral.png'))

def Super():
  print("Super apasat")
  lbl1.config(text="Player Move: Super")
  val_hp_super = citeste_hp_super()
  check_end_match(val_hp_super)
  print(val_hp_super)
  if float(val_hp_super[3])>=5.0:
    #print("SUPER IF")
    file = open('Input.txt', 'w')
    file.write('Super\n')
    for i in range(1,len(val_hp_super)):
      file.write(val_hp_super[i] + '\n')
    file.close()
    print("VAL IN SUPER ", val_hp_super)

    baza_fapte()
    val_hp_super = citeste_hp_super()
    print(val_hp_super)
    if(val_hp_super[0] == 'Super'):
      update_image("desene pt ui/draw_super.png")
      lbl2.config(text="Enemy Move: Super")
    else:
      update_image("desene pt ui/player_super.png")
      lbl2.config(text="Enemy Move: Super")
  else:
    #ToDo: fa butonu de super unavailable daca nu ai 5 bare
    #print("SUPER ELSE")
    file = open('Input.txt', 'w')
    for i in range(1,len(val_hp_super)):
      file.write(val_hp_super[i] + '\n')
    file.close()

    baza_fapte()
    val_hp_super = citeste_hp_super()
    if(val_hp_super[0] == 'Super'):
      update_image("desene pt ui/cpu_super.png")
      lbl2.config(text="Enemy Move: Super")
  
  lbl3.config(text=f"HP: {val_hp_super[1]}")
  lbl4.config(text=f"SP: {min(5.0,float(val_hp_super[3]))}")
  lbl5.config(text=f"HP: {val_hp_super[2]}")
  lbl6.config(text=f"SP: {min(5.0,float(val_hp_super[4]))}")

  interfata.update()
  interfata.after(1000, update_image('desene pt ui/neutral.png'))

def update_image(new_image_path):
  global img
  img = tk.PhotoImage(file=new_image_path)
  lbl.config(image=img)
  lbl.image = img

def enable_disable_super():
  val_hp_super = citeste_hp_super()
  if float(val_hp_super[3])<5.0:
    buton4['state']='disabled'
  else:
    buton4['state']='normal'

#---GUI---
def gui():
  global lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl, interfata, img, buton4
  
  interfata=tk.Tk()
  interfata.title("Lethal Fight 1")
  interfata.geometry("600x750")
  
  background_image = tk.PhotoImage(file="desene pt ui/background.png")
  background_label = tk.Label(interfata, image=background_image)
  background_label.place(x=0, y=0, relwidth=1, relheight=1)

  buton1=tk.Button(interfata, text="Light Punch",height=4,width=20, bg='#F7E155', command=lambda:[LightPunch(), enable_disable_super()])
  buton2=tk.Button(interfata, text="Heavy Punch",height=4,width=20, bg='#F75555', command=lambda:[HeavyPunch(), enable_disable_super()])
  buton3=tk.Button(interfata, text="Block",height=4,width=20, bg='#55CDF7', command=lambda:[Block(),enable_disable_super()])
  buton4=tk.Button(interfata, text="Super",height=4,width=20, bg='#EA61FB', command=lambda:[Super(),enable_disable_super()], state='disabled')

  buton1.pack()
  buton2.pack()
  buton3.pack()
  buton4.pack()

  buton1.place(x=100,y=550)
  buton2.place(x=350,y=550)
  buton3.place(x=100,y=650)
  buton4.place(x=350,y=650)

  img=tk.PhotoImage(file="desene pt ui/neutral.png")
  lbl=tk.Label(interfata,image=img)
  lbl.pack()
  lbl.place(x=100,y=100)

  lbl1=tk.Label(interfata,text="Player Move:... ", fg="white", background="purple") 
  lbl1.pack()
  lbl1.place(x=110,y=80)

  lbl2=tk.Label(interfata,text="Enemy Move:... ", fg="white", background="purple") 
  lbl2.pack()
  lbl2.place(x=350,y=80)

  lbl3=tk.Label(interfata,text="HP: 100 ", fg="white", background="purple") 
  lbl3.pack()
  lbl3.place(x=110,y=60)

  lbl4=tk.Label(interfata,text="SP: 0.0 ", fg="white", background="purple") 
  lbl4.pack()
  lbl4.place(x=110,y=40)

  lbl5=tk.Label(interfata,text="HP: 100 ", fg="white", background="purple") 
  lbl5.pack()
  lbl5.place(x=350,y=60)

  lbl6=tk.Label(interfata,text="SP: 0.0 ", fg="white", background="purple") 
  lbl6.pack()
  lbl6.place(x=350,y=40)

  
  update_interface()
  #print("before mainloop")
  interfata.mainloop()
  #print("after mainloop")
  
def update_interface():
  global lista_val
  lista_val = citeste_hp_super()
  if lista_val[0] in ["Player Wins", "CPU Wins"]:
    lbl1.config(text=lista_val[0])
  else:
    lbl1.config(text="Player Move:...")

#---MAIN---
output_reset()
first_move()
lista_val = []
lista_val = citeste_hp_super()

#while lista_val[1] not in ["Player Wins", "CPU Wins", "Draw"]:
print("Lista val before gui= ",lista_val)
baza_fapte()
gui()
lista_val = citeste_hp_super()
print("Lista val after gui= ",lista_val)

  


  
  

