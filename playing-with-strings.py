'''
playing-with-strings.py


'''

name                = 'Gabriel'
lastName            = 'Medina'
fullName            = name + " " + lastName

print(fullName)


longString          = "This is a text that was taken from somewhere This is a text that was taken from somewhere This is a text that was taken from somewhere This is a text that was taken from somewhere This is a text that was taken from somewhere  This is a text that was taken from somewhere "
print(longString)

print(' ------------------- ')

# Equivalent
longString          = "This is a text that was taken from somewhere\
This is a text that was taken from somewhere\
This is a text that was taken from somewhere\
This is a text that was taken from somewhere\
This is a text that was taken from somewhere\
This is a text that was taken from somewhere\ "
print(longString)

print(" ------ ")
longString          = """This is a text that was taken from somewhere
This is a text that was taken from somewhere
This is a text that was taken from somewhere
This is a text that was taken from somewhere 
This is a text that was taken from somewhere
This is a text that was taken from somewhere """
print(longString)


print(" ------ ")
longString          = "SAMPLE"
print(longString)
longString          = "012345"
print(longString)

print(" ------ ")
longString          = "SAMPLE"
print(longString[0])
print(longString[-1])
print(longString[1:])
print(longString[:1])
print(longString[:])
print(longString[:3])

link                = 'https://www.python.org/doc/'
http                = 'https://'
isHttp              = (http == link[:8])
print('Is HTTP:',isHttp)
