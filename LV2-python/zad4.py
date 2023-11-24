import numpy as np
import matplotlib.pyplot as plt

def crno_bijela_img(square_size, square_amount_h, square_amount_w):
    crna_kocka = np.zeros((square_size, square_size))
    bijela_kocka = np.ones((square_size, square_size)) * 255
    rows = []
    for i in range(square_amount_h):
        row = []
        for j in range(square_amount_w):
            if (i+j) % 2 == 0:
                row.append(crna_kocka)
            else:
                row.append(bijela_kocka)
        rows.append(np.hstack(row))
    img = np.vstack(rows)
    return img.astype('uint8')

generated_img = crno_bijela_img(50, 4, 5)
plt.imshow(generated_img, cmap='gray', vmin=0, vmax=255)
plt.show()