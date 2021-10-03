#packages

#NumPy
#Pendulum
#Python Imaging Library
#MoviePy
#Requests
#Tkinter
#PyQt
#Pandas
#Py32
#PyTest

#commandprompt
py -m pip --version
py -m pip list
py -m pip install camelcase
py -m pip uninstall camelcase
py -m pip install --upgrade pip

import camelcase

x= camelcase.CamelCase()

a= "hi there! this is a message to check if the letters of each word are capitalised"

print(x.hump(a))



