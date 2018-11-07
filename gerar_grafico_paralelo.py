import os
import matplotlib.pyplot as plt
import numpy as np

#salva a pasta raiz
root = os.getcwd()

#cria os arrays que vao armazenar os valores de cada execucao em cada tamanho de matriz
seq_100 = []
seq_200 = []
seq_300 = []
seq_400 = []
seq_500 = []
seq_600 = []
seq_700 = []
seq_800 = []
seq_900 = []
seq_1k  = []
seq_1k1 = []
seq_1k2 = []
seq_1k3 = []
seq_1k4 = []
seq_1k5 = []
seq_1k6 = []
seq_1k7 = []
seq_1k8 = []
seq_1k9 = []
seq_2k  = []

#armazena todos em um unico array
arrays = [
    seq_100, seq_200, seq_300, seq_400, seq_500, seq_600, seq_700, seq_800, seq_900, seq_1k,
    seq_1k1, seq_1k2, seq_1k3, seq_1k4, seq_1k5, seq_1k6, seq_1k7, seq_1k8, seq_1k9, seq_2k 
]

#troca para o diretorio que contem os valores
os.chdir("tempos_sequencial")

#salva os valores em um array gigante
times = []
for file in os.listdir(os.getcwd()):
    with open(file) as f:
        times.append([x.replace("\n", "") for x in f.readlines()])
  
#salva os valores em cada array, daqueles criados anteriormente
for size in range(10):
    for num in range(20):
        arrays[num].append(float(times[size][num]))

#calcula os valoes minimos, medios e maximos de cada execucao
min_values = [min(seq_100), min(seq_200), min(seq_300), min(seq_400), min(seq_500), min(seq_600), min(seq_700), min(seq_800), min(seq_900), min(seq_1k),
              min(seq_1k1), min(seq_1k2), min(seq_1k3), min(seq_1k4), min(seq_1k5), min(seq_1k6), min(seq_1k7), min(seq_1k8), min(seq_1k9), min(seq_2k)]
avr_values = [np.average(seq_100), np.average(seq_200), np.average(seq_300), np.average(seq_400), np.average(seq_500), np.average(seq_600), np.average(seq_700), np.average(seq_800), np.average(seq_900), np.average(seq_1k),
              np.average(seq_1k1), np.average(seq_1k2), np.average(seq_1k3), np.average(seq_1k4), np.average(seq_1k5), np.average(seq_1k6), np.average(seq_1k7), np.average(seq_1k8), np.average(seq_1k9), np.average(seq_2k)]
max_values = [max(seq_100), max(seq_200), max(seq_300), max(seq_400), max(seq_500), max(seq_600), max(seq_700), max(seq_800), max(seq_900), max(seq_1k),
              max(seq_1k1), max(seq_1k2), max(seq_1k3), max(seq_1k4), max(seq_1k5), max(seq_1k6), max(seq_1k7), max(seq_1k8), max(seq_1k9), max(seq_2k)]

#vai para a pasta dos graficos
os.chdir(root + "/graficos")

#gera o gráfico final das execucoes
fig, axes = plt.subplots(figsize=(12,5))

axes.plot(min_values, label="min", color="green")
axes.plot(avr_values, label="avr", color="blue")
axes.plot(max_values, label="max", color="red")
axes.set_ylabel("Tempo de execução (s)")
axes.set_xlabel("Tamanho matrizes")
axes.set_xticks(range(0,20))
axes.set_xticklabels(range(100,2100,100))

# custom grid appearance
axes.grid(color='black', alpha=0.4, linestyle='dashed', linewidth=0.5)

axes.legend()
fig.savefig("sequencial.jpg", dpi=200)