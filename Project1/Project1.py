#Rodrigo Salvador dos Santos Perestrelo, 106074
#Este documento visa dar as minhas respostas ao enunciado do Projeto1

#Primeiro Exercício - Justificação de textos:

#Função 1.2.1 - Limpa Texto:

def limpa_texto(texto):
    """
    limpa_texto:(cad.carateres) --> (cad.carateres)
    A função recebe uma cadeia de carateres qualquer e, através das funções built in .split e .join, retomamos a cadeia de carateres
    sem os carateres brancos, com as palavras separadas pelo carater espaço.
    """
    
    texto = texto.split() #A divisão da string original é feita sempre que se encontra o caráter espaço
    texto_limpo = " ".join(texto)
    return (texto_limpo) #Retornamos assim a cadeia de carateres limpa, apenas com um caratér espaço a separar as palavras.


#Função 1.2.2 - Corta Texto:

def corta_texto(texto_limpo,larg_col):
    """
    corta_texto:(cad.carateres) x (inteiro) --> (cad.carateres) x (cad_carateres)
    A função recebe uma cadeia de carateres limpa e um inteiro positivo, largura da coluna, e devolve duas subcadeias de
    carateres limpa. A primeira subcadeia com palavras completas até à largura máxima da coluna fornecida e a segunda com
    o restante texto de entrada.
    """

    tup = ()
    if larg_col >= len(texto_limpo): #se a largura for superior ao tamanho da cadeia limpa
        tup += (texto_limpo, '')
        return tup
    elif (texto_limpo[larg_col-1] == ' '): #se o ultimo carater da cadeia for um espaço
        tup = tup + (texto_limpo[0:larg_col-1], texto_limpo[larg_col:])
        return tup
    else:
        while (larg_col-1 >= 0):
            if (texto_limpo[larg_col-1] == ' ') and (larg_col-1 > 0): #objetivo de encontrar um carater espaço para dividir cadeia
                tup = tup + (texto_limpo[0:larg_col-1], texto_limpo[larg_col:])
                return tup
            elif (larg_col-1) == 0: #se apenas se puder dividir a cadeia no início da mesma
                tup = tup +  ('',texto_limpo)
                return tup
            else:
                larg_col -= 1 #ao diminuir a largura máxima da coluna, procuramos um carater espaço antecedente para dividir a cadeia


#Função 1.2.3 - Insere Espaços:

def insere_espacos(texto_limpo,larg_col):
    """
    insere_espaços:(cad.carateres) x (inteiro) --> (cad.carateres)
    A função recebe uma cadeia de carateres correspondente a um texto limpo e um inteiro positivo, largura máxima da coluna.
    Se a cadeia possuir uma unica palavra, devolve a palavra com espaços à direita da mesma até atingir a largura pretendida.
    Se a cadeia possuir mais q uma palavra, devolve a cadeia de palavras com espaços entre as palavras até atingir a largura pretendida.
    """

    texto_limpo = limpa_texto(texto_limpo) #temos a certeza q a cadeia de carateres se encontra limpa
    l_pal = texto_limpo.split(' ') #cada palavra é um elemento da lista
    n_pal = len(l_pal) #numero de palavras da cadeia de carateres
    n_espacos = 0
    if (n_pal == 1):
        while len(texto_limpo) < larg_col: #quando tem apenas uma palavra, inserem-se espaços à sua direita
            texto_limpo += ' '
        return texto_limpo
    else:
            n_espacos = ((larg_col+(n_pal-1)) - len(texto_limpo)) #calcular o numero de espaços a colocar no meio das palavras
            while n_espacos > 0: 
                for x in range(len(l_pal)-1): #para colocar um espaço à direita de cada elemento da lista (ou seja, entre duas palavras), um de cada vez, no sentido da esquerda para a direita
                    l_pal[x] = l_pal[x] + ' '
                    n_espacos -= 1
                    if (n_espacos == 0): #acaba quando não há mais espaços a colocar
                        break
    texto_limpo = ''.join(l_pal) #para juntar a lista de palavras(já com os espaços inseridos)
    return texto_limpo


