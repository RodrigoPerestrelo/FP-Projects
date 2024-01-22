#Rodrigo Salvador dos Santos Perestrelo, 106074
#Este documento visa dar as minhas respostas ao enunciado do Projeto2

#Exercício 2.1.1 - TAD Gerador
#O TAD gerador é usado para representar o estado de um gerador de números pseudo-aleatórios xorshift.
#A representação utilizada para um gerador é de uma lista de tamanho 2, onde a primeira posição é ocupada pelos bits e a segunda pela seed/estado.

#Função Cria Gerador (Construtor):

def cria_gerador(bits,seed):
    """
    cria_gerador:(inteiro) x (inteiro) --> (lista)
    A função recebe um inteiro correspondente ao número de bits do gerador (32 ou 64) e um inteiro positivo correspondente à seed ou estado inicial, e devolve
    uma lista, correspondendo ao gerador, na qual a primeira posição é o numero de bits e a segunda a seed.
    """

    if not isinstance(bits,int) or (bits != 32 and bits != 64): #verificação do primeiro argumento, bits
        raise ValueError('cria_gerador: argumentos invalidos')
    if not isinstance(seed,int) or seed<=0 or seed>2**bits: #verificação do segundo argumento, seed
        raise ValueError('cria_gerador: argumentos invalidos')
    return [bits,seed] #lista correspondente ao gerador

#Função Cria Copia Gerador (Construtor):
 
def cria_copia_gerador(gerador):
    """
    cria_copia_gerador:(lista) --> (lista)
    A função recebe uma lista, correspondente ao gerador a ser copiado, e devolve uma lista ,cópia do gerador, ou seja, uma nova lista igual à fornecida.
    """

    bits = gerador[0] #copia-se a variável bits do gerador fornecido
    seed = gerador[1] #copia-se a variável seed do gerador fornecido
    return cria_gerador(bits,seed) #devolve-se a cópia criada do gerador fornecido

#Função Obtem Estado (Seletor):

def obtem_estado(gerador):
    """
    obtem_estado:(lista) --> (inteiro)
    A função recebe uma lista, correspondendo a um gerador, e devolve um inteiro, correspondendo ao estado atual desse gerador, sem o alterar.
    """

    return gerador[1] #devolve a primeira posição da lista, que corresponde à seed (ou estado)

#Função Define Estado (Modificador):

def define_estado(gerador,estado):
    """
    define_estado:(lista) x (inteiro) --> (inteiro)
    A função recebe uma lista, correspondendo ao gerador, e um inteiro, correspondendo a um estado.
    A função define o novo valor do estado do gerador fornecido como sendo o estado fornecido e devolve esse mesmo estado.
    """

    gerador[1] = estado #Modifica o estado do gerador fornecido
    return estado

#Função Atualiza Estado (Modificador):

