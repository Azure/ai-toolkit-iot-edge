# Welcome to the Azure Machine Learning and IoT Edge Solution Template

The integration of Azure Machine Learning and Azure IoT Edge enables organizations and developers to apply AI and ML to data that can’t make it to the cloud due to data sovereignty, privacy, and/or bandwidth issues. All models created using Azure Machine Learning can now be deployed to IoT gateways and devices with the Azure IoT Edge runtime. Models are operationalized as containers and can run on many types of hardware, from very small devices all the way to powerful servers.

We're releasing this solution template to accompany the toolkit to help get you started with AI and Azure IoT Edge. This solution template and toolkit will show you how to package deep learning models in Azure IoT Edge-compatible Docker containers and expose those models as REST APIs. We've included examples to help get you started, but the possibilities are endless. We'll be adding new examples and tools often. The models can be used as-is or and customized to better meet your specific needs and use cases. 

Please ask any questions on our [forum](https://social.msdn.microsoft.com/forums/azure/en-US/home?forum=MachineLearning).  We welcome your feedback and contributions and look forward to building together.

## Concepts
* [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/preview/) is designed for data scientists to build, deploy, manage, and monitor models at any scale
* [Azure IoT Edge](https://aka.ms/azure-iot-edge-doc) moves cloud analytics and custom business logic to devices as an Internet of Things (IoT) service that builds on top of IoT Hub
* [AI Toolkit for Azure IoT Edge](https://github.com/Azure/ai-toolkit-iot-edge) is an evolving set of scripts, sample code, and tutorials that enable you to easily set up a test environment and run AI and ML on an edge device

## Image processing using AI on the edge
Deploying this solution template sets up the Azure resources to meet many use cases.  One use case for edge devices is image processing and object classification.  For example, images taken by cameras of products on an assembly line in a factory may be analyzed for manufacturing defects without having to send the images to the cloud.  To simplify this problem for the tutorial, we will create and deploy a model that will take in an image of a handwritten digit and predict what that number is.  We will use the well-known [MNIST](http://yann.lecun.com/exdb/mnist/) data set and a pre-trained [TensorFlow](https://www.tensorflow.org/) model.

## Azure environment set up
If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.

