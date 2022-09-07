### EE400 - Métodos da Engenharia Elétrica###
### Trabalho 1 ###
### Fernando Teodoro de Cillo - RA 197029###

### Importando os pacotes que usaremos###
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D


### Definindo o valor do campo vetorial constante ###
Campo = 15

### Definindo o ângulo de rotação  ###
El = 45

### Vértices do polígono que define o captador (em forma de coelho ###
x = [7, 7, 7, 6, 8, 9, 8, 7, 6, 6, 7, 7, 8, 8, 9, 9, 8, 4, 3, 3, 4, 4, 2, 2, 3, 3, 2, 2, 3, 2, 1, 1, 2.5, 2.5, 1, 1, 2, 3, 4, 5]
y = [19, 18, 17, 16, 17, 17, 16, 14, 13, 12, 10, 8, 7, 5, 6, 4, 3, 1, 1, 2, 2, 3, 3, 4, 4, 6, 5, 6, 8, 7, 6, 7, 9, 12, 12, 13, 14, 15, 15, 17]

### Adicionando o primeiro ponto ao fim da lista para fechar a figura###
x.append(x[0])
y.append(y[0])


### CALCULANDO O FLUXO MAGNÉTICO ###

### Inicializando as variáveis ###
D = 0 # "Determinante" que será utilizado para calcular a área
A = 0 # Área do polígono
phi = 0 # Fluxo magnético

### Cauculando o "determinante" D ###
for i in range(0, len(x)-1):
  D = D + x[i]*y[i+1] - x[i+1]*y[i]

### Calculando a área A do polígono ###
A = abs(D)/2
print("\nA área da figura é igual a "+ str(A)+" u.a.")

### Printando o valor do campo ###
print("\nO campo magnético na região é de" + str(Campo)+" T.")

### Calculando o fluxo magnético phi através do captador ###
phi = Campo * A *np.cos(2*np.pi) #theta = 2*pi nos dá o valor máximo do fluxo
print("\nO fluxo magnético máximo vale "+ str(phi)+" Wb.\n")



### PLOTANDO AS FIGURAS###

### Criando o plot do campo vetorial ###
xmesh, ymesh, zmesh = np.meshgrid(x, x, 1)
fig=plt.figure('Campo magnético através do captador')
ax = plt.axes(projection='3d', azim=-45, elev=45)

### Definindo a função para calcular o campo ###
def F(x, y, z):
    u = z
    v = x
    w = Campo*z/z
    return np.array([u, v, w])

### Criando os vetores ###
umesh,vmesh,wmesh = F(xmesh,ymesh,zmesh)
l = 0.0002
ax.quiver(xmesh,ymesh,zmesh - l - 0.99999, umesh, vmesh, wmesh , length=l/10, color='g')
ax.quiver(xmesh,ymesh+ 9,zmesh - l - 0.99999, umesh, vmesh, wmesh , length=l/10, color='g') # aumentando a extensão do plot
plt.plot(x, y) # Figura do captador #

t = np.linspace(0, 5, 500)
ph = Campo* A* np.cos(2 * np.pi * t)
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(t, ph, lw=4, color='r')
ax.set_xlabel('Tempo (s)', fontsize=22)
ax.set_ylabel('Fluxo magnético (Wb)', fontsize=22)
ax.grid()
plt.xlim([0,5])
plt.show()