#Função 1.2.4 - Justifica Texto:

def justifica_texto(texto,larg_col):
    """
    justifica_texto: (cad.carateres) x (inteiro) --> (tuplo)
    A função recebe uma cadeia de carateres não vazia, correspondente a um texto, e um inteiro positivo, largura máxima da coluna.
    Devolve um tuplo de cadeias de carateres justificadas, de comprimento igual à largura máxima da coluna.
    Para tal acrescenta-se carateres espaço no meio das palavras ou à sua direita, conforme descrito nas funções anteriores.
    """

    texto = limpa_texto(texto) #limpa-se os carateres brancos
    tup_texto_f = ()

    if (larg_col <= 0) or (type(larg_col) != int):
        raise ValueError ("justifica_texto: argumentos invalidos")
    if (type(texto) != str) or (len(texto) == 0):
        raise ValueError ("justifica_texto: argumentos invalidos")
    for palavra in (texto.split(' ')):
        if (len(palavra) > larg_col):
            raise ValueError ("justifica_texto: argumentos invalidos")
    
    while (len(texto) > larg_col): #enquanto for possível fazer linhas "completas", ou seja, no final pode ocorrer que não se tenha uma linha do tamanho da coluna 
            tup_texto = corta_texto(texto,larg_col+1) #corta-se o texto conforme descrito anteriormente
            linha_cortada = tup_texto[0]
            linha_cortada = insere_espacos(linha_cortada,larg_col) #insere-se espaços conforme descrito anteriormente
            tup_texto_f = tup_texto_f + (linha_cortada,)
            texto = tup_texto[1] #para se considerar apenas o texto que ainda não foi cortado
    while len(texto) != (larg_col): #para corrijir a possibilidade da ultima linha não ser do tamanho da largura da coluna, acrescenta-se carateres espaço à sua direita
            texto += ' '
    tup_texto_f = tup_texto_f + (texto,)
    return tup_texto_f




#Segundo Exercício - Método de Hondt:

#Função 2.2.1 - Calcula Quocientes:

def calcula_quocientes(d_inicial,n_deputados):
    """
    calcula_quocientes: (dicionário) x (inteiro) --> (dicionário)
    A função recebe um dicionário, votos apurados num circulo, e um inteiro positivo, número de deputados, e devolve um dicionário, com as mesmas chaves
    do dicionário argumento (partidos), com os quocientes calculados segundo o método de Hondt (ordenados por ordem decrescente).
    """

    d_final = {} #novo dicionário para não alterar o de entrada
    cont = 1
    l_apoio = [] 
    for chave in d_inicial: #para cada partido
        while cont < (n_deputados+1):
            l_apoio += [(d_inicial[chave])/cont] #lista com os quocientes calculados
            cont += 1
        d_final[chave] = l_apoio
        l_apoio = [] #a lista passa a ser novamente vazia, uma vez que o próximo ciclo será para um partido diferente
        cont = 1
    return d_final 


#Função 2.2.2 - Atribui Mandatos:

def atribui_mandatos(d_inicial,n_deputados):
    """
    atribui_mandatos: (dicionário) x (inteiro) --> (lista)
    A função recebe um dicionário, com os votos apurados num circulo, e um inteiro, numero de deputados, e devolve a lista ordenada contendo as cadeias de carateres
    dos partidos que obtiveram cada mandato. A primeira posição da lista corresponde ao nome do partido que obteve o primeiro deputado, etc.
    """

    d_quocientes = calcula_quocientes(d_inicial,n_deputados)
    cont = 0
    max = 0
    chave_max = ''
    l_res = []
    d_cont = {chave: 0 for chave in d_quocientes} #dicionário de contadores, para cada chave em que calculou os quocientes
    
    while cont<n_deputados: #enquanto os deputados não forem todos "distríbuidos" pelos partidos
        for chave in d_quocientes:
            if max < d_quocientes[chave][d_cont[chave]]:
                chave_max = chave #atualiza-se a chave máxima para a chave do partido que possui mais votos
                max = d_quocientes[chave][d_cont[chave]] #atualiza-se os votos para o maior numero de votos que se encontrar pelos partidos
            elif max == d_quocientes[chave][d_cont[chave]]:
                if (int(d_cont[chave_max]) > int(d_cont[chave])): #os mandatos são distribuídos por ordem ascendente às listas menos votadas
                    chave_max = chave
                    max = d_quocientes[chave][d_cont[chave]]
                else:
                    chave_max = chave_max
                    max = d_quocientes[chave][d_cont[chave_max]]
        l_res += [chave_max] #adiciona-se o nome do partido que obteve o deputado
        d_cont[chave_max] += 1 #desta forma passamos para a posição seguinte, do partido em específico, dos quocientes obtidos para o partido
        max = 0
        cont += 1
    return l_res


