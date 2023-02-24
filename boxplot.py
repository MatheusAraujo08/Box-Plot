# Carregamento das bibliotecas

import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# Carregamento de Dados

dados_seguros = [0.9, 1.0, 1.7, 2.9, 3.1, 5.3, 5.5, 6.9, 12.2, 12.9, 14.0, 33.6]


# Processamento dos dados

q1 = np.percentile(dados_seguros, 25, method="averaged_inverted_cdf")
q2 = np.percentile(dados_seguros, 50, method="averaged_inverted_cdf")
q3 = np.percentile(dados_seguros, 75, method="averaged_inverted_cdf")
dq = q3-q1

limite_inferior= np.fmax(0.9, q1 - 1.5*dq)
limite_superior= np.fmin(33.6, q3 + 1.5*dq)

# Criação do boxplot

box = plt.boxplot (dados_seguros)


# apresentação dos dados

print("este é o quartil 1",q1)
print("este é o quartil 2",q2)
print("este é o quartil 3",q3)

print( "limite inferior é :", limite_inferior)
print( "limite superior é : ", limite_superior)

plt.title("Boxplot Vinícius Seguradoras")
plt.xlabel("seguradoras")
plt.ylabel("Fatia de mercado")
plt.show()