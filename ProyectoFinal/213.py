import pandas as pd
import json
import random
from textblob import TextBlob

# Lista de lugares proporcionados
lugares = [
    "Bahia de Matanchen", "Playa Los Muertos", "Bucerias Art Walk", "Centro Historico de Tepic",
    "Galerias Vallarta", "Isla de Coral", "Islas Marietas", "Manantial La Tovara",
    "Mercado del Pueblo Sayulita", "Mexcaltitan", "Playa Destiladeras", "Playa El Anclote",
    "Playa Los Ayala", "Splash Water Park", "The Jazz Foundation", "Isla Isabel",
    "Cerro de la Contaduria", "Santuario de Cocodrilos El Cora"
]

# Funciones para crear datos ficticios
def crear_descripcion(lugar):
    descripcion_base = f"Un destino popular para los amantes de {random.choice(['la naturaleza', 'la historia', 'el arte', 'la playa', 'la aventura'])}, {lugar} ofrece una experiencia única con su {random.choice(['hermoso paisaje', 'rica historia cultural', 'vibrante escena artística', 'relajante ambiente de playa', 'emocionante aventura'])}."
    return descripcion_base

def calificacion_tripadvisor():
    return round(random.uniform(1, 5), 1)

def generar_comentarios_y_sentimiento():
    comentarios = []
    sentimientos = []
    for _ in range(random.randint(3, 10)):  # Número aleatorio de comentarios
        comentario = f"Es un lugar {random.choice(['increíble', 'agradable', 'no tan bueno', 'fantástico', 'decepcionante'])}. {random.choice(['Me encantó', 'Podría ser mejor', 'Fue una experiencia única', 'No cumplió mis expectativas', 'Superó mis expectativas'])}."
        comentarios.append(comentario)
        analisis = TextBlob(comentario)
        sentimientos.append(analisis.sentiment.polarity)

    json_comentarios = json.dumps(comentarios)
    promedio_sentimiento = sum(sentimientos) / len(sentimientos) if sentimientos else 0
    return json_comentarios, promedio_sentimiento

# Crear el DataFrame
data = []
for lugar in lugares:
    descripcion = crear_descripcion(lugar)
    location = random.choice(['sur', 'norte', 'oriente', 'occidente'])
    calificacion = calificacion_tripadvisor()
    comentarios, sentimiento = generar_comentarios_y_sentimiento()
    data.append([lugar, descripcion, location, calificacion, comentarios, sentimiento])

df = pd.DataFrame(data, columns=["Lugar", "Description", "Location", "Clasificacion TripAdvisor", "Comentarios", "Sentimiento"])

# Agregar una columna para "Promedio Clasificación Usuarios"
df['Promedio Clasificacion Usuarios'] = df.apply(lambda row: round(random.uniform(1, 5), 1), axis=1)

# Guardar el DataFrame en un archivo CSV
#csv_file_path = '/mnt/data/Lugares_Turisticos.csv'
csv_file_path = 'C:\\Users\\LENOVO\\Desktop\\Espe\\Modulo 4\\ProyectoFinal\\Lugares_Turisticos.csv'

df.to_csv(csv_file_path, index=False)

csv_file_path

