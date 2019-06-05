# Welcome to the AI Toolkit for Azure IoT Edge

The integration of Azure Machine Learning and Azure IoT Edge enables organizations and developers to apply AI and ML to data that can’t make it to the cloud due to data sovereignty, privacy, and/or bandwidth issues. All models created using Azure Machine Learning can now be deployed to IoT gateways and devices with the Azure IoT Edge runtime. Models are operationalized as containers and can run on many types of hardware, from very small devices all the way to powerful servers.

We're releasing this toolkit to help get you started with AI and Azure IoT Edge. The toolkit will show you how to package deep learning models in Azure IoT Edge-compatible Docker containers and expose those models as REST APIs. We've included examples to help get you started, but the possibilities are endless. We'll be adding new examples and tools often. The models can be used as-is or and customized to better meet your specific needs and use cases. 

Please ask any questions on our [forum](https://social.msdn.microsoft.com/forums/azure/en-US/home?forum=MachineLearning).  We welcome your feedback and contributions and look forward to building together.

## Concepts
* [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/service/) is designed for data scientists to build, deploy, manage, and monitor models at any scale
* [Azure IoT Edge](https://aka.ms/azure-iot-edge-doc) moves cloud analytics and custom business logic to devices as an Internet of Things (IoT) service that builds on top of IoT Hub
* AI Toolkit for Azure IoT Edge is an evolving set of scripts, sample code, and tutorials that enable you to easily set up a test environment and run AI and ML on an edge device

# Quick start
## AI on the edge
One use case for edge devices is image processing and object classification.  For example, images taken by cameras of products on an assembly line in a factory may be analyzed for manufacturing defects without having to send the images to the cloud.  To simplify this problem for the tutorial, we will create and deploy a model that will take in an image of a handwritten digit and predict what that number is.  We will use the well-known [MNIST](http://yann.lecun.com/exdb/mnist/) data set and a pre-trained [TensorFlow](https://www.tensorflow.org/) model.

## Environment set up
If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free/?WT.mc_id=A261C142F) before you begin.

1. [Get started with Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/service)
1. [Create an IoT Hub and register an IoT Edge device](https://aka.ms/azure-iot-edge-doc)
1. [Create an IoT Edge device](https://github.com/Azure/ai-toolkit-iot-edge/tree/master/Azure%20IoT%20Edge%20on%20DSVM) with the Data Science VM (DSVM)
  * You will need a connection string from the IoT Hub you created in the previous step
  * This DSVM doubles as an IoT Edge device and the machine you can use to operationalize models

## Set up Model Management for Azure ML
If you are already an Azure ML user then skip to the next section.

If you are not using the DSVM from the previous section for Azure ML, then [set up Model Management](https://docs.microsoft.com/en-us/azure/machine-learning/preview/deployment-setup-configuration) on your machine.

Otherwise, follow these steps (more details in the [Model Management documentation](https://docs.microsoft.com/en-us/azure/machine-learning/preview/deployment-setup-configuration)):

1. Connect and log into the DSVM you created in the previous section
2. Open a command prompt (type `az ml -h` to see options)
3. Run the script below to configure Docker correctly (Docker is pre-installed on the DSVM). **Remember to log out and log back in after running the script.**
```
sudo /opt/microsoft/azureml/initial_setup.sh
```
4. Set up the environment (only needs to be done one time).  Note when completing the environment setup:
  * You are prompted to sign in to Azure. To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the provided code to authenticate.
  * During the authentication process, you are prompted for an account to authenticate with. Important: Select an account that has a valid Azure subscription and sufficient permissions to create resources in the account.
  * When the log-in is complete, your subscription information is presented and you are prompted whether you wish to continue with the selected account.

5. Register the environment provider by entering the following command:

```azurecli
az provider register -n Microsoft.MachineLearningCompute
```
6. Set up a local environment using the following command. The resource group name is optional.

```azurecli
az ml env setup -l [Azure Region, e.g. eastus2] -n [your environment name] [-g [existing resource group]]
```

7. The local environment setup command creates the following resources in your subscription:
* A resource group (if not provided, or if the name provided does not exist)
* A storage account
* An Azure Container Registry (ACR)
* An Application insights account

After setup completes successfully, set the environment to be used using the following command:

```azurecli
az ml env set -n [environment name] -g [resource group]
```
*Note:* For subsequent deployments, you only need to use the set command above to reuse it.

You are now ready to deploy your saved model as a web service.

## Create container for Azure IoT Edge
[Follow these steps](https://github.com/Azure/ai-toolkit-iot-edge/tree/master/MNIST%20classification%20with%20TensorFlow) to create the container for deployment to Azure IoT Edge running on your DSVM.

# Next Steps
Check out our set of rich tutorials, where you can create, train, and deploy models for [predictive maintenance](https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-predictive-maintenance), [aerial image classification](https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-aerial-image-classification), [energy demand time series forecasting](https://docs.microsoft.com/en-us/azure/machine-learning/preview/scenario-time-series-forecasting), and more.  Then create your own!

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
