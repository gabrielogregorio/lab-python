#boneca.py
import os
import sys
import ctypes
from ctypes import wintypes
import win32con
import sys
import os
import sys
import ctypes
from ctypes import wintypes
import esky
import win32con
import requests

version = requests.get("http://127.0.0.1:1022/").json()['version']

if hasattr(sys, "frozen"):
	app = esky.Esky(sys.executable,version )
	app.auto_update()
	print('safe')

byref = ctypes.byref
user32 = ctypes.windll.user32

HOTKEYS = {
    1 : (win32con.VK_SNAPSHOT, 0), ####Essa Linha Pega a tecla "PRINT SCREEN"
    2 : (win32con.VK_F4, win32con.MOD_WIN)
}

def handle_win_f3 ():
    os.startfile(os.path.join(os.path.realpath(os.path.dirname(sys.argv[0])),"imagem.png"))

def handle_win_f4 ():
    user32.PostQuitMessage (0)

HOTKEY_ACTIONS = {
    1 : handle_win_f3,
    2 : handle_win_f4
}

# Registrando as chaves sem dar o print pra ficar escondido na tela.
for id, (vk, modifiers) in HOTKEYS.items ():
    #print "Registering id", id, "for key", vk
    pass
    if not user32.RegisterHotKey (None, id, modifiers, vk):
        #print "Unable to register id", id
        pass
# Executando as funções e tirando o registro das chaves depois do encerramento do programa.
try:
    msg = wintypes.MSG ()
    while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
            if action_to_take:
                action_to_take ()
        user32.TranslateMessage (byref (msg))
        user32.DispatchMessageA (byref (msg))
finally:
    for id in HOTKEYS.keys ():
        user32.UnregisterHotKey (None, id)
