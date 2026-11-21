#!/bin/bash
DEST="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Workflow Integration Plugins/MagicMaskFree"

echo "Creating plugin directory (requires sudo)..."
sudo mkdir -p "$DEST"
sudo cp -R plugin/* "$DEST/"
sudo cp requirements.txt "$DEST/"
sudo chown -R $(whoami) "$DEST"

echo "Setting up Python virtual environment..."
cd "$DEST"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Done! Restart DaVinci Resolve and check Workspace > Workflow Integrations > Magic Mask Free."
