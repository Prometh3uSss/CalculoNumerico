import tkinter as tk
import random
from tkinter import messagebox
import functools
import matplotlib.pyplot as plt
import numpy as np

class LoginGUI:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        # Centrar la ventana en la pantalla
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        center_x = (screen_width // 2) - (300 // 2)
        center_y = (screen_height // 2) - (150 // 2)
        master.geometry(f"300x150+{center_x}+{center_y}")

        # Crear widgets de login
        self.label_usuario = tk.Label(master, text="Usuario:")
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(master)
        self.entry_usuario.pack()

        self.label_contraseña = tk.Label(master, text="Contraseña:")
        self.label_contraseña.pack()

        self.entry_contraseña = tk.Entry(master, show="*")
        self.entry_contraseña.pack()

        self.button_login = tk.Button(master, text="Iniciar sesión", command=self.login)
        self.button_login.pack()

    def login(self):
        # Lógica de login aquí
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if usuario == "admin" and contraseña == "password":
            self.master.destroy()  # Cierra la ventana de login
            operaciones_gui = OperacionesGUI()  # Abre la ventana de operaciones
            operaciones_gui.root.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

class OperacionesGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Operaciones con Conjuntos")

        # Centrar la ventana en la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = (screen_width // 2) - (600 // 2)
        center_y = (screen_height // 2) - (400 // 2)
        self.root.geometry(f"600x400+{center_x}+{center_y}")

        # Agregar un frame con barra de desplazamiento vertical
        self.frame_operaciones = tk.Frame(self.root)
        self.frame_operaciones.pack(fill="both", expand=True)

        self.canvas_operaciones = tk.Canvas(self.frame_operaciones)
        self.canvas_operaciones.pack(side="left", fill="both", expand=True)

        self.scrollbar_operaciones = tk.Scrollbar(self.frame_operaciones, orient="vertical", command=self.canvas_operaciones.yview)
        self.scrollbar_operaciones.pack(side="right", fill="y")

        self.canvas_operaciones.configure(yscrollcommand=self.scrollbar_operaciones.set)

        # Agregar un frame dentro del canvas para contener los widgets
        self.frame_widgets = tk.Frame(self.canvas_operaciones)
        self.canvas_operaciones.create_window((0, 0), window=self.frame_widgets, anchor="nw")

        # Crear widgets de operaciones dentro del frame_widgets
        self.label_operaciones = tk.Label(self.frame_widgets, text="Operaciones con Conjuntos")
        self.label_operaciones.pack()

        # Crear entradas para conjuntos
        self.label_elementos_universal = tk.Label(self.frame_widgets, text="Número de elementos del conjunto universal:")
        self.label_elementos_universal.pack()

        self.entry_elementos_universal = tk.Entry(self.frame_widgets)
        self.entry_elementos_universal.pack()

        self.button_generar_conjunto_universal = tk.Button(self.frame_widgets, text="Generar Conjunto Universal", command=self.generar_conjunto_universal)
        self.button_generar_conjunto_universal.pack()

        self.text_conjunto_universal = tk.Text(self.frame_widgets, height=10, width=60)
        self.text_conjunto_universal.pack()

        # Etiquetas para los subconjuntos
        self.label_subconjuntos = tk.Label(self.frame_widgets, text="Subconjuntos:")
        self.label_subconjuntos.pack()

        self.label_subconjunto_a = tk.Label(self.frame_widgets, text="A = {}")
        self.label_subconjunto_a.pack()

        self.label_subconjunto_b = tk.Label(self.frame_widgets, text="B = {}")
        self.label_subconjunto_b.pack()

        self.label_subconjunto_c = tk.Label(self.frame_widgets, text="C = {}")
        self.label_subconjunto_c.pack()

        self.label_subconjunto_d = tk.Label(self.frame_widgets, text="D = {}")
        self.label_subconjunto_d.pack()

        # Crear checkboxes para seleccionar subconjuntos
        self.checkbutton_a = tk.BooleanVar()
        self.checkbutton_b = tk.BooleanVar()
        self.checkbutton_c = tk.BooleanVar()
        self.checkbutton_d = tk.BooleanVar()

        self.checkbutton_a.set(True)
        self.checkbutton_b.set(True)
        self.checkbutton_c.set(True)
        self.checkbutton_d.set(True)

        self.checkbox_a = tk.Checkbutton(self.frame_widgets, text="A", variable=self.checkbutton_a)
        self.checkbox_a.pack()

        self.checkbox_b = tk.Checkbutton(self.frame_widgets, text="B", variable=self.checkbutton_b)
        self.checkbox_b.pack()

        self.checkbox_c = tk.Checkbutton(self.frame_widgets, text="C", variable=self.checkbutton_c)
        self.checkbox_c.pack()

        self.checkbox_d = tk.Checkbutton(self.frame_widgets, text="D", variable=self.checkbutton_d)
        self.checkbox_d.pack()

        # Crear botones para operaciones
        self.button_union = tk.Button(self.frame_widgets, text="Unión", command=functools.partial(self.operacion, "Unión"))
        self.button_union.pack()

        self.button_interseccion = tk.Button(self.frame_widgets, text="Intersección", command=functools.partial(self.operacion, "Intersección"))
        self.button_interseccion.pack()

        self.button_diferencia = tk.Button(self.frame_widgets, text="Diferencia", command=functools.partial(self.operacion, "Diferencia"))
        self.button_diferencia.pack()

        self.button_complemento = tk.Button(self.frame_widgets, text="Complemento", command=functools.partial(self.operacion, "Complemento"))
        self.button_complemento.pack()

        # Crear botón para generar diagrama de Venn
        self.button_generar_diagrama_venn = tk.Button(self.frame_widgets, text="Generar Diagrama de Venn", command=self.generar_diagrama_venn)
        self.button_generar_diagrama_venn.pack()

        # Agregar un botón para mostrar el instructivo
        self.button_instructivo = tk.Button(self.frame_widgets, text="Instructivo", command=self.mostrar_instructivo)
        self.button_instructivo.pack()

        # Crear área de texto para mostrar resultados
        self.text_resultado = tk.Text(self.frame_widgets, height=10, width=60)
        self.text_resultado.pack()

        self.operacion_tipo = None

        self.frame_widgets.update_idletasks()
        self.canvas_operaciones.configure(scrollregion=self.canvas_operaciones.bbox("all"))

    # Método para mostrar el instructivo
    def mostrar_instructivo(self):
        instructivo = """
        Instructivo de uso del programa

        1. Inicio de sesión
        --------------------

        Para comenzar a utilizar el programa, debes iniciar sesión en la ventana de login. Ingresa el usuario y la contraseña en los campos correspondientes y haz clic en el botón "Iniciar sesión". 
        Si la información es correcta, se te mostrará la ventana de operaciones con conjuntos.

        2. Ventana de operaciones
        -------------------------

        La ventana de operaciones es donde se realizan las operaciones con conjuntos. En esta ventana, puedes:

        * Generar un conjunto universal: Ingresa el número de elementos que deseas que tenga el conjunto universal en el campo "Número de elementos del conjunto universal". Luego, haz clic en el botón 
        "Generar Conjunto Universal". El programa generará automáticamente un conjunto universal con el número de elementos que ingresaste.
        * Visualizar el conjunto universal: El conjunto universal se mostrará en el área de texto "Conjunto Universal".
        * Generar subconjuntos: El programa generará automáticamente cuatro subconjuntos disjuntos (A, B, C y D) a partir del conjunto universal. Los subconjuntos se mostrarán en las etiquetas correspondientes.
        * Seleccionar subconjuntos: Puedes seleccionar los subconjuntos que dese as utilizar para realizar operaciones mediante los checkboxes correspondientes.

        3. Operaciones con subconjuntos
        -----------------------------

        Puedes realizar las siguientes operaciones con los subconjuntos seleccionados:

        * Unión: Muestra el conjunto resultante de la unión de los subconjuntos seleccionados. Haz clic en el botón "Unión" para realizar esta operación.
        * Intersección: Muestra el conjunto resultante de la intersección de los subconjuntos seleccionados. Haz clic en el botón "Intersección" para realizar esta operación.
        * Diferencia: Muestra el conjunto resultante de la diferencia entre los subconjuntos seleccionados. Haz clic en el botón "Diferencia" para realizar esta operación.
        * Complemento: Muestra el conjunto resultante del complemento de los subconjuntos seleccionados. Haz clic en el botón "Complemento" para realizar esta operación.

        4. Visualización de resultados
        -----------------------------

        Los resultados de las operaciones se mostrarán en el área de texto "Resultado". Puedes visualizar los resultados de las operaciones realizadas con los subconjuntos seleccionados.

        5. Generación de diagrama de Venn
        -----------------------------

        Puedes generar un diagrama de Venn que muestra la relación entre los subconjuntos seleccionados. Haz clic en el botón "Generar Diagrama de Venn" para realizar esta operación.
        El diagrama de Venn se mostrará en una ventana emergente.

        6. Instructivo
        -------------

        Puedes visualizar este instructivo en cualquier momento haciendo clic en el botón "Instructivo".
        El instructivo se mostrará en una ventana emergente.
        """
        messagebox.showinfo("Instructivo", instructivo)

    def generar_diagrama_venn(self):
        seleccionados = []
        if self.checkbutton_a.get():
            seleccionados.append('A')
        if self.checkbutton_b.get():
            seleccionados.append('B')
        if self.checkbutton_c.get():
            seleccionados.append('C')
        if self.checkbutton_d.get():
            seleccionados.append('D')

        operacion = self.operacion_tipo
        if operacion == "Unión":
            self.generar_diagrama_venn_interno("Unión", seleccionados)
        elif operacion == "Intersección":
            self.generar_diagrama_venn_interno("Intersección", seleccionados)
        elif operacion == "Diferencia":
            self.generar_diagrama_venn_interno("Diferencia", seleccionados)
        elif operacion == "Complemento":
            self.generar_diagrama_venn_interno("Complemento", seleccionados)

    def generar_diagrama_venn_interno(self, operacion, subconjuntos):
        fig, ax = plt.subplots()
        circles = []
        for i, subset in enumerate(subconjuntos):
            circle = plt.Circle((i, 0), 1, fill=False)
            ax.add_artist(circle)
            circles.append(circle)

            # Add label to the circle
            ax.text(i, 1.1, subset, ha='center', va='center')

        if operacion == "Intersección":
            # Add elements to the diagram
            elementos = list(set.intersection(*[self.subconjuntos[subset] for subset in subconjuntos]))
            num_elementos = len(elementos)
            angulos = np.linspace(0, 2*np.pi, num_elementos, endpoint=False)
            for j, elemento in enumerate(elementos):
                # Calcula la posición del elemento en la intersección
                x = (len(subconjuntos) - 1) / 2
                y = 0.5 * np.sin(angulos[j])
                ax.text(x, y, str(elemento), ha='center', va='center')
        elif operacion == "Unión":
            # Add elements to the diagram
            elementos = list(set.union(*[self.subconjuntos[subset] for subset in subconjuntos]))
            num_elementos = len(elementos)
            angulos = np.linspace(0, 2*np.pi, num_elementos, endpoint=False)
            for j, elemento in enumerate(elementos):
                ax.text(0.5 + np.cos(angulos[j]), np.sin(angulos[j]), str(elemento), ha='center', va='center')
        elif operacion == "Diferencia":
            # Add elements to the diagram
            elementos = list(set.difference(*[self.subconjuntos[subset] for subset in subconjuntos]))
            num_elementos = len(elementos)
            angulos = np.linspace(0, 2*np.pi, num_elementos, endpoint=False)
            for j, elemento in enumerate(elementos):
                ax.text(0.5 + np.cos(angulos[j]), np.sin(angulos[j]), str(elemento), ha='center', va='center')
        elif operacion == "Complemento":
            # Add elements to the diagram
            elementos = list(set.difference(self.subconjuntos['U'], *[self.subconjuntos[subset] for subset in subconjuntos]))
            num_elementos = len(elementos)
            angulos = np.linspace(0, 2*np.pi, num_elementos, endpoint=False)
            for j, elemento in enumerate(elementos):
                ax.text(0.5 + np.cos(angulos[j]), np.sin(angulos[j]), str(elemento), ha='center', va='center')

        ax.set_xlim(-2, 4)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')

        plt.show()

    def generar_conjunto_universal(self):
        try:
            num_elementos = int(self.entry_elementos_universal.get())
            conjunto_universal = set(random.sample(range(1, 100), num_elementos))
            self.text_conjunto_universal.delete(1.0, tk.END)
            self.text_conjunto_universal.insert(tk.END, f"U = {{{', '.join(str(x) for x in conjunto_universal)}}}")

            # Generar subconjuntos disjuntos
            self.subconjuntos = {
                'A': set(),
                'B': set(),
                'C': set(),
                'D': set(),
            }
            for i, subconjunto in enumerate(self.subconjuntos.values()):
                while len(subconjunto) < random.randint(1, len(conjunto_universal)):
                    elemento = random.choice(list(conjunto_universal))
                    if elemento not in subconjunto:
                        subconjunto.add(elemento)

            self.label_subconjunto_a.config(text=f"A = {self.subconjuntos['A']}")
            self.label_subconjunto_b.config(text=f"B = {self.subconjuntos['B']}")
            self.label_subconjunto_c.config(text=f"C = {self.subconjuntos['C']}")
            self.label_subconjunto_d.config(text=f"D = {self.subconjuntos['D']}")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero")

    def operacion(self, operacion_tipo):
        self.operacion_tipo = operacion_tipo
        try:
            conjunto_universal = set(self.text_conjunto_universal.get("1.0", tk.END).replace("U = {", "").replace("}", "").split(", "))
            conjunto_universal = set(int(x) for x in conjunto_universal)

            subconjuntos = {
                'A': set(self.label_subconjunto_a.cget("text").replace("A = {", "").replace("}", "").split(", ")),
                'B': set(self.label_subconjunto_b.cget("text").replace("B = {", "").replace("}", "").split(", ")),
                'C': set(self.label_subconjunto_c.cget("text").replace("C = {", "").replace("}", "").split(", ")),
                'D': set(self.label_subconjunto_d.cget("text").replace("D = {", "").replace("}", "").split(", ")),
            }

            subconjuntos = {k: set(int(x) for x in v) for k, v in subconjuntos.items()}

            seleccionados = []
            if self.checkbutton_a.get():
                seleccionados.append('A')
            if self.checkbutton_b.get():
                seleccionados.append('B')
            if self.checkbutton_c.get():
                seleccionados.append('C')
            if self.checkbutton_d.get():
                seleccionados.append('D')

            if operacion_tipo == "Unión":
                resultado = set()
                for subconjunto in seleccionados:
                    resultado = resultado.union(subconjuntos[subconjunto])
                self.text_resultado.delete (1.0, tk.END)
                self.text_resultado.insert(tk.END, f"{' U '.join(seleccionados)} = {{{', '.join(str(x) for x in resultado)}}}")
            elif operacion_tipo == "Intersección":
                resultado = conjunto_universal
                for subconjunto in seleccionados:
                    resultado = resultado.intersection(subconjuntos[subconjunto])
                self.text_resultado.delete(1.0, tk.END)
                self.text_resultado.insert(tk.END, f"{' ∩ '.join(seleccionados)} = {{{', '.join(str(x) for x in resultado)}}}")
            elif operacion_tipo == "Diferencia":
                resultado = self.subconjuntos[seleccionados[0]]
                for subconjunto in seleccionados[1:]:
                    resultado = resultado.difference(self.subconjuntos[subconjunto])
                self.text_resultado.delete(1.0, tk.END)
                self.text_resultado.insert(tk.END, f"{' - '.join(seleccionados)} = {{{', '.join(str(x) for x in resultado)}}}")
            elif operacion_tipo == "Complemento":
                resultado = conjunto_universal
                for subconjunto in seleccionados:
                    resultado = resultado.difference(subconjuntos[subconjunto])
                self.text_resultado.delete(1.0, tk.END)
                self.text_resultado.insert(tk.END, f"U {' - '.join(seleccionados)} = {{{', '.join(str(x) for x in resultado)}}}")
        except ValueError:
            messagebox.showerror("Error", "Error al procesar los conjuntos")

if __name__ == "__main__":
    root = tk.Tk()
    login_gui = LoginGUI(root)
    root.mainloop()
