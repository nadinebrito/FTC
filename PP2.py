def Pi(e_inicial,n_estados):
    pi = []
    for n in range(n_estados):
        if(n == e_inicial):
            pi.append(1)
        else:
            pi.append(0)
    return(pi)


def Eta(e_finais,n_estados):
    eta = []
    for i in range(n_estados):
        eta.append(0)
    for j in range(len(e_finais)):
        for n in range(n_estados):
            if(e_finais[j]==n):
                eta[e_finais[j]] = 1
    return(eta)

def Xa(n_estados,delta):
    alfa = ['a', 'b']
    Xa=[]
    
    for q in range(n_estados):
        Xa.append([])
        for w in range(n_estados):
            Xa[q].append(0)

    for e in range(n_estados):
        for r in range(n_estados):
            if(r == delta[e][0]):
                Xa[e][r] = 1
    return (Xa)

def Xb(n_estados,delta):
    alfa = ['a', 'b']
    Xb=[]

    for q in range(n_estados):
        Xb.append([])
        for w in range(n_estados):
            Xb[q].append(0)

    for e in range(n_estados):
        for r in range(n_estados):
            if(r == delta[e][1]):
                Xb[e][r] = 1
    return(Xb)

def Matriz (linha, coluna):
    matriz = []
    for n in range(linha):
        linhas = []
        for m in range(coluna):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def Multiplica(matriz, matriz2,linha,coluna,lendo2):
    C = Matriz(linha, coluna)
    for i in range(linha):
        for j in range(coluna):
            val = 0
            for k in range(lendo2):
                val = val + matriz[i][k] * matriz2[k][j]
            C[i][j] = val
    return C
  
def VerificaPalavra(a,b,palavra):
    acm = []
    for letra in range(len(palavra)):
        if(palavra[letra]== 'a'):
            if(len(acm)==0):
                acm = a
            else:
                linha = len(acm)
                coluna = len(acm[0])
                lendo2 = len(a)
                acm = Multiplica(acm,a,linha,coluna,lendo2)
        if(palavra[letra]== 'b'):
            if(len(acm)==0):
                acm = b
            else:
                linha = len(acm)
                coluna = len(acm[0])
                lendo2 = len(b)
                acm = Multiplica(acm,b,linha,coluna,lendo2)
    return(acm)

def Palavra(a,b):
    acm = []
    palavra = str(input())
    acm = VerificaPalavra(a,b,palavra)
    return(acm)
    
def VerificaAceitaRejeita(Pi,Palavra,Eta):
    acm = 0 
    mp = [] 
    resultado = []
    for i in range(len(Pi)):
        for j in range(len(Palavra[0])):
            acm = acm + Pi[j] * Palavra[j][i]
        mp.append(acm)
        acm = 0

    for i in range(len(mp)):
        for j in range(1):
            acm = acm + mp[i] * Eta[i]
    resultado.append(acm)
    acm = 0

    if (resultado[0] == 1):
        print('ACEITA')
    if (resultado[0] == 0):
        print('REJEITA')


dic = str(input())
dicionario = eval(dic)

n_estados = dicionario['estados']
e_inicial = dicionario['inicial']
e_finais = dicionario['final']
delta = dicionario['delta']


pi = Pi(e_inicial,n_estados)
eta = Eta(e_finais,n_estados)
a = Xa(n_estados,delta)
b = Xb(n_estados,delta)
qtd_palavras = int(input())
for g in range(qtd_palavras):
    palavra = Palavra(a,b)
    VerificaAceitaRejeita(pi,palavra,eta)