#Função 2.2.3 -  Obtem Partidos:

def obtem_partidos(d_inicial):
    """
    obtem_partidos: (dicionário) --> (lista)
    A função recebe um dicionário, com informação sobre as eleições num território com vários circulos eleitorais, e devolve a lista com o nome de todos os partidos
    que participaram nas eleições, ordenada por ordem alfabética.
    """

    l_res = []
    for regiao in d_inicial: #para cada circulo eleitoral
        for partido in d_inicial[regiao]['votos']: #para cada partido no circulo eleitoral
            if partido not in l_res: #adiciona-se se apenas se ainda não se encontra na lista
                l_res += [partido]
    l_res.sort() #ordena-se a lista
    return l_res


#Função 2.2.4 - Obtem Resultado Eleições:

def obtem_resultado_eleicoes(d_eleicoes):
    """
    resultado_eleições: (dicionário) --> (lista)
    A função recebe um dicionário, com informação sobre as eleições num território com vários circulos eleitorais, e devolve a lista ordenada de comprimento igual ao
    número total de partidos com os resultados das eleições. Cada elemento da lista é um tuplo de tamanho 3, contendo o nome de um partido, o número total de 
    deputados obtidos e o número total de votos obtidos pelo mesmo.
    A lista encontra-se ordenada por ordem decrescente, de acordo com o número de deputados obtidos e, em caso de empate, de acordo com o  número de votos.
    """

    list_mandatos = []

    if (type(d_eleicoes) != dict) or (len(d_eleicoes) == 0): #verificação da validade dos argumentos
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    for circ_elei in d_eleicoes:
        if (type(circ_elei)!= str) or (len(circ_elei) == 0):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if (type(d_eleicoes[circ_elei]) != dict) or (len(d_eleicoes[circ_elei]) == 0) or (len(d_eleicoes[circ_elei]) != 2) or ('votos' not in d_eleicoes[circ_elei]) or ('deputados' not in d_eleicoes[circ_elei]):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        if (d_eleicoes[circ_elei]['deputados'] <= 0) or ((len(d_eleicoes[circ_elei]['votos'])) < 1) or ((type(d_eleicoes[circ_elei]["votos"]) != dict)) or (type(d_eleicoes[circ_elei]['deputados']) != int):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        for partido in d_eleicoes[circ_elei]['votos']:
            if (type(partido) != str):
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            if (type(d_eleicoes[circ_elei]['votos'][partido]) != int) or (d_eleicoes[circ_elei]['votos'][partido] < 0) :
                raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        list_mandatos += (atribui_mandatos(d_eleicoes[circ_elei]['votos'],d_eleicoes[circ_elei]['deputados'])) #vai obter todos os deputados eleitos de todos os circulos eleitorais
        
    l_part = obtem_partidos(d_eleicoes)
    l_final = []
    t_final = ()
    max_votos = 0

    for partido in l_part: #para cada partido que participou nas eleições
        for circ_elei in d_eleicoes:
            if (partido in d_eleicoes[circ_elei]['votos']):
                max_votos += (d_eleicoes[circ_elei]['votos'][partido]) #vai obter o numero total de votos de cada partido, somando os de cada circulo eleitoral
                if max_votos == 0:
                    raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        t_final = ((partido,(list_mandatos.count(partido)),max_votos),) #list_mandatos.count(partido) - conta-se o numero de deputados eleitos de um partido de todos os circ.eleiorais
        l_final += ((t_final))
        max_votos = 0

    l_final = sorted(l_final, key= lambda x: (-x[1], -x[2])) #lista passa a estar ordenada de acordo com os requisitos especificados
    return l_final




