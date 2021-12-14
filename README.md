# Auto-Join-Class
    
Dependencies:   
1) Download git fom here: https://git-scm.com/downloads  
2) Download python3, the procedure will vary based on your OS.  
    
    - To check if python3 is installed open the command prompt and type `python3` and hit enter. If it opens the microsoft store page for python3, it is not installed, and you can install it from there.  
    
    - If you are using Mac Catalina, python3 is installed by default. If not you can install it here: https://www.python.org/downloads/.    
      However, if you have homebrew installed, you can just run `brew install python` in the terminal.  
    
    - The inctructions to install python on all the different Linux distros are out of the scope of this article.   
    
    
Open powershell (Windows) or the terminal (Linux/Mac) and copy paste the following command:
```git clone https://github.com/Phantasm702/Auto-Join-Class.git```
This will install the main script, the setup script and the necessary config files.
    
Windows:    
Run `python3 Auto-Join-Class\setup.py` to complete the setup.   
*The following is optional, but recommended*    
After this, create a shortcut for the script.py file which is located in the Auto-Join-Class folder.    
The feature to join the class on keybind has not yet been implemented on windows, as there is no way to execute the script after pressing the keybind automatically.    
However I do have some ideas in order to implement this, and will do so after furter testing.   
    
Mac/Linux:      
Run `python3 Auto-Join-Class/setup.py` in the terminal to complete the setup.   
*The following is optional, but recommended*    
*Instructions copy pasted from stack overflow thread: https://stackoverflow.com/questions/62014315/can-i-run-a-python-script-from-a-keyboard-shortcut*  
you can create a 'quick action' in Automate using an apple script to tell Terminal to do something like 'tell application "Terminal" to do script "python3    /home/username/path/to/script.py"'. Then, you can go into your keyboard shortcut preferences and add a hotkey to the action.
The instructions for creating a keyboard shortcut for the Different linux distros vary. 
