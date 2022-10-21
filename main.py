# Importa o módulo a ser utilizado 
import gmplot

# Efetuando o download do mapa
gmap1 = gmplot.GoogleMapPlotter(28.7041, 77.1025, 13 )

# Convertendo o mapa a HTML e salvando no local definido
gmap1.draw( "/local-do-arquivo/map.html" )