def atualiza_estado(gerador):
    """
    atualiza_estado:(lista) --> (inteiro)
    A função recebe uma lista, correspondendo ao gerador, e atualiza o estado do gerador fornecido de acordo com o algoritmo xorshift
    de geração de números pseudoaleatórios, e devolvendo-o.
    """

    if gerador[0] == 32: #se o gerador possuir 32 bits
        gerador[1]^= (gerador[1] << 13) & 0xFFFFFFFF           #algoritmo xorshift de geração de números pseudoaleatórios
        gerador[1] ^= (gerador[1] >> 17) & 0xFFFFFFFF
        gerador[1] ^= (gerador[1] << 5) & 0xFFFFFFFF
    if gerador[0] == 64: #se o gerador possuir 64 bits
        gerador[1]^= (gerador[1] << 13) & 0xFFFFFFFFFFFFFFFF   #algoritmo xorshift de geração de números pseudoaleatórios
        gerador[1] ^= (gerador[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= (gerador[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return gerador[1] #devolve a seed (ou estado)

#Função Eh Gerador (Reconhecedor):

def eh_gerador(arg):
    """
    eh_gerador:(universal) --> (booleano)
    A função recebe um argumento qualquer e devolve 'True' caso o seu argumento seja um TAD gerador, ou 'False', caso contrário.
    """

    return isinstance(arg,list) and len(arg) == 2 and\
    isinstance(arg[0],int) and (arg[0] == 32 or arg[0] == 64) and\
    isinstance(arg[1],int) and (arg[1]>0) and (arg[1]<2**32)

#Função Geradores Iguais (Teste):

def geradores_iguais(ger1,ger2):
    """
    geradores_iguais:(lista) x (lista) --> (booleano)
    A função recebe duas listas, correspondendo a dois geradores, e verifica se as duas listas fornecidas são geradores válidos e se são iguais,
    devolvendo 'True' se assim for e 'False' caso contrário.
    """

    return eh_gerador(ger1) and eh_gerador(ger2) and ger1 == ger2   #utiliza-se a função eh_gerador para verificar se são geradores válidos

#Função Gerador Para String (Transformador):

def gerador_para_str(gerador):
    """
    gerador_para_str:(lista) --> (string)
    A função recebe uma lista, correspondendo ao gerador, e devolve a cadeia de carateres que o representa.
    """

    return f'xorshift{gerador[0]}(s={gerador[1]})' #gerador[0] corresponde aos bits e gerador[1] à seed/estado

#Função Gera Numero Aleatório (Função de Alto Nível):

def gera_numero_aleatorio(gerador,int_max):
    """
    gera_numero_aleatorio:(lista) x (inteiro) --> (inteiro) 
    A função recebe uma lista e um inteiro, correspondendo a um gerador e a um inteiro máximo que pode ser gerado. A função atualiza o estado do gerador e devolve 
    um número aleatório no intervalo [1, inteiro máximo], obtido a partir da soma de 1 com o resto da divisão inteira do estado do gerador pelo inteiro máximo fornecido.
    """

    atualiza_estado(gerador)
    return 1+(obtem_estado(gerador)%int_max)

#Função Gera Carater Aleatório (Função de Alto Nível):

def gera_carater_aleatorio(gerador,carat_max):
    """
    gera_carater_aleatorio:(lista) x (string) --> (string)
    A função recebe uma lista e uma string, correspondendo a um gerador e a um caráter maiusculo. A função atualiza o estado do gerador e devolve um caráter maiusculo
    aleatório no intervalo [A,carater máximo], este é obtido como o caráter na posição dada pelo resto da divisão inteira do estado do gerador pelo tamanho da cadeia de
    carateres formada por todos os carateres entre 'A' e o carater máximo fornecido.
    """

    atualiza_estado(gerador)
    return chr((obtem_estado(gerador)%(ord(carat_max)-ord('A')+1))+65) #(ord(carat_max)-ord('A')+1) corresponde ao tamanho da cadeia de carateres formada 
                                                                       #por todos os carateres entre 'A' e o carater máximo fornecido.


#Exercício 2.1.2 TAD Coordenada
#O TAD imutável coordenada é usado para representar a coordenada que ocupa uma parcela em um campo de minas.
#A representação utilizada para uma coordenada é de um tuplo de tamanho 2, onde na primeira posição se encontra a coluna e na segunda a linha.

#Função Cria Coordenada (Construtor):

def cria_coordenada(col,lin):
    """
    cria_coordenada:(string) x (inteiro) --> (tuplo)
    A função recebe uma string (letra maiuscula), correspondente a uma coluna, e um inteiro positivo (entre 1 e 99), correspondendo auma linha, e devolve
    um tuplo correspondente a uma coordenada, na qual a primeira posição é a coluna e a segunda a linha.
    """

    if (not isinstance(col,str)) or (len(col) != 1) or ord(col)<65 or ord(col)>90: #verificação do argumento coluna
        raise ValueError('cria_coordenada: argumentos invalidos')
    if (not isinstance(lin,int)) or (lin<=0) or (lin>99): #verificação do argumento linha
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (col,lin) #tuplo correspondente à coordenada

#Função Obtem Coluna (Seletor):

def obtem_coluna(coordenada):
    """
    obtem_coluna:(tuplo) --> (string)
    A função recebe um tuplo, correspondendo a uma coordenada, e devolve uma string, correspondendo ao caráter da coluna, sem o alterar.
    """

    return coordenada[0] #devolve a primeira posição do tuplo, que corresponde à coluna

#Função Obtem Linha (Seletor):

def obtem_linha(coordenada):
    """
    obtem_linha:(tuplo) --> (inteiro)
    A função recebe um tuplo, correspondendo a uma coordenada, e devolve um inteiro, correspondendo à linha, sem o alterar.
    """

    return coordenada[1] #devolve a segunda posição do tuplo, que corresponde à linha

#Função Eh Coordenada (Reconhecedor):

def eh_coordenada(coordenada):
    """
    eh_coordenada:(universal) --> (booleano)
    A função recebe um argumento qualquer e devolve 'True' caso o seu argumento seja um TAD coordenada, ou 'False', caso contrário.
    """

    return isinstance(coordenada,tuple) and (len(coordenada) == 2) and\
    isinstance(coordenada[0],str) and len(coordenada[0])==1 and (ord(coordenada[0])>=65) and (ord(coordenada[0])<=90) and\
    isinstance(coordenada[1],int) and (coordenada[1]>0) and (coordenada[1]<=99)

#Função Coordenadas Iguais (Teste):

def coordenadas_iguais(coord1,coord2):
    """
    coordenadas_iguais:(lista) x (lista) --> (booleano)
    A função recebe duas listas, correspondendo a duas coordenadas, e verifica se as duas listas fornecidas são coordenadas válidos e se são iguais,
    devolvendo 'True' se assim for e 'False' caso contrário.
    """

    return eh_coordenada(coord1) and eh_coordenada(coord2) and coord1 == coord2 #utiliza-se a função eh_coordenada para verificar se são coordenadas válidas

#Função Coordenada Para String (Transformador):

def coordenada_para_str(coordenada):
    """
    coordenada_para_str:(tuplo) --> (string)
    A função recebe uma lista, correspondendo à coordenada, e devolve a cadeia de carateres que a representa.
    """

    if obtem_linha(coordenada) < 10: #é necessário adicionar um 0 à esquerda do numero, se o mesmo apenas possuir 1 dígito
        return str(coordenada[0]) + str(0) + str(obtem_linha(coordenada))
    if obtem_linha(coordenada) >= 10:
        return str(coordenada[0]) + str(obtem_linha(coordenada))

#Função String Para Coordenada (Transformador):

def str_para_coordenada(str_coordenada):
    """
    str_para_coordenada:(string) --> (tuplo)
    A função recebe uma string, correspondendo a uma cadeia de carateres que representa uma coordenada, e devolve a coordenada representada pela string.
    """

    if str_coordenada[1] == 0: #verifica-se se corresponde a um número de um dígito
        return (str_coordenada[0],int(str_coordenada[2]))
    return (str_coordenada[0],int(str_coordenada[1:])) #utiliza-se slicing para dividir a parte da coluna da parte da linha (da coordenada representada pela string)

#Função Obtem Coordenadas Vizinhas (Função de Alto Nível):

def obtem_coordenadas_vizinhas(coordenada):
    """
    obtem_coordenadas_vizinhas:(tuplo) --> (tuplo)
    A função recebe um tuplo, correspondente a uma coordenada, e devolve um tuplo com as coordenadas vizinhas à coordenada fornecida,
    começando pela coordenada na diagonal acima-esquerda da fornecida e seguindo no sentido horário.
    """

    tup_res = () #o tup_apoio fornece as coordenadas vizinhas, pela ordem pretendida, da coordenada fornecida
    tup_apoio = ((chr(ord(obtem_coluna(coordenada))-1),(obtem_linha(coordenada))),(chr(ord(obtem_coluna(coordenada))-1),(obtem_linha(coordenada)+1)),\
    (chr(ord(obtem_coluna(coordenada))),(obtem_linha(coordenada)+1)),(chr(ord(obtem_coluna(coordenada))+1),(obtem_linha(coordenada)+1)),(chr(ord(obtem_coluna(coordenada))+1),(obtem_linha(coordenada))),\
    (chr(ord(obtem_coluna(coordenada))+1),(obtem_linha(coordenada))-1),(chr(ord(obtem_coluna(coordenada))),(obtem_linha(coordenada))-1),(chr(ord(obtem_coluna(coordenada))-1),(obtem_linha(coordenada)-1)))
    for coord_viz in tup_apoio:
        if eh_coordenada((coord_viz)): #verifica-se se a coordenada vizinha obtida pelo tup_apoio é válida
            tup_res = (coord_viz,) + tup_res
    return tup_res

#Função Obtem Coordenada Aleatória (Função de Alto Nível):

def obtem_coordenada_aleatoria(coord,ger):
    """
    obtem_coordenada_aleatoria:(tuplo) x (lista) --> (tuplo)
    A função recebe um tuplo, correspondendo a uma coordenada, e uma lista, correspondendo a um gerador e devolve uma coordenada gerada aleatoriamente
    como descrito anteriormente. Ou seja, a coordenada fornecida determina a maior coluna e maior linha possíveis.
    """

    coluna = gera_carater_aleatorio(ger,obtem_coluna(coord)) #gera-se o caráter que corresponde à coluna
    linha = gera_numero_aleatorio(ger,obtem_linha(coord)) #gera-se o numero que corresponde à linha
    return cria_coordenada(coluna,linha) #cria-se a coordenada com a coluna e a linha obtidas


#Exercício 2.1.3 TAD Parcela
#O TAD parcela é usado para representar as parcelas de um campo do jogo das minas.
#As parcelas são caracterizadas pela seu estado (tapada, limpa ou marcada) e podem esconder uma mina.
#A representação utilizada para uma parcela é de um dicionáro com duas chaves 'estado' e 'mina', onde os valores de 'estado' podem ser 'tapada', 'limpa', ou
#'marcada' e os valores de 'mina' podem ser 'True' ou 'False'.

#Função Cria Parcela (Construtor):

def cria_parcela():
    """
    cria_parcela:{} --> (dicionário)
    A função devolve um dicionário, correspondendo a uma parcela, cujo estado é 'tapada' e que não possui uma mina escondida.
    """

    return {'estado': 'tapada' , 'mina': False}  #cada parcela é um dicionário cujas chaves são 'estado' e 'mina'

#Função Cria Copia Parcela (Construtor):

def cria_copia_parcela(parcela):
    """
    cria copia parcela:(dicionario) --> (dicionario)
    A função recebe um dicionario, correspondente à parcela a ser copiada, e devolve um dicionario ,cópia da parcela, ou seja, um novo dicionário igual ao fornecido.
    """

    parcela_copia = cria_parcela()
    parcela_copia['estado'] = parcela['estado'] #copia-se o valor da chave 'estado' da parcela fornecida
    parcela_copia['mina'] = parcela['mina']     #copia-se o valor da chave 'mina' da parcela fornecida
    return parcela_copia #devolve-se a cópia criada da parcela fornecida

#Função Limpa Parcela (Modificador):

def limpa_parcela(parcela):
    """
    limpa_parcela:(dicionario) --> (dicionario)
    A função recebe um dicionario, correspondente a uma parcela, e modifica destrutivamente a parcela, modificando o seu estado para limpa. Devolve a própria parcela.
    """

    parcela['estado'] = 'limpa' #Modifica destrutivamente o valor da chave 'estado' da parcela
    return parcela

#Função Marca Parcela (Modificador):

def marca_parcela(parcela):
    """
    marca_parcela:(dicionario) --> (dicionario)
    A função recebe um dicionário, correspondendo a uma parcela, e modifica destrutivamente a parcela, modificando o seu estado para marcada (com uma bandeira).
    Devolve a própria parcela.
    """

    parcela['estado'] = 'marcada' #Modifica destrutivamente o valor da chave 'estado' da parcela
    return parcela

#Função Desmarca Parcela (Modificador):

def desmarca_parcela(parcela):
    """
    desmarca_parcela:(dicionario) --> (dicionario)
    A função recebe um dicionário, correspondendo a uma parcela, e modifica destrutivamente a parcela, modificando o seu estado para tapada. Devolve a própria parcela.
    """

    parcela['estado'] = 'tapada' #Modifica destrutivamente o valor da chave 'estado' da parcela
    return parcela

#Função Esconde Mina (Modificador):

def esconde_mina(parcela):
    """
    esconde_mina:(dicionario) --> (dicionario)
    A função recebe um dicionário, correspondendo a uma parcela, e modifica destrutivamente a parcela, escondendo uma mina na parcela. Devolve a própria parcela.
    """

    parcela['mina'] = True #Modifica destrutivamente o valor da chave 'mina' da parcela
    return parcela

#Função Eh Parcela (Reconhecedor):

def eh_parcela(arg):
    """
    eh_parcela:(universal) --> (booleano)
    A função recebe um argumento qualquer e devolve 'True' caso o seu argumento seja um TAD parcela, ou 'False', caso contrário.
    """

    return isinstance(arg,dict) and (len(arg) == 2) and ('estado' in arg) and ('mina' in arg)\
    and (type(arg['estado']) == str) and (arg['estado'] == 'tapada' or arg['estado'] == 'limpa' or arg['estado'] == 'marcada')\
    and (type(arg['mina']) == bool) and (arg['mina'] == True or arg['mina'] == False)

#Função Eh Parcela Tapada (Reconhecedor):

def eh_parcela_tapada(parcela):
    """
    eh_parcela_tapada:(dicionario) --> (booleano)
    A função recebe um dicionário, correspondente a uma parcela, e devolve 'True' caso a parcela se encontre tapada, ou False caso contrário.
    """

    return parcela['estado'] == 'tapada'

#Função Eh Parcela Marcada (Reconhecedor):

def eh_parcela_marcada(parcela):
    """
    eh_parcela_marcada:(dicionario) --> (booleano)
    A função recebe um dicionário, correspondente a uma parcela, e devolve 'True' caso a parcela se encontre marcada com uma bandeira, ou False caso contrário.
    """

    return parcela['estado'] == 'marcada'

#Função Eh Parcela Limpa (Reconhecedor):

def eh_parcela_limpa(parcela):
    """
    eh_parcela_limpa:(dicionario) --> (booleano)
    A função recebe um dicionário, correspondente a uma parcela, e devolve 'True' caso a parcela se encontre limpa, ou False caso contrário.
    """

    return parcela['estado'] == 'limpa'

#Função Eh Parcela Minada (Reconhecedor):

def eh_parcela_minada(parcela):
    """
    eh_parcela_minada:(dicionario) --> (booleano)
    A função recebe um dicionário, correspondente a uma parcela, e devolve 'True' caso a parcela esconda uma mina, ou False caso contrário.
    """

    return parcela['mina'] == True

#Função Parcelas Iguais (Teste):

def parcelas_iguais(parc1,parc2):
    """
    parcelas_iguais:(dicionario) x (dicionario) --> (booleano)
    A função recebe dois dicionários, correspondendo a duas parcelas, e verifica se os dois dicionarios fornecidos são parcelas válidas e se são iguais,
    devolvendo 'True' se assim for e 'False' caso contrário.
    """

    return (eh_parcela(parc1) and eh_parcela(parc2) and (parc1 == parc2)) #utiliza-se a função eh_parcela para verificar se são parcelas válidas

#Função Parcela Para String (Transformador):

def parcela_para_str(parcela):
    """
    parcela_para_str:(dicionario) --> (string)
    A função recebe um dicionario, correspondendo a uma parcela, e devolve a cadeia de caracteres que representa a parcela em função do seu estado:
    parcelas tapadas ('#'), parcelas marcadas ('@'), parcelas limpas sem mina ('?') e parcelas limpas com mina ('X').
    """

    if eh_parcela_tapada(parcela): return '#'
    if eh_parcela_marcada(parcela): return '@'
    if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela): return '?'
    if eh_parcela_limpa(parcela) and eh_parcela_minada(parcela): return 'X'

#Função Alterna Bandeira (Função de Alto Nivel):

def alterna_bandeira(parcela):
    """
    alterna_bandeira:(dicionario) --> (booleano)
    A função recebe um dicionario, correspondente a uma parcela, e modifica-a destrutivamente da seguinte forma:
    desmarca se estiver marcada e marca se estiver tapada, devolvendo 'True'. Em qualquer outro caso, não modifica a parcela e devolve 'False'.
    """

    if eh_parcela_marcada(parcela): #desmarca se estiver marcada
        desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela): #marca se estiver tapada
        marca_parcela(parcela)
        return True
    return False


#Exercício 2.1.4 TAD Campo
#O TAD campo é usado para representar o campo de minas do jogo das minas.
#A representação utilizada para um campo de minas é de uma lista, que contém listas, onde cada uma é de tamanho dois, possuindo na primeira posição
#um tuplo coordenada, conforme especificado anteriormente, e na segunda posição um dicionário parcela, conforme especificado anteriormente.

#Função Cria Campo (Construtor):

def cria_campo(col_final,lin_final):
    """
    cria_campo:(string) x (inteiro) --> (lista)
    A função recebe uma string, correspondente ao carater da coluna final do campo de minas, e um inteiro positivo (de 1 a 99), correspondentes à linha final do campo
    de minas, e devolve o campo do tamanho pretendido formado por parcelas tapadas sem minas.
    """

    if (not isinstance(col_final,str)) or (len(col_final) != 1) or ord(col_final)<65 or ord(col_final)>90: #verificação do argumento coluna
        raise ValueError('cria_campo: argumentos invalidos')
    if (not isinstance(lin_final,int)) or (lin_final<=0) or (lin_final>99): #verficação do argumento linha
        raise ValueError('cria_campo: argumentos invalidos')
    
    campo = [] #campo é uma lista de listas, onde cada uma tem tamanho dois. Na primeira posição encontra-se o tuplo da coordenada e na segunda posição encontra-se o dicionário da parcela.
    for contador_linha in range(1,lin_final+1): #é necessário adicionar 1 para que inclua a ultima linha (ou coluna) pretendida
        for contador_col in range(65,ord(col_final)+1): #65 corresponde à ord da letra 'A'; 
            campo += [[cria_coordenada(chr(contador_col),contador_linha),cria_parcela()]] #utiliza-se chr para converter o numero da ordem para a letra maiscula pretendida
    return campo

#Função Cria Copia do Campo (Construtor):

def cria_copia_campo(campo):
    """
    cria_copia_campo:(lista) --> (lista)
    A função recebe uma lista, correspondente a um campo a ser copiada, e devolve uma lista ,cópia do campo, ou seja, uma nova lista igual à fornecida.
    """

    copia_campo = [] #tenha-se como célula cada coordenada e sua respetiva parcela, ou seja, cada lista que possui um tuplo coordenada e um dicionario parcela
    for celula in campo: #criam-se células iguais às células do campo fornecido, uma a uma
        copia_campo += [[celula[0],cria_copia_parcela(celula[1])]]
    return copia_campo #devolve-se a cópia criada do campo fornecida

#Função Obtem Ultima Coluna (Seletor):

def obtem_ultima_coluna(campo):
    """
    obtem_ultima_coluna:(lista) --> (string)
    A função recebe uma lista, correspondente a um campo, e devolve a cadeia de carateres que corresponde à última coluna do campo de minas.
    """

    return campo[-1][0][0] #acede-se à ultima célula do campo, ao tuplo (coordenada) da célula, e, por fim, à coluna da coordenada

#Função Obtem Ultima Linha (Seletor):

def obtem_ultima_linha(campo):
    """
    obtem_ultima_coluna:(lista) --> (inteiro)
    A função recebe uma lista, correspondente a um campo, e devolve o valor inteiro que corresponde à última linha do campo de minas.
    """

    return campo[-1][0][1]  #acede-se à ultima célula do campo, ao tuplo (coordenada) da célula, e, por fim, à linha da coordenada

#Função Obtem Parcela (Seletor):

def obtem_parcela(campo,coord):
    """
    obtem_parcela:(lista) x (tuplo) --> (dicionario)
    A função recebe uma lista, correspondente a um campo, e um tuplo, correspondente a uma coordenada, e devolve a parcela do campo que se encontra na coordenada fornecida.
    """

    for celula in campo: #procura-se célula a célula do campo
        if celula[0] == coord: #até se achar a célula que possui a coordenada fornecida
            return celula[1] #retornamos a parcela

#Função Obtem Coordenadas (Seletor):

def obtem_coordenadas(campo,estado):
    """
    obtem_coordenadas:(lista) x (string) --> (tuplo)
    A função recebe uma lista, correspondente a um campo, e uma string, e devolve o tuplo formado pelas coordenadas (ordenadas em ordem ascendente da esquerda à direita e de cima para baixo)
    das parcelas dependendo da string fornecida:
    'limpas' para as parcelas limpas;
    'tapadas' para as parcelas tapadas;
    'marcadas' para as parcelas marcadas;
    e 'minadas' para as parcelas que escondem minas.
    """

    tup_res = ()
    for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1): #65 é ordem de A, ou seja, da coluna A à coluna limite do campo
        for contador_linha in range(1,obtem_ultima_linha(campo)+1): #da linha 1 à linha limite do campo
            for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1): #adiciona-se sempre 1 no range para que a linha ou coluna 'limite' também seja contabilizada
                if estado == 'minadas':
                    if eh_parcela_minada(obtem_parcela(campo,cria_coordenada(chr(contador_col),contador_linha))): #se a parcela tinha valor 'True' no 'mina'
                        tup_res += (cria_coordenada(chr(contador_col),contador_linha),)
                elif estado == 'tapadas':
                    if eh_parcela_tapada(obtem_parcela(campo,cria_coordenada(chr(contador_col),contador_linha))): #se a parcela tinha valor 'tapada' no 'estado'
                        tup_res += (cria_coordenada(chr(contador_col),contador_linha),)
                elif estado == 'marcadas':
                    if eh_parcela_marcada(obtem_parcela(campo,cria_coordenada(chr(contador_col),contador_linha))): #se a parcela tinha valor 'marcada' no 'estado'
                        tup_res += (cria_coordenada(chr(contador_col),contador_linha),)
                elif estado == 'limpas':
                    if eh_parcela_limpa(obtem_parcela(campo,cria_coordenada(chr(contador_col),contador_linha))): #se a parcela tinha valor 'limpa' no 'estado'
                        tup_res += (cria_coordenada(chr(contador_col),contador_linha),)
        return tup_res #devolve-se o tuplo das coordenadas conforme o critério solicitado para as parcelas

