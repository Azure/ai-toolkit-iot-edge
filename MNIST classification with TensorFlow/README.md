# MNIST handwritten digit classification using TensorFlow
The [full tutorial](https://github.com/Azure/MachineLearningSamples-tf/tree/RuonanO16N) contains all the steps and code to train and operationalize a model using Azure ML.  The abbreviated instructions here focus on creating the Docker container with the model.

1. Open the [Azure ML CLI](https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-service-deploy) and set your environment

2. You need these files:
* [my_ConvNet_MNIST_model.data-00000-of-00001](https://1drv.ms/u/s!Ap459opCDg3lgQp9a_kqXIZ2hAUo)
* my_ConvNet_MNIST_model.index
* my_ConvNet_MNIST_model.meta
* checkpoint
* conda_dependencies.yml
* webservice_driver.py

Deploy the trained model.
```
$ az ml service create realtime -m my_ConvNet_MNIST_model.meta -d my_ConvNet_MNIST_model.data-00001-of-00000 -d my_ConvNet_MNIST_model.index -d checkpoint -f webservice_driver.py -n [your service name] -r python -c conda_dependencies.yml
```

3. Test the model
```
$ python webservice_invoke.py
```

4. Your Docker image is now stored in Azure Container Registry and ready for [deployment to an Azure IoT Edge device](https://docs.microsoft.com/en-us/azure/machine-learning/preview/deploy-to-iot-edge-device) or [consumption](https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-consumption).
