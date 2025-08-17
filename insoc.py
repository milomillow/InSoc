import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("Pressione qualquer tecla para continuar...")

def mostrar_menu():
    clear_screen()
    print("Menu:\n")
    print("1. SOBRE A BANDA")
    print("2. MEMBROS")
    print("3. ÁLBUM")
    print("4. LISTAS DE MÚSICAS")
    print("5. MENSAGEM SECRETA")
    print("6. SAIR")

def sobre_banda():
    clear_screen()
    print("Information Society é uma banda de synthpop americana, fundada em 1982.")
    esperar_tecla()

def membros():
    clear_screen()
    print("Membros principais:\n- Kurt Harland\n- Paul Robb\n- James Cassidy")
    esperar_tecla()

def album():
    clear_screen()
    print("Álbum de estreia: Information Society (1988)")
    esperar_tecla()

def listas_musicas():
    clear_screen()
    print("Algumas músicas do álbum de estreia:\n- Running\n- What's on Your Mind\n- Repetition")
    esperar_tecla()

def mensagem_secreta():
    clear_screen()
    codigo = input("Digite o código secreto: ")
    if codigo == "2":
        print("Parabéns! Você descobriu a mensagem secreta da banda!")
    else:
        print("Código incorreto. Tente novamente mais tarde.")
    esperar_tecla()

def main():
    clear_screen()
    print("Esta é uma recriação do software promocional do Information Society, criado por MiloMilow.")
    print("Você pode ver o repositório no GitHub. :)")
    esperar_tecla()

    while True:
        mostrar_menu()
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            sobre_banda()
        elif escolha == "2":
            membros()
        elif escolha == "3":
            album()
        elif escolha == "4":
            listas_musicas()
        elif escolha == "5":
            mensagem_secreta()
        elif escolha == "6":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
            esperar_tecla()

if __name__ == "__main__":
    main()
