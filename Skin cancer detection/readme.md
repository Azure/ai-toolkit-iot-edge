# Mobile AI: Using Azure Machine Learning Workbench to develop Mobile AI applications for the Intelligent Edge

This full-length tutorial shows how to use Azure Machine Learning services (preview) end to end for creating a machine learning model for Skin Cancer Detection and run it on mobile phones.

Skin cancer is the most common form of cancer, globally accounting for at least 40% of cases. If detected at an early stage, it can be controlled. We want to create a mobile AI application for everyone to be able to quickly detect whether they need to seek help. The app can flag a set of images which in turn helps the doctors to be more efficient and only focus on the most critical images.

For this tutorial, we use the ISIC Skin Cancer dataset (https://isic-archive.com/). You can refer to this GitHub link (https://github.com/antriv/ISIC-Dataset-Downloader) to find out how to download this research dataset. 
In this tutorial, we - 
1) Build the Model using Azure Machine Learning
2) Convert the model to CoreML
3) Use the CoreML model in an iOS application

Azure Machine Learning Workbench is a cross-platform desktop application, which makes the modeling and model deployment process much faster versus what was possible before. 

Here we build an AI model that will take the image of a mole in real time and try to predict if the person is at risk or not. We create the deep learning model using a few simple functions and open-source packages supported in Azure ML. We use Azure Machine Learning Workbench to build this Skin Cancer detection model using Keras with Tensorflow backend. We use the Workbench for building the machine learning model and convert the model to CoreML format. We can drop this CoreML model in a Xamarin app and run the Xamarin app on an iPhone. 

## Prerequisites:
	pip install tensorflow keras tqdm h5py

## WorkBench experimentation steps:
To install and create the experimentation framework using AMLWorkbench, please follow the simple tutorial here (https://docs.microsoft.com/en-us/azure/machine-learning/preview/quickstart-installation). 
We upload the root folder as a project in AML Workbench. Once the project is created
1) We run the train_skin_cancer_app.py 
2) This produces a trained model
3) We then run the test_skin_cancer_app.py to test the accuracy of the model

## Running the AI model in iPhone
To bring the trained model on an iPhone and run it on the phone without any connection, we use the CoreML with a Xamarin App. We pip install coreML in the Workbench & run the keras_to_coreml_converter.py. This creates the mlmodel compatible to run on iOS. 

Now to use this CoreML model witha Xamarin app, we follow 4 steps:
1) Download a sample Xamarin app from here (https://github.com/Azure-Samples/cognitive-services-ios-customvision-sample)
2) We replace the Custom Vision API model here with our custom model which we created using AML Workbench.
3) We follow the instructions in this link (https://developer.xamarin.com/guides/ios/platform_features/introduction-to-ios11/coreml/).
4) We compile the coreml model in Xcode 9 or manually using the xcrun command
	"xcrun coremlcompiler compile {model.mlmodel} {outputFolder}"
5) We add a compiled CoreML model to the Resources directory of the project.  
6) Next I change the name of the model in the view controller file and load the compiled model
7) In view controller, we change the result extraction function to output the messages we want the app to spit out
8) Please find a sample ViewController.cs file in  the git here.

Thus we have a video version of the Xamarin app here which uses a real-time video feed as input and outputs a label. If the predicted label is at risk, the app suggests see a doctor. If the predicted label is not at risk, the app indicates all clear. 

With only 3 lines of code change in our sample Xamarin app, we can run any AI model model on our phone. We’re looking forward to seeing how you may utilize Azure Machine Learning for your business. Thank you! 

## Pretrained models
We have links to 2 pretrained models :

Link to pretrained KERAS Skin Cancer Model: https://microsoft-my.sharepoint.com/:u:/p/antriv/EbZqTzEk4uFJl5DBbaVkMRcBttyz8OXDJ_UxTrediVbUEw?e=VOqoCb

Link to Pretrained COREML Skin Cancer model: https://microsoft-my.sharepoint.com/:u:/p/antriv/EclA9kLa7Q5DsYG1yOIJjZUBjldLjeA1e0VF9FsE1gzj5w?e=IKkNUw
