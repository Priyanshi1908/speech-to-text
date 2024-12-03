#!/usr/bin/env bash

   echo "Starting script execution"

   # Update package list and install PortAudio development library
   echo "Installing PortAudio development library"
   apt-get update && apt-get install -y portaudio19-dev

   echo "PortAudio installed"

   # Verify installation
   dpkg -l | grep portaudio

   # Upgrade pip
   echo "Upgrading pip"
   pip install --upgrade pip

   # Install Python dependencies from requirements.txt
   echo "Installing Python dependencies"
   pip install -r requirements.txt

   echo "Script execution completed"