#Função Obtem Numero Minas Vizinhas (Seletor):

def obtem_numero_minas_vizinhas(campo,coord):
    """
    obtem_numero_minas_vizinhas:(lista) x (tuplo) --> (inteiro)
    A função recebe uma lista, correspondente a um campo, e um tuplo, correspondente a uma coordenada, e devolve o número de parcelas vizinhas da parcela na
    coordenada fornecida que escondem uma mina.
    """

    cont_minas = 0
    for coord in obtem_coordenadas_vizinhas(coord): #verifica-se coordenada a coordenada das coordenadas vizinhas
        if ord(obtem_ultima_coluna(campo))>=ord(obtem_coluna(coord)) and obtem_ultima_linha(campo)>=obtem_linha(coord): #se for uma coordenada válida no campo fornecido
            if eh_parcela_minada(obtem_parcela(campo,coord)): #e se a sua parcela possuir uma mina
                cont_minas += 1
    return cont_minas

#Função Eh Campo (Reconhecedor):

def eh_campo(campo):
    """
    eh_campo:(universal) --> (booleano)
    A função recebe um argumento qualquer e devolve 'True' caso o seu argumento seja um TAD parcela, ou 'False', caso contrário.
    """

    if (not isinstance(campo,list)) or (len(campo)<1) or (len(campo)>2574): #verifica-se se é uma lista e se o seu tamanho está entre 1 e o máximo de células possivéis(26x99)
        return False
    for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1):
        for contador_linha in range(1,obtem_ultima_linha(campo)+1):
            for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1): 
                if (ord(obtem_ultima_coluna(campo))-64) == (obtem_ultima_linha(campo)): #o campo não pode ser quadrado
                    return False
                if (not eh_coordenada(cria_coordenada(chr(contador_col),contador_linha))): #verificam-se se as coordenadas são válidas
                    return False
                if (not eh_parcela(obtem_parcela(campo,cria_coordenada(chr(contador_col),contador_linha)))): #verificam-se as parcelas são válidas
                    return False
    return True

