estoque = []

# função para verificar se o produto já existe no estoque
def verificar_codigo(codigo):
    for produto in estoque:
        if produto['codigo'] == codigo:
            return produto
    return None

# adicionar o produto ao estoque
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    codigo = input("Digite o código do produto: ")
    
    # verificar se o produto existe em estoque
    produto_existe = verificar_codigo(codigo)
    
    if produto_existe:
        print(f"O código {codigo} já está vinculado a um produto")
        att_quantidade = input("Deseja atualizar o estoque deste produto? (S/N): ").lower()
            
        # caso o usuário digite outra letra além do 's' ou 'n'
        while att_quantidade != 's' and att_quantidade !='n':
            print("Opção inválida!")
            att_quantidade = input("Deseja atualizar o estoque deste produto? (S/N): ").lower()       
            
        #se o usuario colocar S, o sistema atualiza o estoque e mostra a nova qntd
        if att_quantidade=='s':
            adicional=float(input("Qual a quantidade que deseja inserir?"))
            produto_existe['quantidade'] += adicional
            print(f"Estoque atualizado com sucesso! Novo total: {produto_existe['quantidade']} ")
        else:
            print("Nenhuma quantidade adicionada ao estoque: ")
    else:
        preco=float(input("Preço sugerido para venda: "))
        
        #condicinal que impede o preço seja negativo
        while preco <= 0: 
            print(" Valor inválido para cadastro de produto!")
            preco=float(input("Preço sugerido para venda: "))
            
        quantidade=float(input("Informe a quantidade que deseja cadastrar: "))
        
        #condicional que impede que a quantidade seja negativa
        while quantidade <= 0: 
            print(" Valor inválido para cadastro de produto!")
            quantidade=float(input("Informe a quantidade que deseja cadastrar: "))
        
        #cadastro do produto no dicionario
        produto = {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade}
        estoque.append(produto)
        print("Produto cadastrado com sucesso!")

#construir a tabela do estoque        
def mostrar_tabela():
    #caso o estoque esteja vazio será apresentado ao usuario que não possui estoque disponivel
    if not estoque:
        print("Estoque vazio.")
    else:
        # se tiver itens no estoque irá imprimir uma tabela
        print("* TABELA DE ESTOQUE * ")
        print("Nome          | Código        | Preço         | Quantidade    ")
        
        for produto in estoque:
            print(f"{produto['nome']:<14}| {produto['codigo']:<14}| {produto['preco']:<14}| {produto['quantidade']:<14}")
            
def salvar_arquivo():
    print('-' * 11 + '\nPROCESSANDO\n' + '-' * 11)
    arquivo = open('estoque.txt', 'a')
    arquivo.close()
    arquivo = open('estoque.txt', 'a')
    for v in estoque:
        arquivo.write(f'{v}\n')
    arquivo.close()
    print('O arquivo estoque.txt foi criado e já está atualizado com o estoque!')
    
#não está importando o arquivo, criar função para carregar arquivo?      
def carregar_arquivo():
    with open('estoque.txt','r') as arquivo:
        conteudo=arquivo.read()
    print(conteudo)
    
    
    
    
    print("to com fome")





def menu():
    print("Supermercado - Menu")
    print("1. Cadastrar novo produto")
    print("2. Mostrar tabela")
    print("3. Salvar arquivo")
    print("4. Fazer comprar")
    print("5. Finalizar o dia")
    print("6. Sair")

menu()
op = int(input("Escolha uma opção: "))
while op != 0:
    if op == 1:
        adicionar_produto()
    elif op == 2:
        mostrar_tabela()
    elif op == 3:
        salvar_arquivo()
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        break
    menu()
    op = int(input("Escolha uma opção: "))