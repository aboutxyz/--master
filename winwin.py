import win32gui, win32ui, win32con,win32api

def tapScreen(x, y):
    """模拟鼠标点击"""
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

tapScreen(163,461)