#Função Eh Coordenada do Campo (Reconhecedor):

def eh_coordenada_do_campo(campo,coord):
    """
    eh_coordenada_do_campo:(lista) x (tuplo) --> (booleano)
    A função recebe uma lista, correspondente a um campo, e recebe um tuplo, correspondente a uma coordenada, e devolve 'True' se a coordenada fornecida
    é uma coordenada válida dentro do campo fornecido, ou 'False' caso contrário.
    """

    return (ord(obtem_coluna(coord)))<=(ord(obtem_ultima_coluna(campo))) and (obtem_linha(coord)<=obtem_ultima_linha(campo)) #verifica-se se a sua coluna e linha fazem parte do campo

#Função Campos Iguais (Teste):

def campos_iguais(campo1,campo2):
    """
    campos_iguais:(lista) x (lista) --> (booleano)
    A função recebe duas listas, correspondendo a dois campos, e verifica se as duas listas fornecidas são campos válidas e se são iguais,
    devolvendo 'True' se assim for e 'False' caso contrário.
    """

    return eh_campo(campo1) and eh_campo(campo2) and (campo1 == campo2) #utiliza-se a função eh_campo para verificar se são campos válidos

#Função Campo para String (Transformador):

def campo_para_str(campo):
    """
    campo_para_str:(lista) --> (string)
    A função recebe uma lista, correspondendo a um campo, e devolve uma cadeia de caracteres que representa o campo de minas.
    """

    str_letras_col = '' #string das letras de cada coluna
    cont_linhas = 0
    str_jogo = '' #string que possui os caráteres representativos de cada celula
    ult_linha = obtem_ultima_linha(campo)
    ult_col = ord(obtem_ultima_coluna(campo))
    num_ult_col = ult_col-64 #dimensão de uma fila; -64 = +1 -65; por exemplo, numero de letras de A a D --> ord(D) - ord(A) +1 --> 68-65+1
    num_prim_col = 0


    while cont_linhas != ult_linha: #enquanto não se verificar todas as linhas
        if (cont_linhas) < 9:
            str_jogo += str(0) + str(cont_linhas+1) + '|' #se o numero da linha tiver apenas um digito, colocamos um zero à sua esquerda
        if (cont_linhas) >= 9:
            str_jogo += str(cont_linhas+1) + '|'
        for celula in campo[num_prim_col:num_ult_col]: #avaliamos as células de cada respetiva fila
            if obtem_coluna(celula[0]) not in str_letras_col: str_letras_col += obtem_coluna(celula[0]) #para se obter todas as letras correspondentes a colunas
            if obtem_coluna(celula[0]) == obtem_ultima_coluna(campo): #se for a ultima célula da fila a ser avaliada, temos que adicionar um '|'
                if eh_parcela_limpa(celula[1]) and obtem_numero_minas_vizinhas(campo,celula[0]) > 0 and not (eh_parcela_minada(celula[1])):
                    str_jogo += str(obtem_numero_minas_vizinhas(campo,celula[0])) + '|\n'
                elif eh_parcela_limpa(celula[1]) and obtem_numero_minas_vizinhas(campo,celula[0]) == 0 and not(eh_parcela_minada(celula[1])):
                    str_jogo += ' |\n'
                else: str_jogo += parcela_para_str(celula[1]) + '|\n'
            else:
                if eh_parcela_limpa(celula[1]) and obtem_numero_minas_vizinhas(campo,celula[0]) > 0 and not (eh_parcela_minada(celula[1])):
                    str_jogo += str(obtem_numero_minas_vizinhas(campo,celula[0]))
                elif eh_parcela_limpa(celula[1]) and obtem_numero_minas_vizinhas(campo,celula[0]) == 0 and not (eh_parcela_minada(celula[1])):
                    str_jogo += ' '
                else: str_jogo += parcela_para_str(celula[1])
        num_prim_col += ult_col-64 #atualiza-se a primeira célula a ser avaliada (nova fila)
        num_ult_col += ult_col-64 #atualiza-se a ultima célula a ser avaliada (nova fila)
        cont_linhas +=1
        
    str_linhas = '+' + (len(str_letras_col)*'-') + '+'
    return '   ' + str_letras_col + '\n' + '  ' + str_linhas + '\n' + str_jogo + '  ' + str_linhas #por fim juntamos as strings na ordem desejada e c os devidos espaços

