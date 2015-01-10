import re
import idaapi
import idc
from idc import *
from idaapi import *
import PyQt4
from PyQt4 import QtCore, QtGui
import idautils

class Shadow(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Plugin Layout to call PyQt APP"
    wanted_name = "PyQt Caller"
    wanted_hotkey = "Alt-F7"



    def init(self):
        idaapi.msg(" Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")
    
    def AddMenuElements(self):
        '''Menus are better than no GUI at all *sigh*'''

        idaapi.add_menu_item("Edit/Plugins/", "call PyQt Plugin", "", 0, self.ShadowCall, ())




    def run(self, arg = 0):
        idaapi.msg("Looks like its working")

        self.AddMenuElements()

    def ShadowCall(self):
        g = globals()
        idahome = idaapi.idadir("QTApps")
        IDAPython_ExecScript(idahome +  "\\test.py", g)



def PLUGIN_ENTRY():
    return Shadow()
