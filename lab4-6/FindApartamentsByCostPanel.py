import wx
from apartament_controller import ApartamentController
from validator import IntValidator

class FindApartamentsByCostPanel(wx.Panel):

    def __init__(self,parent,apartamentController,position,size):
        super(FindApartamentsByCostPanel,self).__init__(parent,pos=position,size=size)
        self.apartamentController = apartamentController
        wx.StaticText(self, label="Apartament minimum cost: ", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.cost=wx.TextCtrl(self,pos=(10,30),size=(50,20))       

        self.addButton = wx.Button(self, label='Find out apartaments with greater cost: ', pos=(20, 70))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self,e):
        if IntValidator.valid(self.cost.GetValue(),0,10000) == False:
            dlg = wx.MessageDialog(None, "Invalid input!", "Info", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return
        cost = int(self.cost.GetValue())
        dlg = wx.MessageDialog(None, "Result:\n"+self.apartamentController.getApartamentsWithCostGreatherThanAsString(cost), "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    

    
