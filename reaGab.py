"""
Library reaGab.py May-2019
Set of functions for easy print

"""
def titu(text,aste):
   width       = len(text)+4
   if len(aste)==0:
      aste        = '*'
   line        = '\n'+aste*width+'\n'
   print(line,aste,' ',text,' ',aste,line,sep='')

def line(dash):
    print(dash*50)
