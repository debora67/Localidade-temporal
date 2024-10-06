import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo para imitar a tendência do gráfico fornecido
posicoes = np.arange(1, 101)  # Posições na pilha LRU
dados_originais = 1 / posicoes ** 1.5  # Tendência para os dados 'Originais' (fração de referências)
dados_embaralhados = 1 / (posicoes ** 2.5)  # Tendência para os dados 'Embaralhados' (tendência mais fraca)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(posicoes, dados_originais, label='Original', color='gray')
plt.plot(posicoes, dados_embaralhados, label='Embaralhado', color='black')
plt.fill_between(posicoes, dados_originais, dados_embaralhados, color='gray', alpha=0.5)
plt.yscale('log')
plt.xscale('linear')
plt.title('(a) Alluvion')
plt.xlabel('Posição na Pilha LRU')
plt.ylabel('Fração de Referências')
plt.legend()

plt.tight_layout()
plt.show()
