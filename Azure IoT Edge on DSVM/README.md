# Welcome to Azure IoT Edge on Data Science Virtual Machine

This tool is an extension to the [Microsoft Azure Data Science Virtual Machine (DSVM)](http://aka.ms/dsvm) to add the Azure IoT Edge capability to bring the power of advanced analytics, machine learning, and artificial intelligence to the edge. The Azure IoT Edge run time will be layered on top of the [Ubuntu edition of the DSVM](http://aka.ms/dsvm/ubuntu),  combining the rich AI and Machine Learning toolset on the DSVM with the capabilities to build applications for the intelligent edge. 



## Pre-requisites
1. You have created an IoT Hub in your Azure subscription
2. You have create IoT edge devices within your IoT hub and have access to the device connection string which you will need when you provision the IoT Edge runtime components on the Data Science VM. 

Click the button below to create a Data Science VM and add-on the IoT Edge Runtime components.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2FDataScienceVM%2Fmaster%2FExtensions%2FIoTEdge%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>


**Note**: The VM Extension templates used in the Deploy to Azure operation above are available on the [DataScienceVM Github repo](https://github.com/Azure/DataScienceVM/tree/master/Extensions/IoTEdge). 
