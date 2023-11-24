import numpy as np
import matplotlib.pyplot as plt

def plavo_crvena_slika(square_size, square_amount_h, square_amount_w):
    plava = np.zeros((square_size, square_size, 3))  #Return a new array of given shape and type, filled with zeros.
    plava[:, :, 2] = 255
    crvena = np.ones((square_size, square_size, 3)) #returns a new array of given shape and data type, where the element's value is set to 1.
    crvena[:, :, 0] = 255
    rows = []  #tu definiramo redove
    for i in range(square_amount_h):
        row = []
        for j in range(square_amount_w):
            if (i + j) % 2 == 0:
                row.append(plava)
            else:
                row.append(crvena)
        rows.append(np.hstack(row))
    img = np.vstack(rows)
    return img.astype('uint8')


generated_img = plavo_crvena_slika(50, 4, 5)
plt.imshow(generated_img, cmap='gray', vmin=0, vmax=255)
plt.show()