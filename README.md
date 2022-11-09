# CacheSimulator
Cache Replace Policy Simulator

# Instrucciones para correr el programa}

## Pasos a seguir:

Para correr el programa se deben seguir los siguientes pasos:


 1. Abra una consola de comandos en el directorio con los archivos
 2. Asegúrese que en el directorio se encuentra el directorio **traces** con los 27 archivos ".txt.gz" correspondiente a los diferentes traces. Es decir debe **renombrar el folder que contiene los traces para que se llame traces**. No descomprina ninguno de los traces interiores, debe trabajar con el.gz en cada uno.
 3. **Corra: python cache\_simulator.py  -s X -a X -b X -r X}**
 4. Debe sustituir X por un número según correspondan los parámetros



## Parámetros para correr el programa 


1. -s Corresponde a la capacidad total
del caché. Valores validos son: 2, 4, 8,16, 64, 128.

2.  -a Corresponde a la cantidad de “ways”
en cada set. Valores validos son: 1, 2, 4, 8, 16


3. -b Indica la cantidad de bytes que tiene cada bloque en la caché. Valores validos son: 16, 32, 64, 128 

4. -r Indica la política de reemplazo usada para expulsar bloques del caché. Una “l” (ele) indica LRU, una “r” (erre) indica aleatoria. El default es LRU

5. -t Indica el trace específico que quiere utilizarse para correr los resultados. El default es 465.tonto-1769B.trace.txt.gz


## Parámetros mínimos que necesitan el simulador:}

Para correr adecuadamente el simulador se necesitan como mínimo setear los siguientes parámetros:

1. -s Capacidad total
del caché. 

2.  -a Cantidad de “ways”
en cada set. 

3. -b Cantidad de bytes que tiene cada bloque en la caché. 

