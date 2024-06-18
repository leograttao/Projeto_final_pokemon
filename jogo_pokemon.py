import os
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, ttk
from PIL import Image, ImageTk

rodada = 0
turno = 0
pasta_imagens = os.path.join("C:\\leonardo\\aula puc\\jogo pokemon\\images\\")

pokedex = [
    ['Charizard', 1200, 4000, 120, "Charizard.png"],
    ['Blastoise', 120, 40, 120, "Blastoise.png"],
    ['Venusaur', 120, 40, 120, "Venusaur.png"],
    ["Pikachu", 100, 45, 100, "pikachu.png"],
    ["Snorlax", 150, 35, 150, "Snorlax.png"],
    ["Chansey", 110, 40, 110, "Chansey.png"],
    ["Torterra", 180, 35, 180, "Torterra.png"]
]
insignias = []

pokemon_fogo = [
    ['Magby', 64, 20, 64, "Magby.png"],
    ['Chimchar', 62, 17, 62, "Chimchar.png"],
    ['Magmar', 67, 25, 67, "Magmar.png"],
    ['Blaziken', 140, 37, 140, "Blaziken.png"],
    ['Magmortar', 160, 38, 160, "Magmortar.png"],
    ['Moltres', 400, 57, 400, "Moltres.png"]
]

pokemon_agua = [
    ['Psyduck', 60, 22, 60, "Psyduck.png"],
    ['Froakie', 60, 17, 60, "Froakie.png"],
    ['Greninja', 75, 32, 75, "Greninja.png"],
    ['Feraligatr', 132, 29, 132, "Feraligart.png"],
    ['Swampert', 120, 32, 120, "Swampert.png"],
    ['Kyogre', 400, 50, 400, "Kyogre.png"]
]

pokemon_lendario = [
    ['Articuno', 120, 40, 120, "Articuno.png"],
    ['Zapdos', 380, 30, 380, "Zapdos.png"],
    ['Ho-Oh', 300, 30, 300, "Ho-oh.png"],
    ['Regirock', 700, 25, 700, "Regirock.png"],
    ['Raikou', 300, 44 , 300, "Raikou.png"],
    ['Mewtwo', 500, 58, 500, "Mewtwo.png"]
]

def batalha(pokemon1, pokemon2):
    resultado = f"\nBatalha entre {pokemon1[0]} e {pokemon2[0]} começa!\n"
    turno = 0
    while esta_vivo(pokemon1) and esta_vivo(pokemon2):
        turno += 1
        resultado += f"Turno {turno}:\n"
        dano = atacar(pokemon1, pokemon2)
        resultado += f"{pokemon1[0]} ataca {pokemon2[0]} causando {dano} de dano. Vida de {pokemon2[0]}: {pokemon2[1]}\n"
        
        if not esta_vivo(pokemon2):
            resultado += f"{pokemon2[0]} foi derrotado! {pokemon1[0]} vence a batalha!\n"
            break

        dano = atacar(pokemon2, pokemon1)
        resultado += f"{pokemon2[0]} ataca {pokemon1[0]} causando {dano} de dano. Vida de {pokemon1[0]}: {pokemon1[1]}\n"

        if not esta_vivo(pokemon1):
            resultado += f"{pokemon1[0]} foi derrotado! {pokemon2[0]} vence a batalha!\n"
            break
    messagebox.showinfo("Resultado da Batalha", resultado)

def atacar(atacante, defensor):
    dano = random.randint(0, atacante[2])
    defensor[1] -= dano
    return dano

def esta_vivo(pokemon):
    return pokemon[1] > 0

def restaurar_vida(pokemon):
    pokemon[1] = pokemon[3]

def restaurar_vida_lista(lista_pokemons):
    for pokemon in lista_pokemons:
        restaurar_vida(pokemon)

