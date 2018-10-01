# Azure IoT Edge Anomaly Detection Tutorial
These instructions are for creating the module used for anomaly detection in the [tutorial](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-deploy-machine-learning/).

1. Follow the [instructions in the documentation](https://docs.microsoft.com/en-us/azure/machine-learning/service/quickstart-get-started) to create an Azure Machine Learning workspace.  [Sample notebooks](https://aka.ms/aml-notebooks) for all the steps are also available.

2. Follow this [sample notebook](https://aka.ms/aml-notebook-deployment-aci) to create a Docker container image.

3. Your Docker image is now stored in Azure Container Registry and ready for [deployment to an Azure IoT Edge device](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-deploy-to-iot) or [deployment to the cloud](https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-deploy-to-aci).
