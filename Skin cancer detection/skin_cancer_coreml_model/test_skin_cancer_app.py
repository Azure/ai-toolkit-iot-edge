from sklearn.datasets import load_files       
from keras.utils import np_utils
import numpy as np
from glob import glob
import keras
from keras.preprocessing import image                  
from tqdm import tqdm
from keras.models import load_model
from PIL import ImageFile                            
ImageFile.LOAD_TRUNCATED_IMAGES = True    

# define function to load train, test, and validation datasets
def load_dataset(path):
    data = load_files(path)
    condition_files = np.array(data['filenames'])
    condition_targets = np_utils.to_categorical(np.array(data['target']), 2)
    return condition_files, condition_targets

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)


def condition(img_path):
    label = 'None'
    score = 0
    test_tensor = path_to_tensor(img_path).astype('float32')/255
    # obtain predicted vector
    condition_prediction = model.predict(test_tensor)
    print condition_prediction
    benign, malignant = condition_prediction.max(axis=0)
    if benign > malignant:
    	label = 'benign'
	score = benign
    else:
        label = 'malignant'
	score = malignant
    return label, score

### Test a malignant image 
test_image = '/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/test_images/malignant/54e755f6bae47850e86cdfef.jpg'
model = load_model('/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/weights.best.from_scratch.6.hdf5')
label, score = condition(test_image)
print label, score

### Test a benign image 
test_image = '/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/test_images/benign/57eea3479fc3c12a89bb51fa.jpg'
model = load_model('/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/weights.best.from_scratch.6.hdf5')
label, score = condition(test_image)
print label, score



