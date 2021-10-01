#Cálculo calificación alumno
#55% promedio de sus tres calificaciones parciales
#30% calificación del examen final
#15% calificación trabajo final

print("\nCálculo nota final alumno. Introduzca las notas correspondientes.\n")

parcial1=float(input("1º parcial: "))
parcial2=float(input("2º parcial: "))
parcial3=float(input("3º parcial: "))

examenfinal=float(input("Examen final: "))

trabajofinal=float(input("Trabajo final: "))

calificacion=((parcial1+parcial2+parcial3)/3)*0.55+examenfinal*0.30+trabajofinal*0.15

print("\nCalificación del alumno: %.2f" % (calificacion))