# Mobile AI: Using Azure Machine Learning Workbench to develop Mobile AI applications for the Intelligent Edge

This full-length tutorial shows how to use Azure Machine Learning services (preview) end to end for creating a machine learning model for Skin Cancer Detection and run it on mobile phones.

Skin cancer is the most common form of cancer, globally accounting for at least 40% of cases. If detected at an early stage, it can be controlled. We want to create a mobile AI application for everyone to be able to quickly detect whether they need to seek help. The app can flag a set of images which in turn helps the doctors to be more efficient and only focus on the most critical images.

For this tutorial, we use the ISIC Skin Cancer dataset. You can refer to this GitHub link to find out how to download this research dataset. 
In this tutorial, we - 
1.Build the Model using Azure Machine Learning
2.Convert the model to CoreML
3.Use the CoreML model in an iOS application

Azure Machine Learning Workbench is a cross-platform desktop application, which makes the modeling and model deployment process much faster versus what was possible before. 

Here we build an AI model that will take the image of a mole in real time and try to predict if the person is at risk or not. We create the deep learning model using a few simple functions and open-source packages supported in Azure ML. We use Azure Machine Learning Workbench to build this Skin Cancer detection model using Keras with Tensorflow backend. We use the Workbench for building the machine learning model and convert the model to CoreML format. We can drop this CoreML model in a Xamarin app and run the Xamarin app on an iPhone. 

Prerequisites:
	pip install tensorflow
	pip install keras
	pip install tqdm
	pip install h5py
		
We have the data in the format below:
	-train
	   -benign
	   -malignant
	-validation
	   -benign
	   -malignant
	test
	   -benign
	   -malignant

Experimentation steps:
To install and create the experimentation framework using AMLWorkbench, please follow the simple tutorial here. 
We upload the root folder as a project in AML Workbench. Once the project is created -
	- We run the train_skin_cancer_app.py 
	- This produces a trained model
	- We then run the test_skin_cancer_app.py to test the accuracy of the model
To bring the trained model on an iPhone and run it on the phone without any connection, we use the CoreML with a Xamarin App. We pip install coreML in the Workbench 

& run the keras_to_coreml_converter.py. This creates the mlmodel compatible to run on iOS. We drop this mlmodel to a Xamarin app, and only with 3 lines of code change we can run the model on our phone. We have two versions of the app here:
1) The AzureML.CoreML.Photo uses a static photo as input and outputs a label. 
2) The AzureML.CoreML.Video uses a real-time video feed as input and outputs a label. 
If the predicted label is at risk, the app suggests see a doctor. If the predicted label is not at risk, the app indicates all clear. 

As we see here, AML Workbench makes it amazingly easy to develop the end-2-end pipeline for Intelligent Edge applications. Hope you find this app useful. We’re looking forward to seeing how you may utilize Azure Machine Learning for your business. Thank you!

