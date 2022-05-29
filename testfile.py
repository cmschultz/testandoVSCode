#versão BETA
dist     = float(input("Distância entre drones(metros): "))                              #Medido pelo drone Gato(perseguidor) que corre atrás do drone
                                                                                         #Rato(perseguido).
velRato  = float(input("Digite a velocidade do drone que esta sendo perseguido: "))      #RATO: drone controlado por um piloto, traz um fator de aleatoriedade 
                                                                                         #para o perseguidor.
velGato  = float(input("Digite a velocidade do drone que esta perseguindo: "))           #GATO: drone autônomo perseguidor. Ele deve medir distâncias, a própria 
                                                                                         #velocidade e a velocidade do outro drone. 

#Vel relativa POSITIVA:  Afastamento
#Vel relativa NEGATIVA:  Aproximação
#Vel relativa ZERO:      Ideal
def calculaVelRelativa(velRato, velGato):
        return velRato - velGato


velRelativa = calculaVelRelativa(velRato - velGato)


#Essa função busca a seguinte condição (considerando 1D):
# Velrelativa == 0
# dist        == 0
def controleDistancia(dist):
    #Para velocidade relativa == 0
    if   dist < 1  and velRelativa == 0:
        print("Diminuir X velocidade do Gato.")
    elif dist == 1 and velRelativa == 0:
        print("Mantém, tá perfeito.")
    elif dist > 1  and velRelativa == 0:
        print("Aumentar X velocidade do Gato.")
    #Para velocidade relativa > 0
    elif dist < 1  and velRelativa > 0:
        print("Mantém, tá afastando.")
    elif dist == 1 and velRelativa > 0:
        print("Aumentar X velocidade do Gato.")
    elif dist > 1  and velRelativa > 0:
        print("Aumentar 2X velocidade do Gato.")
    #Para velocidade relativa < 0
    elif dist < 1  and velRelativa < 0:
        print("Diminuir X velocidade do Gato.")
    elif dist == 1 and velRelativa < 0:
        print("Diminuir 2X velocidade do Gato.")
    elif dist > 1  and velRelativa < 0:
        print("Mantém aproximando até dar 1 metro.")
    
#Problema: Muitas variações de comando em pouco tempo.
#talvez mexer com ranges de valores. Por exemplo: de 1 a 1,5 metros
#velociadade relativa de até 5 km/h.
#Essa versão aqui é a Beta.
