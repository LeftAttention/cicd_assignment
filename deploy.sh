#!/bin/bash

# Define the repository, temporary directory, and Nginx HTML directory
REPO="https://github.com/LeftAttention/cicd_assignment.git"
DIR="$HOME/deployments/cicd_deployment/tmp_git_repo"
NGINX_HTML_DIR="/var/www/html"

# Clone the repository
git clone --depth=1 $REPO $DIR

# Copy the updated HTML file to the Nginx directory with sudo
sudo cp $DIR/index.html $NGINX_HTML_DIR

# Restart Nginx to apply changes
sudo systemctl restart nginx

# Clean up - delete the cloned repository
rm -rf $DIR