#Função Coloca Minas (Função de Alto Nível):

def coloca_minas(campo,coord,ger,n_minas):
    """
    coloca_minas:(lista) x (tuplo) x (lista) x (inteiro) --> (lista)
    A função recebe uma lista, correspondente a um campo, um tuplo, correspondente a uma coordenada, uma lista, correspondente a um gerador e um inteiro, correspondente ao
    numero de minas a colocar, por esta ordem. A função modifica destrutivamente o campo, escondendo o numero de minas fornecido em parcelas dentro do campo.
    As coordenadas das minas são geradas em sequencia, utilizando o gerador fornecido, de modo a que não coincidam com a coordenada fornecida nem com nenhuma
    vizinha desta, nem se sobreponham com minas colocadas anteriormente.
    """

    cont_min_col = 0
    tup_coord_ger = () #para sabermos em que coordenadas já foram colocadas minas
    while cont_min_col < n_minas: #enquanto todas as minas nao forem colocadas
        c1 = (obtem_coordenada_aleatoria((obtem_ultima_coluna(campo),(obtem_ultima_linha(campo))),ger)) #coordenada gerada
        if  c1 != coord and (c1 not in obtem_coordenadas_vizinhas(coord)) and (c1 not in tup_coord_ger): #se não coincir com a coordenada fornecida, nem com nenhuma vizinha desta, nem se sobrepor com minas colocadas anteriormente
            esconde_mina(obtem_parcela(campo,c1))
            tup_coord_ger += (c1,) #adiciona-se a coordenada de onde foi colocada a mina a tuplo, para que não voltemos a colocar mina nesta coordenada
            cont_min_col +=1
    return campo

