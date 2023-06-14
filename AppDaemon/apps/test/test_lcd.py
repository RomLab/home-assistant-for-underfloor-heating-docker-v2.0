import i2c_lcd_driver

degree = [      
    [ 0b00111,
	  0b00101,
	  0b00111,
	  0b00000,
	  0b00000,
	  0b00000,
	  0b00000,
	  0b00000
    ],]

first_floor_lcd= i2c_lcd_driver.lcd(0x20)  
first_floor_lcd.lcd_load_custom_chars(degree)

second_floor_lcd= i2c_lcd_driver.lcd(0x21)  
second_floor_lcd.lcd_load_custom_chars(degree)

third_floor_lcd= i2c_lcd_driver.lcd(0x23)  
third_floor_lcd.lcd_load_custom_chars(degree)
    
fourth_floor_lcd= i2c_lcd_driver.lcd(0x25)
fourth_floor_lcd.lcd_load_custom_chars(degree)

first_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
first_floor_lcd.lcd_display_string("Cidlo 3: 18" + chr(0) + "C", 2)

second_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
second_floor_lcd.lcd_display_string("Cidlo 3: 18" + chr(0) + "C", 2)

third_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
third_floor_lcd.lcd_display_string("Cidlo 3: 18" + chr(0) + "C", 2)

fourth_floor_lcd.lcd_display_string("  Zatop v krbu!", 1)
fourth_floor_lcd.lcd_display_string("Cidlo 3: 18" + chr(0) + "C", 2)
