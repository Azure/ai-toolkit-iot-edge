# Azure IoT Edge Anomaly Detection Tutorial
These instructions are for creating the module used for anomaly detection in the [tutorial](https://docs.microsoft.com/en-us/azure/iot-edge/tutorial-deploy-machine-learning/).

1. Open the [Azure ML CLI](https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-service-deploy) and set your environment.  If you haven't set up your environment, go to the [Environment set up section](https://github.com/Azure/ai-toolkit-iot-edge).
2. Deploy the trained model
```
$ az ml service create realtime --model-file model.pkl -f iot_score.py -n [your service name] -r python
```
3. Your Docker image is now stored in Azure Container Registry and ready for [deployment to an Azure IoT Edge device](https://docs.microsoft.com/en-us/azure/machine-learning/preview/deploy-to-iot-edge-device) or [consumption](https://docs.microsoft.com/en-us/azure/machine-learning/preview/model-management-consumption).
