import win32print

printer = "Xprinter XP-365B"

data = b"""
SIZE 60 mm,30 mm
GAP 0 mm,0 mm
CLS
TEXT 20,20,"3",0,1,1,"HELLO"
PRINT 1
"""

h = win32print.OpenPrinter(printer)
win32print.StartDocPrinter(h, 1, ("test", None, "RAW"))
win32print.StartPagePrinter(h)
win32print.WritePrinter(h, data)
win32print.EndPagePrinter(h)
win32print.EndDocPrinter(h)
win32print.ClosePrinter(h)
