import xml.dom
import xml.dom.minidom
import sys
import codecs

import Tkinter
import ScrolledText
import tkFileDialog
import tkMessageBox
import tkFont

class Menu(Tkinter.Menu):

    def createMenuItem(bar, xmlElement, parent):
        attrs = xmlElement.attributes
        type = attrs['type'].value if attrs.has_key('type') else None
        tearoffMenu = True if attrs.has_key('tearoff') and attrs['tearoff'].value == 'True' else False
        labelText = attrs['label'].value if attrs.has_key('label') else ''
        commandText = attrs['command'].value if attrs.has_key('command') else '0'
        underlineText = attrs['underline'].value if attrs.has_key('underline') else None
        acceleratorText = attrs['accelerator'].value if attrs.has_key('accelerator') else None

        menuItem = None

        if type == 'cascade':
            menuItem = Tkinter.Menu(parent, tearoff = tearoffMenu)
            parent.add_cascade(label = labelText, menu = menuItem, underline = underlineText)
            for element in xmlElement.childNodes:
                if element.nodeType == xml.dom.Node.ELEMENT_NODE:
                    bar.createMenuItem(element, menuItem)
        elif type == 'command':
            parent.add_command(label = labelText, command = lambda: eval(commandText), underline = underlineText, accelerator = acceleratorText)
        elif type == 'separator':
            parent.add_separator()

        return menuItem

    def __init__(self, master = None, xmlObject = None):
        Tkinter.Menu.__init__(self, master)

        # XML Parsing
        for element in xmlObject.getElementsByTagName('menus'):
            for node in element.childNodes:
                if node.nodeType == xml.dom.Node.ELEMENT_NODE:
                    self.createMenuItem(node, self)

     #   self.pack()

class TextArea(ScrolledText.ScrolledText):

    def __init__(self, master):
        ScrolledText.ScrolledText.__init__(self, master, maxundo = 256, wrap = None)

class Application(Tkinter.Frame):

    def __init__(self, master = None):
        Tkinter.Frame.__init__(self, master)

        self.master.title('Editor')
        self.config(width = 640, height = 480)

        # menubar
        # XMLロード
        xmlObject = xml.dom.minidom.parse("menus.xml")

        # メニューバー作成
        menuBar = Menu(self, xmlObject)
        self.master.configure(menu = menuBar)

        # コンテンツ
        textArea = TextArea(self)

        self.pack()


if __name__ == '__main__':
    root = Tkinter.Tk()
    application = Application()
    application.mainloop()
    #root.destroy()