import random

PRODUCTOSPRUEBA = ["Mi banana","Tu Durazno","Preservativo","Juguete Raro","Plumbus","Leche Normal","Vibrer","Una Concha","Salchichón","Cuernos que te quedan","Pepino","Mantequilla de mani","Agujero en Pared","Galleta Humilde", "Tornillo Volador", "Zapato que Muerde", "Cactus Suave", "Cuerda Floja", "Piedra Cantante", "Camisa Invisible", "Cepillo Atrevido", "Pelota de Espinas", "Sombrero con Hueco", "Llave que no Abre", "Taza que Habla"]

def getProducts():
    random.shuffle(PRODUCTOSPRUEBA)
    return [{"name":producto,"price":random.randint(2,400)*100} for producto in PRODUCTOSPRUEBA]


