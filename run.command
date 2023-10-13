#!/bin/bash
echo "Starting Script"
cd /Users/wilsonteng/venv
source bin/activate
python3 Prices.py
echo "Script ran successfully!"
read -p "Press Enter to continue..."