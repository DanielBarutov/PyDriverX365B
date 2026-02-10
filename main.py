from escpos.printer import Usb

""" Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
p = Usb(0x1fc9, 0x2016, 0, profile="default")
p.text("Hello World\n")
p.profile.media['width']['pixel'] = 576

p.cut()
