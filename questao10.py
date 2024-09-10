    library = []

def exibir_opcoes():
    print("Menu Biblioteca ")
    print("1 - Adicionar livro ")
    print("2 - Listar todos os livros ")
    print("3 - Buscar livro ")

def add_book(library, title, author):
    library.append(title, author)

def list_books(library):
    print(library)

def find_book_by_title(dadosInformados):
    

while True:
    exibir_opcoes()

    opcao = int(input("Escolha uma Opção:"))

    if opcao = 1:
        title = input(print("Digite o nome livro"))
        author = input(print("Digite o nome do Autor"))
        library.add_book(library, title, author)
        elif opcao = 2:
            list_books()
            elif opcao = 3:
                dadosInformados = str(input"Por favor digite o nome do livro ou autor")
                find_book_by_title.find(dadosInformados)


