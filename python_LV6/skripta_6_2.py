from tensorflow import keras
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np


filename = 'test.png'

img = mpimg.imread(filename)[:, :, :3]
img = color.rgb2gray(img)
img = resize(img, (28, 28))

plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()

# Prebaciti sliku u vektor odgovarajuće veličine
img = img.reshape(1, 28*28)

# Vrijednosti piksela kao float32 (bijela znamenka na crnoj pozadini) - po potrebi zakomentirajte ovisno o kakvoj je input slika

# Učitavanje istrenirane neuronske mreže
model = keras.models.load_model("FCN/")

# Napravi predikciju
prediction = model.predict(img)
predicted_label = np.argmax(prediction)

# Ispisi predikciju
print("Predicted label:", predicted_label)

# Prikazi sliku s predikcijom
plt.figure()
plt.imshow(img.reshape(28, 28), cmap=plt.get_cmap('gray'))
plt.title("Predicted label: " + str(predicted_label))
plt.show()