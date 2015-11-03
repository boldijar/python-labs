import wx
from apartament_controller import ApartamentController
from AddBillPanel import *
from EditBillPanel import *
from DeleteAllApartamentBillsPanel import *
from DeleteCertainBillsPanel import *
from FindApartamentsByCostPanel import *
from FindCertainBillsOfAllApartaments import *
from validator import IntValidator
from DeleteBillsOfApartamentsInRange import *
from ClearCertainBillsOfAllApartaments import *
from FindCostOfBills import *
apartamentController = ApartamentController()
        
class windowClass(wx.Frame):

    
    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title=title,size=(800,700))
        
        addBillPanel = AddBillPanel(self,apartamentController,(0,0),(300,300))
        editBillPanel= EditBillPanel(self,apartamentController,(305,0),(150,300))
        DeleteAllApartamentBillsPanel(self,apartamentController,(460,0),(200,100))
        DeleteCertainBillsPanel(self,apartamentController,(460,105),(240,100))
        FindApartamentsByCostPanel(self,apartamentController,(0,305),(250,100))
        FindCertainBillsOfAllApartaments(self,apartamentController,(255,305),(250,100))
        ClearCertainBillsOfAllApartaments(self,apartamentController,(510,305),(250,100))
        DeleteBillsOfApartamentsInRange(self,apartamentController,(5,410),(250,200))
        FindCostOfBills(self,apartamentController,(255,410),(250,100))
        wx.Button(addBillPanel, label='Show bills', pos=(200, 10)).Bind(wx.EVT_BUTTON, self.OnShowBills)
        wx.Button(addBillPanel, label='Undo', pos=(200, 40)).Bind(wx.EVT_BUTTON, self.OnUndo)
        self.Show()

    def OnUndo(self,e):
        apartamentController.undo()
        dlg = wx.MessageDialog(None, "Done", "Successfully undone", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
        
    def OnShowBills(self,e):
        dlg = wx.MessageDialog(None, apartamentController.getAllApartamentsAndBills(), "Bills", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
         
app = wx.App()

windowClass(None,title="Epic window")                


app.MainLoop()
