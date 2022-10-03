"""A multi-scene editor plugin for novelyst.

Compatibility: novelyst v0.42 API 
Requires Python 3.6+
Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_rich_editor
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
import tkinter as tk
from tkinter import messagebox
from nveditorlib.nv_editor_globals import *
from nveditorlib.scene_editor import SceneEditor


class Plugin:
    """novelyst multi-scene editor plugin class.
    
    Public methods:
        on_quit() -- apply changes before closing the editor windows.       
    """
    VERSION = '@release'
    NOVELYST_API = '1.0'
    DESCRIPTION = 'A multi-scene "rich text" editor'
    URL = 'https://peter88213.github.io/novelyst_rich_editor'

    def install(self, ui):
        """Add a submenu to the main menu.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        # Add the "Edit" command to novelyst's "Scene" menu.
        self._ui.sceneMenu.add_separator()
        self._ui.sceneMenu.add_command(label=_('Edit'), underline=0, command=self._edit_scene)
        self._ui.tv.tree.bind('<Double-1>', self._edit_scene)
        self._ui.tv.tree.bind('<Return>', self._edit_scene)
        self.sceneEditors = {}
        try:
            path = os.path.dirname(sys.argv[0])
            if not path:
                path = '.'
            self._icon = tk.PhotoImage(file=f'{path}/icons/{ICON}.png')
        except:
            self._icon = None

    def _edit_scene(self, event=None):
        """Create a scene editor window with a menu bar, a text box, and a status bar."""
        if self._ui.isLocked:
            messagebox.showinfo(PLUGIN, _('Cannot edit scenes, because the project is locked.'))
            return

        try:
            nodeId = self._ui.tv.tree.selection()[0]
            if nodeId.startswith(self._ui.tv.SCENE_PREFIX):
                # A scene is selected
                scId = nodeId[2:]
                if scId in self.sceneEditors and self.sceneEditors[scId].isOpen:
                    self.sceneEditors[scId].lift()
                    return

                self.sceneEditors[scId] = SceneEditor(self._ui, scId, WINDOW_SIZE, icon=self._icon)
        except IndexError:
            # Nothing selected
            pass

    def on_quit(self, event=None):
        """Close all open scene editor windows."""
        for scId in self.sceneEditors:
            if self.sceneEditors[scId].isOpen:
                self.sceneEditors[scId].on_quit()

