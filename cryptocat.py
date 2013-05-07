#!/usr/bin/python
# This file is part of pyCryptoCat.
#
# Copyleft Simone Margaritelli
# evilsocket@gmail.com
# http://www.evilsocket.net
# http://www.emoticode.net

import gtk, webkit
import sys
import os

class CryptoCat:
    version = '1.0.0'
    starter = 'files/index.html'

    def __init__(self):
        self.window    = gtk.Window()
        self.webview   = webkit.WebView()
        self.cryptocat = 'file://' +  os.path.dirname(os.path.realpath(__file__)) + '/' + self.starter

        settings = self.webview.get_settings()
        # Make webview load file:// urls without security exceptions
        settings.set_property('enable-universal-access-from-file-uris', True)
        settings.set_property('enable-file-access-from-file-uris', True)
        # Enable audio notifications
        settings.set_property('enable-webaudio', True)
        # Set default encoding
        settings.set_property('default-encoding', 'utf-8')

        with open('init.js', 'r') as initjs:
          self.initjs = initjs.read()

        # get dom ready event
        self.webview.connect("load-finished", self._view_load_finished_cb)

        self.window.set_title( 'pyCryptoCat v' + self.version )                                                                                                                               
        self.window.connect( 'destroy', gtk.main_quit )

        self.window.add(self.webview)
   
    def _js( self, code ):
        self.webview.execute_script(code)

    def _view_load_finished_cb(self, view, frame):
      # run initialization code
      self._js( self.initjs )

    def run(self):
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.show_all()
        self.webview.open( self.cryptocat )
        gtk.main()

cc = CryptoCat()
cc.run()
