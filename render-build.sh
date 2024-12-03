#!/usr/bin/env bash

# Install PortAudio library and development tools
apt-get update && apt-get install -y portaudio19-dev

# Proceed with the default Render build process
pip install -r requirements.txt
