import pyautogui as py

def automatizaYoutube(lista_musicas):
    for musicas in lista_musicas:
        if musicas == lista_musicas[0]:
            iniciando(musicas)
        else:
            adicionandoOutrasMusicas(musicas)
def iniciando(musicas):
    py.PAUSE = 4
    py.press('win')
    py.write("google chrome")
    py.press("enter")
    py.click(x=857, y=757)
    py.hotkey("ctrl", "t")
    py.write("https://music.youtube.com/")
    py.press("enter")
    py.click(x=874, y=99)
    py.write(f"{musicas}")
    py.press("enter")
    py.click(x=286, y=213)
    py.press("enter")
    py.click(x=1076, y=270)
    py.click(x=1221, y=392)

def adicionandoOutrasMusicas(musicas):
    py.PAUSE = 4
    py.click(x=874, y=99)
    py.hotkey("ctrl", "a")
    py.write(f"{musicas}")
    py.press("enter")
    py.click(x=286, y=213)
    py.press("enter")
    py.click(x=1076, y=270)
    py.click(x=1221, y=392)

def mostraLista():
    py.click(x=1322, y=693)

lista_musicas = []
contador_musicas = 0

while True:

    nome_artista = input('Insira o nome do artista: ')
    nome_musica = input('Insira o nome da musica: ')

    if nome_artista and nome_musica:
        contador_musicas = contador_musicas + 1
        faixa_musica = f'{nome_artista} - {nome_musica}'
        lista_musicas.append(faixa_musica)

    if contador_musicas > 2:
        opcao = input(' [F] Finalizar Lista | [A] Adicionario Itens:')

        if opcao == "A":
            continue
        elif opcao == "F":
            break
        else:
            print('Opção inválida!')
            continue

for numero_musica, musica in enumerate(lista_musicas):
   print(f'{numero_musica}-) {musica}')

opcao = input('R-) Remove Item | C-) Confirma Lista: ')

if opcao == 'R':
    while True:
        remove_item_lista = int(input(
            'Especifique o número que gostaria de remover de acordo com sua posição na lista:  '))
        if remove_item_lista:
            lista_musicas.pop(remove_item_lista)
            novo_tamanho_lista = len(lista_musicas)
            for numero_musica, musica in enumerate(lista_musicas):
                print(f'{numero_musica}-) {musica}')
        sair_continuar = input('R-) Remove Item | C-) Confirma Lista:  ')
        if sair_continuar == 'R':
            continue
        else:
            automatizaYoutube(lista_musicas)
            break
else:
    automatizaYoutube(lista_musicas)

mostraLista()