#Terceiro Exercício - Solucao de Sistemas de Equacoes

#Função 3.2.1 - Produto interno:

def produto_interno(t_vetor1,t_vetor2):
    """
    produto_interno: (tuplo) x (tuplo) --> (real)
    A função recebe dois tuplos de números com a mesma dimensão (dois vetores) e devolve o resultado do produto interno desses dois vetores.
    """

    contador1 = 0
    res = 0
    while contador1 < (len(t_vetor1)):
        res += (t_vetor1[contador1] * t_vetor2[contador1]) #produto interno
        contador1 += 1
    return float(res)


#Função 3.2.2 - Verifica convergencia:

def verifica_convergencia(tup_matrizA,tup_res,tup_solX,precisao):
    """
    verifica_convergencia: (tuplo) x (tuplo) x (tuplo) x (real) --> (booleano)
    A função recebe um tuplo de tuplos (representando uma matriz de entrada), um tuplo representando o vetor de constantes C, um tuplo representando
    a solução X e um numero real, representando a precisão.
    Se o valor absoluto do erro de todas as equações for inferior à precisão, a função devolve True, caso devolve, retoma False.
    """

    lista_res = [0]*len(tup_matrizA) #tem que possuir a mesma dimensão q uma linha da matriz quadrada
    contador1 = 0
    contador2 = 0

    for linha in tup_matrizA:
        contador2 = 0
        for valor in linha: #com o ciclo calcula-se assim o resultado de Ax
            lista_res[contador1] += (valor * tup_solX[contador2])
            contador2 += 1
        contador1 +=1 

    contador1 = 0

    while contador1 < len(lista_res): #resta-nos avaliar se as respostas fornecidas são válidas, de acordo com a precisão pretendida
        if (abs(lista_res[contador1] - tup_res[contador1]) > precisao):
            return False
        contador1 +=1
    return True


#Função 3.2.3 - Retira Zeros Diagonal:

def retira_zeros_diagonal(tup_matriz,tup_vetor):
    """
    retira_zeros_diagonal: (tuplo) x (tuplo) --> (tuplo) x (tuplo)
    A função recebe um tuplo de tuplos (representando uma matriz de entrada) e um tuplo representando o vetor de constantes, e devolve
    uma nova matriz com as mesmas linhas que a de entrada, mas com estas reordenadas, de forma a não existirem valores 0 na diagonal. 
    O segundo parametro que devolve é o vetor de entrada com a mesma reordenação de linhas que a aplicada à matriz.
    """

    list_matriz, list_vetor = [], []
    cont1,cont2,cont3 = 0,0,0
    tup_matriz_final, tup_vetor_final = (),()

    for valor in tup_vetor: #criam-se listas com os mesmos valores que os tuplos para facilitar possíveis alterações
        list_vetor += [valor] 
    for linha in tup_matriz:
        list_matriz += (linha,)

    while cont1 < len(list_matriz):
        while cont2 < len(list_matriz[cont1]):
            if cont2 == cont1 and list_matriz[cont1][cont2] == 0: #se está numa das posições da diagonal e é 0
                while list_matriz[cont3][cont2] == 0 and (cont3 < len(list_matriz)): #enquanto não encontrar uma linha sem 0 nessa posição da diagonal
                    cont3 +=1
                list_matriz[cont1], list_matriz[cont3] = list_matriz[cont3], list_matriz[cont1] #troca-se a ordem das linhas para que não haja valor 0 as posições da diagonal
                list_vetor[cont1],list_vetor[cont3] = list_vetor[cont3],list_vetor[cont1]
                cont3 = 0
            cont2 +=1    
        cont1 +=1
        cont2 = 0

    for valor in list_vetor: #como pretendemos devolver tuplos, damos os valores das listas aos tuplos
        tup_vetor_final += (valor,)
    for linha in list_matriz:
        tup_matriz_final += (linha,)

    return tup_matriz_final,tup_vetor_final


