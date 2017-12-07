import wx  # 开发任一wxPython程序所必须的五个基本步骤：1导入必须的wxPython包

class App(wx.App):  # 2子类化wxPython应用程序类

    def OnInit(self):  # 3定义一个应用程序的初始化方法
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True


app = App()  # 4创建一个应用程序类的实例
app.MainLoop()  # 5进入这个应用程序的主事件循环

"""
下面的代码演示了如何定义我们的wx.App的子类：
class MyApp(wx.App):

     def OnInit(self):
        frame = wx.Frame(parent=None, id=-1, title=”Bare”)
        frame.Show()
        return True
wx.Frame接受三个参数，仅第一个是必须的，其余的都有默认值
调用Show()方法使frame可见，否则不可见
frame.Show(False) # 使框架不可见.
frame.Show(True) # True是默认值，使框架可见.
frame.Hide() # 等同于frame.Show(False)

创建一个应用程序实例并进入它的主事件循环
这步是创建wx.App子类的实例，并调用它的MainLoop()方法：
app = App()
app.MainLoop()
一旦进入主事件循环，控制权将转交给wxPython。wxPython GUI程序主要
响应用户的鼠标和键盘事件。当一个应用程序的所有框架被关闭后，这个
app.MainLoop()方法将返回且程序退出
"""