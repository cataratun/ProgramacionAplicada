import tkinter as tk
#Importa el módulo tkinter para crear la interfaz gráfica

def click_button(value):
    #Esta función agrega el número o símbolo al campo de entrada
    current = entry.get()
    entry.delete(0, tk.END)
    #Borra el contenido actual del campo de entrada
    entry.insert(0, current + str(value))
    #Inserta el nuevo valor al final del contenido actual

def clear_entry():
    #Esta función borra todo el contenido del campo de entrada
    entry.delete(0, tk.END)

def calculate_result():
    result = eval(entry.get())
    #Evalúa la expresión matemática
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
    #Muestra el resultado

root = tk.Tk()
#Crea la ventana principal
root.title("Calculadora")
#Establece el título
root.geometry("450x450")
#Tamaño de la ventana

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="left")
#Campo de entrada donde se muestran los números y resultados
entry.pack(fill="both", padx=10, pady=10)

buttons_frame = tk.Frame(root)
#Contenedor para los botones
buttons_frame.pack()

#Lista con los botones organizados por filas, ahora con paréntesis
buttons = [
    ["(", ")", "C", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

#Crear los botones de la calculadora
for row_values in buttons:
    row = tk.Frame(buttons_frame)
    row.pack(expand=True, fill="both")
    for value in row_values:
        if value == "":
            #Espacio vacío donde no se quiere mostrar nada
            tk.Label(row).pack(side="left", expand=True, fill="both", padx=5, pady=4)
        elif value == "=":
            btn = tk.Button(row, text=value, font=("Arial", 20), command=calculate_result)
            btn.pack(side="left", expand=True, fill="both", padx=5, pady=4)
        elif value == "C":
            btn = tk.Button(row, text=value, font=("Arial", 20), command=clear_entry)
            btn.pack(side="left", expand=True, fill="both", padx=5, pady=4)
        else:
            btn = tk.Button(row, text=value, font=("Arial", 20), command=lambda val=value: click_button(val))
            btn.pack(side="left", expand=True, fill="both", padx=5, pady=4)

root.mainloop()
#Inicia el bucle principal de la interfaz
