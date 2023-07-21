from datetime import datetime

fecha_actual = datetime.now()

cadena_fecha = "Fecha actual: {: %d-%m-%Y}".format(fecha_actual)
cadena_hora = "Hora actual: {: %H:%M:%S}".format(fecha_actual)

print(cadena_fecha)
print(cadena_hora)
