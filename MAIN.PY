# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias = int(input("¿Cuántos días de temperaturas deseas ingresar? "))
    for i in range(dias):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i+1} en grados Celsius: "))
                break  # Si la entrada es válida, salimos del bucle
            except ValueError:
                print("Por favor, ingrese un número válido.")
        temperaturas.append(temp)
    return temperaturas

# Función para calcular estadísticas
def calcular_estadisticas(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
    return promedio, max_temp, min_temp

# Función para mostrar aviso cuando las temperaturas sean extremas
def verificar_temperaturas_extremas(temperaturas):
    for i, temp in enumerate(temperaturas):
        if temp < -0:
            print(f"Aviso: Temperatura extremadamente baja en el día {i+1}: {temp} °C")
        elif temp > 40:
            print(f"Aviso: Temperatura extremadamente alta en el día {i+1}: {temp} °C")

# Función principal
def analizar_temperaturas():
    temperaturas = ingresar_temperaturas()
    promedio, max_temp, min_temp = calcular_estadisticas(temperaturas)
    
    print(f"\nEstadísticas de Temperaturas:")
    print(f"Promedio de temperatura: {promedio:.2f} °C")
    print(f"Temperatura máxima: {max_temp} °C")
    print(f"Temperatura mínima: {min_temp} °C")
    
    # Verificar temperaturas extremas
    verificar_temperaturas_extremas(temperaturas)

# Llamar a la función principal
if __name__ == "__main__":
    analizar_temperaturas()
