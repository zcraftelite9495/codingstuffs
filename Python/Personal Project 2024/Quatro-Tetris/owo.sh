#!/bin/bash

# Check if snap is installed
if command -v snap > /dev/null; then
  # If snap is installed, save the version to a variable
  SNAP_VERSION=$(snap --version | grep -oE 'snap[[:space:]]+([0-9.]+)' | sed 's/^snap //' | sed 's/[[:space:]]//g')
else
  # If snap is not installed, save "Not Installed" to the variable
  SNAP_VERSION="Not Installed"
fi

# Print the version of snap or "Not Installed"
echo "Snap version: $SNAP_VERSION"