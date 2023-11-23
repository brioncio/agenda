def incluir (vetor):
    pessoa = {}
    pessoa["nome"]= input ("Informe o nome: ")
    pessoa["email"]= input ("Informe o email: ")
    pessoa["telefone"]= input ("Informe o número de telefone: ")
    
def pesquisar(vetor, nomeBusca):
    posicao = -1
    encontrado = False
    for elemento in vetor:
        posicao = posicao + 1 
        if elemento ["nome"].lower() == nomeBusca.lower():
            encontrado = True 
            break
    if encontrado:
        return posicao
    else:
        return -1
  
def listar(vetor):      
    for elemento in vetor:
        print(f"""{elemento['nome']}\t
                {elemento['email']}
                \t{elemento['telefone']}""")
            