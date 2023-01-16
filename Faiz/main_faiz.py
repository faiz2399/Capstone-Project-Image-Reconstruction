import pickle
import numpy as np
import matplotlib.pyplot as plt





file = open('imagenet_subset.pkl', 'rb')

# dump information to that file
ds_p = pickle.load(file)



plt.figure()
plt.imshow(ds_p[1])

plt.figure()

plt.imshow(np.array(ds_p['train'][1]["image"]))


plt.figure()

plt.imshow(np.array(ds_p['train'][4]["image"]))



# close the file
file.close()