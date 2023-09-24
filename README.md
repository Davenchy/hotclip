# HotClip

- This script will memories text you copy and whenever you press a hotkey
it will save it to a file

## Modules to install

- This script requires modules to be installed

1. pyperclip: for clipboard operations
2. pynput: for keyboard hotkey operations

- Inside virtual environment run `pip install -r requirements.txt`

## Usage

- Simply run the script

```bash
$ ./hotclip.py
```

- Use the `-h` flag to see the help message for more details

```bash
$ ./hotclip.py -h
usage: hotclip.py [-h] [--hotkey HOTKEY] [--delay DELAY] [--output OUTPUT] [--print | --no-print | -p]
               [--test-mode | --no-test-mode | -t] [--listen-mode | --no-listen-mode | -l]

options:
  -h, --help            show this help message and exit
  --hotkey HOTKEY, -k HOTKEY
                        Hotkey to listen for (default: <ctrl>+<alt>+i)
  --delay DELAY, -d DELAY
                        Delay between clipboard checks (default: 0.4)
  --output OUTPUT, -o OUTPUT
                        Output file to append saved text to (default: notes.txt)
  --print, --no-print, -p
                        Print logs to stdout (default: False)
  --test-mode, --no-test-mode, -t
                        This mode does not save to file, useful for debugging, use with -p (default: False)
  --listen-mode, --no-listen-mode, -l
                        This mode prints any pressed key to stdout, useful for picking hotkeys (default: False)
```
