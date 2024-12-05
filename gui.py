#! /usr/bin/python3

import tkinter as tk

def calcular_siguiente():
    numero_actual = int(entry.get())
    siguiente_numero = numero_actual + 1
    resultado_label.config(text=f"Siguiente entero: {siguiente_numero}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Siguiente Entero")

# Crear una entrada de texto
entry = tk.Entry(ventana)
entry.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Calcular", command=calcular_siguiente)
boton.pack(pady=5)

# Crear una etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="Siguiente entero: ")
resultado_label.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()


if __name__ == "__main__":
    pass