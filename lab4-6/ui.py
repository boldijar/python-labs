import wx


class windowClass(wx.Frame):

    
    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title=title,size=(600,400))

        # add panel
        self.panel = wx.Panel(self)

        wx.StaticText(self.panel, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.apartamentNumber=wx.TextCtrl(self.panel,pos=(10,30),size=(50,20))

        wx.StaticText(self.panel, label="Bill cost",style=wx.ALIGN_CENTRE,pos=(10,50))
        self.billCost=wx.TextCtrl(self.panel,pos=(10,70),size=(50,20))

        wx.StaticText(self.panel, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,90)) 
        self.billType = wx.ComboBox(self.panel, pos=(10, 110), choices=['Water','Sewerage','Gas','Other'] ,style=wx.CB_READONLY)
        self.billType.SetStringSelection('Water')

        self.addButton = wx.Button(self.panel, label='Add bill', pos=(20, 150))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnClick)
        
        self.Show()

    def OnClick(self,e):
        dlg = wx.MessageDialog(None, "Bill added!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
app = wx.App()

windowClass(None,title="Epic window")                


app.MainLoop()
