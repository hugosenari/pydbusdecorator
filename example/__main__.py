#insert projet at path
# not required if installed
import sys
from  os import path
my_dir = path.dirname(path.abspath(__file__))
sys.path = [my_dir + "/../"] + sys.path


#Import decorators
#-----------------

from dbusdecorator import DbusAttr, DbusInterface, DbusMethod, get_uri

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

# use this if you don't know your object name
#----------------------
uri = [player for player in get_uri('org.mpris.MediaPlayer2.+')] 

#Use your definition
#-------------------
mediaplayer2 = Player(
   dbus_interface_info={'dbus_uri': uri[0]})
mediaplayer2.Next()
vol = mediaplayer2.Volume
print(mediaplayer2.Volume)
mediaplayer2.Volume = vol - 0.1
print(mediaplayer2.Volume) # integer = 1 :P