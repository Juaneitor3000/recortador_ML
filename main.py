import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import sys
import funciones
import os

try:
    filename=sys.argv[1]
    #if "open with" has been used
    print(filename)
    funciones.contar_recortar_extraer(filename)
    
except:
    #do nothing
    pass

#create the root window
root = tk.Tk()
root.title('Recortador de Etiquetas 1.2             Enero 2024-Juan Marcano')
root.resizable(False, False)
root.geometry('500x100')

def select_file():
    filetypes = (
        ('archivos pdf', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Abrir un Archivo',
        initialdir='/',
        filetypes=filetypes)
    funciones.contar_recortar_extraer(filename)
    showinfo(
        title='Archivo Seleccionado',
        message="Se ha guardado una copia recortada del documento"
    )
   
# open button
open_button = ttk.Button(
    root,
    text='Abrir un archivo',
    command=select_file,
)

open_button.pack(expand=True)

# run the application
root.mainloop()