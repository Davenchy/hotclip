#!/usr/bin/env python3
"""This script will append to a file whatever you copied
whenever you press the hotkey"""

import pyperclip
from pynput import keyboard
from time import sleep
import argparse


def hotkey_handler(file, text, log, isTestMode):
    """It saves passed text variable to the passed file path

    Args:
        file (str): The file path to append to
        text (str): The text to save
        log (bool): Whether to print logs to stdout
        isTestMode (bool): Whether to save to file"""

    if isTestMode:
        print("hotkey triggered")
        return

    text = text.strip()
    if not text:
        return

    text = text + '\n'
    with open(file, 'a+') as f:
        f.seek(0)  # Go to the beginning of the file
        lines = f.readlines()
        if text not in lines:
            f.write(text)
            if log:
                print('Saved to file!')
        elif log:
            print('Duplicate!')


def listen_mode():
    """Listen to pressed keys and print to stdout"""
    print('listen mode')
    try:
        with keyboard.Listener(on_press=print) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('Exiting...')
        exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--hotkey', '-k',
        default="<ctrl>+<alt>+i",
        help='Hotkey to listen for'
    )
    parser.add_argument(
        '--delay', '-d',
        type=float,
        default=0.4,
        help='Delay between clipboard checks'
    )
    parser.add_argument(
        '--output', '-o',
        default='notes.txt',
        help='Output file to append saved text to'
    )
    parser.add_argument(
        '--print', '-p',
        action=argparse.BooleanOptionalAction,
        default=False,
        help='Print logs to stdout'
    )
    parser.add_argument(
        '--test-mode', '-t',
        action=argparse.BooleanOptionalAction,
        default=False,
        help='This mode does not save to file, useful for debugging, use with \
        -p'
    )
    parser.add_argument(
        '--listen-mode', '-l',
        action=argparse.BooleanOptionalAction,
        default=False,
        help='This mode prints any pressed key to stdout, useful for picking \
        hotkeys'
    )
    args = parser.parse_args()
    stored_text = None

    if args.listen_mode:
        listen_mode()

    # listen for hotkey and call save_to_file
    with keyboard.GlobalHotKeys({
        args.hotkey: lambda: hotkey_handler(
            args.output, stored_text, args.print, args.test_mode)
    }) as kb_listener:
        if args.print:
            print('ready')
        try:
            while True:
                # read text from clipboard
                c_text = pyperclip.paste()
                # if text not empty and has changed save it to variable
                if c_text and c_text != stored_text:
                    stored_text = c_text
                    if args.print:
                        print("Copied:", stored_text)
                # delay to decrease clipboard calls
                sleep(args.delay)
        except KeyboardInterrupt:
            exit(0)
