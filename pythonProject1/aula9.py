import shutil


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #.split() funcao que serve para toda vez que encontrar o comando , será inserido numa lista.
    #rint(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media1 = lambda notas: sun([int(i) for i in notas]) / 4
        print(media1(lista_notas))

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, 'c:/teste')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'c:/teste')


if __name__ == '__main__':
    move_arquivo('notas.txt')


    #escrever_arquivo('primeira linha.\n')
    #aluno = 'joao, 10,6,3,9\n'
    #atualizar_arquivo('notas.txt' , aluno)
    #ler_arquivo('teste.txt')
    # escrever_arquivo('Criando o arquivo em outro diretorio')
    #aluno = '\nRafael,7,5,8,4'
    #atualizar_arquivo('tste.txt', aluno)
    #media_notas('notas.txt')

