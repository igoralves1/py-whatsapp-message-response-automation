# py-whatsapp-message-response-automation


# VENV
- Check if venv is installed:
```
pip3 list
Package                Version
---------------------- --------------
absl-py                1.1.0
apturl                 0.5.2
attrs                  21.4.0
...                    ...
```
- If venv is not in the list install it:
```
pip3 install virtualenv
```
- Create a virtual environment:
```
python3 -m venv wtap-msg-auto
```
- The folder `wtap-msg-auto` as been created.
```
ll
total 20
drwxrwxr-x  4 ila ila 4096 Jul  3 14:40 .
drwxrwxr-x 13 ila ila 4096 Jul  3 14:27 ..
drwxrwxr-x  8 ila ila 4096 Jul  3 14:30 .git
-rw-rw-r--  1 ila ila  426 Jul  3 14:55 README.md
drwxrwxr-x  5 ila ila 4096 Jul  3 14:40 wtap-msg-auto
```
- Check inside `wtap-msg-auto`:
```
wtap-msg-auto(main)$ ll
total 24
drwxrwxr-x 5 ila ila 4096 Jul  3 14:40 .
drwxrwxr-x 4 ila ila 4096 Jul  3 14:40 ..
drwxrwxr-x 2 ila ila 4096 Jul  3 14:40 bin
drwxrwxr-x 2 ila ila 4096 Jul  3 14:40 include
drwxrwxr-x 3 ila ila 4096 Jul  3 14:40 lib
lrwxrwxrwx 1 ila ila    3 Jul  3 14:40 lib64 -> lib
-rw-rw-r-- 1 ila ila   70 Jul  3 14:40 pyvenv.cfg
```
- In order to work with venv needs to activate it:
```
/wtap-msg-auto(main)$ source bin/activate
(wtap-msg-auto) ila@ila:~/Documents/vhosts/py-whatsapp-message-response-automation/wtap-msg-auto(main)$ 
```
- When we see (wtap-msg-auto) ila@ila:~/... that means that the environment is activated and ready to work.

# Back to the WhatsApp Auto Response Bot in Python
- [Part 1](https://www.youtube.com/watch?v=T2QFP_Y6AUU)
- [Part 2](https://www.youtube.com/watch?v=J_7oiOSdP0c)
- [Part 1](https://www.youtube.com/watch?v=5Rz-vzOe7j4)

Intall dependencies:
1. OpenCV
    ```
    pip3 install opencv-python

    Collecting opencv-python
    Using cached opencv_python-4.6.0.66-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (60.9 MB)
    Collecting numpy>=1.14.5
    Downloading numpy-1.23.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (17.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 17.0/17.0 MB 2.2 MB/s eta 0:00:00
    Installing collected packages: numpy, opencv-python
    Successfully installed numpy-1.23.0 opencv-python-4.6.0.66
    ```
2. pyautogui
    ```
    pip3 install pyautogui

    Collecting pyautogui
    Downloading PyAutoGUI-0.9.53.tar.gz (59 kB)
    ...
    Successfully installed PyTweening-1.0.4 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.2.0 pyscreeze-0.1.28 python3-Xlib-0.15
    ```
3. pyperclip
   ```
    pip3 install pyperclip

    Requirement already satisfied: pyperclip in ./lib/python3.10/site-packages (1.8.2)
    NOTE: already installed previously
   ```
4. 