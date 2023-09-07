#!/bin/bash

# Define the desired version of Chromedriver
CHROMEDRIVER_VERSION="116.0.5845.96"

# Determine the latest version of Chromedriver available
if [ "$CHROMEDRIVER_VERSION" == "latest" ]; then
    CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
fi

# Define the base URL for Chromedriver downloads
BASE_URL="https://chromedriver.storage.googleapis.com"

# Determine the appropriate download URL based on the Linux architecture
if [ "$(uname -m)" == "x86_64" ]; then
    DOWNLOAD_URL="$BASE_URL/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
else
    DOWNLOAD_URL="$BASE_URL/$CHROMEDRIVER_VERSION/chromedriver_linux32.zip"
fi

# Create a temporary directory for the download
TEMP_DIR=$(mktemp -d)

# Download and extract Chromedriver
echo "Downloading Chromedriver version $CHROMEDRIVER_VERSION..."
wget -q --show-progress -O "$TEMP_DIR/chromedriver.zip" "$DOWNLOAD_URL"
unzip -qq "$TEMP_DIR/chromedriver.zip" -d "$TEMP_DIR"

# Move Chromedriver to the desired location
echo "Installing Chromedriver..."
sudo mv "$TEMP_DIR/chromedriver" /usr/local/bin/chromedriver

# Set the correct permissions
sudo chmod +x /usr/local/bin/chromedriver
sudo export PATH="/usr/local/bin:$PATH"

# Clean up temporary files
rm -rf "$TEMP_DIR"

echo "Chromedriver installation complete!"