from PyPDF2 import PdfWriter, PdfReader
import fitz
import os

#inputfile_path = "H:\My Drive\RECORTE PDF\ml.pdf"
#inputfile_path2 = "H:\My Drive\RECORTE PDF\ml_salida2.pdf"
#outputfile_path = "H:\My Drive\RECORTE PDF\ml_salida5.pdf"

def recortar_etiquetas_ml(inputfile_path,outputfile_path):
    print("Iniciando recorte de etiquetas...")
    reader1 = PdfReader(inputfile_path)  
    reader2 = PdfReader(inputfile_path)
    reader3 = PdfReader(inputfile_path)  
    writer = PdfWriter()
    recorte_superior=25   #   DISTANCIA EN PIXELES QUE RECORTA DE LA PARTE SUPERIOR
    recorte_inferior=140  #   DISTANCIA EN PIXELES QUE RECORTA DE LA PARTE INFERIOR

    totalPages1 = len(reader1.pages)
    print(f"Páginas Totales del documento de entrada: {totalPages1}")

    for i in range(totalPages1-1):
    
   
        page1 = reader1.pages[i]
        
        #print (page1.mediabox.right)
        #print (page1.mediabox.top)
        page1.mediabox.upper_right = (
            page1.mediabox.right-550,
            page1.mediabox.top-recorte_superior,
        )
        page1.mediabox.lower_left = (
            page1.mediabox.left+25,
            page1.mediabox.bottom+recorte_inferior,
        )

 
        writer.add_page(page1)

        page2 = reader2.pages[i]
        #print (page2.mediabox.right)
        #print (page2.mediabox.top)
        page2.mediabox.upper_right = (
            page2.mediabox.right-285,
            page2.mediabox.top-recorte_superior,
        )
        page2.mediabox.lower_left = (
            page2.mediabox.left+290,
            page2.mediabox.bottom+recorte_inferior,
        )

        writer.add_page(page2)

        page3 = reader3.pages[i]
        #print (page3.mediabox.right)-
        #print (page3.mediabox.top)
        page3.mediabox.upper_right = (
            page3.mediabox.right-20,
            page3.mediabox.top-recorte_superior,
        )
        page3.mediabox.lower_left = (
            page3.mediabox.left+555,
            page3.mediabox.bottom+recorte_inferior,
        )
    
        writer.add_page(page3)
    with open(outputfile_path, "wb") as fp:
        writer.write(fp)
    totalPages1 = len(writer.pages)
    #print(f"Páginas Totales salida intermedia: {totalPages1}")    
   
def contar_etiquetas(inputfile_path):
    print("Realizando conteo de etiquetas")
    texto=""
    input_pdf = fitz.open(inputfile_path)
    for pgno in range(input_pdf.page_count-1):
        page = input_pdf[pgno]
        texto = texto + page.get_text()
    #print(texto)  # A efectos de revisar el texto que encontró.
    cuenta_flex=texto.count("Envío Flex")
    cuenta_mercado_envios=(texto.count("Ciudad de destino:"))
    cuenta_mercado_envios=cuenta_mercado_envios//2    # se ha añadido ya que el lector PDF muestra duplicada la palabra. Se divide entre 2. division entera)
    cuenta=cuenta_flex+cuenta_mercado_envios
    print("Se encontraron " + str(cuenta_flex)+" etiquetas FLEX en el archivo.")
    print("Se encontraron " + str(cuenta_mercado_envios)+" etiquetas mercado envios en el archivo.")
    print("Se encontraron en total:" + str(cuenta)+" etiquetas.")
    input_pdf.close()
    return cuenta

def extraer_etiquetas(inputfile_path,outputfile_path,count):
    print("Realizando extraccion de "+str(count)+" etiquetas")
    input_pdf = fitz.open(inputfile_path)
    output_pdf = fitz.open()
    for pgno in range(count):
        #page = input_pdf[pgno]
        output_pdf.insert_pdf(input_pdf,from_page=pgno,to_page = pgno)
    input_pdf.close()
    output_pdf.save(outputfile_path)
    
    output_pdf.close()

def contar_recortar_extraer(filename):
    entrada=filename
    salida=filename
    salida=salida.replace(".pdf","_RECORTADO.pdf")
    cantidad=contar_etiquetas(entrada)
    recortar_etiquetas_ml(entrada,salida)
    extraer_etiquetas(salida,salida,cantidad)
    mensaje="Se guardará una copia recortada del archivo:\n\n"+ salida+"\n\n Cantidad de etiquetas: " + str(cantidad)+"\n\n"
    print(salida)
    os.system("start " + salida)
    #showinfo(
     #   title='Archivo Seleccionado',
     #   message=mensaje
    #)
    
    


#recortar_etiquetas_ml(inputfile_path,outputfile_path)
#extraer_etiquetas(outputfile_path,outputfile_path,contar_etiquetas(inputfile_path))


