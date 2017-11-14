#!/bin/bash
# Install IOT Edge Runtime and register the edge device
source /anaconda/bin/activate
pip install -U azure-iot-edge-runtime-ctl
iotedgectl setup --connection-string $1 --auto-cert-gen-force-no-passwords
iotedgectl start
