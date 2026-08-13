acervo = []

while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1 — Cadastrar")
    print("2 — Consultar")
    print("3 — Listar")
    print("4 — Remover pelo título")
    print("5 — Mais antigo")
    print("0 — Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        # Cadastrar livro
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação: "))
        
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano
        }
        
        acervo.append(livro)
        print("Livro cadastrado.")
        
    elif opcao == "2":
        # Consultar livro por título 
        if not acervo:
            print("Acervo vazio.")
        else:
            titulo_busca = input("Digite o título que deseja consultar: ").lower()
            encontrado = False
            
            for livro in acervo:
                if livro.get("titulo", "").lower() == titulo_busca:
                    autor = livro.get("autor")
                    ano = livro.get("ano", "Ano não informado")
                    print(f"Autor: {autor} | Ano: {ano}")
                    encontrado = True
                    break
                    
            if not encontrado:
                print("Não está no acervo.")
                
    elif opcao == "3":
        # Listar todos os livros
        if not acervo:
            print("Acervo vazio.")
        else:
            for livro in acervo:
                titulo = livro.get("titulo")
                ano = livro.get("ano", "S/N")
                autor = livro.get("autor")
                print(f"{titulo} ({ano}) - {autor}")
            
            total = len(acervo)
            print(f"Total: {total} livros.")
            
    elif opcao == "4":
        # Remover livro pelo título
        if not acervo:
            print("Acervo vazio.")
        else:
            titulo_remover = input("Digite o título do livro que deseja remover: ").lower()
            removido = False
            
            for livro in acervo:
                if livro.get("titulo", "").lower() == titulo_remover:
                    acervo.remove(livro)
                    print("Livro removido com sucesso.")
                    removido = True
                    break
                    
            if not removido:
                print("Não está no acervo.")
                
    elif opcao == "5":
        # Mostrar o livro mais antigo (menor ano)
        if not acervo:
            print("Acervo vazio.")
        else:
            mais_antigo = acervo[0]
            for livro in acervo:
                if livro.get("ano", float("inf")) < mais_antigo.get("ano", float("inf")):
                    mais_antigo = livro
            
            titulo = mais_antigo.get("titulo")
            ano = mais_antigo.get("ano", "S/N")
            autor = mais_antigo.get("autor")
            print(f"Livro mais antigo: {titulo} ({ano}) - {autor}")
            
    elif opcao == "0":
        # Sair do programa
        print("Encerrando o programa. Até logo!")
        break
        
    else:
        # Opção inválida
        print("Opção que não existe no menu: avisa e mostra o menu de novo, sem quebrar.")