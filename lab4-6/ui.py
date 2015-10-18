import wx
from bill import Bill
from bill import BillMethods
from bill_type import BillType
from apartament import Apartament
from apartament import Apartaments

apartaments = Apartaments()

def addBill(apartamentNumber,billType,cost):
    bill = Bill(billType,cost)
    apartaments.get(apartamentNumber).addBill(bill)

addBill(2,2,100)

class windowClass(wx.Frame):

    
    def __init__(self,parent,title):
        super(windowClass,self).__init__(parent,title=title,size=(800,400))

        # add panel
        self.panel = wx.Panel(self,size=(300,300))

        wx.StaticText(self.panel, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.apartamentNumber=wx.TextCtrl(self.panel,pos=(10,30),size=(50,20))

        wx.StaticText(self.panel, label="Bill cost",style=wx.ALIGN_CENTRE,pos=(10,50))
        self.billCost=wx.TextCtrl(self.panel,pos=(10,70),size=(50,20))

        wx.StaticText(self.panel, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,90)) 
        self.billType = wx.ComboBox(self.panel, pos=(10, 110), choices=['Water','Sewerage','Gas','Other'] ,style=wx.CB_READONLY)
        self.billType.SetStringSelection('Water')

        self.addButton = wx.Button(self.panel, label='Add bill', pos=(20, 150))
        self.addButton.Bind(wx.EVT_BUTTON, self.OnAddBill)

        # end add panel


        
        # edit bill panel
        self.editBillPanel = wx.Panel(self,pos=(300,0),size=(300,300))

        wx.StaticText(self.editBillPanel, label="Apartament number (1-100)", style=wx.ALIGN_CENTRE,pos=(10,10))
        self.editBillApartamentNumber=wx.TextCtrl(self.editBillPanel,pos=(10,30),size=(50,20))

        wx.StaticText(self.editBillPanel, label="Bill cost",style=wx.ALIGN_CENTRE,pos=(10,130))
        self.editBillBillCost=wx.TextCtrl(self.editBillPanel,pos=(10,150),size=(50,20))

        wx.StaticText(self.editBillPanel, label="Bill type",style=wx.ALIGN_CENTRE,pos=(10,90)) 
        self.editBillBillType = wx.ComboBox(self.editBillPanel, pos=(10, 110), choices=['Water','Sewerage','Gas','Other'] ,style=wx.CB_READONLY)
        self.editBillBillType.SetStringSelection('Water')

        wx.StaticText(self.editBillPanel, label="Bill id",style=wx.ALIGN_CENTRE,pos=(10,50))
        self.editBillBillId=wx.TextCtrl(self.editBillPanel,pos=(10,70),size=(50,20))


        self.editBillEditButton = wx.Button(self.editBillPanel, label='Edit bill', pos=(20, 180))
        self.editBillEditButton.Bind(wx.EVT_BUTTON, self.OnEditBill)

        # end edit bill panel

        
        wx.Button(self.panel, label='Show bills', pos=(200, 10)).Bind(wx.EVT_BUTTON, self.OnShowBills)
        
        self.Show()

    def OnShowBills(self,e):
        dlg = wx.MessageDialog(None, apartaments.getAllApartamentsAndBills(), "Bills", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnAddBill(self,e):
        apNumber = int(self.apartamentNumber.GetValue())
        billCost=int(self.billCost.GetValue())
        billType=self.billType.GetCurrentSelection()+1
        addBill(apNumber,billType,billCost)
        dlg = wx.MessageDialog(None, "Bill added!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnEditBill(self,e):
        apNumber = int(self.editBillApartamentNumber.GetValue())
        billCost=int(self.editBillBillCost.GetValue())
        billType=self.editBillBillType.GetCurrentSelection()+1
        billId=int(self.editBillBillId.GetValue())
        apartaments.editBill(apNumber,billId,billCost,billType)
        dlg = wx.MessageDialog(None, "Bill added!", "Info", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
app = wx.App()

windowClass(None,title="Epic window")                


app.MainLoop()
