# Mobile AI: Using Azure Machine Learning Workbench to develop Mobile AI applications for the Intelligent Edge

This full-length tutorial shows how to use Azure Machine Learning services (preview) end to end for creating a machine learning model for Skin Cancer Detection and run it on mobile phones.

Skin cancer is the most common form of cancer, globally accounting for at least 40% of cases. If detected at an early stage, it can be controlled. We want to create a mobile AI application for everyone to be able to quickly detect whether they need to seek help. The app can flag a set of images which in turn helps the doctors to be more efficient and only focus on the most critical images.

For this tutorial, we use the ISIC Skin Cancer [dataset] (https://isic-archive.com/). You can refer to this GitHub [link] (https://github.com/antriv/ISIC-Dataset-Downloader) to find out how to download this research dataset. 
In this tutorial, we - 
1) Build the Model using Azure Machine Learning
2) Convert the model to CoreML
3) Use the CoreML model in an iOS application

Azure Machine Learning Workbench is a cross-platform desktop application, which makes the modeling and model deployment process much faster versus what was possible before. 

Here we build an AI model that will take the image of a mole in real time and try to predict if the person is at risk or not. We create the deep learning model using a few simple functions and open-source packages supported in Azure ML. We use Azure Machine Learning Workbench to build this Skin Cancer detection model using Keras with Tensorflow backend. We use the Workbench for building the machine learning model and convert the model to CoreML format. We can drop this CoreML model in a Xamarin app and run the Xamarin app on an iPhone. 

## Prerequisites:
	pip install tensorflow keras tqdm h5py

## Experimentation steps:
To install and create the experimentation framework using AMLWorkbench, please follow the simple tutorial here. 
We upload the root folder as a project in AML Workbench. Once the project is created -
	- We run the train_skin_cancer_app.py 
	- This produces a trained model
	- We then run the test_skin_cancer_app.py to test the accuracy of the model

To bring the trained model on an iPhone and run it on the phone without any connection, we use the CoreML with a Xamarin App. We pip install coreML in the Workbench & run the keras_to_coreml_converter.py. This creates the mlmodel compatible to run on iOS. 

Now to use this CoreML model witha Xamarin app, we follow 4 steps:
1) Download asample Xamarin app fron [here] (https://github.com/Azure-Samples/cognitive-services-ios-customvision-sample)
2) We replace the custom Vision API model here with our custom model which we created using AML Workbench.
3) We compile the coreml model in Xcode 9 or manually using the xcrun command. 
4) We add a compiled CoreML model to the Resources directory of the project.  
5) Next I change the name of the model in the controller file and load the compiled model here 
6) In view controller, we change the result extraction function to output the messages we want the app to spit out. 

Thus we have a video version of the Xamarin app here which uses a real-time video feed as input and outputs a label. If the predicted label is at risk, the app suggests see a doctor. If the predicted label is not at risk, the app indicates all clear. 

With only 3 lines of code change in our sample Xamarin app, we can run any AI model model on our phone. We’re looking forward to seeing how you may utilize Azure Machine Learning for your business. Thank you! 
