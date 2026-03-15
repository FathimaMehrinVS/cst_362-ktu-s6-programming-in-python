from breezypythongui import EasyFrame
class TextFieldDemo(EasyFrame):
    "Accept 2 input boxes and concatenate 2 strings"
    def __init__(self):
        "Setting up the window and widgets"
        EasyFrame.__init__(self,title="Text Field Demo")
        self.addLabel(text="Input1",row=0,column=0)
        self.inputField1=self.addTextField(text="",row=0,column=1)
        self.addLabel(text="Input2",row=1,column=0)
        self.inputField2=self.addTextField(text="",row=1,column=1)
        self.addLabel(text="Output",row=2,column=0)
        self.outputField=self.addTextField(text="",row=2,column=1,state="readonly")
        self.addButton(text="Concatenate",row=3,column=0,columnspan=2,command=self.concatenate)
    def concatenate(self):
        t1=self.inputField1.getText()
        t2=self.inputField2.getText()
        result=t1+t2
        self.outputField.setText(result)
u1=TextFieldDemo()
u1.mainloop()