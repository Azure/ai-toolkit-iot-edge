## Instructions

Create a device identity for your simulated device so that it can communicate with your IoT hub. Since IoT Edge devices behave and can be managed differently than typical IoT devices, you declare this to be an IoT Edge device from the beginning.

* Click [here]({Outputs.iotEdgeDevice}) to **Add IoT Edge Device** 

1. In the Azure portal, navigate to your IoT hub.
1. Select **IoT Edge (preview)** then select **Add IoT Edge Device**.

   ![Add IoT Edge Device](https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/includes/media/iot-edge-register-device/add-device.png)

1. Give your simulated device a unique device ID.
1. Select **Save** to add your device.
1. Select your new device from the list of devices.
1. Copy the value for **Connection string--primary key**.
1. Paste into the **IoT Edge Device Connection string--primary key** parameter below and click Next.