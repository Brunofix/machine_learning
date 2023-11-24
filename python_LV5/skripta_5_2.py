import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image 
from sklearn.cluster import KMeans

# ucitaj sliku
img = image.imread("example.png")

# prikazi sliku
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray')
plt.show() 


# TODO: predstavi sliku kao vektor
(h,w) =img.shape
img_array=img.reshape(h*w,1)


# TODO: primijeni K-means na vektor (sliku)
n_colors=3
kmeans=KMeans(n_clusters=n_colors,random_state=0).fit(img_array)


# TODO: zamijeni svjetlinu svakog piksela s najblizim centrom
img_approx=kmeans.predict(img_array)
img_approx=img_approx.astype(np.float32)

for i in range(0,n_colors):
    img_approx[img_approx==i]=kmeans.cluster_centers_[i]

    img_approx=img_approx.reshape(h,w)


# TODO: prikazi dobivenu aproksimaciju (sliku)
plt.figure()
plt.subplot(1,2,1)
plt.title("input slika")
plt.imshow(img, cmap='gray')
plt.subplot(1,2,2)
plt.title('kompresirana')
plt.imshow(img_approx,cmap='gray')
plt.show()