#Função Limpa Campo (Função de Alto Nível):

def limpa_campo(campo,coord):
    """
    limpa_campo:(lista) x (tuplo) --> (lista)
    A função recebe uma lista, correspondente a um campo, e um tuplo, correspondente a uma coordenada, e modifica destrutivamente o campo, limpando a parcela
    na coordenada fornecida, devolvendo-o.
    Se não houver nenhuma mina vizinha escondida, limpa iterativamente todas as parcelas vizinhas tapadas. Caso a parcela se encontre já limpa, a operação não tem efeito.
    """

    if not eh_parcela_limpa(obtem_parcela(campo,coord)): #Se a parcela da coordenada dada não se encontra já limpa
        limpa_parcela(obtem_parcela(campo,coord))
        if obtem_numero_minas_vizinhas(campo,coord) == 0 and not eh_parcela_minada(obtem_parcela(campo,coord)): #se a parcela que limpamos não for minada e não possuir minas nas parcelas vizinhas
            for coordenada in obtem_coordenadas_vizinhas(coord): #para cada coordenada vizinha
                if eh_coordenada_do_campo(campo,coordenada) and not eh_parcela_marcada(obtem_parcela(campo,coordenada)): #limpamos as parcelas vizinhas e as suas vizinhas...etc até não ser mais possível
                    limpa_campo(campo,coordenada)
                    if not eh_parcela_limpa(obtem_parcela(campo,coord)) and not eh_parcela_marcada(obtem_parcela(campo,coordenada)): #limpamos apenas a parcela se a mesma não estiver marcada ou não estiver já limpa
                        limpa_parcela(obtem_parcela(campo,coordenada))
    return campo


