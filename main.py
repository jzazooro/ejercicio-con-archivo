def main():
    ejecutar=True

    while ejecutar==True:
        eje=str(input("¿Quieres ejecutar el programa?: "))

        if eje=="si" or eje=="SI" or eje=="Si":
            ejercicio=notas()
            ejercicio.imprimir()

        if eje!="si" or eje!="SI" or eje!="Si":
            ejecutar=False
if __main__=='__main__':
    main() 
    