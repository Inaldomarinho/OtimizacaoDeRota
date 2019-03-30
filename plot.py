import matplotlib.pyplot as plt

def plot(caminho):
    im = plt.imread("mapa.PNG")
    plt.imshow(im, zorder=1)
    x = []
    y = []
    for no in caminho:
        plt.scatter(no.x, no.y, zorder=3, color='#1f77b4')
        x.append(no.x)
        y.append(no.y)

    plt.plot(x, y, label='line 2')
    plt.show()