def introducao():
    global nome_jogador
    nome_jogador = simpledialog.askstring("Introdução", "Olá, sou o professor Carvalho, um pesquisador Pokémon. Qual é o seu nome?")
    if nome_jogador:
        messagebox.showinfo("Bem-vindo", f"Ótimo, então você é {nome_jogador}!! Prepare-se para embarcar em uma aventura emocionante no mundo dos Pokémon!\n")
        menu_principal()

def menu_principal():
    menu_frame.pack(fill="both", expand=True)
    label_bem_vindo.config(text=f"Bem-vindo {nome_jogador}, sua jornada pokémon se inicia aqui!!")
    
def listar_pokedex():
    top = Toplevel()
    top.title("Pokédex")
    for idx, pokemon in enumerate(pokedex):
        caminho_imagem = os.path.join(pasta_imagens, pokemon[4])
        img = Image.open(caminho_imagem)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        label = Label(top, text=f"{pokemon[0]}\nVida: {pokemon[1]}\nDano: {pokemon[2]}", image=photo, compound="top")
        label.image = photo
        label.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)

def ver_insignias():
    top = Toplevel()
    top.title("Insígnias")
    
    for idx, insignia in enumerate(insignias):
        caminho_imagem = os.path.join(pasta_imagens, f"{insignia}.png")
        img = Image.open(caminho_imagem)
        img = img.resize((100, 100)) 
        photo = ImageTk.PhotoImage(img)
            
        label = Label(top, text=insignia, image=photo, compound="top")
        label.image = photo
        label.grid(row=idx // 3, column=idx % 3, padx=10, pady=10)

def iniciar_batalha(pokemon_escolhido, pokemons, ginasio, rodada):
    if rodada == 0:
        resultado = f"\nVocê entrou no {ginasio}, terá que enfrentar 5 pokémons e 1 pokémon lendário!!\n"
        resultado += f"Bem-vindo ao {ginasio} Pokémon, liga competitiva dos melhores treinadores de todo o mundo!!!\n"
        for n in range(6):
            resultado += f"Rodada {n+1}: {pokemons[n][0]}\n"
        messagebox.showinfo(ginasio, resultado)
    
    while rodada < 6:
        resultado_batalha = f"\nRodada {rodada+1}:\n"
        batalha(pokemon_escolhido, pokemons[rodada])
        if pokemon_escolhido[1] <= 0:
            tentativa = messagebox.askyesno("Pokemon Derrotado", "Seu Pokémon foi derrotado, deseja escolher outro Pokémon da sua Pokédex para batalhar?")
            if tentativa:
                escolher_pokemon(pokemons, ginasio, rodada)
                return
            else:
                messagebox.showinfo("Derrota", "Você foi derrotado. O ginásio será reiniciado.")
                restaurar_vida_lista(pokedex)
                restaurar_vida_lista(pokemons)
                return
        else:
            rodada += 1
            if rodada == 6:
                messagebox.showinfo("Vitória", f"Parabéns, você venceu o ginásio e ganhou a insígnia de {ginasio}!")
                insignias.append(f"insignia de {ginasio.lower()}")
                restaurar_vida_lista(pokemons)
                pokedex.append(pokemons[5])
                verificar_fim_de_jogo()
                return

def escolher_pokemon(pokemons, ginasio, rodada=0):
    top = Toplevel()
    top.title("Escolha seu Pokémon")

    def escolher(pokemonn):
        pokemon_escolhido = pokedex[pokemonn]
        top.destroy()
        iniciar_batalha(pokemon_escolhido, pokemons, ginasio, rodada)
    
    for pokemonn, pokemon in enumerate(pokedex):
        caminho_imagem = os.path.join(pasta_imagens, pokemon[4])
        img = Image.open(caminho_imagem)
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        btn = ttk.Button(top, text=f"{pokemon[0]}\nVida: {pokemon[1]}\nDano: {pokemon[2]}", image=photo, compound="top", command=lambda idx=pokemonn: escolher(idx))
        btn.image = photo
        btn.grid(row=pokemonn // 3, column=pokemonn % 3, padx=10, pady=10)

def verificar_fim_de_jogo():
    if len(insignias) == 3:
        messagebox.showinfo("Fim de Jogo", "Parabéns! Você coletou todas as insígnias e se tornou um campeão Pokémon!")
        root.destroy()

def salvar_jogo():
    if not os.path.exists("pok_insig_data"):
        os.makedirs("pok_insig_data")
    
    with open("pok_insig_data/pokedex.txt", "w") as file:
        for pokemon in pokedex:
            file.write(f"{pokemon[0]}, {pokemon[1]}, {pokemon[2]}, {pokemon[3]}, {pokemon[4]}\n")
    
    with open("pok_insig_data/insignas.txt", "w") as file:
        for insignia in insignias:
            file.write(f"{insignia}\n")
    
    messagebox.showinfo("Salvar Jogo", "Pokédex e Insígnias salvas com sucesso em pok_insig_data!")

def carregar_jogo():
    global pokedex, insignias
    
    if os.path.exists("pok_insig_data"):
        pokedex = []
        with open("pok_insig_data/pokedex.txt", "r") as file:
            for line in file:
                dados_pokemon = line.strip().split(", ")
                pokedex.append([dados_pokemon[0], int(dados_pokemon[1]), int(dados_pokemon[2]), int(dados_pokemon[3]), dados_pokemon[4]])
        
        insignias = []
        with open("pok_insig_data/insignas.txt", "r") as file:
            for line in file:
                insignias.append(line.strip())
        
        messagebox.showinfo("Carregar Jogo", "Pokédex e Insígnias carregadas com sucesso de pok_insig_data!")
        menu_principal()
        verificar_fim_de_jogo()
    else:
        messagebox.showwarning("Carregar Jogo", "Nenhum jogo salvo encontrado.")

root = tk.Tk()
root.title("Aventura Pokémon")

menu_frame = tk.Frame(root, bg="black") 
menu_frame.pack(fill="both", expand=True)

label_bem_vindo = tk.Label(menu_frame, text="", font=("Helvetica", 16))
label_bem_vindo.pack(pady=20)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

btn_ginasio_fogo = ttk.Button(menu_frame, text="Entrar no Ginásio de Fogo", command=lambda: escolher_pokemon(pokemon_fogo, "Ginásio de Fogo" ))
btn_ginasio_fogo.pack(pady=10)

btn_ginasio_agua = ttk.Button(menu_frame, text="Entrar no Ginásio de Água", command=lambda: escolher_pokemon(pokemon_agua, "Ginásio de Água"))
btn_ginasio_agua.pack(pady=10)

btn_ginasio_lendario = ttk.Button(menu_frame, text="Entrar no Ginásio Lendário", command=lambda: escolher_pokemon(pokemon_lendario, "Ginásio Lendário"))
btn_ginasio_lendario.pack(pady=10)

btn_listar_pokedex = ttk.Button(menu_frame, text="Listar Pokémon da Pokédex", command=listar_pokedex)
btn_listar_pokedex.pack(pady=10)

btn_ver_insignias = ttk.Button(menu_frame, text="Ver Insígnias", command=ver_insignias)
btn_ver_insignias.pack(pady=10)

btn_salvar_jogo = ttk.Button(menu_frame, text="Salvar Jogo", command=salvar_jogo)
btn_salvar_jogo.pack(pady=10)

btn_carregar_jogo = ttk.Button(menu_frame, text="Carregar Jogo", command=carregar_jogo)
btn_carregar_jogo.pack(pady=10)

btn_sair = ttk.Button(menu_frame, text="Sair", command=root.quit)
btn_sair.pack(pady=10)

if os.path.exists("savegame.json"):
    carregar_jogo()
else:
    introducao()

root.mainloop()
