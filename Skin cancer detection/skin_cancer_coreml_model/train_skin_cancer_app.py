
# coding: utf-8

# In[1]:

from sklearn.datasets import load_files       
from keras.utils import np_utils
import numpy as np
from glob import glob
import keras

# define function to load train, test, and validation datasets
def load_dataset(path):
    data = load_files(path)
    condition_files = np.array(data['filenames'])
    condition_targets = np_utils.to_categorical(np.array(data['target']), 2)
    return condition_files, condition_targets

# load train, test, and validation datasets
train_files, train_targets = load_dataset('/data/Keras_Transfer_Learning/ISIC_Skin_Cancer/data/train')
valid_files, valid_targets = load_dataset('/data/Keras_Transfer_Learning/ISIC_Skin_Cancer/data/validation')
test_files, test_targets = load_dataset('/data/Keras_Transfer_Learning/ISIC_Skin_Cancer/data/test')

# load list of dog names
condition_names = [item[58:-1] for item in sorted(glob("/data/Keras_Transfer_Learning/ISIC_Skin_Cancer/data/train/*/"))]
print (condition_names)
# print statistics about the dataset
print('There are %d total categories.' % len(condition_names))
print('There are %s total images.\n' % len(np.hstack([train_files, valid_files, test_files])))
print('There are %d training images.' % len(train_files))
print('There are %d validation images.' % len(valid_files))
print('There are %d test images.'% len(test_files))


# In[2]:

from keras.preprocessing import image                  
from tqdm import tqdm

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)


# ---
# <a id='step3'></a>
# ## Step 3: Create a CNN to Classify Dog Breeds (from Scratch)
# 
# ### Pre-process the Data
# 
# We rescale the images by dividing every pixel in every image by 255.

# In[3]:

from PIL import ImageFile                            
ImageFile.LOAD_TRUNCATED_IMAGES = True                 

# pre-process the data for Keras
train_tensors = paths_to_tensor(train_files).astype('float32')/255
valid_tensors = paths_to_tensor(valid_files).astype('float32')/255
test_tensors = paths_to_tensor(test_files).astype('float32')/255


# ### (IMPLEMENTATION) Model Architecture
# 

# In[4]:
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(224, 224, 3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='sigmoid'))

model.summary()


# ### Compile the Model

# In[ ]:
#opt = keras.optimizers.Adadelta()
opt = keras.optimizers.Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])


# ### Train the Model
# 

# In[ ]:

from keras.callbacks import ModelCheckpoint  

### TODO: specify the number of epochs that you would like to use to train the model.

epochs = 15

checkpointer = ModelCheckpoint(filepath='weights.best.from_scratch.6.hdf5', 
                               verbose=1, save_best_only=True)

model.fit(train_tensors, train_targets, 
          validation_data=(valid_tensors, valid_targets),
          epochs=epochs, batch_size=10, callbacks=[checkpointer], verbose=1)

# ### Load the Model with the Best Validation Loss

# In[5]:

model.load_weights('weights.best.from_scratch.6.hdf5')


# ### Test the Model
# 

# In[6]:

# get index of predicted dog breed for each image in test set
condition_predictions = [np.argmax(model.predict(np.expand_dims(tensor, axis=0))) for tensor in test_tensors]

# report test accuracy
test_accuracy = 100*np.sum(np.array(condition_predictions)==np.argmax(test_targets, axis=1))/len(condition_predictions)
print('Test accuracy: %.4f%%' % test_accuracy)

