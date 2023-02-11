
#instalação  pip intall plotly
#instalação  pip intall  pandas

#Importar uma base de dados
importar  pandas  como  pd

#remova a (#) para o codigo rodar e mude o csv, para tipo de arquivo que vc quer utilizar
tabela  =  pd . read_csv ( "telecom_users.csv" )

#Visualizar a base de dados
tabela  =  tabela . drop ( "Sem nome: 0" , eixo = 1 )
exibição ( tabela )
#Entender quais são as informações tão disponíveis
#Descobrir as cagadas da base de dados


#Ordenar palvra do produto,Ordenar numero 
from operator import itemgetter, attrgetter

class produto:
    def __init__(self, nome, nota, valor):
        self.nome = nome
        self.nota = nota
        self.valor = valor
    def __repr__(self):
        return repr((self.nome, self.nota, self.valor))

produto_objeto = [
    produto('livro', 'A', 30),
    produto('Caderno', 'B', 12),
    produto('Lapis de Cor', 'B', 10),
    produto('Estojo', 'C', 13),

]

print(sorted(produto_objeto, key=attrgetter('valor'), reverse=True))





