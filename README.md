# 2048 Game (v1.0)

Play 2048 game in GUI window.

# Packages

These packages are needed to be installed in order to run python files.

```cmd
pip3 install pygame
```

# Download Code

## Linux
### Installing
<li>Install python3 on your device. Then run</li>

```cmd
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
```

<li>Now run these commands to download & run code</li>

```cmd
git clone https://github.com/cybersaksham/2048-Game
cd 2048-Game
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

### Uninstalling
```cmd
deactivate
cd ..
rm -rf 2048-Game
```

## Windows
### Installing
<li>Install python3 & pip3 on your device.</li>

<li>Now run these commands to download & run code</li>

```cmd
git clone https://github.com/cybersaksham/2048-Game
cd 2048-Game
python3 -m venv venv
.\venv\Scripts\activate
pip3 install -r requirements.txt
python3 main.py
```

### Uninstalling

```cmd
deactivate
cd ..
rmdir /S 2048-Game
```
