from PIL import Image
import numpy as np


def find_color(i, j, arr, height, width):
    counter = np.sum(arr[i: i + height, j: j + width]) / 3
    counter = counter // (height * width)
    return counter


def make_result_img(arr, height_1, width_1, steps):
    height = len(arr)
    width = len(arr[1])
    i = 0
    while i < height:
        j = 0
        while j < width:
            color = find_color(i, j, arr, height_1, width_1)
            arr[i: i + height_1, j: j + width_1, :] = int(color // steps) * steps
            j = j + width_1
        i = i + height_1

name_of_img = input('Name of Image: ')
img = Image.open(name_of_img)
arr = np.array(img, dtype='int64')
height = input('Height: ')
width = input('Width: ')
steps_number = int(input('Number of steps : '))
make_result_img(arr, int(height), int(width), steps_number)
arr = arr.astype(np.uint8)
res = Image.fromarray(arr)
res.save('res.jpg')