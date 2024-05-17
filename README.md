# PyRemoteControl
Remote control of Agilent 33522B 2-channel waveform generator.

# Installation
```cmd
git clone git@github.com:JzzzHung/PyRemoteControl.git
conda create --name PyRemoteControl python=3.8
conda activate PyRemoteControl
cd PyRemoteControl/
pip install -r requirements.txt
```

# Usage
```cmd
python example.py
```
1. Run example.py can get the VISA address of your Agilent 33522B.
2. Replace "VISA_ADDRESS" in line 5 of Agilent33522B.py with the VISA address obtained in the previous step.
3. Execute playground.ipynb