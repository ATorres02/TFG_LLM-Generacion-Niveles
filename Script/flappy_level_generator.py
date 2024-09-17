from PIL import Image

# Definimos los sprites de cada caracter ASCII
sprite_map = {
    'X': 'sprites/blue_platform.png',
    'A': 'sprites/blue_rock.png',
    ' ': 'sprites/void.png',
    'P': 'sprites/brown_rock.png',
    'H': 'sprites/mushroom.png',
    'U': 'sprites/unicorn.png',
    'F': 'sprites/flappy.png',
    'E': 'sprites/ebira.png',
    '=': 'sprites/wall.png',
}

# Función para cargar y redimensionar un sprite a un tamaño mayor para favorecer
# la visualización de la imagen
def load_sprite(path, size):
    sprite = Image.open(path)
    sprite = sprite.resize(size)
    return sprite

# Función para transformar la matriz ASCII en una imagen
def ascii_to_image(ascii_matrix, sprite_size):
    rows = len(ascii_matrix)
    cols = len(ascii_matrix[0])
    img_width = cols * sprite_size[0]
    img_height = rows * sprite_size[1]
    
    # Creamos una imagen vacía
    output_image = Image.new('RGB', (img_width, img_height))

    # Rellenamos la imagen mientras recorremos la matriz
    for y, row in enumerate(ascii_matrix):
        for x, char in enumerate(row):
            if char in sprite_map:
                sprite = load_sprite(sprite_map[char], sprite_size)
                output_image.paste(sprite, (x * sprite_size[0], y * sprite_size[1]))
    
    return output_image

# Separamos todas las matrices guardadas en el txt
def load_ascii_matrices_from_file(filename, delimiter='---'):
    with open(filename, 'r') as file:
        content = file.read()
        matrices = content.split(delimiter)
        ascii_matrices = [matrix.strip().splitlines() for matrix in matrices if matrix.strip()]
    return ascii_matrices

# Cargamos las matrices ASCII desde el archivo
ascii_matrices = load_ascii_matrices_from_file('examples.txt')

# Definimos el nuevo tamaño de los sprites
sprite_size = (32, 32)

# Generamos las imágenes para cada matriz ASCII y las guardamos
for i, ascii_matrix in enumerate(ascii_matrices, start=1):
    output_image = ascii_to_image(ascii_matrix, sprite_size)
    #output_image.show()
    output_image.save(f'level{i}.png')
