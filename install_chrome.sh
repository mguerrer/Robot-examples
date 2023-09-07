#!/bin/bash

# Download and install the latest version of Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Update the system package list and install any missing dependencies
sudo apt update
sudo apt install -f

# Clean up the downloaded package file
rm google-chrome-stable_current_amd64.deb