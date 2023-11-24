import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
import numpy as np
import matplotlib as sct

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

X=generate_data(500,1)
plt.figure()
plt.scatter(X[:,0],X[:,1])
plt.show()

KMeans= KMeans(n_clusters=3)
KMeans.fit(X)

plt.scatter(X[:,0],X[:,1],c=KMeans.labels_)
plt.show()


inertia_list = []
for num_clusters in range(1, 20):
    kmeans_model = KMeans(n_clusters=num_clusters, init="k-means++")
    kmeans_model.fit(X)
    inertia_list.append(kmeans_model.inertia_)

# plot the inertia curve
plt.plot(range(1,20),inertia_list)
plt.scatter(range(1,20),inertia_list)
plt.scatter(3, inertia_list[3], marker="X", s=300, c="r")
plt.xlabel("Number of Clusters", size=13)
plt.ylabel("Inertia Value", size=13)
plt.title("Inertia", size=17)
plt.show()