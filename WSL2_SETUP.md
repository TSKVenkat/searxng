# 🚀 SearXNG on Windows via WSL2 (The Reliable Way)

Native Windows execution of SearXNG is experimental and prone to static file and plugin issues. **WSL2 (Windows Subsystem for Linux)** is the recommended way to run it perfectly on Windows.

## 1. Install WSL2 (If not already installed)
Open **PowerShell as Administrator** and run:
```powershell
wsl --install
```
*Restart your computer if prompted.*

## 2. Set Up SearXNG in WSL
Open **Ubuntu** (or your installed Linux distro) from the Start Menu and run these commands:

```bash
# 1. Update system
sudo apt update && sudo apt install -y python3-venv python3-pip git

# 2. Navigate to your existing Windows folder (no need to re-clone!)
# /mnt/c/Users/mohana/Desktop/searxng maps to C:\Users\mohana\Desktop\searxng
cd /mnt/c/Users/mohana/Desktop/searxng

# 3. Create a Linux-native virtual environment
# (We can't use the Windows one)
python3 -m venv searxng-wsl
source searxng-wsl/bin/activate

# 4. Install dependencies
pip install -U pip setuptools wheel
pip install -e .

# 5. Run SearXNG!
export SEARXNG_DEBUG=1
python searx/webapp.py
```

## 3. Access It
Open your Windows browser and go to:
👉 **http://127.0.0.1:8888**

It will work perfectly with all styles, plugins, and engines enabled!

## 4. (Optional) Run in Background
To keep it running in the background:
```bash
nohup python searx/webapp.py > searxng.log 2>&1 &
```
