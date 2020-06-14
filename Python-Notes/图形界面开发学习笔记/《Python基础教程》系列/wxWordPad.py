#encoding=utf-8
import wx
import os


class MyFrame(wx.Frame):
    def __init__(self):
        self.file = ''
        self.content = []
        self.count = 0
        self.width = 700
        self.height = 500
        wx.Frame.__init__(self, None, -1, u'记事本',
                          size=(self.width, self.height))
        self.panel = wx.Panel(self, -1)
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menubar.Append(menu1, u'文件')
        menu1.Append(1001, u'打开')
        menu1.Append(1002, u'保存')
        menu1.Append(1003, u'另存为')
        menu1.Append(1004, u'退出')
        menu2 = wx.Menu()
        menubar.Append(menu2, u'编辑')
        menu2.Append(2001, u'撤销')
        menu2.Append(2002, u'清空')
        menu2.Append(2003, u'剪切  Ctrl + X')
        menu2.Append(2004, u'复制  Ctrl + C')
        menu2.Append(2005, u'粘贴  Ctrl + V ')
        menu2.Append(2006, u'全选  Ctrl + A',)

        menu = wx.Menu()
        ctrla = menu.Append(-1, "\tCtrl-A")
        ctrlc = menu.Append(-1, "\tCtrl-C")
        ctrlx = menu.Append(-1, "\tCtrl-X")
        ctrlv = menu.Append(-1, "\tCtrl-V")
        ctrls = menu.Append(-1, "\tCtrl-S")
        menubar.Append(menu, '')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnSelect, ctrla)
        self.Bind(wx.EVT_MENU, self.OnCopy, ctrlc)
        self.Bind(wx.EVT_MENU, self.OnCut, ctrlc)
        self.Bind(wx.EVT_MENU, self.OnPaste, ctrlv)
        self.Bind(wx.EVT_MENU, self.OnTSave, ctrls)

        self.Bind(wx.EVT_MENU, self.OnOpen, id=1001)
        self.Bind(wx.EVT_MENU, self.OnSave, id=1002)
        self.Bind(wx.EVT_MENU, self.OnSaveAll, id=1003)
        self.Bind(wx.EVT_MENU, self.OnExit, id=1004)

        self.Bind(wx.EVT_MENU, self.OnBack, id=2001)
        self.Bind(wx.EVT_MENU, self.OnClear, id=2002)
        self.Bind(wx.EVT_MENU, self.OnCut, id=2003)
        self.Bind(wx.EVT_MENU, self.OnCopy, id=2004)
        self.Bind(wx.EVT_MENU, self.OnPaste, id=2005)
        self.Bind(wx.EVT_MENU, self.OnSelect, id=2006)
        self.Bind(wx.EVT_SIZE, self.OnResize)

        new = wx.Image('./icons/new.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        open = wx.Image('./icons/open.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        exit = wx.Image('./icons/exit.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        save = wx.Image('./icons/save.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        saveall = wx.Image('./icons/saveall.png',
                           wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        back = wx.Image('./icons/back.png',
                        wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        go = wx.Image('./icons/go.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        clear = wx.Image('./icons/clear.png',
                         wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        toolbar = self.CreateToolBar(wx.TB_HORIZONTAL | wx.TB_TEXT)
        toolbar.AddSimpleTool(100, new, 'New')
        toolbar.AddSimpleTool(200, open, 'Open')
        toolbar.AddSimpleTool(300, exit, 'Exit')
        toolbar.AddSimpleTool(400, save, 'Save')
        toolbar.AddSimpleTool(500, saveall, 'Save All')
        toolbar.AddSimpleTool(600, back, 'Back')
        toolbar.AddSimpleTool(700, go, 'Go')
        toolbar.AddSimpleTool(800, clear, 'Clear')
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnTOpen, id=200)
        self.Bind(wx.EVT_TOOL, self.OnTExit, id=300)
        self.Bind(wx.EVT_TOOL, self.OnTSave, id=400)
        self.Bind(wx.EVT_TOOL, self.OnTBack, id=600)
        self.Bind(wx.EVT_TOOL, self.OnTGo, id=700)
        self.Bind(wx.EVT_TOOL, self.OnTClear, id=800)

        self.text = wx.TextCtrl(self.panel, -1, pos=(2, 2), size=(
            self.width-10, self.height-50), style=wx.HSCROLL | wx.TE_MULTILINE)

        self.popupmenu = wx.Menu()  # 创建一个菜单
        for text in "Cut  Copy Paste SelectAll".split():  # 填充菜单
            item = self.popupmenu.Append(-1, text)
            self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
            self.panel.Bind(wx.EVT_CONTEXT_MENU,
                            self.OnShowPopup)  # 绑定一个显示菜单事件

    def OnShowPopup(self, event):  # 弹出显示
        pos = event.GetPosition()
        pos = self.panel.ScreenToClient(pos)
        self.panel.PopupMenu(self.popupmenu, pos)

    def OnPopupItemSelected(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()
        if text == 'Cut':
            self.OnCut(event)
        elif text == 'Copy':
            self.OnCopy(event)
        elif text == 'Paste':
            self.OnPaste(event)
        elif text == 'SelectAll':
            self.OnSelect(event)

    def OnOpen(self, event):
        filterFile = " All files (*.*) |*.*"
        opendialog = wx.FileDialog(
            self, u"选择文件", os.getcwd(), "", filterFile, wx.OPEN)
        if opendialog.ShowModal() == wx.ID_OK:
            self.file = opendialog.GetPath()
            f = open(self.file)
            self.text.write(f.read())
            f.close()
        opendialog.Destroy()

    def OnTOpen(self, event):
        filterFile = "All files (*.*) |*.*"
        opendialog = wx.FileDialog(
            self, u"选择文件", os.getcwd(), "", filterFile, wx.OPEN)
        if opendialog.ShowModal() == wx.ID_OK:
            self.file = opendialog.GetPath()
            f = open(self.file)
            self.text.write(f.read())
            f.close()
            self.content.append(self.text.GetValue())
        opendialog.Destroy()

    def OnSave(self, event):
        filterFile = "All files (*.*) |*.*"
        opendialog = wx.FileDialog(
            self, u'保存文件', os.getcwd(), "", filterFile, wx.SAVE)
        if opendialog.ShowModal() == wx.ID_OK:
            self.file = opendialog.GetPath()
            self.text.SaveFile(self.file)

    def OnTSave(self, event):
        if self.file == '':
            filterFile = "All files (*.*) |*.*"
            opendialog = wx.FileDialog(
                self, u'保存文件', os.getcwd(), "", filterFile, wx.SAVE)
            if opendialog.ShowModal() == wx.ID_OK:
                self.file = opendialog.GetPath()
                self.text.SaveFile(self.file)
                self.content.append(self.text.GetValue())
                self.count = self.count+1
        else:
            self.text.SaveFile(self.file)
            self.content.append(self.text.GetValue())
            self.count = self.count+1

    def OnSaveAll(self, event):
        pass

    def OnExit(self, event):
        self.Close()

    def OnTExit(self, event):
        self.Close()

    def OnBack(self, event):
        self.text.Undo()

    def OnTBack(self, event):
        try:
            self.count = self.count-1
            self.text.SetValue(self.content[self.count])
        except IndexError:
            self.count = 0

    def OnTGo(self, event):
        try:
            self.count = self.count+1
            self.text.SetValue(self.content[self.count])
        except IndexError:
            self.count = len(self.content)-1

    def OnClear(self, event):
        self.text.Clear()

    def OnTClear(self, event):
        self.text.Clear()

    def OnCut(self, event):
        self.text.Cut()

    def OnCopy(self, event):
        self.text.Copy()

    def OnPaste(self, event):
        self.text.Paste()

    def OnSelect(self, event):
        self.text.SelectAll()

    def OnResize(self, event):

        newsize = self.GetSize()

        width = newsize.GetWidth()-10

        height = newsize.GetHeight()-50

        self.text.SetSize((width, height))

        self.text.Refresh()


if __name__ == '__main__':
    app = wx.App()
    myFrame = MyFrame()
    myFrame.Show()
    app.MainLoop()
