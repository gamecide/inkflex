#!/usr/bin/env python

import sys
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

from export_starling import *

class MainWin (inkex.Effect):

    def __init__(self):
        
        # Initialize inkex module
        inkex.Effect.__init__(self)
        
        #Set the Glade file
        self.gladefile = "gui/MainWindow.glade"  
        self.wTree = gtk.glade.XML(self.gladefile) 
        
        #Get the Main Window, and connect the "destroy" event
        self.window = self.wTree.get_widget("MainWindow")
        if (self.window):
            self.window.connect("destroy", gtk.main_quit)
        else:
            raise Exception("I couldn't find the window called "+window_name+"!")

        #Define colors
        self.white = gtk.gdk.color_parse('#FFFFFF')
        self.inkblue = gtk.gdk.color_parse('#37abc8')
        self.dark_gray = gtk.gdk.color_parse('#5a5a5a')
        self.ligth_gray = gtk.gdk.color_parse('#F0F0F0')
        
        #Set window backgrounds
        self.window.modify_bg(gtk.STATE_NORMAL, self.white)
        
        top = self.wTree.get_widget("top")
        top.modify_bg(gtk.STATE_NORMAL, self.dark_gray)
          
        bottom = self.wTree.get_widget("bottom")
        bottom.modify_bg(gtk.STATE_NORMAL, self.ligth_gray)
        
        #Create selection buttons
        self.flashBtn = self.wTree.get_widget("flashBtn")
        self.flashBtn.modify_bg(gtk.STATE_NORMAL, self.white)
        self.flashBtn.connect('enter-notify-event', self.hover_color)
        self.flashBtn.connect('leave-notify-event', self.active_color)
        
        self.starlingBtn = self.wTree.get_widget("starlingBtn")
        self.starlingBtn.modify_bg(gtk.STATE_NORMAL, self.white)
        self.starlingBtn.connect('enter-notify-event', self.hover_color)
        self.starlingBtn.connect('leave-notify-event', self.active_color)
        self.starlingBtn.connect('button-release-event', self.export_action_starling)
        
        self.html5Btn = self.wTree.get_widget("html5Btn")
        self.html5Btn.modify_bg(gtk.STATE_NORMAL, self.white)
        self.html5Btn.connect('enter-notify-event', self.hover_color)
        self.html5Btn.connect('leave-notify-event', self.active_color)
        
        #Create configure button
        self.configureImg = self.wTree.get_widget("configureImg")
        self.configureBtn = self.wTree.get_widget("configureBtn")
        self.configureBtn.connect('enter-notify-event', self.hover_configure)
        self.configureBtn.connect('leave-notify-event', self.active_configure)
        
        #Create quit button
        self.quitImg = self.wTree.get_widget("quitImg")
        self.quitBtn = self.wTree.get_widget("quitBtn")
        self.quitBtn.connect('enter-notify-event', self.hover_quit)
        self.quitBtn.connect('leave-notify-event', self.active_quit)
        self.quitBtn.connect('button-release-event', gtk.main_quit)
        
        #Show the Main Window
        self.window.show()
        
    def hover_color(self, widget, event):
        widget.modify_bg(gtk.STATE_NORMAL, self.inkblue)
    
    def active_color(self, widget, event):
        widget.modify_bg(gtk.STATE_NORMAL, self.white)
    
    def hover_configure(self, widget, event):
        self.configureImg.set_alignment(1.0,0.0)
    
    def active_configure(self, widget, event):
        self.configureImg.set_alignment(0.0,0.0)
        
    def hover_quit(self, widget, event):
        self.quitImg.set_alignment(1.0,0.0)
    
    def active_quit(self, widget, event):
        self.quitImg.set_alignment(0.0,0.0)
            
    def export_action_starling(self, widget, event):
        export_to_starling(self.document)
        
# Start program
if __name__ == "__main__":
     
    main = MainWin()
    
    # Get access to main SVG document
    main.affect()
    
    gtk.main()
     
