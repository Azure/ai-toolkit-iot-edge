#!/bin/bash
# Install IOT Edge Runtime and register the edge device

# HOME is not set when the extension runs, so set it now
export HOME=$2

usermod -aG docker $2

source /anaconda/bin/activate root
pip install -U azure-iot-edge-runtime-ctl
iotedgectl setup --connection-string $1 --auto-cert-gen-force-no-passwords
iotedgectl start

chmod 644 /etc/azure-iot-edge/config.json