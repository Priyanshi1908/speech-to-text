#!/usr/bin/env bash

   echo "Starting script execution"

   # Update package list and install PortAudio development library
   echo "Installing PortAudio development library"
   apt-get update && apt-get install -y portaudio19-dev

   echo "PortAudio installed"

   # Upgrade pip
   echo "Upgrading pip"
   pip install --upgrade pip

   # Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install Python dependencies from requirements.txt
   echo "Installing Python dependencies"
   pip install -r requirements.txt

   # Verify gunicorn installation
   echo "Gunicorn location:"
   which gunicorn

   echo "Script execution completed"