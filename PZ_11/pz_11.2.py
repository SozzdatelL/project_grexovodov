#Из заданной строки отобразить только цифры.
import string

s = "TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."
digits = ''.join(c for c in s if c in string.digits)
print(digits)