#Exercício 2.2.1 - Funções Adicionais

#Função Jogo Ganho:

def jogo_ganho(campo):
    """
    jogo_ganho:(lista) --> (booleano)
    A função recebe uma lista, correspondente a um campo do jogo das minas, e devolve 'True' se todas as parcelas sem minas se encontram limpas, ou 'False' caso contrário.
    """

    for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1):
        for contador_linha in range(1,obtem_ultima_linha(campo)+1):
            for contador_col in range(65,ord(obtem_ultima_coluna(campo))+1): #verificamos para todas as celulas do campo
                if not eh_parcela_minada(obtem_parcela(campo,(cria_coordenada(chr(contador_col),contador_linha)))): #se não for uma parcela com mina
                    if not eh_parcela_limpa(obtem_parcela(campo,(cria_coordenada(chr(contador_col),contador_linha)))): #se não estiver limpa
                        return False 
    return True


#Exercício 2.2.2 - Funções Adicionais

#Função Turno Jogador:

def turno_jogador(campo):
    """
    turno_jogador:(lista) --> (booleano)
    A função recebe uma lista, correspondente a um campo de minas, e oferece ao jogador a opção de escolher uma ação e uma coordenada a aplicar essa ação.
    A função modifica destrutivamente o campo, de acordo com ação escolhida([Des]Marcar ou Limpar), devolvendo 'False' caso o jogador tenha limpo uma parcela que continha uma mina,
    ou True caso contrário.
    """

    acao = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while acao != 'L' and acao != 'M': #até o jogador inserir uma letra válida, correspondente a uma ação
        acao = input('Escolha uma ação, [L]impar ou [M]arcar:')
    coord = input('Escolha uma coordenada:') #até o jogador inserir uma coordenada válida no campo dado
    while len(coord)!= 3  or ord(coord[0])<65 or ord(coord[0])>90 or ord(coord[1]) < 48 or ord(coord[1]) > 57 or ord(coord[2]) < 48 or ord(coord[2]) > 57\
    or not eh_coordenada(str_para_coordenada(coord)) or not eh_coordenada_do_campo(campo,str_para_coordenada(coord)):
        coord = input('Escolha uma coordenada:')
    coord = str_para_coordenada(coord)

    #obtem-se assim a ação e a coordenada a aplicar essa ação

    if acao == 'L': #se a ação for Limpar
        if eh_parcela_minada(obtem_parcela(campo,coord)): #se for parcela minada a ser limpa, devolve-se 'False'
            limpa_campo(campo,coord)
            return False
        else:
            limpa_campo(campo,coord)
            return True
    if acao == 'M': #se a ação for (Des)Marcar
        alterna_bandeira(obtem_parcela(campo,coord))
        return True


