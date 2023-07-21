from datetime import datetime

fecha_actual = datetime.now()

cadena_fecha = "Current date: {: %m-%d-%Y}".format(fecha_actual)
cadena_hora = "Current time: {: %H:%M:%S}".format(fecha_actual)

print(cadena_fecha)
print(cadena_hora)
