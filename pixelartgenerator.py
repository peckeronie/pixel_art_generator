from PIL import Image


def makePixelArt(input_path, output_path, num_width, num_height, pixel_size):
    #initialize a new image
    new_img = Image.new('RGB', (num_width*pixel_size, num_height*pixel_size), color = 'red')
    
    img = None
    try:
        img  = Image.open(input_path)
    except IOError:
        return "Error"
    
    pixel_width = img.width/num_width
    pixel_height = img.height/num_height
    
    for i in range (0, num_width):
        for j in range(0, num_height):
            start_width = i * pixel_width
            end_width = start_width + pixel_width
            start_height = j * pixel_height
            end_height = start_height + pixel_height
            
            putColorPixel(img, start_height, end_height, start_width, end_width, pixel_size, new_img, i, j)
    
    new_img.save(output_path)
    print("Done")


def putColorPixel(img, start_height, end_height, start_width, end_width, pixel_size, new_img, i, j):
    # store (r, g, b) for that area into block_color
    block_color = getAverageColor(img, int(start_height), int(end_height), int(start_width), int(end_width))
    for a in range(0, pixel_size):
        for b in range(0, pixel_size):
            new_img.putpixel((i * pixel_size + a, j * pixel_size + b), block_color)

def getAverageColor(img, start_height, end_height, start_width, end_width):

    r_total = 0
    g_total = 0
    b_total = 0
    count = 0
    
    for x in range(start_width, end_width):
        for y in range(start_height, end_height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1
    return (int(r_total/count), int(g_total/count), int(b_total/count))





