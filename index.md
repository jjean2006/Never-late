# Auto-Class-Join script

## Ever been late to class?
With this script, never worry about that again. 

With a simple keybind, you can retrieve the link to join the respective class, and put it in the browser.

[Github repository link](https://github.com/Phantasm702/Auto-Join-Class)

## Install Instructions:
### - Dependencies:
1. Download git fom here: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. The script is written in Python3. So you will need that installed.  

    - To check if python3 is installed open the command prompt and type python3 and hit enter. If it opens the microsoft store page for python3(windows), or return "Command not found" (Mac/Linux) it is not installed.  
    - If you are using MacOS Catalina, Python3 is installed by default. If not you can install it here: [https://git-scm.com/downloads](https://www.python.org/downloads/).  
    - Linux users can install it from [https://git-scm.com/downloads](https://www.python.org/downloads/) as well.  
    - If you're using windows, click the "Get" button on the microsoft store page.  

### - Windows:
Run the following commands:
```
git clone https://github.com/Phantasm702/Auto-Join-Class.git
python3 Auto-Join-Class\setup.py 
```
Then answer the questions to complete the setup.  
*The following is optional, but recommended*  
After this, create a shortcut for the script.py file which is located in the Auto-Join-Class folder.
The feature to join the class on keybind has not yet been implemented on windows, as there is no way to execute the script after pressing the keybind automatically.
However I do have some ideas in order to implement this, and will do so after furter testing.

### - Mac/Linux
Run the following commands:
```
git clone https://github.com/Phantasm702/Auto-Join-Class.git
python3 Auto-Join-Class/setup.py
```
*The following is optional, but recommended*
If you are using a Mac:
- Open the shortcuts app
- Create a new shortcut to "Tell terminal to run Auto-Join-Class/script.py" and set it to run for a keyboard shortcut.

The instructions for getting the script to execute on a keyboard shortcut very from linux distro to distro.


## To-Do:
- Implement 'execute on shortcut' on windows using pynput.  
- Send push notifications when joining class, with the class name so that the user can make sure they're joining the right class.  
- Implement 'remind when class is starting' feature.  
