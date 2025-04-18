
def validateInt(question, min, max):
   option = int(input(question))
   while((option < min) or (option > max)):
        option = int(input(question))
   return option     

def createArchive(fileName):
    try:
        game = open(fileName, "wt+")
        game.close()
    except:
        print("Erro na criação do arquivo.")
    else:
        print(f"Arquivo {fileName} criado com sucesso.")

def existArchive(fileName):
    try:
        game = open(fileName, "rt")
        game.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def listArchive(fileName):
    try:
        game = open(fileName, "rt")
    except:
        print("Erro ao ler arquivo")
    else:
        print(game.read())
    finally:
        game.close()            


def registerGame(archive,gameName,videoGameName):
    try:
        game = open(archive, "at")
    except:
        print("Erro ao abrir o arquivo")
    else:
        game.write(f"{gameName}:{videoGameName}\n")
    finally:
        game.close()    

    
archive = "game.txt"
if existArchive(archive):
    print("Arquivo localizado no computador")
else:
    print("Arquivo inexistente")
    createArchive(archive)


while True:
     print (" Cadastro de jogos ")    
     print ("1 - Cadastrar novo jogo")
     print ("2 - Listar jogos cadastrados")
     print ("3 - sair")

     option = validateInt("Escolha a opção desejada: ", 1, 3)
     if option == 1:
         print("Cadastrar novo jogo selecionado...")    
         gameName = input("Informe o jogo: ")  
         videoGameName = input("Informe seu video Game: ") 
         registerGame(archive,gameName, videoGameName)

     elif option == 2:
         print("Listar jogos cadastrados selecionados...")
         listArchive(archive)
         
     elif option ==3:
         print('Encerrando programa...')
         break
         