#Exercicio 2.2.3 - Funções Adicionais

#Função Minas:

def minas(caract_c,ult_l,n_minas,dim_ger,seed):
    """
    minas:(string) x (inteiro) x (inteiro) x (inteiro) x (inteiro) --> (booleano)
    Esta função é a função principal que permite jogar ao jogo das minas.
    A função recebe uma string, correspondente à ultima coluna do campo, e 4 valores inteiros correspondendo, respetivamente, a: última linha do campo; ao número
    de parcelas com minas; dimensão de um gerador de números d; e estado inicial (ou seed) para a geração de números aleatórios.
    A função devolve 'True' se o jogador conseguir ganhar o jogo (limpar todas as parcelas não minadas), ou 'False' caso contrário. 
    """

    #criar o gerador do campo
    if not isinstance(dim_ger,int) or (dim_ger != 32 and dim_ger != 64):
        raise ValueError('minas: argumentos invalidos')
    if not isinstance(seed,int) or seed<=0 or seed>2**dim_ger:
        raise ValueError('minas: argumentos invalidos')

    gerador = cria_gerador(dim_ger,seed)
    if not eh_gerador(gerador):
        raise ValueError('minas: argumentos invalidos')
    
    #verificar se o numero de minas fornecido é valido
    if not isinstance(n_minas,int) or (n_minas<1):# or n_minas>(((ord(caract_c)-64)*ult_l)-((len(obtem_coordenadas_vizinhas(coord)))+1)):
        raise ValueError('minas: argumentos invalidos')
    
    #criar o campo de jogo
    if (not isinstance(caract_c,str)) or (len(caract_c) != 1) or ord(caract_c)<65 or ord(caract_c)>90:
        raise ValueError('minas: argumentos invalidos')
    if (not isinstance(ult_l,int)) or (ult_l<=0) or (ult_l>99):
        raise ValueError('minas: argumentos invalidos')

    campo = cria_campo(caract_c,ult_l)
    if not eh_campo(campo):
        raise ValueError('minas: argumentos invalidos')

    cont_bandeiras = 0

    print((f'   [Bandeiras {cont_bandeiras}/{n_minas}]')) #imprime pela primeira vez o numero de bandeiras e o campo de jogo, sem minas
    print(campo_para_str(campo))

    coord = input('Escolha uma coordenada:') #pedimos uma primeira coordenada ao utilizador, para, a partir dela, colocar as minas no campo
    while len(coord)!= 3  or ord(coord[0])<65 or ord(coord[0])>90 or ord(coord[1]) < 48 or ord(coord[1]) > 57 or ord(coord[2]) < 48 or ord(coord[2]) > 57\
    or not eh_coordenada(str_para_coordenada(coord)) or not eh_coordenada_do_campo(campo,str_para_coordenada(coord)):
        coord = input('Escolha uma coordenada:') #pedimos a coordenada enquanto o utilizador não fornecer uma válida
    coord = str_para_coordenada(coord)

    #colocar as minas no campo
    coloca_minas(campo,coord,gerador,n_minas)

    limpa_campo(campo,coord)
    while not jogo_ganho(campo):
        cont_bandeiras = len(obtem_coordenadas(campo,'marcadas'))
        print((f'   [Bandeiras {cont_bandeiras}/{n_minas}]'))
        print(campo_para_str(campo))
        turno_jogador(campo)
        if jogo_ganho(campo):
            cont_bandeiras = len(obtem_coordenadas(campo,'marcadas'))
            print((f'   [Bandeiras {cont_bandeiras}/{n_minas}]'))
            print(campo_para_str(campo))
            print('VITORIA!!!')
            return True
        for coordenada in obtem_coordenadas(campo,'minadas'): #se houver parcelas minadas e limpas, perde-se o jogo
            if eh_parcela_limpa(obtem_parcela(campo,coordenada)):
                cont_bandeiras = len(obtem_coordenadas(campo,'marcadas'))
                print((f'   [Bandeiras {cont_bandeiras}/{n_minas}]'))
                print(campo_para_str(campo))
                print('BOOOOOOOM!!!')
                return False