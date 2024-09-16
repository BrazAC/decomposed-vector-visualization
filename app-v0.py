import matplotlib.pyplot as plt
import numpy as np
import time

def main():
    fig, ax = plt.subplots()
    v = [-5.5,-2]
    moduloV = (v[0]**2 + v[1]**2)**(1/2) 
    cosAngulo = [v[0]/moduloV]
    senAngulo = [v[1]/moduloV]

    #([x's das origens], [y's das origens], [x's dos pontos finais], [y's dos pontos finais])
    ax.quiver([0], [0], v[0], v[1], angles="xy", scale_units = "xy", scale = 1, color = ["black"])
    #Vetores decompostos
    coordDecompX = [cosAngulo[0] * moduloV, 0]
    coordDecompY = [0, senAngulo[0] * moduloV]
    ax.quiver([0], [0], coordDecompX[0], coordDecompX[1], angles="xy", scale_units = "xy", scale = 1, color = ["b"]) #x
    ax.quiver([0], [0], coordDecompY[0], coordDecompY[1], angles="xy", scale_units = "xy", scale = 1, color = ["r"]) #y

    #Determinando ticks dos eixos cartesianos
    v[0] = int(v[0])
    v[1] = int(v[1])
    print(v[0])
    if v[0] > 0 and v[1] > 0: #quadrante 1
        plt.xticks(range(-1 * v[0], v[0]+2, 1))
        plt.yticks(range(-1 * v[1], v[1]+2, 1))
    elif v[0] < 0 and v[1] > 0: #quadrante 2
        plt.xticks(range(v[0]-1, (-1 * v[0]) + 2, 1))
        plt.yticks(range(-1 * v[1], v[1]+2, 1))
    elif v[0] < 0 and v[1] < 0: #quadrante 3
        plt.xticks(range(v[0]-1, (-1 * v[0]) + 2, 1))
        plt.yticks(range(v[1]-1, (-1 * v[1]) + 2, 1))
    elif v[0] > 0 and v[1] < 0: #quadrante 4
        plt.xticks(range(-1 * v[0], v[0]+2, 1))
        plt.yticks(range(v[1]-1, (-1 * v[1]) + 2, 1))


    #Determinando labels
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.grid()
    plt.show()
        

if __name__ == "__main__":
    main()