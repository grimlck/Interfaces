#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import netifaces

class MWPanel(wx.Panel):
    def __init__(self, parent):

        self.if_dict = {}

        # since we are on Windows, we need to map interface IDs to human readable names
        for i in xrange(0, len(netifaces.interfaces())):
            if i < 9:
                if_name = 'interface0'+str(i+1)
            else:
                if_name = 'interface'+str(i+1)

            self.if_dict[if_name] = netifaces.interfaces()[i]

        self.interface_list = [interface for interface in self.if_dict.iterkeys()]

        # Panel
        wx.Panel.__init__(self, parent)

        # Combo box and label
        self.lbl_interfaces = wx.StaticText(self, label="Select interface:")
        self.cb_interfaces = wx.ComboBox(self, style=wx.CB_DROPDOWN,
                choices=sorted(self.interface_list))

        # ComboBox events bindings
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.cb_interfaces)

        # Text control
        self.tc_information = wx.TextCtrl(self, size=(300,200), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # Sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        comboSizer = wx.BoxSizer(wx.VERTICAL)
        gridBagSizer = wx.GridBagSizer(hgap=5, vgap=5)

        # Compose widget arrangement
        comboSizer.Add(self.lbl_interfaces)
        comboSizer.Add(self.cb_interfaces)
        gridBagSizer.Add(comboSizer, pos=(0,0))
        gridBagSizer.Add(self.tc_information, pos=(1,0))
        mainSizer.Add(gridBagSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

    # Event handlers
    def EvtComboBox(self, event):
        '''when a  item in the combo box is selected, write the interface
        information to the TextControl'''

        self.tc_information.SetValue('Interface Informations\n----------------------------\n')
        try:
            for item in netifaces.ifaddresses(self.if_dict[self.cb_interfaces.GetValue()])[netifaces.AF_INET]:
                if 'addr' in item:
                    self.tc_information.AppendText('IP-Address:\t%s\n' % item['addr'])
                if 'netmask' in item:
                    self.tc_information.AppendText('Netmask:\t\t%s\n' % item['netmask'])
                if 'broadcast' in item:
                    self.tc_information.AppendText('Broadcast:\t%s\n' %
                            item['broadcast'])

            for item in netifaces.ifaddresses(self.if_dict[self.cb_interfaces.GetValue()])[netifaces.AF_LINK]:
                if 'addr' in item:
                    self.tc_information.AppendText('MAC-Address:\t%s\n' % item['addr'])

            self.tc_information.AppendText('Name:\t\t%s\n' %
                   self.if_dict[self.cb_interfaces.GetValue()])

        except KeyError:
            self.tc_information.SetValue('No address assigned')

class MainWindow(wx.Frame):
    def __init__(self, parent, title, size, style):
        wx.Frame.__init__(self, parent, title=title, size=size, style=style)

        # Menu bar
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", '''Information about
                this program''')
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Exit the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        # intance of the Panel we created before
        mainPanel = MWPanel(self)

        # Status bar
        self.CreateStatusBar()

        # Actually show this window 
        self.Show()


        # Event bindings
        self.Bind(wx.EVT_MENU, self.on_about, menuAbout)
        self.Bind(wx.EVT_MENU, self.on_exit, menuExit)

    # Event handlers
    def on_about(self, e):
        dlg = wx.MessageDialog(self, '''A program to show information about the
                computer's network interface''', "About Interfaces", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def on_exit(self, e):
        self.Close(True)


def main():
    app = wx.App(False)
    MainWindow(None,title="Interfaces", size=(340,350),
            style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
    app.MainLoop()


if __name__ == "__main__":
    main()
