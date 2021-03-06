# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 Aboobacker MK <aboobackervyd@gmail.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE
import os        
import new
import sys
from Queue import Queue # A queue type to communicate between threads
import thread # A simple thread launcher
from ConfigParser import ConfigParser # The ConfigParser is used to store preferences of the program

import gettext
from gettext import gettext as _
gettext.textdomain('apertium-ui')
import dbus # Used to connect to the Apertium D-Bus service
#import tolk 

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('apertium_ui')

from apertium_ui_lib import Window
from apertium_ui.AboutApertiumUiDialog import AboutApertiumUiDialog
from apertium_ui.PreferencesApertiumUiDialog import PreferencesApertiumUiDialog

# See apertium_ui_lib.Window.py for more details about how this class works
class ApertiumUiWindow(Window):
    __gtype_name__ = "ApertiumUiWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(ApertiumUiWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutApertiumUiDialog
        self.PreferencesDialog = PreferencesApertiumUiDialog

        # Code for other initialization actions should be added here.
        self.toolbar=self.builder.get_object("maintoolbar")
        context=self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)
        currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen","Russian Ruble", "Mexican peso", "Swiss franc"]
        self.combolang=self.builder.get_object("combolang")
        self.combolang.set_entry_text_column(0)
        for currency in currencies:
            self.combolang.append_text(currency)
    def setup_combo(self, modes, combo):
        """Set the combo box up to display simple a list of text and
        add everything in 'modes' to the list.
        """
        self.combolang=self.builder.get_object("combolang")
        #combo.set_model(Gtk.ListStore(Gobject.TYPE_STRING))
        #cell = gtk.CellRendererText() # Tell the combobox we're just rendering text
        #combo.pack_start(cell, True) # Add the text renderer to the combo box
        #combo.add_attribute(cell, "text", 0) # Tell the combobox that we just want to show text

        for mode in modes: # Add everything in 'modes' to the combobox
            combo.append_text(mode)
        combo.set_active(0) # Set the combobox to the first entry

        return combo
    def on_source_text_preedit_changed(self,widget):
        print "hello"
    def on_quitbutton_clicked(self,widget):
        print "exit"
        #self.save_config()
        Gtk.main_quit()
    def on_combolang_changed(self,widget):
        self.setup_combo(self,self.builder.get_object("combolang"))

