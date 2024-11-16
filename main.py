from PIL import Image

def rgb_to_greyscale(r, g, b):
    greyscale = 0.299*r + 0.587*g + 0.114*b
    return greyscale

def greyscale_to_letter(greyscale):
    if 0 <= greyscale < 51:
        return 'A'
    elif 51 <= greyscale < 102:
        return 'B'
    elif 102 <= greyscale < 153:
        return 'C'
    elif 154 <= greyscale < 205:
        return 'D'
    else:
        return 'E'
    
def image_to_letter(image_name, converted_name):
    image = Image.open(image_name)
    pixels = image.load()
    width, height = image.size
    print(width, height)

    letter_image = [[1 for i in range(height)] for j in range(width)]

    for i in range(height):
        for j in range(width):
            r, g, b = pixels[j, i]

            greyscale = rgb_to_greyscale(r, g, b)
            letter = greyscale_to_letter(greyscale)
            letter_image[j][i] = letter

    art = open(converted_name, 'w')
    for i in letter_image:
        art.write(''.join(i) + '\n')
    
    art.close()

image_to_letter('bee.movie.jpg', 'bee.movie.txt')