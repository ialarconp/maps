#Bibliotecas
import geopandas
import matplotlib.pyplot as plt

#Guardando los datos que usaremos
path = geopandas.datasets.get_path("naturalearth_lowres")
world = geopandas.read_file(path)

#Graficar nuestro mapa
ax = world.plot()
world[world.continent == 'South America'].plot(ax = ax, cmap = 'Greens')
plt.show()
