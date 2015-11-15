#insert projet at path
# not required if installed
import sys
from  os import path
my_dir = path.dirname(path.abspath(__file__))
sys.path = [my_dir + "/../"] + sys.path


#Import decorators
#-----------------

from dbusdecorator import DbusAttr, DbusInterface, DbusMethod

#Define dbus interface
#----------------------

@DbusInterface('org.mpris.MediaPlayer2.Player', '/org/mpris/MediaPlayer2')
class Player(object):
    '''
    Your interface info
    '''
    
    @DbusMethod
    def Next(self):
        '''
        Your method
        '''

    @DbusAttr
    def Volume(self): 
        '''
        Your attribute
        '''

#Use your definition
#-------------------
mediaplayer2 = Player(
   dbus_interface_info={
      'dbus_uri': 'org.mpris.MediaPlayer2.gmusicbrowser'})
mediaplayer2.Next()
print(mediaplayer2.Volume)
mediaplayer2.Volume = 1
print(mediaplayer2.Volume) # integer = 1 :P