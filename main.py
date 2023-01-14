import pyautogui as py


def rodandoAutomacaoYoutube(lista_usuario):
    for musicas in lista_usuario:
        if musicas == lista_usuario[0]:
            iniciando(musicas)
        else:
            adicionandoOutrasMusicas(musicas)
    mostraLista()


def iniciando(musicas):
    py.PAUSE = 4
    py.press('win')
    py.write("google chrome")
    py.press("enter")
    py.click(x=800, y=336)
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


def adicionandoElementoLista(lista_usuario):
    while True:
        nome_artista = input('Artista: ')
        nome_musica = input('Musica: ')

        if nome_artista and nome_musica:
            faixa_musica = f'{nome_artista} - {nome_musica}'
            lista_usuario.append(faixa_musica)

            print('-------------------- ITEM ADICIONADO -----------------------')
            print()
            for i, musicas in enumerate(lista_usuario):
                print(f'{i}-) {musicas}')

            continuar_adicionando = input(
                'Deseja continuar adicionando ? [S] Sim | [N] Não: ')

            match continuar_adicionando:
                case 'S':
                    continue
                case 'N':
                    editarListaCriada(lista_usuario)
                    break
        else:
            print('Alguma coisa aconteceu, por favor, mencione os dois itens')


def removendoElementoLista(lista_usuario):
    while True:
        remove_item_lista = int(input(
            'Especifique o número que gostaria de remover de acordo com sua posição na lista:  '))
        lista_usuario.pop(remove_item_lista)

        for numero_musica, musica in enumerate(lista_usuario):
            print(f'{numero_musica}-) {musica}')

        sair_continuar = input('R-) Remove Item | C-) Confirma Lista:  ')
        if sair_continuar == 'R':
            continue
        else:
            rodandoAutomacaoYoutube(lista_usuario)
            break


def editarListaCriada(lista_usuario):
    print()
    for i, musicas in enumerate(lista_usuario):
        print(f'{i}-) {musicas}')

    editar_lista_usuario = input(
        '[A] Adicionar | [E] Excluir | [C] Confirmar:')

    match editar_lista_usuario:
        case 'A':  # Adicionar Elemento
           adicionandoElementoLista(lista_usuario)

        case 'E':  # Excluir Elemento
            removendoElementoLista(lista_usuario)

        case 'C':  # Confirmar
            rodandoAutomacaoYoutube(lista_usuario)

        case _:    # Caracter não reconhecido
            print('Caracter Não Reconhecido')
            editarListaCriada(lista_usuario)


def mostrarPlaylistCompleta(lista_usuario):
    print()
    for i, musicas in enumerate(lista_usuario):
        print(f'{i}-) {musicas}')

    confirma_lista_criada = input('[C] Confirmar | [E] Editar Lista:  ')

    while True:
        match confirma_lista_criada:
            case 'C':
                rodandoAutomacaoYoutube(lista_usuario)
                break
            case 'E':
                editarListaCriada(lista_usuario)
                break
            case _:    # Caracter não reconhecido
                mostrarPlaylistCompleta(lista_usuario)
                continue


lista_usuario = []
contador_musica = 0

while True:
    nome_artista = input('Artista: ')
    nome_musica = input('Musica: ')

    if nome_artista and nome_musica:
        faixa_musica = f'{nome_artista} - {nome_musica}'
        lista_usuario.append(faixa_musica)
        contador_musica += 1

        if contador_musica > 2:
            finalizar_playlist = input(
                'Pressione [F] caso queira finalizar a playlist: ')

            match finalizar_playlist:
                case 'F':
                    mostrarPlaylistCompleta(lista_usuario)
                    break
                case _:    # Caracter não reconhecido
                    continue
