Downloading the dataset -
Dataset_imagenet.ipynb 

Preparing the dataset - 
Data_loader.ipynb removes the black and white images
Image_editing.ipynb changes the images to blemished,blurred and noisy images.

We took the data from ImageNet, since there are 14M images, we just took a subset of the same from HuggingFace. More, info can be found in the above 
mentioned files and the final report.

Models :

To address the second low risk problem, we built a Fully Connected Autoencoder model. The basic idea behind an autoencoder [1] is to encode an input image into a compressed representation and then decode the compressed representation back into an output image that is similar to the original input image