#Função 3.2.4 - Eh Diagonal Dominante:

def eh_diagonal_dominante(tup_matriz):
    """
    eh_diagonal_dominante: (tuplo) --> (booleano)
    A função recebe um tuplo de tuplos (matriz quadrada), no mesmo formato das funções anteriores.
    Devolve True caso seja uma matriz diagonalmente dominante, e False caso contrário.
    """

    linha,soma,indice_valor = 0,0,0
    
    while linha < len(tup_matriz):
        while indice_valor < len(tup_matriz[linha]):
            if indice_valor != linha: #se o valor não se encontra na posição da diagonal
                soma += abs(tup_matriz[linha][indice_valor])
            indice_valor+=1
        if not (abs(tup_matriz[linha][linha]) >= abs(soma)): #verificamos se a matriz é diagonalmente dominante para cada linha
            return False #se não cumprir o requesito especificado numa certa linha
        soma = 0 #é necessário colocar a "soma" e o "indice_valor" a 0 para cada linha
        indice_valor = 0
        linha += 1
    return True


#Função 3.2.5 - Resolve sistema:

def resolve_sistema(matriz,tup_vetorC, precisao):
    """
    resolve_sistema: (tuplo)x(tuplo)x(real) --> (tuplo)
    A função recebe um tuplo de tuplos (matriz quadrada), no mesmo formato das funções anteriores, correspondente aos coeficientes das equações do sistema,
    um tuplo de números representando o vetor das constantes, e um valor real positivo correspondente à precisão pretendida para a solução.
    Devolve um tuplo, que  é a solução do sistema de equações de entrada, aplicando o método de Jacobi descrito.
    """
    
    #validação de argumentos
    if (len(matriz) == 0) or (type(matriz) != tuple) or type(tup_vetorC) != tuple or len(tup_vetorC) < 1 or len(tup_vetorC) != len(matriz) or precisao <= 0:
        raise ValueError("resolve_sistema: argumentos invalidos")
    if (type(precisao) != float):
        raise ValueError("resolve_sistema: argumentos invalidos")
    for linha in matriz:
        if (type(linha) != tuple):
            raise ValueError("resolve_sistema: argumentos invalidos")
        if len(matriz) != len(linha):
            raise ValueError("resolve_sistema: argumentos invalidos")
        for valor in linha:
            if (type(valor) != int and type(valor) != float):
                raise ValueError("resolve_sistema: argumentos invalidos")
    for valor in tup_vetorC:
        if (type(valor) != int and type(valor) != float):
            raise ValueError("resolve_sistema: argumentos invalidos")

    matriz_limpa,tup_vetorC = (retira_zeros_diagonal(matriz,tup_vetorC)) #obtem-se a matriz reoordenada sem zeros na diagonal, e o seu respetivo vetor de constantes reoordenado

    if not eh_diagonal_dominante(matriz_limpa): #verifica-se se a matriz é diagonalmente dominante
        raise ValueError ("resolve_sistema: matriz nao diagonal dominante")
    
    list_res = [0]*len(matriz_limpa) #têm que possuir a mesma dimensão q uma linha da matriz quadrada
    tup_res = [0]*len(matriz_limpa)
    list_res_ant = [0]*len(matriz_limpa)

    cont1 = 0

    while not verifica_convergencia(matriz_limpa,tup_vetorC,tuple(tup_res),precisao): #enquanto o resultado não possuir a precisão pretendida
        while cont1 != len(list_res):
            list_res_ant[cont1] = list_res[cont1] #obtêm-se os resultados "anteriores" necessários para o método de Jacobi
            cont1+=1
        cont1 = 0
        while cont1 != len(list_res):
            list_res[cont1] = list_res_ant[cont1] + (tup_vetorC[cont1] - produto_interno(matriz_limpa[cont1],tuple(list_res_ant)))/ matriz_limpa[cont1][cont1] #método de Jacobi
            cont1 += 1
        cont1 = 0
        for valor in list_res: 
            tup_res[cont1] = valor 
            cont1 += 1
        cont1 = 0
    
    return tuple(tup_res) #pretendemos devolver sob a forma de tuplo
