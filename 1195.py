class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                    self.chave,
                                    self.direita and self.direita.chave)

def PreencheNodo(raiz, v):
    if (raiz.chave < 0):
        raiz.chave = v
        return
    if(v <= raiz.chave):
        if(not raiz.esquerda):
            raiz.esquerda = NodoArvore(v)
            return
        else:
            PreencheNodo(raiz.esquerda, v)
    if(v > raiz.chave):
        if(not raiz.direita):
            raiz.direita = NodoArvore(v)
            return
        else:
            PreencheNodo(raiz.direita, v)


def ImprimeArvore(raiz, tipo):
    if(raiz != None):
        if(tipo == 1):
            print(" %d" % raiz.chave, end="")
            ImprimeArvore(raiz.esquerda, tipo)
            ImprimeArvore(raiz.direita, tipo)
        if(tipo == 2):
            ImprimeArvore(raiz.esquerda, tipo)
            print(" %d" % raiz.chave, end="")
            ImprimeArvore(raiz.direita, tipo)
        if(tipo == 3):
            ImprimeArvore(raiz.esquerda, tipo)
            ImprimeArvore(raiz.direita, tipo)
            print(" %d" % raiz.chave, end="")

def main():

    ncasos = int(input())

    for i in range(ncasos):
        tam = int(input())
        noh = list(map(int,input().split()))
        count = i+1
        raiz = NodoArvore(-1)
        for d in range(tam):
            PreencheNodo(raiz, noh[d])

        print(f"Case {count}:", end="")
        print("\nPre.:", end="")
        tipo = 1
        ImprimeArvore(raiz, tipo)
        print("\nIn..:", end="")
        tipo = 2
        ImprimeArvore(raiz, tipo)
        print("\nPost:", end="")
        tipo = 3
        ImprimeArvore(raiz, tipo)
        print("\n")

main()