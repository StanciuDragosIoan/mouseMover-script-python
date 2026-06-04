python3 -m venv mover-env
source mover-env/bin/activate
pip install pyautogui
python mover.py

# one line 
python3 -m venv mover-env && source mover-env/bin/activate && pip install pyautogui && python mover.py

# one line better 
python3 -m venv mover-env && mover-env/bin/pip install pyautogui && mover-env/bin/python mover.py
