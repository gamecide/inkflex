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

class MainWin ():

    def __init__(self):
	 
        #Set the Glade file
        self.gladefile = "gui/ConfigureWindow.glade"  
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
        
# Start program
if __name__ == "__main__":
     
    main = MainWin()
    gtk.main()
     
