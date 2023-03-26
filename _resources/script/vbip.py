#| fig-align: "center"
#| fig-cap: "Contribution des haut-parleurs et leur résultante, en rouge"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

spkrStep=np.pi/2
spkrStart=np.pi/4

db=lambda x: 20*np.log10(np.abs(x))
dbnorm=lambda x: 20*np.log10(np.abs(x)/np.max(x))
q=lambda phi: np.tan(phi)/np.tan(spkrStep/2)

fig, ax=plt.subplots()
fig.tight_layout()

sourceAzim = -np.pi/8
source = [1.4, 1.4*np.sin(sourceAzim)/np.cos(sourceAzim)]
speakersAzim = np.arange(spkrStart,2*np.pi+spkrStart,spkrStep)
speakers = []

for azim in speakersAzim:
    speakers.append([np.cos(azim),np.sin(azim)])

for speakerPos in speakers:
    ax.plot(speakerPos[0]*1.05, speakerPos[1]*1.05, "D", ms=20, color='black')
ax.plot(source[0], source[1], "o", ms=20, color='purple')

L=[]

# First speaker vector
X=speakers[0][0]
Y=speakers[0][1]
vNorm=(np.sqrt((1+q(sourceAzim))/2))

vec=np.array([-X,-Y])
vec=np.dot(vNorm/np.linalg.norm(vec),vec)
L.append(vec)

ax.quiver(X, Y, vec[0], vec[1], color='g', units='xy', scale=1)

# Second Speaker vector
X=speakers[len(speakers)-1][0]
Y=speakers[len(speakers)-1][1]
vNorm=(np.sqrt((1-q(sourceAzim))/2))

vec=np.array([-X,-Y])
vec=np.dot(vNorm/np.linalg.norm(vec),vec)
L.append(vec)

ax.quiver(X, Y, vec[0], vec[1], color='g', units='xy', scale=1)

#Plot V vector
V=np.add.reduce(L)
ax.quiver(0, 0, -V[0], -V[1], color='r', units='xy', scale=1)

#Plot E vector
sumSquare=0
sumSquareVec=[]
for vec in L:
    sumSquareVec.append(np.dot(np.power(np.linalg.norm(vec),2/np.linalg.norm(vec)),vec))
    sumSquare=sumSquare+np.power(np.linalg.norm(vec),2)
E=np.dot(np.add.reduce(sumSquareVec),1/sumSquare)
print(E)
ax.quiver(0, 0, -E[0], -E[1], color='b', units='xy', scale=1)

square_lim=1.6
ax.set_ylim(-square_lim,square_lim)
ax.set_xlim(-square_lim,square_lim)
# ax.set_rticks([-20, -12, -6, 0, 6])  # Less radial ticks
ax.legend()
ax.grid(True)
ax.set_aspect("equal")
plt.show()