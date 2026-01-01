from scipy import misc
import matplotlib.pyplot as plt
face = misc.face(gray = True)
plt.imshow(face, cmap=plt.cm.gray)
plt.show()
face.shape

h = face.shape[0]
w = face.shape[1]
zoom_face = face[h//4 : -h//4, w//4 : -w//4]
zoom_face[zoom_face > 150] = 255
plt.imshow(zoom_face, cmap=plt.cm.gray)
plt.show

face = face[::2, ::2]
#cette ligne permet de divisé le poids de l'image en deux sans perdre trop de qualité