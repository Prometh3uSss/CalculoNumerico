import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel

class ProposicionMolecularApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Constructor de Proposiciones Moleculares")
        
        self.proposiciones = []
        self.conectivos = []  # Lista para almacenar los conectivos
        
        # Etiqueta y campo de entrada
        self.label = tk.Label(root, text="Introduce una proposición:")
        self.label.pack()
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        
        # Botón para agregar proposición
        self.add_button = tk.Button(root, text="Agregar Proposición", command=self.agregar_proposicion)
        self.add_button.pack()
        
        # Lista para mostrar proposiciones
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.pack()
        
        # Botón para mostrar la fórmula
        self.show_button = tk.Button(root, text="Mostrar Fórmula", command=self.mostrar_formula)
        self.show_button.pack()
        
        # Botón para eliminar proposición
        self.delete_button = tk.Button(root, text="Eliminar Proposición", command=self.eliminar_proposicion)
        self.delete_button.pack()
        
        # Botón para editar proposición
        self.edit_button = tk.Button(root, text="Editar Proposición", command=self.editar_proposicion)
        self.edit_button.pack()
        
        # Botón para combinar proposiciones
        self.combine_button = tk.Button(root, text="Combinar Proposiciones", command=self.abrir_combinar_proposiciones)
        self.combine_button.pack()
        
        # Área de texto para mostrar resultados
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()
        
        # Botones para conectivos lógicos
        self.btn_disyuncion = tk.Button(root, text="Disyunción (∨)", command=lambda: self.agregar_conectivo("∨"))
        self.btn_disyuncion.pack()
        
        self.btn_conjuncion = tk.Button(root, text="Conjunción (∧)", command=lambda: self.agregar_conectivo("∧"))
        self.btn_conjuncion.pack()
        
        self.btn_negacion = tk.Button(root, text="Negación (¬)", command=lambda: self.agregar_conectivo("¬"))
        self.btn_negacion.pack()
        
        self.btn_condicional = tk.Button(root, text="Condicional (→)", command=lambda: self.agregar_conectivo("→"))
        self.btn_condicional.pack()
        
        self.btn_bicondicional = tk.Button(root, text="Bicondicional (↔)", command=lambda: self.agregar_conectivo("↔"))
        self.btn_bicondicional.pack()

    def agregar_proposicion(self):
        proposicion = self.entry.get().strip()
        if proposicion:
            self.proposiciones.append(proposicion)
            self.listbox.insert(tk.END, proposicion)  # Agregar a la lista
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
            messagebox.showinfo("Éxito", f"Proposición '{proposicion}' agregada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una proposición.")
    
    def agregar_conectivo(self, conectivo):
        seleccion = self.listbox.curselection()  # Obtener la selección actual
        if seleccion:
            index = seleccion[0]  # Solo se permite un conectivo por el momento
            self.conectivos.append((index, conectivo))  # Guardar el índice y el conectivo
            self.listbox.insert(index + 1, conectivo)  # Insertar el conectivo después de la proposición seleccionada
            self.listbox.select_set(index + 1)  # Seleccionar el conectivo recién agregado
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una proposición para agregar un conectivo.")

    def mostrar_formula(self):
        if not self .proposiciones and not self.conectivos:
            messagebox.showwarning("Advertencia", "No hay proposiciones para mostrar.")
            return
        
        formula = []  # Inicializar la lista para la fórmula
        for i in range(len(self.proposiciones)):
            formula.append(self.proposiciones[i])
            # Verificar si hay un conectivo después de la proposición
            for index, conectivo in self.conectivos:
                if index == i:
                    formula.append(conectivo)
        
        # Agregar la última proposición si existe
        if self.proposiciones:
            formula.append(self.proposiciones[-1])
        
        self.result_text.delete(1.0, tk.END)  # Limpiar el área de texto
        self.result_text.insert(tk.END, f"Fórmula Bien Formada:\n{' '.join(formula)}")

    def eliminar_proposicion(self):
        seleccion = self.listbox.curselection()  # Obtener la selección actual
        if seleccion:
            for index in reversed(seleccion):  # Eliminar en orden inverso para evitar problemas de índice
                proposicion = self.listbox.get(index)  # Obtener la proposición seleccionada
                if proposicion in self.proposiciones:
                    self.proposiciones.remove(proposicion)  # Eliminar de la lista interna
                self.listbox.delete(index)  # Eliminar de la lista visual
            messagebox.showinfo("Éxito", "Proposición(es) eliminada(s).")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una proposición para eliminar.")

    def editar_proposicion(self):
        seleccion = self.listbox.curselection()  # Obtener la selección actual
        if seleccion:
            proposicion_actual = self.listbox.get(seleccion)  # Obtener la proposición seleccionada
            nueva_proposicion = simpledialog.askstring("Editar Proposición", "Introduce la nueva proposición:")
            if nueva_proposicion:
                index = self.proposiciones.index(proposicion_actual)  # Obtener el índice de la proposición actual
                self.proposiciones[index] = nueva_proposicion  # Actualizar la proposición en la lista interna
                self.listbox.delete(seleccion)  # Eliminar la proposición antigua de la lista visual
                self.listbox.insert(seleccion, nueva_proposicion)  # Agregar la nueva proposición en la misma posición
                messagebox.showinfo("Éxito", f"Proposición '{proposicion_actual}' editada a '{nueva_proposicion}'.")
            else:
                messagebox.showwarning("Advertencia", "La nueva proposición no puede estar vacía.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una proposición para editar.")

    def abrir_combinar_proposiciones(self):
        if not self.proposiciones:
            messagebox.showwarning("Advertencia", "No hay proposiciones para combinar.")
            return
        
        self.ventana_combinar = Toplevel(self.root)
        self.ventana_combinar.title("Combinar Proposiciones")
        
        self.listbox_combinar = tk.Listbox(self.ventana_combinar, height=10, width=50, selectmode=tk.MULTIPLE)
        self.listbox_combinar.pack()
        
        for proposicion in self.proposiciones:
            self.listbox_combinar.insert(tk.END, proposicion)  # Agregar proposiciones a la nueva lista
        
        self.boton_confirmar = tk.Button(self.ventana_combinar, text="Confirmar Combinación", command=self.confirmar_combinacion)
        self.boton_confirmar.pack()
        
        self.boton_cancelar = tk.Button(self.ventana_combinar, text="Cancelar", command=self.ventana_combinar.destroy)
        self.boton_cancelar.pack()
        
        # Botones para mover proposiciones
        self.boton_arriba = tk.Button(self.ventana_combinar, text="Mover Arriba", command=self.mover_arriba)
        self.boton_arriba.pack()
        
        self.boton_abajo = tk.Button(self.ventana_combinar, text="Mover Abajo", command=self.mover_abajo)
        self.boton_abajo.pack()

    def mover_arriba(self):
        seleccion = self.listbox_combinar.curselection()  # Obtener la selección actual
        if seleccion:
            for index in seleccion:
                if index > 0:  # Asegurarse de que no se mueva fuera de los límites
                    item = self.listbox_combinar.get(index)
                    self.listbox_combinar.delete(index)
                    self.listbox_combinar.insert(index - 1, item)  # Mover hacia arriba
                    self.listbox_combinar.select_set(index - 1)  # Seleccionar el nuevo índice

    def mover_abajo(self):
        seleccion = self.listbox_combinar.curselection()  # Obtener la selección actual
        if seleccion:
            for index in reversed(seleccion):  # Mover hacia abajo en orden inverso
                if index < self.listbox_combinar.size() - 1:  # Asegurarse de que no se mueva fuera de los límites
                    item = self.listbox_combinar.get(index)
                    self.listbox_combinar.delete(index)
                    self.listbox_combinar.insert(index + 1, item)  # Mover hacia abajo
                    self.listbox_combinar.select_set(index + 1)  # Seleccionar el nuevo índice

    def confirmar_combinacion(self):
        seleccion = self.listbox_combinar.curselection()  # Obtener las selecciones actuales
        if seleccion:
            combinacion = ' + '.join(self.listbox_combinar.get(i) for i in seleccion)  # Combinar las proposiciones seleccionadas
            self.result_text.delete(1.0, tk.END)  # Limpiar el área de texto
            self.result_text.insert(tk.END, f"Combinación de Proposiciones:\n{combinacion}")
            self.ventana_combinar.destroy()  # Cerrar la ventana de combinación
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona al menos una proposición para combinar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProposicionMolecularApp(root)
    root.mainloop()