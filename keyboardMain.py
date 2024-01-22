import keyboard;
import pyautogui;
import src.ciphers.ciphers as ciphers;

def replace_text(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name;

        if not key.isalpha(): return;

        if len(key) == 1:
            if hasattr(event, 'simulated') and event.simulated:
                # Skip processing if the event is from simulated typing
                return;

            keyboard.press_and_release('backspace');
            ciphered_key = ciphers.affineCipher(key, 5, 8);
            pyautogui.press(ciphered_key);

keyboard.hook(replace_text);
print("Running, press 'Ctrl + C' to quit");
keyboard.wait();