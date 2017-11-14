import coremltools
import h5py
scale = 1/255.
output_labels = ['benign', 'malignant']
coreml_model = coremltools.converters.keras.convert('/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/weights.best.from_scratch.6.hdf5')

coreml_model.author = ''   
coreml_model.short_description = 'Model to classify skin cancer'      
print(coreml_model)
coreml_model.save('/Users/ted/Documents/skin_cancer_edge/skin_cancer_coreml_27_shared_folder/weights_skin_cancer.mlmodel')
