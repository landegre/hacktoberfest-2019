# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:37:26 2019

@author: Saputra
"""

myunicodestr1 = u"Hi Class!"
myunicodestr2 = u"Hi\u0020Class!"
print (myunicodestr1, myunicodestr2) 
newunicode = u'\xe4\xf6\xfc'
print (newunicode)
newstr = newunicode.encode('utf-8') 
print (newstr)
print (u'\u0420\u043e\u0441\u0441\u0438\u044f',newstr, 'utf-8')
