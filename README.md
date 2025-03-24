# qute-rofi-translate

This script allows you to translate selected text in **qutebrowser** and display the result in **rofi**. Below are the steps to set up and use the script.

---

### 1. **Install Dependencies**
Make sure you have the following programs installed:
- **qutebrowser** (browser).
- **rofi** (menu for displaying the result).
- **trans** (command-line utility for text translation).
- **sh** (Python module for running shell commands)

Install them if they are not already installed.

---

### 2. **Download or Create the Script**
Create a script file, for example, `qute-rofi-translate.py`, and paste the code from `qute-rofi-translate.py` into it.

---

### 3. **Make the Script Executable**
To make the script executable, run:
```bash
chmod +x qute-rofi-translate.py
```

---

### 4. **Add the Script to qutebrowser's Config**
Open the qutebrowser configuration file. It is located at: `~/.config/qutebrowser/config.py`

Add the following line to the config:
```python
# Bind the script to a hotkey (e.g., ,t)
config.bind(',t', 'spawn ~/path/to/qute-rofi-translate.py {primary}', mode='normal')
```

Replace `/path/to/qute-rofi-translate.py` with the full path to your script.

---

### 5. **Usage**
1. Highlight text on any webpage in qutebrowser.
2. Press the hotkey (e.g., `,t`).
3. The translation of the selected text will appear in the **rofi** window.

---

### 6. **Additional Settings**
- **Changing the Translation Language**: To change the translation language, edit the `TARGET_LANG` variable in the script. For example, use `"en"` for English.
- **Using a Different Translation Service**: If you want to use a different service (e.g., DeepL), modify the command in `subprocess.run`.

---

### Example Script Path
If you saved the script in your home directory, the path might look like this:
```bash
/home/your-username/qute-rofi-translate.py
```
