# MIT License

# Copyright (c) 2020 Netherlands Film Academy

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sgtk
from hutil.Qt import QtCore
import hou

class TkHoudiniFlipbook(sgtk.platform.Application):
    """
    A Shotgun Toolkit app to create flipbook of your current scene with use of SGTK templates. 
    """

    def init_app(self):
        """
        Import Python modules and other initialisation.
        """

        self.tk_houdini_flipbook = self.import_module("tk_houdini_flipbook")


        # register the flipbook command
        self.engine.register_command(
            "Flipbook to Shotgun...",
            self.__show_dialog,
            {
                "short_name": "flipbook"
            },
        )

    def __show_dialog(self):
        """
        Launch the UI for the flipbook settings.
        """
        
        self.dialog = self.tk_houdini_flipbook.FlipbookDialog(self)
        self.dialog.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
        self.dialog.setModal(True)
        self.dialog.show()