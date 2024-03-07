from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import freesans20
import writer

detector = machine.ADC(Pin(28))
#conversion_factor = 3.3 / (65535)

WIDTH  = 128                                          
HEIGHT = 32                                             

i2c = I2C(1,scl=Pin(27),sda=Pin(26), freq=2000000 )
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    reading = detector.read_u16()
    oled.fill(0)
    oled.text("Odczyt *",0,0)
    font_writer = writer.Writer(oled, freesans20)
    font_writer.set_textpos(0, 32)
    font_writer.printstring(str(reading))
    print(reading)
    oled.show() 
    time.sleep(0.5)
    reading = detector.read_u16()
    oled.fill(0)
    oled.text("Odczyt",0,0)
    font_writer = writer.Writer(oled, freesans20)
    font_writer.set_textpos(0, 32)
    font_writer.printstring(str(reading))
    print(reading)
    oled.show()
    time.sleep(0.5)

