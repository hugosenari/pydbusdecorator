'''
Created with dbus2any pydbusclient.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require python dbus

Parameters:

* /im/pidgin/purple/PurpleObject
* im.pidgin.purple.PurpleService
* 

'''

import dbus


def get_introspectable_dbus_client():
    session_bus = dbus.SessionBus()
    return session_bus.get_object('im.pidgin.purple.PurpleService',
                                  '/im/pidgin/purple/PurpleObject')
    
class Introspectable(object):
    '''
    Introspectable
    
    Usage:
    ------
    
    Instantiate this class and access the instance members and methods
    '''
    def __init__(self, interface=None, object_path=None, bus_name=None, *arg, **kw):
        '''Constructor'''
        self._dbus_interface = interface or "org.freedesktop.DBus.Introspectable"
        self._dbus_object_path = object_path or "/im/pidgin/purple/PurpleObject"
        self._dbus_name = bus_name or "im.pidgin.purple.PurpleService"
        self._dbus_object = get_introspectable_dbus_client()

    
    
    def Introspect(self, *arg, **kw):
        """
        Introspect method:

        Parameters
        ----------

        data:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.Introspect( *arg, **kw)
  
def get_purpleinterface_dbus_client():
    session_bus = dbus.SessionBus()
    return session_bus.get_object('im.pidgin.purple.PurpleService',
                                  '/im/pidgin/purple/PurpleObject')
    
class PurpleInterface(object):
    '''
    PurpleInterface
    
    Usage:
    ------
    
    Instantiate this class and access the instance members and methods
    '''
    def __init__(self, interface=None, object_path=None, bus_name=None, *arg, **kw):
        '''Constructor'''
        self._dbus_interface = interface or "im.pidgin.purple.PurpleInterface"
        self._dbus_object_path = object_path or "/im/pidgin/purple/PurpleObject"
        self._dbus_name = bus_name or "im.pidgin.purple.PurpleService"
        self._dbus_object = get_purpleinterface_dbus_client()

    
    
    def PurpleAccountsFindAny(self, arg_name, arg_protocol, *arg, **kw):
        """
        PurpleAccountsFindAny method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            protocol:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsFindAny( arg_name, arg_protocol, *arg, **kw)
    
    def PurpleAccountsFindConnected(self, arg_name, arg_protocol, *arg, **kw):
        """
        PurpleAccountsFindConnected method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            protocol:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsFindConnected( arg_name, arg_protocol, *arg, **kw)
    
    def PurpleBlistNodeIsChat(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeIsChat method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeIsChat( arg_node, *arg, **kw)
    
    def PurpleBlistNodeIsBuddy(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeIsBuddy method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeIsBuddy( arg_node, *arg, **kw)
    
    def PurpleBlistNodeIsContact(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeIsContact method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeIsContact( arg_node, *arg, **kw)
    
    def PurpleBlistNodeIsGroup(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeIsGroup method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeIsGroup( arg_node, *arg, **kw)
    
    def PurpleBuddyIsOnline(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyIsOnline method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIsOnline( arg_buddy, *arg, **kw)
    
    def PurpleBlistNodeHasFlag(self, arg_node, arg_flags, *arg, **kw):
        """
        PurpleBlistNodeHasFlag method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            flags:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeHasFlag( arg_node, arg_flags, *arg, **kw)
    
    def PurpleBlistNodeShouldSave(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeShouldSave method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeShouldSave( arg_node, *arg, **kw)
    
    def PurpleConnectionIsConnected(self, arg_connection, *arg, **kw):
        """
        PurpleConnectionIsConnected method:

        Parameters
        ----------

        connection:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionIsConnected( arg_connection, *arg, **kw)
    
    def PurpleConnectionIsValid(self, arg_connection, *arg, **kw):
        """
        PurpleConnectionIsValid method:

        Parameters
        ----------

        connection:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionIsValid( arg_connection, *arg, **kw)
    
    def PurpleConvIm(self, arg_conversation, *arg, **kw):
        """
        PurpleConvIm method:

        Parameters
        ----------

        conversation:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvIm( arg_conversation, *arg, **kw)
    
    def PurpleConvChat(self, arg_conversation, *arg, **kw):
        """
        PurpleConvChat method:

        Parameters
        ----------

        conversation:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChat( arg_conversation, *arg, **kw)
    
    def PurpleAccountNew(self, arg_username, arg_protocol_id, *arg, **kw):
        """
        PurpleAccountNew method:

        Parameters
        ----------

        username:
            type: s,
            direction: in;
            protocol_id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountNew( arg_username, arg_protocol_id, *arg, **kw)
    
    def PurpleAccountDestroy(self, arg_account, *arg, **kw):
        """
        PurpleAccountDestroy method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountDestroy( arg_account, *arg, **kw)
    
    def PurpleAccountConnect(self, arg_account, *arg, **kw):
        """
        PurpleAccountConnect method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountConnect( arg_account, *arg, **kw)
    
    def PurpleAccountRegister(self, arg_account, *arg, **kw):
        """
        PurpleAccountRegister method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRegister( arg_account, *arg, **kw)
    
    def PurpleAccountDisconnect(self, arg_account, *arg, **kw):
        """
        PurpleAccountDisconnect method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountDisconnect( arg_account, *arg, **kw)
    
    def PurpleAccountNotifyAdded(self, arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw):
        """
        PurpleAccountNotifyAdded method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            remote_user:
            type: s,
            direction: in;
            id:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountNotifyAdded( arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw)
    
    def PurpleAccountRequestAdd(self, arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw):
        """
        PurpleAccountRequestAdd method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            remote_user:
            type: s,
            direction: in;
            id:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRequestAdd( arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw)
    
    def PurpleAccountRequestCloseWithAccount(self, arg_account, *arg, **kw):
        """
        PurpleAccountRequestCloseWithAccount method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRequestCloseWithAccount( arg_account, *arg, **kw)
    
    def PurpleAccountRequestClose(self, arg_ui_handle, *arg, **kw):
        """
        PurpleAccountRequestClose method:

        Parameters
        ----------

        ui_handle:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRequestClose( arg_ui_handle, *arg, **kw)
    
    def PurpleAccountRequestChangePassword(self, arg_account, *arg, **kw):
        """
        PurpleAccountRequestChangePassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRequestChangePassword( arg_account, *arg, **kw)
    
    def PurpleAccountRequestChangeUserInfo(self, arg_account, *arg, **kw):
        """
        PurpleAccountRequestChangeUserInfo method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRequestChangeUserInfo( arg_account, *arg, **kw)
    
    def PurpleAccountSetUsername(self, arg_account, arg_username, *arg, **kw):
        """
        PurpleAccountSetUsername method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            username:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetUsername( arg_account, arg_username, *arg, **kw)
    
    def PurpleAccountSetPassword(self, arg_account, arg_password, *arg, **kw):
        """
        PurpleAccountSetPassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            password:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetPassword( arg_account, arg_password, *arg, **kw)
    
    def PurpleAccountSetAlias(self, arg_account, arg_alias, *arg, **kw):
        """
        PurpleAccountSetAlias method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetAlias( arg_account, arg_alias, *arg, **kw)
    
    def PurpleAccountSetUserInfo(self, arg_account, arg_user_info, *arg, **kw):
        """
        PurpleAccountSetUserInfo method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            user_info:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetUserInfo( arg_account, arg_user_info, *arg, **kw)
    
    def PurpleAccountSetBuddyIconPath(self, arg_account, arg_path, *arg, **kw):
        """
        PurpleAccountSetBuddyIconPath method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            path:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetBuddyIconPath( arg_account, arg_path, *arg, **kw)
    
    def PurpleAccountSetProtocolId(self, arg_account, arg_protocol_id, *arg, **kw):
        """
        PurpleAccountSetProtocolId method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            protocol_id:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetProtocolId( arg_account, arg_protocol_id, *arg, **kw)
    
    def PurpleAccountSetConnection(self, arg_account, arg_gc, *arg, **kw):
        """
        PurpleAccountSetConnection method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            gc:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetConnection( arg_account, arg_gc, *arg, **kw)
    
    def PurpleAccountSetRememberPassword(self, arg_account, arg_value, *arg, **kw):
        """
        PurpleAccountSetRememberPassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetRememberPassword( arg_account, arg_value, *arg, **kw)
    
    def PurpleAccountSetCheckMail(self, arg_account, arg_value, *arg, **kw):
        """
        PurpleAccountSetCheckMail method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetCheckMail( arg_account, arg_value, *arg, **kw)
    
    def PurpleAccountSetEnabled(self, arg_account, arg_ui, arg_value, *arg, **kw):
        """
        PurpleAccountSetEnabled method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetEnabled( arg_account, arg_ui, arg_value, *arg, **kw)
    
    def PurpleAccountSetProxyInfo(self, arg_account, arg_info, *arg, **kw):
        """
        PurpleAccountSetProxyInfo method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            info:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetProxyInfo( arg_account, arg_info, *arg, **kw)
    
    def PurpleAccountSetPrivacyType(self, arg_account, arg_privacy_type, *arg, **kw):
        """
        PurpleAccountSetPrivacyType method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            privacy_type:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetPrivacyType( arg_account, arg_privacy_type, *arg, **kw)
    
    def PurpleAccountSetStatusTypes(self, arg_account, arg_status_types, *arg, **kw):
        """
        PurpleAccountSetStatusTypes method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            status_types:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetStatusTypes( arg_account, arg_status_types, *arg, **kw)
    
    def PurpleAccountSetStatusList(self, arg_account, arg_status_id, arg_active, arg_attrs, *arg, **kw):
        """
        PurpleAccountSetStatusList method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            active:
            type: i,
            direction: in;
            attrs:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetStatusList( arg_account, arg_status_id, arg_active, arg_attrs, *arg, **kw)
    
    def PurpleAccountGetSilenceSuppression(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetSilenceSuppression method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetSilenceSuppression( arg_account, *arg, **kw)
    
    def PurpleAccountSetSilenceSuppression(self, arg_account, arg_value, *arg, **kw):
        """
        PurpleAccountSetSilenceSuppression method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetSilenceSuppression( arg_account, arg_value, *arg, **kw)
    
    def PurpleAccountClearSettings(self, arg_account, *arg, **kw):
        """
        PurpleAccountClearSettings method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountClearSettings( arg_account, *arg, **kw)
    
    def PurpleAccountRemoveSetting(self, arg_account, arg_setting, *arg, **kw):
        """
        PurpleAccountRemoveSetting method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            setting:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRemoveSetting( arg_account, arg_setting, *arg, **kw)
    
    def PurpleAccountSetInt(self, arg_account, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetInt method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetInt( arg_account, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountSetString(self, arg_account, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetString method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetString( arg_account, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountSetBool(self, arg_account, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetBool method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetBool( arg_account, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountSetUiInt(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetUiInt method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetUiInt( arg_account, arg_ui, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountSetUiString(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetUiString method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetUiString( arg_account, arg_ui, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountSetUiBool(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
        """
        PurpleAccountSetUiBool method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountSetUiBool( arg_account, arg_ui, arg_name, arg_value, *arg, **kw)
    
    def PurpleAccountIsConnected(self, arg_account, *arg, **kw):
        """
        PurpleAccountIsConnected method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountIsConnected( arg_account, *arg, **kw)
    
    def PurpleAccountIsConnecting(self, arg_account, *arg, **kw):
        """
        PurpleAccountIsConnecting method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountIsConnecting( arg_account, *arg, **kw)
    
    def PurpleAccountIsDisconnected(self, arg_account, *arg, **kw):
        """
        PurpleAccountIsDisconnected method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountIsDisconnected( arg_account, *arg, **kw)
    
    def PurpleAccountGetUsername(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetUsername method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetUsername( arg_account, *arg, **kw)
    
    def PurpleAccountGetPassword(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetPassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetPassword( arg_account, *arg, **kw)
    
    def PurpleAccountGetAlias(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetAlias method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetAlias( arg_account, *arg, **kw)
    
    def PurpleAccountGetUserInfo(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetUserInfo method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetUserInfo( arg_account, *arg, **kw)
    
    def PurpleAccountGetBuddyIconPath(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetBuddyIconPath method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetBuddyIconPath( arg_account, *arg, **kw)
    
    def PurpleAccountGetProtocolId(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetProtocolId method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetProtocolId( arg_account, *arg, **kw)
    
    def PurpleAccountGetProtocolName(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetProtocolName method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetProtocolName( arg_account, *arg, **kw)
    
    def PurpleAccountGetConnection(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetConnection method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetConnection( arg_account, *arg, **kw)
    
    def PurpleAccountGetNameForDisplay(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetNameForDisplay method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetNameForDisplay( arg_account, *arg, **kw)
    
    def PurpleAccountGetRememberPassword(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetRememberPassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetRememberPassword( arg_account, *arg, **kw)
    
    def PurpleAccountGetCheckMail(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetCheckMail method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetCheckMail( arg_account, *arg, **kw)
    
    def PurpleAccountGetEnabled(self, arg_account, arg_ui, *arg, **kw):
        """
        PurpleAccountGetEnabled method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetEnabled( arg_account, arg_ui, *arg, **kw)
    
    def PurpleAccountGetProxyInfo(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetProxyInfo method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetProxyInfo( arg_account, *arg, **kw)
    
    def PurpleAccountGetPrivacyType(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetPrivacyType method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetPrivacyType( arg_account, *arg, **kw)
    
    def PurpleAccountGetActiveStatus(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetActiveStatus method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetActiveStatus( arg_account, *arg, **kw)
    
    def PurpleAccountGetStatus(self, arg_account, arg_status_id, *arg, **kw):
        """
        PurpleAccountGetStatus method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetStatus( arg_account, arg_status_id, *arg, **kw)
    
    def PurpleAccountGetStatusType(self, arg_account, arg_id, *arg, **kw):
        """
        PurpleAccountGetStatusType method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetStatusType( arg_account, arg_id, *arg, **kw)
    
    def PurpleAccountGetStatusTypeWithPrimitive(self, arg_account, arg_primitive, *arg, **kw):
        """
        PurpleAccountGetStatusTypeWithPrimitive method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            primitive:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetStatusTypeWithPrimitive( arg_account, arg_primitive, *arg, **kw)
    
    def PurpleAccountGetPresence(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetPresence method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetPresence( arg_account, *arg, **kw)
    
    def PurpleAccountIsStatusActive(self, arg_account, arg_status_id, *arg, **kw):
        """
        PurpleAccountIsStatusActive method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountIsStatusActive( arg_account, arg_status_id, *arg, **kw)
    
    def PurpleAccountGetStatusTypes(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetStatusTypes method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetStatusTypes( arg_account, *arg, **kw)
    
    def PurpleAccountGetInt(self, arg_account, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetInt method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetInt( arg_account, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetString(self, arg_account, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetString method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetString( arg_account, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetBool(self, arg_account, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetBool method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetBool( arg_account, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetUiInt(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetUiInt method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetUiInt( arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetUiString(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetUiString method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetUiString( arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetUiBool(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
        """
        PurpleAccountGetUiBool method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            ui:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            default_value:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetUiBool( arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw)
    
    def PurpleAccountGetLog(self, arg_account, arg_create, *arg, **kw):
        """
        PurpleAccountGetLog method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            create:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetLog( arg_account, arg_create, *arg, **kw)
    
    def PurpleAccountDestroyLog(self, arg_account, *arg, **kw):
        """
        PurpleAccountDestroyLog method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountDestroyLog( arg_account, *arg, **kw)
    
    def PurpleAccountAddBuddy(self, arg_account, arg_buddy, *arg, **kw):
        """
        PurpleAccountAddBuddy method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddy:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountAddBuddy( arg_account, arg_buddy, *arg, **kw)
    
    def PurpleAccountAddBuddyWithInvite(self, arg_account, arg_buddy, arg_message, *arg, **kw):
        """
        PurpleAccountAddBuddyWithInvite method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddy:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountAddBuddyWithInvite( arg_account, arg_buddy, arg_message, *arg, **kw)
    
    def PurpleAccountAddBuddies(self, arg_account, arg_buddies, *arg, **kw):
        """
        PurpleAccountAddBuddies method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddies:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountAddBuddies( arg_account, arg_buddies, *arg, **kw)
    
    def PurpleAccountAddBuddiesWithInvite(self, arg_account, arg_buddies, arg_message, *arg, **kw):
        """
        PurpleAccountAddBuddiesWithInvite method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddies:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountAddBuddiesWithInvite( arg_account, arg_buddies, arg_message, *arg, **kw)
    
    def PurpleAccountRemoveBuddy(self, arg_account, arg_buddy, arg_group, *arg, **kw):
        """
        PurpleAccountRemoveBuddy method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddy:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRemoveBuddy( arg_account, arg_buddy, arg_group, *arg, **kw)
    
    def PurpleAccountRemoveBuddies(self, arg_account, arg_buddies, arg_groups, *arg, **kw):
        """
        PurpleAccountRemoveBuddies method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddies:
            type: i,
            direction: in;
            groups:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRemoveBuddies( arg_account, arg_buddies, arg_groups, *arg, **kw)
    
    def PurpleAccountRemoveGroup(self, arg_account, arg_group, *arg, **kw):
        """
        PurpleAccountRemoveGroup method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountRemoveGroup( arg_account, arg_group, *arg, **kw)
    
    def PurpleAccountChangePassword(self, arg_account, arg_orig_pw, arg_new_pw, *arg, **kw):
        """
        PurpleAccountChangePassword method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            orig_pw:
            type: s,
            direction: in;
            new_pw:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountChangePassword( arg_account, arg_orig_pw, arg_new_pw, *arg, **kw)
    
    def PurpleAccountSupportsOfflineMessage(self, arg_account, arg_buddy, *arg, **kw):
        """
        PurpleAccountSupportsOfflineMessage method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountSupportsOfflineMessage( arg_account, arg_buddy, *arg, **kw)
    
    def PurpleAccountGetCurrentError(self, arg_account, *arg, **kw):
        """
        PurpleAccountGetCurrentError method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountGetCurrentError( arg_account, *arg, **kw)
    
    def PurpleAccountClearCurrentError(self, arg_account, *arg, **kw):
        """
        PurpleAccountClearCurrentError method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountClearCurrentError( arg_account, *arg, **kw)
    
    def PurpleAccountsAdd(self, arg_account, *arg, **kw):
        """
        PurpleAccountsAdd method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountsAdd( arg_account, *arg, **kw)
    
    def PurpleAccountsRemove(self, arg_account, *arg, **kw):
        """
        PurpleAccountsRemove method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountsRemove( arg_account, *arg, **kw)
    
    def PurpleAccountsDelete(self, arg_account, *arg, **kw):
        """
        PurpleAccountsDelete method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountsDelete( arg_account, *arg, **kw)
    
    def PurpleAccountsReorder(self, arg_account, arg_new_index, *arg, **kw):
        """
        PurpleAccountsReorder method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            new_index:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountsReorder( arg_account, arg_new_index, *arg, **kw)
    
    def PurpleAccountsGetAll(self, *arg, **kw):
        """
        PurpleAccountsGetAll method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsGetAll( *arg, **kw)
    
    def PurpleAccountsGetAllActive(self, *arg, **kw):
        """
        PurpleAccountsGetAllActive method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsGetAllActive( *arg, **kw)
    
    def PurpleAccountsFind(self, arg_name, arg_protocol, *arg, **kw):
        """
        PurpleAccountsFind method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            protocol:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsFind( arg_name, arg_protocol, *arg, **kw)
    
    def PurpleAccountsRestoreCurrentStatuses(self, *arg, **kw):
        """
        PurpleAccountsRestoreCurrentStatuses method:
        """
        return self._dbus_object.PurpleAccountsRestoreCurrentStatuses( *arg, **kw)
    
    def PurpleAccountsSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleAccountsSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleAccountsSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleAccountsGetUiOps(self, *arg, **kw):
        """
        PurpleAccountsGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAccountsGetUiOps( *arg, **kw)
    
    def PurpleAccountsInit(self, *arg, **kw):
        """
        PurpleAccountsInit method:
        """
        return self._dbus_object.PurpleAccountsInit( *arg, **kw)
    
    def PurpleAccountsUninit(self, *arg, **kw):
        """
        PurpleAccountsUninit method:
        """
        return self._dbus_object.PurpleAccountsUninit( *arg, **kw)
    
    def PurpleBlistNew(self, *arg, **kw):
        """
        PurpleBlistNew method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNew( *arg, **kw)
    
    def PurpleSetBlist(self, arg_blist, *arg, **kw):
        """
        PurpleSetBlist method:

        Parameters
        ----------

        blist:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSetBlist( arg_blist, *arg, **kw)
    
    def PurpleGetBlist(self, *arg, **kw):
        """
        PurpleGetBlist method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetBlist( *arg, **kw)
    
    def PurpleBlistGetRoot(self, *arg, **kw):
        """
        PurpleBlistGetRoot method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistGetRoot( *arg, **kw)
    
    def PurpleBlistGetBuddies(self, *arg, **kw):
        """
        PurpleBlistGetBuddies method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistGetBuddies( *arg, **kw)
    
    def PurpleBlistNodeNext(self, arg_node, arg_offline, *arg, **kw):
        """
        PurpleBlistNodeNext method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            offline:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeNext( arg_node, arg_offline, *arg, **kw)
    
    def PurpleBlistNodeGetParent(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetParent method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetParent( arg_node, *arg, **kw)
    
    def PurpleBlistNodeGetFirstChild(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetFirstChild method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetFirstChild( arg_node, *arg, **kw)
    
    def PurpleBlistNodeGetSiblingNext(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetSiblingNext method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetSiblingNext( arg_node, *arg, **kw)
    
    def PurpleBlistNodeGetSiblingPrev(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetSiblingPrev method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetSiblingPrev( arg_node, *arg, **kw)
    
    def PurpleBlistShow(self, *arg, **kw):
        """
        PurpleBlistShow method:
        """
        return self._dbus_object.PurpleBlistShow( *arg, **kw)
    
    def PurpleBlistDestroy(self, *arg, **kw):
        """
        PurpleBlistDestroy method:
        """
        return self._dbus_object.PurpleBlistDestroy( *arg, **kw)
    
    def PurpleBlistSetVisible(self, arg_show, *arg, **kw):
        """
        PurpleBlistSetVisible method:

        Parameters
        ----------

        show:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistSetVisible( arg_show, *arg, **kw)
    
    def PurpleBlistUpdateBuddyStatus(self, arg_buddy, arg_old_status, *arg, **kw):
        """
        PurpleBlistUpdateBuddyStatus method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            old_status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistUpdateBuddyStatus( arg_buddy, arg_old_status, *arg, **kw)
    
    def PurpleBlistUpdateNodeIcon(self, arg_node, *arg, **kw):
        """
        PurpleBlistUpdateNodeIcon method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistUpdateNodeIcon( arg_node, *arg, **kw)
    
    def PurpleBlistUpdateBuddyIcon(self, arg_buddy, *arg, **kw):
        """
        PurpleBlistUpdateBuddyIcon method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistUpdateBuddyIcon( arg_buddy, *arg, **kw)
    
    def PurpleBlistRenameBuddy(self, arg_buddy, arg_name, *arg, **kw):
        """
        PurpleBlistRenameBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRenameBuddy( arg_buddy, arg_name, *arg, **kw)
    
    def PurpleBlistAliasContact(self, arg_contact, arg_alias, *arg, **kw):
        """
        PurpleBlistAliasContact method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAliasContact( arg_contact, arg_alias, *arg, **kw)
    
    def PurpleBlistAliasBuddy(self, arg_buddy, arg_alias, *arg, **kw):
        """
        PurpleBlistAliasBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAliasBuddy( arg_buddy, arg_alias, *arg, **kw)
    
    def PurpleBlistServerAliasBuddy(self, arg_buddy, arg_alias, *arg, **kw):
        """
        PurpleBlistServerAliasBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistServerAliasBuddy( arg_buddy, arg_alias, *arg, **kw)
    
    def PurpleBlistAliasChat(self, arg_chat, arg_alias, *arg, **kw):
        """
        PurpleBlistAliasChat method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAliasChat( arg_chat, arg_alias, *arg, **kw)
    
    def PurpleBlistRenameGroup(self, arg_group, arg_name, *arg, **kw):
        """
        PurpleBlistRenameGroup method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRenameGroup( arg_group, arg_name, *arg, **kw)
    
    def PurpleChatNew(self, arg_account, arg_alias, arg_components, *arg, **kw):
        """
        PurpleChatNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            components:
            type: a{ss},
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleChatNew( arg_account, arg_alias, arg_components, *arg, **kw)
    
    def PurpleChatDestroy(self, arg_chat, *arg, **kw):
        """
        PurpleChatDestroy method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleChatDestroy( arg_chat, *arg, **kw)
    
    def PurpleBlistAddChat(self, arg_chat, arg_group, arg_node, *arg, **kw):
        """
        PurpleBlistAddChat method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAddChat( arg_chat, arg_group, arg_node, *arg, **kw)
    
    def PurpleBuddyNew(self, arg_account, arg_name, arg_alias, *arg, **kw):
        """
        PurpleBuddyNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyNew( arg_account, arg_name, arg_alias, *arg, **kw)
    
    def PurpleBuddyDestroy(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyDestroy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyDestroy( arg_buddy, *arg, **kw)
    
    def PurpleBuddySetIcon(self, arg_buddy, arg_icon, *arg, **kw):
        """
        PurpleBuddySetIcon method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            icon:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddySetIcon( arg_buddy, arg_icon, *arg, **kw)
    
    def PurpleBuddyGetAccount(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetAccount method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetAccount( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetName(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetName method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetName( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetIcon(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetIcon method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetIcon( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetContact(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetContact method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetContact( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetPresence(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetPresence method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetPresence( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetMediaCaps(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetMediaCaps method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetMediaCaps( arg_buddy, *arg, **kw)
    
    def PurpleBuddySetMediaCaps(self, arg_buddy, arg_media_caps, *arg, **kw):
        """
        PurpleBuddySetMediaCaps method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            media_caps:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddySetMediaCaps( arg_buddy, arg_media_caps, *arg, **kw)
    
    def PurpleBlistAddBuddy(self, arg_buddy, arg_contact, arg_group, arg_node, *arg, **kw):
        """
        PurpleBlistAddBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            contact:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAddBuddy( arg_buddy, arg_contact, arg_group, arg_node, *arg, **kw)
    
    def PurpleGroupNew(self, arg_name, *arg, **kw):
        """
        PurpleGroupNew method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleGroupNew( arg_name, *arg, **kw)
    
    def PurpleGroupDestroy(self, arg_group, *arg, **kw):
        """
        PurpleGroupDestroy method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleGroupDestroy( arg_group, *arg, **kw)
    
    def PurpleBlistAddGroup(self, arg_group, arg_node, *arg, **kw):
        """
        PurpleBlistAddGroup method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAddGroup( arg_group, arg_node, *arg, **kw)
    
    def PurpleContactNew(self, *arg, **kw):
        """
        PurpleContactNew method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleContactNew( *arg, **kw)
    
    def PurpleContactDestroy(self, arg_contact, *arg, **kw):
        """
        PurpleContactDestroy method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleContactDestroy( arg_contact, *arg, **kw)
    
    def PurpleContactGetGroup(self, arg_contact, *arg, **kw):
        """
        PurpleContactGetGroup method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleContactGetGroup( arg_contact, *arg, **kw)
    
    def PurpleBlistAddContact(self, arg_contact, arg_group, arg_node, *arg, **kw):
        """
        PurpleBlistAddContact method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAddContact( arg_contact, arg_group, arg_node, *arg, **kw)
    
    def PurpleBlistMergeContact(self, arg_source, arg_node, *arg, **kw):
        """
        PurpleBlistMergeContact method:

        Parameters
        ----------

        source:
            type: i,
            direction: in;
            node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistMergeContact( arg_source, arg_node, *arg, **kw)
    
    def PurpleContactGetPriorityBuddy(self, arg_contact, *arg, **kw):
        """
        PurpleContactGetPriorityBuddy method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleContactGetPriorityBuddy( arg_contact, *arg, **kw)
    
    def PurpleContactSetAlias(self, arg_contact, arg_alias, *arg, **kw):
        """
        PurpleContactSetAlias method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleContactSetAlias( arg_contact, arg_alias, *arg, **kw)
    
    def PurpleContactGetAlias(self, arg_contact, *arg, **kw):
        """
        PurpleContactGetAlias method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleContactGetAlias( arg_contact, *arg, **kw)
    
    def PurpleContactOnAccount(self, arg_contact, arg_account, *arg, **kw):
        """
        PurpleContactOnAccount method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleContactOnAccount( arg_contact, arg_account, *arg, **kw)
    
    def PurpleContactInvalidatePriorityBuddy(self, arg_contact, *arg, **kw):
        """
        PurpleContactInvalidatePriorityBuddy method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleContactInvalidatePriorityBuddy( arg_contact, *arg, **kw)
    
    def PurpleBlistRemoveBuddy(self, arg_buddy, *arg, **kw):
        """
        PurpleBlistRemoveBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRemoveBuddy( arg_buddy, *arg, **kw)
    
    def PurpleBlistRemoveContact(self, arg_contact, *arg, **kw):
        """
        PurpleBlistRemoveContact method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRemoveContact( arg_contact, *arg, **kw)
    
    def PurpleBlistRemoveChat(self, arg_chat, *arg, **kw):
        """
        PurpleBlistRemoveChat method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRemoveChat( arg_chat, *arg, **kw)
    
    def PurpleBlistRemoveGroup(self, arg_group, *arg, **kw):
        """
        PurpleBlistRemoveGroup method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRemoveGroup( arg_group, *arg, **kw)
    
    def PurpleBuddyGetAliasOnly(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetAliasOnly method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetAliasOnly( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetServerAlias(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetServerAlias method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetServerAlias( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetContactAlias(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetContactAlias method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetContactAlias( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetLocalAlias(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetLocalAlias method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetLocalAlias( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetAlias(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetAlias method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetAlias( arg_buddy, *arg, **kw)
    
    def PurpleBuddyGetLocalBuddyAlias(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetLocalBuddyAlias method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetLocalBuddyAlias( arg_buddy, *arg, **kw)
    
    def PurpleChatGetName(self, arg_chat, *arg, **kw):
        """
        PurpleChatGetName method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleChatGetName( arg_chat, *arg, **kw)
    
    def PurpleFindBuddy(self, arg_account, arg_name, *arg, **kw):
        """
        PurpleFindBuddy method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindBuddy( arg_account, arg_name, *arg, **kw)
    
    def PurpleFindBuddyInGroup(self, arg_account, arg_name, arg_group, *arg, **kw):
        """
        PurpleFindBuddyInGroup method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            group:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindBuddyInGroup( arg_account, arg_name, arg_group, *arg, **kw)
    
    def PurpleFindBuddies(self, arg_account, arg_name, *arg, **kw):
        """
        PurpleFindBuddies method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindBuddies( arg_account, arg_name, *arg, **kw)
    
    def PurpleFindGroup(self, arg_name, *arg, **kw):
        """
        PurpleFindGroup method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindGroup( arg_name, *arg, **kw)
    
    def PurpleBlistFindChat(self, arg_account, arg_name, *arg, **kw):
        """
        PurpleBlistFindChat method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistFindChat( arg_account, arg_name, *arg, **kw)
    
    def PurpleChatGetGroup(self, arg_chat, *arg, **kw):
        """
        PurpleChatGetGroup method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleChatGetGroup( arg_chat, *arg, **kw)
    
    def PurpleChatGetAccount(self, arg_chat, *arg, **kw):
        """
        PurpleChatGetAccount method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleChatGetAccount( arg_chat, *arg, **kw)
    
    def PurpleBuddyGetGroup(self, arg_buddy, *arg, **kw):
        """
        PurpleBuddyGetGroup method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyGetGroup( arg_buddy, *arg, **kw)
    
    def PurpleGroupGetAccounts(self, arg_g, *arg, **kw):
        """
        PurpleGroupGetAccounts method:

        Parameters
        ----------

        g:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleGroupGetAccounts( arg_g, *arg, **kw)
    
    def PurpleGroupOnAccount(self, arg_g, arg_account, *arg, **kw):
        """
        PurpleGroupOnAccount method:

        Parameters
        ----------

        g:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleGroupOnAccount( arg_g, arg_account, *arg, **kw)
    
    def PurpleGroupGetName(self, arg_group, *arg, **kw):
        """
        PurpleGroupGetName method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleGroupGetName( arg_group, *arg, **kw)
    
    def PurpleBlistAddAccount(self, arg_account, *arg, **kw):
        """
        PurpleBlistAddAccount method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistAddAccount( arg_account, *arg, **kw)
    
    def PurpleBlistRemoveAccount(self, arg_account, *arg, **kw):
        """
        PurpleBlistRemoveAccount method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRemoveAccount( arg_account, *arg, **kw)
    
    def PurpleBlistGetGroupSize(self, arg_group, arg_offline, *arg, **kw):
        """
        PurpleBlistGetGroupSize method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            offline:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistGetGroupSize( arg_group, arg_offline, *arg, **kw)
    
    def PurpleBlistGetGroupOnlineCount(self, arg_group, *arg, **kw):
        """
        PurpleBlistGetGroupOnlineCount method:

        Parameters
        ----------

        group:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistGetGroupOnlineCount( arg_group, *arg, **kw)
    
    def PurpleBlistLoad(self, *arg, **kw):
        """
        PurpleBlistLoad method:
        """
        return self._dbus_object.PurpleBlistLoad( *arg, **kw)
    
    def PurpleBlistScheduleSave(self, *arg, **kw):
        """
        PurpleBlistScheduleSave method:
        """
        return self._dbus_object.PurpleBlistScheduleSave( *arg, **kw)
    
    def PurpleBlistRequestAddBuddy(self, arg_account, arg_username, arg_group, arg_alias, *arg, **kw):
        """
        PurpleBlistRequestAddBuddy method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            username:
            type: s,
            direction: in;
            group:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRequestAddBuddy( arg_account, arg_username, arg_group, arg_alias, *arg, **kw)
    
    def PurpleBlistRequestAddChat(self, arg_account, arg_group, arg_alias, arg_name, *arg, **kw):
        """
        PurpleBlistRequestAddChat method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            group:
            type: i,
            direction: in;
            alias:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistRequestAddChat( arg_account, arg_group, arg_alias, arg_name, *arg, **kw)
    
    def PurpleBlistRequestAddGroup(self, *arg, **kw):
        """
        PurpleBlistRequestAddGroup method:
        """
        return self._dbus_object.PurpleBlistRequestAddGroup( *arg, **kw)
    
    def PurpleBlistNodeSetBool(self, arg_node, arg_key, arg_value, *arg, **kw):
        """
        PurpleBlistNodeSetBool method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistNodeSetBool( arg_node, arg_key, arg_value, *arg, **kw)
    
    def PurpleBlistNodeGetBool(self, arg_node, arg_key, *arg, **kw):
        """
        PurpleBlistNodeGetBool method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetBool( arg_node, arg_key, *arg, **kw)
    
    def PurpleBlistNodeSetInt(self, arg_node, arg_key, arg_value, *arg, **kw):
        """
        PurpleBlistNodeSetInt method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistNodeSetInt( arg_node, arg_key, arg_value, *arg, **kw)
    
    def PurpleBlistNodeGetInt(self, arg_node, arg_key, *arg, **kw):
        """
        PurpleBlistNodeGetInt method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetInt( arg_node, arg_key, *arg, **kw)
    
    def PurpleBlistNodeSetString(self, arg_node, arg_key, arg_value, *arg, **kw):
        """
        PurpleBlistNodeSetString method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistNodeSetString( arg_node, arg_key, arg_value, *arg, **kw)
    
    def PurpleBlistNodeGetString(self, arg_node, arg_key, *arg, **kw):
        """
        PurpleBlistNodeGetString method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetString( arg_node, arg_key, *arg, **kw)
    
    def PurpleBlistNodeRemoveSetting(self, arg_node, arg_key, *arg, **kw):
        """
        PurpleBlistNodeRemoveSetting method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistNodeRemoveSetting( arg_node, arg_key, *arg, **kw)
    
    def PurpleBlistNodeSetFlags(self, arg_node, arg_flags, *arg, **kw):
        """
        PurpleBlistNodeSetFlags method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            flags:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistNodeSetFlags( arg_node, arg_flags, *arg, **kw)
    
    def PurpleBlistNodeGetFlags(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetFlags method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetFlags( arg_node, *arg, **kw)
    
    def PurpleBlistNodeGetType(self, arg_node, *arg, **kw):
        """
        PurpleBlistNodeGetType method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetType( arg_node, *arg, **kw)
    
    def PurpleBlistNodeGetExtendedMenu(self, arg_n, *arg, **kw):
        """
        PurpleBlistNodeGetExtendedMenu method:

        Parameters
        ----------

        n:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistNodeGetExtendedMenu( arg_n, *arg, **kw)
    
    def PurpleBlistSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleBlistSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBlistSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleBlistGetUiOps(self, *arg, **kw):
        """
        PurpleBlistGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBlistGetUiOps( *arg, **kw)
    
    def PurpleBlistInit(self, *arg, **kw):
        """
        PurpleBlistInit method:
        """
        return self._dbus_object.PurpleBlistInit( *arg, **kw)
    
    def PurpleBlistUninit(self, *arg, **kw):
        """
        PurpleBlistUninit method:
        """
        return self._dbus_object.PurpleBlistUninit( *arg, **kw)
    
    def PurpleBuddyIconNew(self, arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw):
        """
        PurpleBuddyIconNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            username:
            type: s,
            direction: in;
            icon_data:
            type: i,
            direction: in;
            icon_len:
            type: i,
            direction: in;
            checksum:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconNew( arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw)
    
    def PurpleBuddyIconRef(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconRef method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconRef( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconUnref(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconUnref method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconUnref( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconUpdate(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconUpdate method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconUpdate( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconSetData(self, arg_icon, arg_data, arg_len, arg_checksum, *arg, **kw):
        """
        PurpleBuddyIconSetData method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            data:
            type: i,
            direction: in;
            len:
            type: i,
            direction: in;
            checksum:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconSetData( arg_icon, arg_data, arg_len, arg_checksum, *arg, **kw)
    
    def PurpleBuddyIconGetAccount(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetAccount method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetAccount( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconGetUsername(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetUsername method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetUsername( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconGetChecksum(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetChecksum method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetChecksum( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconGetData(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetData method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: ay,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetData( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconGetExtension(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetExtension method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetExtension( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconGetFullPath(self, arg_icon, *arg, **kw):
        """
        PurpleBuddyIconGetFullPath method:

        Parameters
        ----------

        icon:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconGetFullPath( arg_icon, *arg, **kw)
    
    def PurpleBuddyIconsSetForUser(self, arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw):
        """
        PurpleBuddyIconsSetForUser method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            username:
            type: s,
            direction: in;
            icon_data:
            type: i,
            direction: in;
            icon_len:
            type: i,
            direction: in;
            checksum:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconsSetForUser( arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw)
    
    def PurpleBuddyIconsFind(self, arg_account, arg_username, *arg, **kw):
        """
        PurpleBuddyIconsFind method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            username:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsFind( arg_account, arg_username, *arg, **kw)
    
    def PurpleBuddyIconsFindAccountIcon(self, arg_account, *arg, **kw):
        """
        PurpleBuddyIconsFindAccountIcon method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsFindAccountIcon( arg_account, *arg, **kw)
    
    def PurpleBuddyIconsSetAccountIcon(self, arg_account, arg_icon_data, arg_icon_len, *arg, **kw):
        """
        PurpleBuddyIconsSetAccountIcon method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            icon_data:
            type: i,
            direction: in;
            icon_len:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsSetAccountIcon( arg_account, arg_icon_data, arg_icon_len, *arg, **kw)
    
    def PurpleBuddyIconsGetAccountIconTimestamp(self, arg_account, *arg, **kw):
        """
        PurpleBuddyIconsGetAccountIconTimestamp method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsGetAccountIconTimestamp( arg_account, *arg, **kw)
    
    def PurpleBuddyIconsNodeHasCustomIcon(self, arg_node, *arg, **kw):
        """
        PurpleBuddyIconsNodeHasCustomIcon method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsNodeHasCustomIcon( arg_node, *arg, **kw)
    
    def PurpleBuddyIconsNodeFindCustomIcon(self, arg_node, *arg, **kw):
        """
        PurpleBuddyIconsNodeFindCustomIcon method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsNodeFindCustomIcon( arg_node, *arg, **kw)
    
    def PurpleBuddyIconsNodeSetCustomIcon(self, arg_node, arg_icon_data, arg_icon_len, *arg, **kw):
        """
        PurpleBuddyIconsNodeSetCustomIcon method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            icon_data:
            type: i,
            direction: in;
            icon_len:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsNodeSetCustomIcon( arg_node, arg_icon_data, arg_icon_len, *arg, **kw)
    
    def PurpleBuddyIconsNodeSetCustomIconFromFile(self, arg_node, arg_filename, *arg, **kw):
        """
        PurpleBuddyIconsNodeSetCustomIconFromFile method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            filename:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsNodeSetCustomIconFromFile( arg_node, arg_filename, *arg, **kw)
    
    def PurpleBuddyIconsHasCustomIcon(self, arg_contact, *arg, **kw):
        """
        PurpleBuddyIconsHasCustomIcon method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsHasCustomIcon( arg_contact, *arg, **kw)
    
    def PurpleBuddyIconsFindCustomIcon(self, arg_contact, *arg, **kw):
        """
        PurpleBuddyIconsFindCustomIcon method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsFindCustomIcon( arg_contact, *arg, **kw)
    
    def PurpleBuddyIconsSetCustomIcon(self, arg_contact, arg_icon_data, arg_icon_len, *arg, **kw):
        """
        PurpleBuddyIconsSetCustomIcon method:

        Parameters
        ----------

        contact:
            type: i,
            direction: in;
            icon_data:
            type: i,
            direction: in;
            icon_len:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsSetCustomIcon( arg_contact, arg_icon_data, arg_icon_len, *arg, **kw)
    
    def PurpleBuddyIconsSetCaching(self, arg_caching, *arg, **kw):
        """
        PurpleBuddyIconsSetCaching method:

        Parameters
        ----------

        caching:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconsSetCaching( arg_caching, *arg, **kw)
    
    def PurpleBuddyIconsIsCaching(self, *arg, **kw):
        """
        PurpleBuddyIconsIsCaching method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsIsCaching( *arg, **kw)
    
    def PurpleBuddyIconsSetCacheDir(self, arg_cache_dir, *arg, **kw):
        """
        PurpleBuddyIconsSetCacheDir method:

        Parameters
        ----------

        cache_dir:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconsSetCacheDir( arg_cache_dir, *arg, **kw)
    
    def PurpleBuddyIconsGetCacheDir(self, *arg, **kw):
        """
        PurpleBuddyIconsGetCacheDir method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuddyIconsGetCacheDir( *arg, **kw)
    
    def PurpleBuddyIconsInit(self, *arg, **kw):
        """
        PurpleBuddyIconsInit method:
        """
        return self._dbus_object.PurpleBuddyIconsInit( *arg, **kw)
    
    def PurpleBuddyIconsUninit(self, *arg, **kw):
        """
        PurpleBuddyIconsUninit method:
        """
        return self._dbus_object.PurpleBuddyIconsUninit( *arg, **kw)
    
    def PurpleBuddyIconGetScaleSize(self, arg_spec, arg_width, arg_height, *arg, **kw):
        """
        PurpleBuddyIconGetScaleSize method:

        Parameters
        ----------

        spec:
            type: i,
            direction: in;
            width:
            type: i,
            direction: in;
            height:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleBuddyIconGetScaleSize( arg_spec, arg_width, arg_height, *arg, **kw)
    
    def PurpleConnectionNew(self, arg_account, arg_regist, arg_password, *arg, **kw):
        """
        PurpleConnectionNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            regist:
            type: i,
            direction: in;
            password:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionNew( arg_account, arg_regist, arg_password, *arg, **kw)
    
    def PurpleConnectionDestroy(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionDestroy method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionDestroy( arg_gc, *arg, **kw)
    
    def PurpleConnectionSetState(self, arg_gc, arg_state, *arg, **kw):
        """
        PurpleConnectionSetState method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            state:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionSetState( arg_gc, arg_state, *arg, **kw)
    
    def PurpleConnectionSetAccount(self, arg_gc, arg_account, *arg, **kw):
        """
        PurpleConnectionSetAccount method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionSetAccount( arg_gc, arg_account, *arg, **kw)
    
    def PurpleConnectionSetDisplayName(self, arg_gc, arg_name, *arg, **kw):
        """
        PurpleConnectionSetDisplayName method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionSetDisplayName( arg_gc, arg_name, *arg, **kw)
    
    def PurpleConnectionSetProtocolData(self, arg_connection, arg_proto_data, *arg, **kw):
        """
        PurpleConnectionSetProtocolData method:

        Parameters
        ----------

        connection:
            type: i,
            direction: in;
            proto_data:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionSetProtocolData( arg_connection, arg_proto_data, *arg, **kw)
    
    def PurpleConnectionGetState(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionGetState method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionGetState( arg_gc, *arg, **kw)
    
    def PurpleConnectionGetAccount(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionGetAccount method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionGetAccount( arg_gc, *arg, **kw)
    
    def PurpleConnectionGetPrpl(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionGetPrpl method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionGetPrpl( arg_gc, *arg, **kw)
    
    def PurpleConnectionGetPassword(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionGetPassword method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionGetPassword( arg_gc, *arg, **kw)
    
    def PurpleConnectionGetDisplayName(self, arg_gc, *arg, **kw):
        """
        PurpleConnectionGetDisplayName method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionGetDisplayName( arg_gc, *arg, **kw)
    
    def PurpleConnectionUpdateProgress(self, arg_gc, arg_text, arg_step, arg_count, *arg, **kw):
        """
        PurpleConnectionUpdateProgress method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            text:
            type: s,
            direction: in;
            step:
            type: i,
            direction: in;
            count:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionUpdateProgress( arg_gc, arg_text, arg_step, arg_count, *arg, **kw)
    
    def PurpleConnectionNotice(self, arg_gc, arg_text, *arg, **kw):
        """
        PurpleConnectionNotice method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            text:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionNotice( arg_gc, arg_text, *arg, **kw)
    
    def PurpleConnectionError(self, arg_gc, arg_reason, *arg, **kw):
        """
        PurpleConnectionError method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            reason:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionError( arg_gc, arg_reason, *arg, **kw)
    
    def PurpleConnectionErrorReason(self, arg_gc, arg_reason, arg_description, *arg, **kw):
        """
        PurpleConnectionErrorReason method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            reason:
            type: i,
            direction: in;
            description:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionErrorReason( arg_gc, arg_reason, arg_description, *arg, **kw)
    
    def PurpleConnectionSslError(self, arg_gc, arg_ssl_error, *arg, **kw):
        """
        PurpleConnectionSslError method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            ssl_error:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionSslError( arg_gc, arg_ssl_error, *arg, **kw)
    
    def PurpleConnectionErrorIsFatal(self, arg_reason, *arg, **kw):
        """
        PurpleConnectionErrorIsFatal method:

        Parameters
        ----------

        reason:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionErrorIsFatal( arg_reason, *arg, **kw)
    
    def PurpleConnectionsDisconnectAll(self, *arg, **kw):
        """
        PurpleConnectionsDisconnectAll method:
        """
        return self._dbus_object.PurpleConnectionsDisconnectAll( *arg, **kw)
    
    def PurpleConnectionsGetAll(self, *arg, **kw):
        """
        PurpleConnectionsGetAll method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionsGetAll( *arg, **kw)
    
    def PurpleConnectionsGetConnecting(self, *arg, **kw):
        """
        PurpleConnectionsGetConnecting method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionsGetConnecting( *arg, **kw)
    
    def PurpleConnectionsSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleConnectionsSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConnectionsSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleConnectionsGetUiOps(self, *arg, **kw):
        """
        PurpleConnectionsGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConnectionsGetUiOps( *arg, **kw)
    
    def PurpleConnectionsInit(self, *arg, **kw):
        """
        PurpleConnectionsInit method:
        """
        return self._dbus_object.PurpleConnectionsInit( *arg, **kw)
    
    def PurpleConnectionsUninit(self, *arg, **kw):
        """
        PurpleConnectionsUninit method:
        """
        return self._dbus_object.PurpleConnectionsUninit( *arg, **kw)
    
    def PurpleConversationNew(self, arg_type, arg_account, arg_name, *arg, **kw):
        """
        PurpleConversationNew method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationNew( arg_type, arg_account, arg_name, *arg, **kw)
    
    def PurpleConversationDestroy(self, arg_conv, *arg, **kw):
        """
        PurpleConversationDestroy method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationDestroy( arg_conv, *arg, **kw)
    
    def PurpleConversationPresent(self, arg_conv, *arg, **kw):
        """
        PurpleConversationPresent method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationPresent( arg_conv, *arg, **kw)
    
    def PurpleConversationGetType(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetType method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetType( arg_conv, *arg, **kw)
    
    def PurpleConversationSetUiOps(self, arg_conv, arg_ops, *arg, **kw):
        """
        PurpleConversationSetUiOps method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetUiOps( arg_conv, arg_ops, *arg, **kw)
    
    def PurpleConversationsSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleConversationsSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationsSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleConversationGetUiOps(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetUiOps method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetUiOps( arg_conv, *arg, **kw)
    
    def PurpleConversationSetAccount(self, arg_conv, arg_account, *arg, **kw):
        """
        PurpleConversationSetAccount method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetAccount( arg_conv, arg_account, *arg, **kw)
    
    def PurpleConversationGetAccount(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetAccount method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetAccount( arg_conv, *arg, **kw)
    
    def PurpleConversationGetGc(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetGc method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetGc( arg_conv, *arg, **kw)
    
    def PurpleConversationSetTitle(self, arg_conv, arg_title, *arg, **kw):
        """
        PurpleConversationSetTitle method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            title:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetTitle( arg_conv, arg_title, *arg, **kw)
    
    def PurpleConversationGetTitle(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetTitle method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetTitle( arg_conv, *arg, **kw)
    
    def PurpleConversationAutosetTitle(self, arg_conv, *arg, **kw):
        """
        PurpleConversationAutosetTitle method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationAutosetTitle( arg_conv, *arg, **kw)
    
    def PurpleConversationSetName(self, arg_conv, arg_name, *arg, **kw):
        """
        PurpleConversationSetName method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetName( arg_conv, arg_name, *arg, **kw)
    
    def PurpleConversationGetName(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetName method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetName( arg_conv, *arg, **kw)
    
    def PurpleConvChatCbGetAttribute(self, arg_cb, arg_key, *arg, **kw):
        """
        PurpleConvChatCbGetAttribute method:

        Parameters
        ----------

        cb:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatCbGetAttribute( arg_cb, arg_key, *arg, **kw)
    
    def PurpleConvChatCbGetAttributeKeys(self, arg_cb, *arg, **kw):
        """
        PurpleConvChatCbGetAttributeKeys method:

        Parameters
        ----------

        cb:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatCbGetAttributeKeys( arg_cb, *arg, **kw)
    
    def PurpleConvChatCbSetAttribute(self, arg_chat, arg_cb, arg_key, arg_value, *arg, **kw):
        """
        PurpleConvChatCbSetAttribute method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            cb:
            type: i,
            direction: in;
            key:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatCbSetAttribute( arg_chat, arg_cb, arg_key, arg_value, *arg, **kw)
    
    def PurpleConvChatCbSetAttributes(self, arg_chat, arg_cb, arg_keys, arg_values, *arg, **kw):
        """
        PurpleConvChatCbSetAttributes method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            cb:
            type: i,
            direction: in;
            keys:
            type: i,
            direction: in;
            values:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatCbSetAttributes( arg_chat, arg_cb, arg_keys, arg_values, *arg, **kw)
    
    def PurpleConversationSetLogging(self, arg_conv, arg_log, *arg, **kw):
        """
        PurpleConversationSetLogging method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            log:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetLogging( arg_conv, arg_log, *arg, **kw)
    
    def PurpleConversationIsLogging(self, arg_conv, *arg, **kw):
        """
        PurpleConversationIsLogging method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationIsLogging( arg_conv, *arg, **kw)
    
    def PurpleConversationGetImData(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetImData method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetImData( arg_conv, *arg, **kw)
    
    def PurpleConversationGetChatData(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetChatData method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetChatData( arg_conv, *arg, **kw)
    
    def PurpleGetConversations(self, *arg, **kw):
        """
        PurpleGetConversations method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetConversations( *arg, **kw)
    
    def PurpleGetIms(self, *arg, **kw):
        """
        PurpleGetIms method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetIms( *arg, **kw)
    
    def PurpleGetChats(self, *arg, **kw):
        """
        PurpleGetChats method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetChats( *arg, **kw)
    
    def PurpleFindConversationWithAccount(self, arg_type, arg_name, arg_account, *arg, **kw):
        """
        PurpleFindConversationWithAccount method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindConversationWithAccount( arg_type, arg_name, arg_account, *arg, **kw)
    
    def PurpleConversationWrite(self, arg_conv, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
        """
        PurpleConversationWrite method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            mtime:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationWrite( arg_conv, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw)
    
    def PurpleConversationSetFeatures(self, arg_conv, arg_features, *arg, **kw):
        """
        PurpleConversationSetFeatures method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            features:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationSetFeatures( arg_conv, arg_features, *arg, **kw)
    
    def PurpleConversationGetFeatures(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetFeatures method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetFeatures( arg_conv, *arg, **kw)
    
    def PurpleConversationHasFocus(self, arg_conv, *arg, **kw):
        """
        PurpleConversationHasFocus method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationHasFocus( arg_conv, *arg, **kw)
    
    def PurpleConversationUpdate(self, arg_conv, arg_type, *arg, **kw):
        """
        PurpleConversationUpdate method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationUpdate( arg_conv, arg_type, *arg, **kw)
    
    def PurpleConversationGetMessageHistory(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetMessageHistory method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetMessageHistory( arg_conv, *arg, **kw)
    
    def PurpleConversationClearMessageHistory(self, arg_conv, *arg, **kw):
        """
        PurpleConversationClearMessageHistory method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConversationClearMessageHistory( arg_conv, *arg, **kw)
    
    def PurpleConversationMessageGetSender(self, arg_msg, *arg, **kw):
        """
        PurpleConversationMessageGetSender method:

        Parameters
        ----------

        msg:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationMessageGetSender( arg_msg, *arg, **kw)
    
    def PurpleConversationMessageGetMessage(self, arg_msg, *arg, **kw):
        """
        PurpleConversationMessageGetMessage method:

        Parameters
        ----------

        msg:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationMessageGetMessage( arg_msg, *arg, **kw)
    
    def PurpleConversationMessageGetFlags(self, arg_msg, *arg, **kw):
        """
        PurpleConversationMessageGetFlags method:

        Parameters
        ----------

        msg:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationMessageGetFlags( arg_msg, *arg, **kw)
    
    def PurpleConversationMessageGetTimestamp(self, arg_msg, *arg, **kw):
        """
        PurpleConversationMessageGetTimestamp method:

        Parameters
        ----------

        msg:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationMessageGetTimestamp( arg_msg, *arg, **kw)
    
    def PurpleConvImGetConversation(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetConversation method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetConversation( arg_im, *arg, **kw)
    
    def PurpleConvImSetIcon(self, arg_im, arg_icon, *arg, **kw):
        """
        PurpleConvImSetIcon method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            icon:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImSetIcon( arg_im, arg_icon, *arg, **kw)
    
    def PurpleConvImGetIcon(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetIcon method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetIcon( arg_im, *arg, **kw)
    
    def PurpleConvImSetTypingState(self, arg_im, arg_state, *arg, **kw):
        """
        PurpleConvImSetTypingState method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            state:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImSetTypingState( arg_im, arg_state, *arg, **kw)
    
    def PurpleConvImGetTypingState(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetTypingState method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetTypingState( arg_im, *arg, **kw)
    
    def PurpleConvImStartTypingTimeout(self, arg_im, arg_timeout, *arg, **kw):
        """
        PurpleConvImStartTypingTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            timeout:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImStartTypingTimeout( arg_im, arg_timeout, *arg, **kw)
    
    def PurpleConvImStopTypingTimeout(self, arg_im, *arg, **kw):
        """
        PurpleConvImStopTypingTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImStopTypingTimeout( arg_im, *arg, **kw)
    
    def PurpleConvImGetTypingTimeout(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetTypingTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetTypingTimeout( arg_im, *arg, **kw)
    
    def PurpleConvImSetTypeAgain(self, arg_im, arg_val, *arg, **kw):
        """
        PurpleConvImSetTypeAgain method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            val:
            type: u,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImSetTypeAgain( arg_im, arg_val, *arg, **kw)
    
    def PurpleConvImGetTypeAgain(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetTypeAgain method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetTypeAgain( arg_im, *arg, **kw)
    
    def PurpleConvImStartSendTypedTimeout(self, arg_im, *arg, **kw):
        """
        PurpleConvImStartSendTypedTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImStartSendTypedTimeout( arg_im, *arg, **kw)
    
    def PurpleConvImStopSendTypedTimeout(self, arg_im, *arg, **kw):
        """
        PurpleConvImStopSendTypedTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImStopSendTypedTimeout( arg_im, *arg, **kw)
    
    def PurpleConvImGetSendTypedTimeout(self, arg_im, *arg, **kw):
        """
        PurpleConvImGetSendTypedTimeout method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvImGetSendTypedTimeout( arg_im, *arg, **kw)
    
    def PurpleConvImUpdateTyping(self, arg_im, *arg, **kw):
        """
        PurpleConvImUpdateTyping method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImUpdateTyping( arg_im, *arg, **kw)
    
    def PurpleConvImWrite(self, arg_im, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
        """
        PurpleConvImWrite method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            mtime:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImWrite( arg_im, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw)
    
    def PurpleConvPresentError(self, arg_who, arg_account, arg_what, *arg, **kw):
        """
        PurpleConvPresentError method:

        Parameters
        ----------

        who:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            what:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvPresentError( arg_who, arg_account, arg_what, *arg, **kw)
    
    def PurpleConvImSend(self, arg_im, arg_message, *arg, **kw):
        """
        PurpleConvImSend method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImSend( arg_im, arg_message, *arg, **kw)
    
    def PurpleConvSendConfirm(self, arg_conv, arg_message, *arg, **kw):
        """
        PurpleConvSendConfirm method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvSendConfirm( arg_conv, arg_message, *arg, **kw)
    
    def PurpleConvImSendWithFlags(self, arg_im, arg_message, arg_flags, *arg, **kw):
        """
        PurpleConvImSendWithFlags method:

        Parameters
        ----------

        im:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvImSendWithFlags( arg_im, arg_message, arg_flags, *arg, **kw)
    
    def PurpleConvCustomSmileyAdd(self, arg_conv, arg_smile, arg_cksum_type, arg_chksum, arg_remote, *arg, **kw):
        """
        PurpleConvCustomSmileyAdd method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            smile:
            type: s,
            direction: in;
            cksum_type:
            type: s,
            direction: in;
            chksum:
            type: s,
            direction: in;
            remote:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvCustomSmileyAdd( arg_conv, arg_smile, arg_cksum_type, arg_chksum, arg_remote, *arg, **kw)
    
    def PurpleConvCustomSmileyClose(self, arg_conv, arg_smile, *arg, **kw):
        """
        PurpleConvCustomSmileyClose method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            smile:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvCustomSmileyClose( arg_conv, arg_smile, *arg, **kw)
    
    def PurpleConvChatGetConversation(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetConversation method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetConversation( arg_chat, *arg, **kw)
    
    def PurpleConvChatSetUsers(self, arg_chat, arg_users, *arg, **kw):
        """
        PurpleConvChatSetUsers method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            users:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatSetUsers( arg_chat, arg_users, *arg, **kw)
    
    def PurpleConvChatGetUsers(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetUsers method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetUsers( arg_chat, *arg, **kw)
    
    def PurpleConvChatIgnore(self, arg_chat, arg_name, *arg, **kw):
        """
        PurpleConvChatIgnore method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatIgnore( arg_chat, arg_name, *arg, **kw)
    
    def PurpleConvChatUnignore(self, arg_chat, arg_name, *arg, **kw):
        """
        PurpleConvChatUnignore method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatUnignore( arg_chat, arg_name, *arg, **kw)
    
    def PurpleConvChatSetIgnored(self, arg_chat, arg_ignored, *arg, **kw):
        """
        PurpleConvChatSetIgnored method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            ignored:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatSetIgnored( arg_chat, arg_ignored, *arg, **kw)
    
    def PurpleConvChatGetIgnored(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetIgnored method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetIgnored( arg_chat, *arg, **kw)
    
    def PurpleConvChatGetIgnoredUser(self, arg_chat, arg_user, *arg, **kw):
        """
        PurpleConvChatGetIgnoredUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetIgnoredUser( arg_chat, arg_user, *arg, **kw)
    
    def PurpleConvChatIsUserIgnored(self, arg_chat, arg_user, *arg, **kw):
        """
        PurpleConvChatIsUserIgnored method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatIsUserIgnored( arg_chat, arg_user, *arg, **kw)
    
    def PurpleConvChatSetTopic(self, arg_chat, arg_who, arg_topic, *arg, **kw):
        """
        PurpleConvChatSetTopic method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            topic:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatSetTopic( arg_chat, arg_who, arg_topic, *arg, **kw)
    
    def PurpleConvChatGetTopic(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetTopic method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetTopic( arg_chat, *arg, **kw)
    
    def PurpleConvChatSetId(self, arg_chat, arg_id, *arg, **kw):
        """
        PurpleConvChatSetId method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatSetId( arg_chat, arg_id, *arg, **kw)
    
    def PurpleConvChatGetId(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetId method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetId( arg_chat, *arg, **kw)
    
    def PurpleConvChatWrite(self, arg_chat, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
        """
        PurpleConvChatWrite method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            mtime:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatWrite( arg_chat, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw)
    
    def PurpleConvChatSend(self, arg_chat, arg_message, *arg, **kw):
        """
        PurpleConvChatSend method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatSend( arg_chat, arg_message, *arg, **kw)
    
    def PurpleConvChatSendWithFlags(self, arg_chat, arg_message, arg_flags, *arg, **kw):
        """
        PurpleConvChatSendWithFlags method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatSendWithFlags( arg_chat, arg_message, arg_flags, *arg, **kw)
    
    def PurpleConvChatAddUser(self, arg_chat, arg_user, arg_extra_msg, arg_flags, arg_new_arrival, *arg, **kw):
        """
        PurpleConvChatAddUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            extra_msg:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            new_arrival:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatAddUser( arg_chat, arg_user, arg_extra_msg, arg_flags, arg_new_arrival, *arg, **kw)
    
    def PurpleConvChatAddUsers(self, arg_chat, arg_users, arg_extra_msgs, arg_flags, arg_new_arrivals, *arg, **kw):
        """
        PurpleConvChatAddUsers method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            users:
            type: i,
            direction: in;
            extra_msgs:
            type: i,
            direction: in;
            flags:
            type: i,
            direction: in;
            new_arrivals:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatAddUsers( arg_chat, arg_users, arg_extra_msgs, arg_flags, arg_new_arrivals, *arg, **kw)
    
    def PurpleConvChatRenameUser(self, arg_chat, arg_old_user, arg_new_user, *arg, **kw):
        """
        PurpleConvChatRenameUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            old_user:
            type: s,
            direction: in;
            new_user:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatRenameUser( arg_chat, arg_old_user, arg_new_user, *arg, **kw)
    
    def PurpleConvChatRemoveUser(self, arg_chat, arg_user, arg_reason, *arg, **kw):
        """
        PurpleConvChatRemoveUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            reason:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatRemoveUser( arg_chat, arg_user, arg_reason, *arg, **kw)
    
    def PurpleConvChatRemoveUsers(self, arg_chat, arg_users, arg_reason, *arg, **kw):
        """
        PurpleConvChatRemoveUsers method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            users:
            type: i,
            direction: in;
            reason:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatRemoveUsers( arg_chat, arg_users, arg_reason, *arg, **kw)
    
    def PurpleConvChatFindUser(self, arg_chat, arg_user, *arg, **kw):
        """
        PurpleConvChatFindUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatFindUser( arg_chat, arg_user, *arg, **kw)
    
    def PurpleConvChatUserSetFlags(self, arg_chat, arg_user, arg_flags, *arg, **kw):
        """
        PurpleConvChatUserSetFlags method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatUserSetFlags( arg_chat, arg_user, arg_flags, *arg, **kw)
    
    def PurpleConvChatUserGetFlags(self, arg_chat, arg_user, *arg, **kw):
        """
        PurpleConvChatUserGetFlags method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatUserGetFlags( arg_chat, arg_user, *arg, **kw)
    
    def PurpleConvChatClearUsers(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatClearUsers method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatClearUsers( arg_chat, *arg, **kw)
    
    def PurpleConvChatSetNick(self, arg_chat, arg_nick, *arg, **kw):
        """
        PurpleConvChatSetNick method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            nick:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatSetNick( arg_chat, arg_nick, *arg, **kw)
    
    def PurpleConvChatGetNick(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatGetNick method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatGetNick( arg_chat, *arg, **kw)
    
    def PurpleFindChat(self, arg_gc, arg_id, *arg, **kw):
        """
        PurpleFindChat method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindChat( arg_gc, arg_id, *arg, **kw)
    
    def PurpleConvChatLeft(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatLeft method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatLeft( arg_chat, *arg, **kw)
    
    def PurpleConvChatInviteUser(self, arg_chat, arg_user, arg_message, arg_confirm, *arg, **kw):
        """
        PurpleConvChatInviteUser method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            user:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            confirm:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatInviteUser( arg_chat, arg_user, arg_message, arg_confirm, *arg, **kw)
    
    def PurpleConvChatHasLeft(self, arg_chat, *arg, **kw):
        """
        PurpleConvChatHasLeft method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatHasLeft( arg_chat, *arg, **kw)
    
    def PurpleConvChatCbNew(self, arg_name, arg_alias, arg_flags, *arg, **kw):
        """
        PurpleConvChatCbNew method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatCbNew( arg_name, arg_alias, arg_flags, *arg, **kw)
    
    def PurpleConvChatCbFind(self, arg_chat, arg_name, *arg, **kw):
        """
        PurpleConvChatCbFind method:

        Parameters
        ----------

        chat:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatCbFind( arg_chat, arg_name, *arg, **kw)
    
    def PurpleConvChatCbGetName(self, arg_cb, *arg, **kw):
        """
        PurpleConvChatCbGetName method:

        Parameters
        ----------

        cb:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleConvChatCbGetName( arg_cb, *arg, **kw)
    
    def PurpleConvChatCbDestroy(self, arg_cb, *arg, **kw):
        """
        PurpleConvChatCbDestroy method:

        Parameters
        ----------

        cb:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleConvChatCbDestroy( arg_cb, *arg, **kw)
    
    def PurpleConversationGetExtendedMenu(self, arg_conv, *arg, **kw):
        """
        PurpleConversationGetExtendedMenu method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleConversationGetExtendedMenu( arg_conv, *arg, **kw)
    
    def PurpleConversationsInit(self, *arg, **kw):
        """
        PurpleConversationsInit method:
        """
        return self._dbus_object.PurpleConversationsInit( *arg, **kw)
    
    def PurpleConversationsUninit(self, *arg, **kw):
        """
        PurpleConversationsUninit method:
        """
        return self._dbus_object.PurpleConversationsUninit( *arg, **kw)
    
    def PurpleCoreInit(self, arg_ui, *arg, **kw):
        """
        PurpleCoreInit method:

        Parameters
        ----------

        ui:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreInit( arg_ui, *arg, **kw)
    
    def PurpleCoreQuit(self, *arg, **kw):
        """
        PurpleCoreQuit method:
        """
        return self._dbus_object.PurpleCoreQuit( *arg, **kw)
    
    def PurpleCoreGetVersion(self, *arg, **kw):
        """
        PurpleCoreGetVersion method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreGetVersion( *arg, **kw)
    
    def PurpleCoreGetUi(self, *arg, **kw):
        """
        PurpleCoreGetUi method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreGetUi( *arg, **kw)
    
    def PurpleGetCore(self, *arg, **kw):
        """
        PurpleGetCore method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetCore( *arg, **kw)
    
    def PurpleCoreSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleCoreSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleCoreSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleCoreGetUiOps(self, *arg, **kw):
        """
        PurpleCoreGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreGetUiOps( *arg, **kw)
    
    def PurpleCoreMigrate(self, *arg, **kw):
        """
        PurpleCoreMigrate method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreMigrate( *arg, **kw)
    
    def PurpleCoreEnsureSingleInstance(self, *arg, **kw):
        """
        PurpleCoreEnsureSingleInstance method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleCoreEnsureSingleInstance( *arg, **kw)
    
    def PurpleXferNew(self, arg_account, arg_type, arg_who, *arg, **kw):
        """
        PurpleXferNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferNew( arg_account, arg_type, arg_who, *arg, **kw)
    
    def PurpleXfersGetAll(self, *arg, **kw):
        """
        PurpleXfersGetAll method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleXfersGetAll( *arg, **kw)
    
    def PurpleXferRef(self, arg_xfer, *arg, **kw):
        """
        PurpleXferRef method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferRef( arg_xfer, *arg, **kw)
    
    def PurpleXferUnref(self, arg_xfer, *arg, **kw):
        """
        PurpleXferUnref method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferUnref( arg_xfer, *arg, **kw)
    
    def PurpleXferRequest(self, arg_xfer, *arg, **kw):
        """
        PurpleXferRequest method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferRequest( arg_xfer, *arg, **kw)
    
    def PurpleXferRequestAccepted(self, arg_xfer, arg_filename, *arg, **kw):
        """
        PurpleXferRequestAccepted method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            filename:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferRequestAccepted( arg_xfer, arg_filename, *arg, **kw)
    
    def PurpleXferRequestDenied(self, arg_xfer, *arg, **kw):
        """
        PurpleXferRequestDenied method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferRequestDenied( arg_xfer, *arg, **kw)
    
    def PurpleXferGetType(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetType method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetType( arg_xfer, *arg, **kw)
    
    def PurpleXferGetAccount(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetAccount method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetAccount( arg_xfer, *arg, **kw)
    
    def PurpleXferGetRemoteUser(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetRemoteUser method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetRemoteUser( arg_xfer, *arg, **kw)
    
    def PurpleXferGetStatus(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetStatus method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetStatus( arg_xfer, *arg, **kw)
    
    def PurpleXferIsCanceled(self, arg_xfer, *arg, **kw):
        """
        PurpleXferIsCanceled method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferIsCanceled( arg_xfer, *arg, **kw)
    
    def PurpleXferIsCompleted(self, arg_xfer, *arg, **kw):
        """
        PurpleXferIsCompleted method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferIsCompleted( arg_xfer, *arg, **kw)
    
    def PurpleXferGetFilename(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetFilename method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetFilename( arg_xfer, *arg, **kw)
    
    def PurpleXferGetLocalFilename(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetLocalFilename method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetLocalFilename( arg_xfer, *arg, **kw)
    
    def PurpleXferGetBytesSent(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetBytesSent method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetBytesSent( arg_xfer, *arg, **kw)
    
    def PurpleXferGetBytesRemaining(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetBytesRemaining method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetBytesRemaining( arg_xfer, *arg, **kw)
    
    def PurpleXferGetSize(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetSize method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetSize( arg_xfer, *arg, **kw)
    
    def PurpleXferGetLocalPort(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetLocalPort method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: u,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetLocalPort( arg_xfer, *arg, **kw)
    
    def PurpleXferGetRemoteIp(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetRemoteIp method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetRemoteIp( arg_xfer, *arg, **kw)
    
    def PurpleXferGetRemotePort(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetRemotePort method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: u,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetRemotePort( arg_xfer, *arg, **kw)
    
    def PurpleXferGetStartTime(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetStartTime method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetStartTime( arg_xfer, *arg, **kw)
    
    def PurpleXferGetEndTime(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetEndTime method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetEndTime( arg_xfer, *arg, **kw)
    
    def PurpleXferSetCompleted(self, arg_xfer, arg_completed, *arg, **kw):
        """
        PurpleXferSetCompleted method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            completed:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetCompleted( arg_xfer, arg_completed, *arg, **kw)
    
    def PurpleXferSetMessage(self, arg_xfer, arg_message, *arg, **kw):
        """
        PurpleXferSetMessage method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetMessage( arg_xfer, arg_message, *arg, **kw)
    
    def PurpleXferSetFilename(self, arg_xfer, arg_filename, *arg, **kw):
        """
        PurpleXferSetFilename method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            filename:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetFilename( arg_xfer, arg_filename, *arg, **kw)
    
    def PurpleXferSetLocalFilename(self, arg_xfer, arg_filename, *arg, **kw):
        """
        PurpleXferSetLocalFilename method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            filename:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetLocalFilename( arg_xfer, arg_filename, *arg, **kw)
    
    def PurpleXferSetSize(self, arg_xfer, arg_size, *arg, **kw):
        """
        PurpleXferSetSize method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            size:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetSize( arg_xfer, arg_size, *arg, **kw)
    
    def PurpleXferSetBytesSent(self, arg_xfer, arg_bytes_sent, *arg, **kw):
        """
        PurpleXferSetBytesSent method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            bytes_sent:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferSetBytesSent( arg_xfer, arg_bytes_sent, *arg, **kw)
    
    def PurpleXferGetUiOps(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetUiOps method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetUiOps( arg_xfer, *arg, **kw)
    
    def PurpleXferStart(self, arg_xfer, arg_fd, arg_ip, arg_port, *arg, **kw):
        """
        PurpleXferStart method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            fd:
            type: i,
            direction: in;
            ip:
            type: s,
            direction: in;
            port:
            type: u,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferStart( arg_xfer, arg_fd, arg_ip, arg_port, *arg, **kw)
    
    def PurpleXferEnd(self, arg_xfer, *arg, **kw):
        """
        PurpleXferEnd method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferEnd( arg_xfer, *arg, **kw)
    
    def PurpleXferAdd(self, arg_xfer, *arg, **kw):
        """
        PurpleXferAdd method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferAdd( arg_xfer, *arg, **kw)
    
    def PurpleXferCancelLocal(self, arg_xfer, *arg, **kw):
        """
        PurpleXferCancelLocal method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferCancelLocal( arg_xfer, *arg, **kw)
    
    def PurpleXferCancelRemote(self, arg_xfer, *arg, **kw):
        """
        PurpleXferCancelRemote method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferCancelRemote( arg_xfer, *arg, **kw)
    
    def PurpleXferError(self, arg_type, arg_account, arg_who, arg_msg, *arg, **kw):
        """
        PurpleXferError method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            msg:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferError( arg_type, arg_account, arg_who, arg_msg, *arg, **kw)
    
    def PurpleXferUpdateProgress(self, arg_xfer, *arg, **kw):
        """
        PurpleXferUpdateProgress method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferUpdateProgress( arg_xfer, *arg, **kw)
    
    def PurpleXferGetThumbnail(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetThumbnail method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: ay,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetThumbnail( arg_xfer, *arg, **kw)
    
    def PurpleXferGetThumbnailMimetype(self, arg_xfer, *arg, **kw):
        """
        PurpleXferGetThumbnailMimetype method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleXferGetThumbnailMimetype( arg_xfer, *arg, **kw)
    
    def PurpleXferPrepareThumbnail(self, arg_xfer, arg_formats, *arg, **kw):
        """
        PurpleXferPrepareThumbnail method:

        Parameters
        ----------

        xfer:
            type: i,
            direction: in;
            formats:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleXferPrepareThumbnail( arg_xfer, arg_formats, *arg, **kw)
    
    def PurpleXfersInit(self, *arg, **kw):
        """
        PurpleXfersInit method:
        """
        return self._dbus_object.PurpleXfersInit( *arg, **kw)
    
    def PurpleXfersUninit(self, *arg, **kw):
        """
        PurpleXfersUninit method:
        """
        return self._dbus_object.PurpleXfersUninit( *arg, **kw)
    
    def PurpleXfersSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleXfersSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleXfersSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleXfersGetUiOps(self, *arg, **kw):
        """
        PurpleXfersGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleXfersGetUiOps( *arg, **kw)
    
    def PurpleLogFree(self, arg_log, *arg, **kw):
        """
        PurpleLogFree method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogFree( arg_log, *arg, **kw)
    
    def PurpleLogWrite(self, arg_log, arg_type, arg_from, arg_time, arg_message, *arg, **kw):
        """
        PurpleLogWrite method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            from:
            type: s,
            direction: in;
            time:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogWrite( arg_log, arg_type, arg_from, arg_time, arg_message, *arg, **kw)
    
    def PurpleLogGetLogs(self, arg_type, arg_name, arg_account, *arg, **kw):
        """
        PurpleLogGetLogs method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetLogs( arg_type, arg_name, arg_account, *arg, **kw)
    
    def PurpleLogGetSystemLogs(self, arg_account, *arg, **kw):
        """
        PurpleLogGetSystemLogs method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetSystemLogs( arg_account, *arg, **kw)
    
    def PurpleLogGetSize(self, arg_log, *arg, **kw):
        """
        PurpleLogGetSize method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetSize( arg_log, *arg, **kw)
    
    def PurpleLogGetTotalSize(self, arg_type, arg_name, arg_account, *arg, **kw):
        """
        PurpleLogGetTotalSize method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetTotalSize( arg_type, arg_name, arg_account, *arg, **kw)
    
    def PurpleLogGetActivityScore(self, arg_type, arg_name, arg_account, *arg, **kw):
        """
        PurpleLogGetActivityScore method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetActivityScore( arg_type, arg_name, arg_account, *arg, **kw)
    
    def PurpleLogIsDeletable(self, arg_log, *arg, **kw):
        """
        PurpleLogIsDeletable method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogIsDeletable( arg_log, *arg, **kw)
    
    def PurpleLogDelete(self, arg_log, *arg, **kw):
        """
        PurpleLogDelete method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogDelete( arg_log, *arg, **kw)
    
    def PurpleLogGetLogDir(self, arg_type, arg_name, arg_account, *arg, **kw):
        """
        PurpleLogGetLogDir method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogGetLogDir( arg_type, arg_name, arg_account, *arg, **kw)
    
    def PurpleLogSetFree(self, arg_set, *arg, **kw):
        """
        PurpleLogSetFree method:

        Parameters
        ----------

        set:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogSetFree( arg_set, *arg, **kw)
    
    def PurpleLogCommonWriter(self, arg_log, arg_ext, *arg, **kw):
        """
        PurpleLogCommonWriter method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            ext:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogCommonWriter( arg_log, arg_ext, *arg, **kw)
    
    def PurpleLogCommonLister(self, arg_type, arg_name, arg_account, arg_ext, arg_logger, *arg, **kw):
        """
        PurpleLogCommonLister method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            ext:
            type: s,
            direction: in;
            logger:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogCommonLister( arg_type, arg_name, arg_account, arg_ext, arg_logger, *arg, **kw)
    
    def PurpleLogCommonTotalSizer(self, arg_type, arg_name, arg_account, arg_ext, *arg, **kw):
        """
        PurpleLogCommonTotalSizer method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            account:
            type: i,
            direction: in;
            ext:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogCommonTotalSizer( arg_type, arg_name, arg_account, arg_ext, *arg, **kw)
    
    def PurpleLogCommonSizer(self, arg_log, *arg, **kw):
        """
        PurpleLogCommonSizer method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogCommonSizer( arg_log, *arg, **kw)
    
    def PurpleLogCommonDeleter(self, arg_log, *arg, **kw):
        """
        PurpleLogCommonDeleter method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogCommonDeleter( arg_log, *arg, **kw)
    
    def PurpleLogCommonIsDeletable(self, arg_log, *arg, **kw):
        """
        PurpleLogCommonIsDeletable method:

        Parameters
        ----------

        log:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogCommonIsDeletable( arg_log, *arg, **kw)
    
    def PurpleLogLoggerFree(self, arg_logger, *arg, **kw):
        """
        PurpleLogLoggerFree method:

        Parameters
        ----------

        logger:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogLoggerFree( arg_logger, *arg, **kw)
    
    def PurpleLogLoggerAdd(self, arg_logger, *arg, **kw):
        """
        PurpleLogLoggerAdd method:

        Parameters
        ----------

        logger:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogLoggerAdd( arg_logger, *arg, **kw)
    
    def PurpleLogLoggerRemove(self, arg_logger, *arg, **kw):
        """
        PurpleLogLoggerRemove method:

        Parameters
        ----------

        logger:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogLoggerRemove( arg_logger, *arg, **kw)
    
    def PurpleLogLoggerSet(self, arg_logger, *arg, **kw):
        """
        PurpleLogLoggerSet method:

        Parameters
        ----------

        logger:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleLogLoggerSet( arg_logger, *arg, **kw)
    
    def PurpleLogLoggerGet(self, *arg, **kw):
        """
        PurpleLogLoggerGet method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogLoggerGet( *arg, **kw)
    
    def PurpleLogLoggerGetOptions(self, *arg, **kw):
        """
        PurpleLogLoggerGetOptions method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleLogLoggerGetOptions( *arg, **kw)
    
    def PurpleLogInit(self, *arg, **kw):
        """
        PurpleLogInit method:
        """
        return self._dbus_object.PurpleLogInit( *arg, **kw)
    
    def PurpleLogUninit(self, *arg, **kw):
        """
        PurpleLogUninit method:
        """
        return self._dbus_object.PurpleLogUninit( *arg, **kw)
    
    def PurpleNotifySearchresultsFree(self, arg_results, *arg, **kw):
        """
        PurpleNotifySearchresultsFree method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsFree( arg_results, *arg, **kw)
    
    def PurpleNotifySearchresultsNewRows(self, arg_gc, arg_results, arg_data, *arg, **kw):
        """
        PurpleNotifySearchresultsNewRows method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            results:
            type: i,
            direction: in;
            data:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsNewRows( arg_gc, arg_results, arg_data, *arg, **kw)
    
    def PurpleNotifySearchresultsNew(self, *arg, **kw):
        """
        PurpleNotifySearchresultsNew method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsNew( *arg, **kw)
    
    def PurpleNotifySearchresultsColumnNew(self, arg_title, *arg, **kw):
        """
        PurpleNotifySearchresultsColumnNew method:

        Parameters
        ----------

        title:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsColumnNew( arg_title, *arg, **kw)
    
    def PurpleNotifySearchresultsColumnAdd(self, arg_results, arg_column, *arg, **kw):
        """
        PurpleNotifySearchresultsColumnAdd method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            column:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsColumnAdd( arg_results, arg_column, *arg, **kw)
    
    def PurpleNotifySearchresultsRowAdd(self, arg_results, arg_row, *arg, **kw):
        """
        PurpleNotifySearchresultsRowAdd method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            row:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsRowAdd( arg_results, arg_row, *arg, **kw)
    
    def PurpleNotifySearchresultsGetRowsCount(self, arg_results, *arg, **kw):
        """
        PurpleNotifySearchresultsGetRowsCount method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsGetRowsCount( arg_results, *arg, **kw)
    
    def PurpleNotifySearchresultsGetColumnsCount(self, arg_results, *arg, **kw):
        """
        PurpleNotifySearchresultsGetColumnsCount method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsGetColumnsCount( arg_results, *arg, **kw)
    
    def PurpleNotifySearchresultsRowGet(self, arg_results, arg_row_id, *arg, **kw):
        """
        PurpleNotifySearchresultsRowGet method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            row_id:
            type: u,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsRowGet( arg_results, arg_row_id, *arg, **kw)
    
    def PurpleNotifySearchresultsColumnGetTitle(self, arg_results, arg_column_id, *arg, **kw):
        """
        PurpleNotifySearchresultsColumnGetTitle method:

        Parameters
        ----------

        results:
            type: i,
            direction: in;
            column_id:
            type: u,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifySearchresultsColumnGetTitle( arg_results, arg_column_id, *arg, **kw)
    
    def PurpleNotifyUserInfoNew(self, *arg, **kw):
        """
        PurpleNotifyUserInfoNew method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoNew( *arg, **kw)
    
    def PurpleNotifyUserInfoDestroy(self, arg_user_info, *arg, **kw):
        """
        PurpleNotifyUserInfoDestroy method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoDestroy( arg_user_info, *arg, **kw)
    
    def PurpleNotifyUserInfoGetEntries(self, arg_user_info, *arg, **kw):
        """
        PurpleNotifyUserInfoGetEntries method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoGetEntries( arg_user_info, *arg, **kw)
    
    def PurpleNotifyUserInfoGetTextWithNewline(self, arg_user_info, arg_newline, *arg, **kw):
        """
        PurpleNotifyUserInfoGetTextWithNewline method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            newline:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoGetTextWithNewline( arg_user_info, arg_newline, *arg, **kw)
    
    def PurpleNotifyUserInfoAddPair(self, arg_user_info, arg_label, arg_value, *arg, **kw):
        """
        PurpleNotifyUserInfoAddPair method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoAddPair( arg_user_info, arg_label, arg_value, *arg, **kw)
    
    def PurpleNotifyUserInfoAddPairPlaintext(self, arg_user_info, arg_label, arg_value, *arg, **kw):
        """
        PurpleNotifyUserInfoAddPairPlaintext method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoAddPairPlaintext( arg_user_info, arg_label, arg_value, *arg, **kw)
    
    def PurpleNotifyUserInfoPrependPair(self, arg_user_info, arg_label, arg_value, *arg, **kw):
        """
        PurpleNotifyUserInfoPrependPair method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoPrependPair( arg_user_info, arg_label, arg_value, *arg, **kw)
    
    def PurpleNotifyUserInfoRemoveEntry(self, arg_user_info, arg_user_info_entry, *arg, **kw):
        """
        PurpleNotifyUserInfoRemoveEntry method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            user_info_entry:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoRemoveEntry( arg_user_info, arg_user_info_entry, *arg, **kw)
    
    def PurpleNotifyUserInfoEntryNew(self, arg_label, arg_value, *arg, **kw):
        """
        PurpleNotifyUserInfoEntryNew method:

        Parameters
        ----------

        label:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntryNew( arg_label, arg_value, *arg, **kw)
    
    def PurpleNotifyUserInfoAddSectionBreak(self, arg_user_info, *arg, **kw):
        """
        PurpleNotifyUserInfoAddSectionBreak method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoAddSectionBreak( arg_user_info, *arg, **kw)
    
    def PurpleNotifyUserInfoPrependSectionBreak(self, arg_user_info, *arg, **kw):
        """
        PurpleNotifyUserInfoPrependSectionBreak method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoPrependSectionBreak( arg_user_info, *arg, **kw)
    
    def PurpleNotifyUserInfoAddSectionHeader(self, arg_user_info, arg_label, *arg, **kw):
        """
        PurpleNotifyUserInfoAddSectionHeader method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoAddSectionHeader( arg_user_info, arg_label, *arg, **kw)
    
    def PurpleNotifyUserInfoPrependSectionHeader(self, arg_user_info, arg_label, *arg, **kw):
        """
        PurpleNotifyUserInfoPrependSectionHeader method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoPrependSectionHeader( arg_user_info, arg_label, *arg, **kw)
    
    def PurpleNotifyUserInfoRemoveLastItem(self, arg_user_info, *arg, **kw):
        """
        PurpleNotifyUserInfoRemoveLastItem method:

        Parameters
        ----------

        user_info:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoRemoveLastItem( arg_user_info, *arg, **kw)
    
    def PurpleNotifyUserInfoEntryGetLabel(self, arg_user_info_entry, *arg, **kw):
        """
        PurpleNotifyUserInfoEntryGetLabel method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntryGetLabel( arg_user_info_entry, *arg, **kw)
    
    def PurpleNotifyUserInfoEntrySetLabel(self, arg_user_info_entry, arg_label, *arg, **kw):
        """
        PurpleNotifyUserInfoEntrySetLabel method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntrySetLabel( arg_user_info_entry, arg_label, *arg, **kw)
    
    def PurpleNotifyUserInfoEntryGetValue(self, arg_user_info_entry, *arg, **kw):
        """
        PurpleNotifyUserInfoEntryGetValue method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntryGetValue( arg_user_info_entry, *arg, **kw)
    
    def PurpleNotifyUserInfoEntrySetValue(self, arg_user_info_entry, arg_value, *arg, **kw):
        """
        PurpleNotifyUserInfoEntrySetValue method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntrySetValue( arg_user_info_entry, arg_value, *arg, **kw)
    
    def PurpleNotifyUserInfoEntryGetType(self, arg_user_info_entry, *arg, **kw):
        """
        PurpleNotifyUserInfoEntryGetType method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntryGetType( arg_user_info_entry, *arg, **kw)
    
    def PurpleNotifyUserInfoEntrySetType(self, arg_user_info_entry, arg_type, *arg, **kw):
        """
        PurpleNotifyUserInfoEntrySetType method:

        Parameters
        ----------

        user_info_entry:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyUserInfoEntrySetType( arg_user_info_entry, arg_type, *arg, **kw)
    
    def PurpleNotifyClose(self, arg_type, arg_ui_handle, *arg, **kw):
        """
        PurpleNotifyClose method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            ui_handle:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyClose( arg_type, arg_ui_handle, *arg, **kw)
    
    def PurpleNotifyCloseWithHandle(self, arg_handle, *arg, **kw):
        """
        PurpleNotifyCloseWithHandle method:

        Parameters
        ----------

        handle:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifyCloseWithHandle( arg_handle, *arg, **kw)
    
    def PurpleNotifySetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleNotifySetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleNotifySetUiOps( arg_ops, *arg, **kw)
    
    def PurpleNotifyGetUiOps(self, *arg, **kw):
        """
        PurpleNotifyGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleNotifyGetUiOps( *arg, **kw)
    
    def PurpleNotifyInit(self, *arg, **kw):
        """
        PurpleNotifyInit method:
        """
        return self._dbus_object.PurpleNotifyInit( *arg, **kw)
    
    def PurpleNotifyUninit(self, *arg, **kw):
        """
        PurpleNotifyUninit method:
        """
        return self._dbus_object.PurpleNotifyUninit( *arg, **kw)
    
    def PurplePrefsInit(self, *arg, **kw):
        """
        PurplePrefsInit method:
        """
        return self._dbus_object.PurplePrefsInit( *arg, **kw)
    
    def PurplePrefsUninit(self, *arg, **kw):
        """
        PurplePrefsUninit method:
        """
        return self._dbus_object.PurplePrefsUninit( *arg, **kw)
    
    def PurplePrefsAddNone(self, arg_name, *arg, **kw):
        """
        PurplePrefsAddNone method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddNone( arg_name, *arg, **kw)
    
    def PurplePrefsAddBool(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddBool method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddBool( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsAddInt(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddInt method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddInt( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsAddString(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddString method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddString( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsAddStringList(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddStringList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddStringList( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsAddPath(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddPath method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddPath( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsAddPathList(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsAddPathList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsAddPathList( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsRemove(self, arg_name, *arg, **kw):
        """
        PurplePrefsRemove method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsRemove( arg_name, *arg, **kw)
    
    def PurplePrefsRename(self, arg_oldname, arg_newname, *arg, **kw):
        """
        PurplePrefsRename method:

        Parameters
        ----------

        oldname:
            type: s,
            direction: in;
            newname:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsRename( arg_oldname, arg_newname, *arg, **kw)
    
    def PurplePrefsRenameBooleanToggle(self, arg_oldname, arg_newname, *arg, **kw):
        """
        PurplePrefsRenameBooleanToggle method:

        Parameters
        ----------

        oldname:
            type: s,
            direction: in;
            newname:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsRenameBooleanToggle( arg_oldname, arg_newname, *arg, **kw)
    
    def PurplePrefsDestroy(self, *arg, **kw):
        """
        PurplePrefsDestroy method:
        """
        return self._dbus_object.PurplePrefsDestroy( *arg, **kw)
    
    def PurplePrefsSetBool(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetBool method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetBool( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsSetInt(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetInt method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetInt( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsSetString(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetString method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetString( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsSetStringList(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetStringList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetStringList( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsSetPath(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetPath method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetPath( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsSetPathList(self, arg_name, arg_value, *arg, **kw):
        """
        PurplePrefsSetPathList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsSetPathList( arg_name, arg_value, *arg, **kw)
    
    def PurplePrefsExists(self, arg_name, *arg, **kw):
        """
        PurplePrefsExists method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsExists( arg_name, *arg, **kw)
    
    def PurplePrefsGetType(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetType method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetType( arg_name, *arg, **kw)
    
    def PurplePrefsGetBool(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetBool method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetBool( arg_name, *arg, **kw)
    
    def PurplePrefsGetInt(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetInt method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetInt( arg_name, *arg, **kw)
    
    def PurplePrefsGetString(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetString method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetString( arg_name, *arg, **kw)
    
    def PurplePrefsGetStringList(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetStringList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: as,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetStringList( arg_name, *arg, **kw)
    
    def PurplePrefsGetPath(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetPath method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetPath( arg_name, *arg, **kw)
    
    def PurplePrefsGetPathList(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetPathList method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: as,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetPathList( arg_name, *arg, **kw)
    
    def PurplePrefsGetChildrenNames(self, arg_name, *arg, **kw):
        """
        PurplePrefsGetChildrenNames method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            RESULT:
            type: as,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsGetChildrenNames( arg_name, *arg, **kw)
    
    def PurplePrefsDisconnectCallback(self, arg_callback_id, *arg, **kw):
        """
        PurplePrefsDisconnectCallback method:

        Parameters
        ----------

        callback_id:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsDisconnectCallback( arg_callback_id, *arg, **kw)
    
    def PurplePrefsDisconnectByHandle(self, arg_handle, *arg, **kw):
        """
        PurplePrefsDisconnectByHandle method:

        Parameters
        ----------

        handle:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsDisconnectByHandle( arg_handle, *arg, **kw)
    
    def PurplePrefsTriggerCallback(self, arg_name, *arg, **kw):
        """
        PurplePrefsTriggerCallback method:

        Parameters
        ----------

        name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrefsTriggerCallback( arg_name, *arg, **kw)
    
    def PurplePrefsLoad(self, *arg, **kw):
        """
        PurplePrefsLoad method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrefsLoad( *arg, **kw)
    
    def PurplePrefsUpdateOld(self, *arg, **kw):
        """
        PurplePrefsUpdateOld method:
        """
        return self._dbus_object.PurplePrefsUpdateOld( *arg, **kw)
    
    def PurpleRoomlistShowWithAccount(self, arg_account, *arg, **kw):
        """
        PurpleRoomlistShowWithAccount method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistShowWithAccount( arg_account, *arg, **kw)
    
    def PurpleRoomlistNew(self, arg_account, *arg, **kw):
        """
        PurpleRoomlistNew method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistNew( arg_account, *arg, **kw)
    
    def PurpleRoomlistRef(self, arg_list, *arg, **kw):
        """
        PurpleRoomlistRef method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistRef( arg_list, *arg, **kw)
    
    def PurpleRoomlistUnref(self, arg_list, *arg, **kw):
        """
        PurpleRoomlistUnref method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistUnref( arg_list, *arg, **kw)
    
    def PurpleRoomlistSetFields(self, arg_list, arg_fields, *arg, **kw):
        """
        PurpleRoomlistSetFields method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            fields:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistSetFields( arg_list, arg_fields, *arg, **kw)
    
    def PurpleRoomlistSetInProgress(self, arg_list, arg_in_progress, *arg, **kw):
        """
        PurpleRoomlistSetInProgress method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            in_progress:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistSetInProgress( arg_list, arg_in_progress, *arg, **kw)
    
    def PurpleRoomlistGetInProgress(self, arg_list, *arg, **kw):
        """
        PurpleRoomlistGetInProgress method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistGetInProgress( arg_list, *arg, **kw)
    
    def PurpleRoomlistRoomAdd(self, arg_list, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomAdd method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            room:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistRoomAdd( arg_list, arg_room, *arg, **kw)
    
    def PurpleRoomlistGetList(self, arg_gc, *arg, **kw):
        """
        PurpleRoomlistGetList method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistGetList( arg_gc, *arg, **kw)
    
    def PurpleRoomlistCancelGetList(self, arg_list, *arg, **kw):
        """
        PurpleRoomlistCancelGetList method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistCancelGetList( arg_list, *arg, **kw)
    
    def PurpleRoomlistExpandCategory(self, arg_list, arg_category, *arg, **kw):
        """
        PurpleRoomlistExpandCategory method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            category:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistExpandCategory( arg_list, arg_category, *arg, **kw)
    
    def PurpleRoomlistGetFields(self, arg_roomlist, *arg, **kw):
        """
        PurpleRoomlistGetFields method:

        Parameters
        ----------

        roomlist:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistGetFields( arg_roomlist, *arg, **kw)
    
    def PurpleRoomlistRoomNew(self, arg_type, arg_name, arg_parent, *arg, **kw):
        """
        PurpleRoomlistRoomNew method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            parent:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistRoomNew( arg_type, arg_name, arg_parent, *arg, **kw)
    
    def PurpleRoomlistRoomJoin(self, arg_list, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomJoin method:

        Parameters
        ----------

        list:
            type: i,
            direction: in;
            room:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistRoomJoin( arg_list, arg_room, *arg, **kw)
    
    def PurpleRoomlistRoomGetType(self, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomGetType method:

        Parameters
        ----------

        room:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistRoomGetType( arg_room, *arg, **kw)
    
    def PurpleRoomlistRoomGetName(self, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomGetName method:

        Parameters
        ----------

        room:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistRoomGetName( arg_room, *arg, **kw)
    
    def PurpleRoomlistRoomGetParent(self, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomGetParent method:

        Parameters
        ----------

        room:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistRoomGetParent( arg_room, *arg, **kw)
    
    def PurpleRoomlistRoomGetFields(self, arg_room, *arg, **kw):
        """
        PurpleRoomlistRoomGetFields method:

        Parameters
        ----------

        room:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistRoomGetFields( arg_room, *arg, **kw)
    
    def PurpleRoomlistFieldNew(self, arg_type, arg_label, arg_name, arg_hidden, *arg, **kw):
        """
        PurpleRoomlistFieldNew method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            label:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            hidden:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistFieldNew( arg_type, arg_label, arg_name, arg_hidden, *arg, **kw)
    
    def PurpleRoomlistFieldGetType(self, arg_field, *arg, **kw):
        """
        PurpleRoomlistFieldGetType method:

        Parameters
        ----------

        field:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistFieldGetType( arg_field, *arg, **kw)
    
    def PurpleRoomlistFieldGetLabel(self, arg_field, *arg, **kw):
        """
        PurpleRoomlistFieldGetLabel method:

        Parameters
        ----------

        field:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistFieldGetLabel( arg_field, *arg, **kw)
    
    def PurpleRoomlistFieldGetHidden(self, arg_field, *arg, **kw):
        """
        PurpleRoomlistFieldGetHidden method:

        Parameters
        ----------

        field:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistFieldGetHidden( arg_field, *arg, **kw)
    
    def PurpleRoomlistSetUiOps(self, arg_ops, *arg, **kw):
        """
        PurpleRoomlistSetUiOps method:

        Parameters
        ----------

        ops:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleRoomlistSetUiOps( arg_ops, *arg, **kw)
    
    def PurpleRoomlistGetUiOps(self, *arg, **kw):
        """
        PurpleRoomlistGetUiOps method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRoomlistGetUiOps( *arg, **kw)
    
    def PurpleSavedstatusNew(self, arg_title, arg_type, *arg, **kw):
        """
        PurpleSavedstatusNew method:

        Parameters
        ----------

        title:
            type: s,
            direction: in;
            type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusNew( arg_title, arg_type, *arg, **kw)
    
    def PurpleSavedstatusSetTitle(self, arg_status, arg_title, *arg, **kw):
        """
        PurpleSavedstatusSetTitle method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            title:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusSetTitle( arg_status, arg_title, *arg, **kw)
    
    def PurpleSavedstatusSetType(self, arg_status, arg_type, *arg, **kw):
        """
        PurpleSavedstatusSetType method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusSetType( arg_status, arg_type, *arg, **kw)
    
    def PurpleSavedstatusSetMessage(self, arg_status, arg_message, *arg, **kw):
        """
        PurpleSavedstatusSetMessage method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusSetMessage( arg_status, arg_message, *arg, **kw)
    
    def PurpleSavedstatusSetSubstatus(self, arg_status, arg_account, arg_type, arg_message, *arg, **kw):
        """
        PurpleSavedstatusSetSubstatus method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            type:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusSetSubstatus( arg_status, arg_account, arg_type, arg_message, *arg, **kw)
    
    def PurpleSavedstatusUnsetSubstatus(self, arg_saved_status, arg_account, *arg, **kw):
        """
        PurpleSavedstatusUnsetSubstatus method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusUnsetSubstatus( arg_saved_status, arg_account, *arg, **kw)
    
    def PurpleSavedstatusDelete(self, arg_title, *arg, **kw):
        """
        PurpleSavedstatusDelete method:

        Parameters
        ----------

        title:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusDelete( arg_title, *arg, **kw)
    
    def PurpleSavedstatusDeleteByStatus(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusDeleteByStatus method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusDeleteByStatus( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusesGetAll(self, *arg, **kw):
        """
        PurpleSavedstatusesGetAll method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusesGetAll( *arg, **kw)
    
    def PurpleSavedstatusesGetPopular(self, arg_how_many, *arg, **kw):
        """
        PurpleSavedstatusesGetPopular method:

        Parameters
        ----------

        how_many:
            type: u,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusesGetPopular( arg_how_many, *arg, **kw)
    
    def PurpleSavedstatusGetCurrent(self, *arg, **kw):
        """
        PurpleSavedstatusGetCurrent method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetCurrent( *arg, **kw)
    
    def PurpleSavedstatusGetDefault(self, *arg, **kw):
        """
        PurpleSavedstatusGetDefault method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetDefault( *arg, **kw)
    
    def PurpleSavedstatusGetIdleaway(self, *arg, **kw):
        """
        PurpleSavedstatusGetIdleaway method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetIdleaway( *arg, **kw)
    
    def PurpleSavedstatusIsIdleaway(self, *arg, **kw):
        """
        PurpleSavedstatusIsIdleaway method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusIsIdleaway( *arg, **kw)
    
    def PurpleSavedstatusSetIdleaway(self, arg_idleaway, *arg, **kw):
        """
        PurpleSavedstatusSetIdleaway method:

        Parameters
        ----------

        idleaway:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusSetIdleaway( arg_idleaway, *arg, **kw)
    
    def PurpleSavedstatusGetStartup(self, *arg, **kw):
        """
        PurpleSavedstatusGetStartup method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetStartup( *arg, **kw)
    
    def PurpleSavedstatusFind(self, arg_title, *arg, **kw):
        """
        PurpleSavedstatusFind method:

        Parameters
        ----------

        title:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusFind( arg_title, *arg, **kw)
    
    def PurpleSavedstatusFindByCreationTime(self, arg_creation_time, *arg, **kw):
        """
        PurpleSavedstatusFindByCreationTime method:

        Parameters
        ----------

        creation_time:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusFindByCreationTime( arg_creation_time, *arg, **kw)
    
    def PurpleSavedstatusFindTransientByTypeAndMessage(self, arg_type, arg_message, *arg, **kw):
        """
        PurpleSavedstatusFindTransientByTypeAndMessage method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusFindTransientByTypeAndMessage( arg_type, arg_message, *arg, **kw)
    
    def PurpleSavedstatusIsTransient(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusIsTransient method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusIsTransient( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusGetTitle(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusGetTitle method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetTitle( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusGetType(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusGetType method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetType( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusGetMessage(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusGetMessage method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetMessage( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusGetCreationTime(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusGetCreationTime method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetCreationTime( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusHasSubstatuses(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusHasSubstatuses method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusHasSubstatuses( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusGetSubstatus(self, arg_saved_status, arg_account, *arg, **kw):
        """
        PurpleSavedstatusGetSubstatus method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusGetSubstatus( arg_saved_status, arg_account, *arg, **kw)
    
    def PurpleSavedstatusSubstatusGetType(self, arg_substatus, *arg, **kw):
        """
        PurpleSavedstatusSubstatusGetType method:

        Parameters
        ----------

        substatus:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusSubstatusGetType( arg_substatus, *arg, **kw)
    
    def PurpleSavedstatusSubstatusGetMessage(self, arg_substatus, *arg, **kw):
        """
        PurpleSavedstatusSubstatusGetMessage method:

        Parameters
        ----------

        substatus:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSavedstatusSubstatusGetMessage( arg_substatus, *arg, **kw)
    
    def PurpleSavedstatusActivate(self, arg_saved_status, *arg, **kw):
        """
        PurpleSavedstatusActivate method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusActivate( arg_saved_status, *arg, **kw)
    
    def PurpleSavedstatusActivateForAccount(self, arg_saved_status, arg_account, *arg, **kw):
        """
        PurpleSavedstatusActivateForAccount method:

        Parameters
        ----------

        saved_status:
            type: i,
            direction: in;
            account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSavedstatusActivateForAccount( arg_saved_status, arg_account, *arg, **kw)
    
    def PurpleSavedstatusesInit(self, *arg, **kw):
        """
        PurpleSavedstatusesInit method:
        """
        return self._dbus_object.PurpleSavedstatusesInit( *arg, **kw)
    
    def PurpleSavedstatusesUninit(self, *arg, **kw):
        """
        PurpleSavedstatusesUninit method:
        """
        return self._dbus_object.PurpleSavedstatusesUninit( *arg, **kw)
    
    def PurpleSmileyNew(self, arg_img, arg_shortcut, *arg, **kw):
        """
        PurpleSmileyNew method:

        Parameters
        ----------

        img:
            type: i,
            direction: in;
            shortcut:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyNew( arg_img, arg_shortcut, *arg, **kw)
    
    def PurpleSmileyNewFromFile(self, arg_shortcut, arg_filepath, *arg, **kw):
        """
        PurpleSmileyNewFromFile method:

        Parameters
        ----------

        shortcut:
            type: s,
            direction: in;
            filepath:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyNewFromFile( arg_shortcut, arg_filepath, *arg, **kw)
    
    def PurpleSmileyDelete(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyDelete method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSmileyDelete( arg_smiley, *arg, **kw)
    
    def PurpleSmileySetShortcut(self, arg_smiley, arg_shortcut, *arg, **kw):
        """
        PurpleSmileySetShortcut method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            shortcut:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileySetShortcut( arg_smiley, arg_shortcut, *arg, **kw)
    
    def PurpleSmileySetData(self, arg_smiley, arg_smiley_data, arg_smiley_data_len, *arg, **kw):
        """
        PurpleSmileySetData method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            smiley_data:
            type: i,
            direction: in;
            smiley_data_len:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleSmileySetData( arg_smiley, arg_smiley_data, arg_smiley_data_len, *arg, **kw)
    
    def PurpleSmileyGetShortcut(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetShortcut method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetShortcut( arg_smiley, *arg, **kw)
    
    def PurpleSmileyGetChecksum(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetChecksum method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetChecksum( arg_smiley, *arg, **kw)
    
    def PurpleSmileyGetStoredImage(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetStoredImage method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetStoredImage( arg_smiley, *arg, **kw)
    
    def PurpleSmileyGetData(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetData method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: ay,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetData( arg_smiley, *arg, **kw)
    
    def PurpleSmileyGetExtension(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetExtension method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetExtension( arg_smiley, *arg, **kw)
    
    def PurpleSmileyGetFullPath(self, arg_smiley, *arg, **kw):
        """
        PurpleSmileyGetFullPath method:

        Parameters
        ----------

        smiley:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileyGetFullPath( arg_smiley, *arg, **kw)
    
    def PurpleSmileysGetAll(self, *arg, **kw):
        """
        PurpleSmileysGetAll method:

        Parameters
        ----------

        RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileysGetAll( *arg, **kw)
    
    def PurpleSmileysFindByShortcut(self, arg_shortcut, *arg, **kw):
        """
        PurpleSmileysFindByShortcut method:

        Parameters
        ----------

        shortcut:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileysFindByShortcut( arg_shortcut, *arg, **kw)
    
    def PurpleSmileysFindByChecksum(self, arg_checksum, *arg, **kw):
        """
        PurpleSmileysFindByChecksum method:

        Parameters
        ----------

        checksum:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileysFindByChecksum( arg_checksum, *arg, **kw)
    
    def PurpleSmileysGetStoringDir(self, *arg, **kw):
        """
        PurpleSmileysGetStoringDir method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleSmileysGetStoringDir( *arg, **kw)
    
    def PurpleSmileysInit(self, *arg, **kw):
        """
        PurpleSmileysInit method:
        """
        return self._dbus_object.PurpleSmileysInit( *arg, **kw)
    
    def PurpleSmileysUninit(self, *arg, **kw):
        """
        PurpleSmileysUninit method:
        """
        return self._dbus_object.PurpleSmileysUninit( *arg, **kw)
    
    def PurplePrimitiveGetIdFromType(self, arg_type, *arg, **kw):
        """
        PurplePrimitiveGetIdFromType method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurplePrimitiveGetIdFromType( arg_type, *arg, **kw)
    
    def PurplePrimitiveGetNameFromType(self, arg_type, *arg, **kw):
        """
        PurplePrimitiveGetNameFromType method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurplePrimitiveGetNameFromType( arg_type, *arg, **kw)
    
    def PurplePrimitiveGetTypeFromId(self, arg_id, *arg, **kw):
        """
        PurplePrimitiveGetTypeFromId method:

        Parameters
        ----------

        id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrimitiveGetTypeFromId( arg_id, *arg, **kw)
    
    def PurpleStatusTypeNewFull(self, arg_primitive, arg_id, arg_name, arg_saveable, arg_user_settable, arg_independent, *arg, **kw):
        """
        PurpleStatusTypeNewFull method:

        Parameters
        ----------

        primitive:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            saveable:
            type: i,
            direction: in;
            user_settable:
            type: i,
            direction: in;
            independent:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeNewFull( arg_primitive, arg_id, arg_name, arg_saveable, arg_user_settable, arg_independent, *arg, **kw)
    
    def PurpleStatusTypeNew(self, arg_primitive, arg_id, arg_name, arg_user_settable, *arg, **kw):
        """
        PurpleStatusTypeNew method:

        Parameters
        ----------

        primitive:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            user_settable:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeNew( arg_primitive, arg_id, arg_name, arg_user_settable, *arg, **kw)
    
    def PurpleStatusTypeDestroy(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeDestroy method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusTypeDestroy( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeSetPrimaryAttr(self, arg_status_type, arg_attr_id, *arg, **kw):
        """
        PurpleStatusTypeSetPrimaryAttr method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            attr_id:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusTypeSetPrimaryAttr( arg_status_type, arg_attr_id, *arg, **kw)
    
    def PurpleStatusTypeAddAttr(self, arg_status_type, arg_id, arg_name, arg_value, *arg, **kw):
        """
        PurpleStatusTypeAddAttr method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusTypeAddAttr( arg_status_type, arg_id, arg_name, arg_value, *arg, **kw)
    
    def PurpleStatusTypeGetPrimitive(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeGetPrimitive method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetPrimitive( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeGetId(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeGetId method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetId( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeGetName(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeGetName method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetName( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeIsSaveable(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeIsSaveable method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeIsSaveable( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeIsUserSettable(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeIsUserSettable method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeIsUserSettable( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeIsIndependent(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeIsIndependent method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeIsIndependent( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeIsExclusive(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeIsExclusive method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeIsExclusive( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeIsAvailable(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeIsAvailable method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeIsAvailable( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeGetPrimaryAttr(self, arg_type, *arg, **kw):
        """
        PurpleStatusTypeGetPrimaryAttr method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetPrimaryAttr( arg_type, *arg, **kw)
    
    def PurpleStatusTypeGetAttr(self, arg_status_type, arg_id, *arg, **kw):
        """
        PurpleStatusTypeGetAttr method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetAttr( arg_status_type, arg_id, *arg, **kw)
    
    def PurpleStatusTypeGetAttrs(self, arg_status_type, *arg, **kw):
        """
        PurpleStatusTypeGetAttrs method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeGetAttrs( arg_status_type, *arg, **kw)
    
    def PurpleStatusTypeFindWithId(self, arg_status_types, arg_id, *arg, **kw):
        """
        PurpleStatusTypeFindWithId method:

        Parameters
        ----------

        status_types:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusTypeFindWithId( arg_status_types, arg_id, *arg, **kw)
    
    def PurpleStatusAttrNew(self, arg_id, arg_name, arg_value_type, *arg, **kw):
        """
        PurpleStatusAttrNew method:

        Parameters
        ----------

        id:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            value_type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusAttrNew( arg_id, arg_name, arg_value_type, *arg, **kw)
    
    def PurpleStatusAttrDestroy(self, arg_attr, *arg, **kw):
        """
        PurpleStatusAttrDestroy method:

        Parameters
        ----------

        attr:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusAttrDestroy( arg_attr, *arg, **kw)
    
    def PurpleStatusAttrGetId(self, arg_attr, *arg, **kw):
        """
        PurpleStatusAttrGetId method:

        Parameters
        ----------

        attr:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusAttrGetId( arg_attr, *arg, **kw)
    
    def PurpleStatusAttrGetName(self, arg_attr, *arg, **kw):
        """
        PurpleStatusAttrGetName method:

        Parameters
        ----------

        attr:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusAttrGetName( arg_attr, *arg, **kw)
    
    def PurpleStatusAttrGetValue(self, arg_attr, *arg, **kw):
        """
        PurpleStatusAttrGetValue method:

        Parameters
        ----------

        attr:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusAttrGetValue( arg_attr, *arg, **kw)
    
    def PurpleStatusNew(self, arg_status_type, arg_presence, *arg, **kw):
        """
        PurpleStatusNew method:

        Parameters
        ----------

        status_type:
            type: i,
            direction: in;
            presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusNew( arg_status_type, arg_presence, *arg, **kw)
    
    def PurpleStatusDestroy(self, arg_status, *arg, **kw):
        """
        PurpleStatusDestroy method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusDestroy( arg_status, *arg, **kw)
    
    def PurpleStatusSetActive(self, arg_status, arg_active, *arg, **kw):
        """
        PurpleStatusSetActive method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            active:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusSetActive( arg_status, arg_active, *arg, **kw)
    
    def PurpleStatusSetActiveWithAttrsList(self, arg_status, arg_active, arg_attrs, *arg, **kw):
        """
        PurpleStatusSetActiveWithAttrsList method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            active:
            type: i,
            direction: in;
            attrs:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusSetActiveWithAttrsList( arg_status, arg_active, arg_attrs, *arg, **kw)
    
    def PurpleStatusSetAttrBoolean(self, arg_status, arg_id, arg_value, *arg, **kw):
        """
        PurpleStatusSetAttrBoolean method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusSetAttrBoolean( arg_status, arg_id, arg_value, *arg, **kw)
    
    def PurpleStatusSetAttrInt(self, arg_status, arg_id, arg_value, *arg, **kw):
        """
        PurpleStatusSetAttrInt method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            value:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusSetAttrInt( arg_status, arg_id, arg_value, *arg, **kw)
    
    def PurpleStatusSetAttrString(self, arg_status, arg_id, arg_value, *arg, **kw):
        """
        PurpleStatusSetAttrString method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleStatusSetAttrString( arg_status, arg_id, arg_value, *arg, **kw)
    
    def PurpleStatusGetType(self, arg_status, *arg, **kw):
        """
        PurpleStatusGetType method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetType( arg_status, *arg, **kw)
    
    def PurpleStatusGetPresence(self, arg_status, *arg, **kw):
        """
        PurpleStatusGetPresence method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetPresence( arg_status, *arg, **kw)
    
    def PurpleStatusGetId(self, arg_status, *arg, **kw):
        """
        PurpleStatusGetId method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetId( arg_status, *arg, **kw)
    
    def PurpleStatusGetName(self, arg_status, *arg, **kw):
        """
        PurpleStatusGetName method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetName( arg_status, *arg, **kw)
    
    def PurpleStatusIsIndependent(self, arg_status, *arg, **kw):
        """
        PurpleStatusIsIndependent method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusIsIndependent( arg_status, *arg, **kw)
    
    def PurpleStatusIsExclusive(self, arg_status, *arg, **kw):
        """
        PurpleStatusIsExclusive method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusIsExclusive( arg_status, *arg, **kw)
    
    def PurpleStatusIsAvailable(self, arg_status, *arg, **kw):
        """
        PurpleStatusIsAvailable method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusIsAvailable( arg_status, *arg, **kw)
    
    def PurpleStatusIsActive(self, arg_status, *arg, **kw):
        """
        PurpleStatusIsActive method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusIsActive( arg_status, *arg, **kw)
    
    def PurpleStatusIsOnline(self, arg_status, *arg, **kw):
        """
        PurpleStatusIsOnline method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusIsOnline( arg_status, *arg, **kw)
    
    def PurpleStatusGetAttrValue(self, arg_status, arg_id, *arg, **kw):
        """
        PurpleStatusGetAttrValue method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetAttrValue( arg_status, arg_id, *arg, **kw)
    
    def PurpleStatusGetAttrBoolean(self, arg_status, arg_id, *arg, **kw):
        """
        PurpleStatusGetAttrBoolean method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetAttrBoolean( arg_status, arg_id, *arg, **kw)
    
    def PurpleStatusGetAttrInt(self, arg_status, arg_id, *arg, **kw):
        """
        PurpleStatusGetAttrInt method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetAttrInt( arg_status, arg_id, *arg, **kw)
    
    def PurpleStatusGetAttrString(self, arg_status, arg_id, *arg, **kw):
        """
        PurpleStatusGetAttrString method:

        Parameters
        ----------

        status:
            type: i,
            direction: in;
            id:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusGetAttrString( arg_status, arg_id, *arg, **kw)
    
    def PurpleStatusCompare(self, arg_status1, arg_status2, *arg, **kw):
        """
        PurpleStatusCompare method:

        Parameters
        ----------

        status1:
            type: i,
            direction: in;
            status2:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStatusCompare( arg_status1, arg_status2, *arg, **kw)
    
    def PurplePresenceNew(self, arg_context, *arg, **kw):
        """
        PurplePresenceNew method:

        Parameters
        ----------

        context:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceNew( arg_context, *arg, **kw)
    
    def PurplePresenceNewForAccount(self, arg_account, *arg, **kw):
        """
        PurplePresenceNewForAccount method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceNewForAccount( arg_account, *arg, **kw)
    
    def PurplePresenceNewForConv(self, arg_conv, *arg, **kw):
        """
        PurplePresenceNewForConv method:

        Parameters
        ----------

        conv:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceNewForConv( arg_conv, *arg, **kw)
    
    def PurplePresenceNewForBuddy(self, arg_buddy, *arg, **kw):
        """
        PurplePresenceNewForBuddy method:

        Parameters
        ----------

        buddy:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceNewForBuddy( arg_buddy, *arg, **kw)
    
    def PurplePresenceDestroy(self, arg_presence, *arg, **kw):
        """
        PurplePresenceDestroy method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceDestroy( arg_presence, *arg, **kw)
    
    def PurplePresenceAddStatus(self, arg_presence, arg_status, *arg, **kw):
        """
        PurplePresenceAddStatus method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceAddStatus( arg_presence, arg_status, *arg, **kw)
    
    def PurplePresenceSetStatusActive(self, arg_presence, arg_status_id, arg_active, *arg, **kw):
        """
        PurplePresenceSetStatusActive method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            active:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceSetStatusActive( arg_presence, arg_status_id, arg_active, *arg, **kw)
    
    def PurplePresenceSwitchStatus(self, arg_presence, arg_status_id, *arg, **kw):
        """
        PurplePresenceSwitchStatus method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceSwitchStatus( arg_presence, arg_status_id, *arg, **kw)
    
    def PurplePresenceSetIdle(self, arg_presence, arg_idle, arg_idle_time, *arg, **kw):
        """
        PurplePresenceSetIdle method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            idle:
            type: i,
            direction: in;
            idle_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceSetIdle( arg_presence, arg_idle, arg_idle_time, *arg, **kw)
    
    def PurplePresenceSetLoginTime(self, arg_presence, arg_login_time, *arg, **kw):
        """
        PurplePresenceSetLoginTime method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            login_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePresenceSetLoginTime( arg_presence, arg_login_time, *arg, **kw)
    
    def PurplePresenceGetContext(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetContext method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetContext( arg_presence, *arg, **kw)
    
    def PurplePresenceGetAccount(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetAccount method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetAccount( arg_presence, *arg, **kw)
    
    def PurplePresenceGetConversation(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetConversation method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetConversation( arg_presence, *arg, **kw)
    
    def PurplePresenceGetChatUser(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetChatUser method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetChatUser( arg_presence, *arg, **kw)
    
    def PurplePresenceGetBuddy(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetBuddy method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetBuddy( arg_presence, *arg, **kw)
    
    def PurplePresenceGetStatuses(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetStatuses method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetStatuses( arg_presence, *arg, **kw)
    
    def PurplePresenceGetStatus(self, arg_presence, arg_status_id, *arg, **kw):
        """
        PurplePresenceGetStatus method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetStatus( arg_presence, arg_status_id, *arg, **kw)
    
    def PurplePresenceGetActiveStatus(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetActiveStatus method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetActiveStatus( arg_presence, *arg, **kw)
    
    def PurplePresenceIsAvailable(self, arg_presence, *arg, **kw):
        """
        PurplePresenceIsAvailable method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceIsAvailable( arg_presence, *arg, **kw)
    
    def PurplePresenceIsOnline(self, arg_presence, *arg, **kw):
        """
        PurplePresenceIsOnline method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceIsOnline( arg_presence, *arg, **kw)
    
    def PurplePresenceIsStatusActive(self, arg_presence, arg_status_id, *arg, **kw):
        """
        PurplePresenceIsStatusActive method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            status_id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceIsStatusActive( arg_presence, arg_status_id, *arg, **kw)
    
    def PurplePresenceIsStatusPrimitiveActive(self, arg_presence, arg_primitive, *arg, **kw):
        """
        PurplePresenceIsStatusPrimitiveActive method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            primitive:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceIsStatusPrimitiveActive( arg_presence, arg_primitive, *arg, **kw)
    
    def PurplePresenceIsIdle(self, arg_presence, *arg, **kw):
        """
        PurplePresenceIsIdle method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceIsIdle( arg_presence, *arg, **kw)
    
    def PurplePresenceGetIdleTime(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetIdleTime method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetIdleTime( arg_presence, *arg, **kw)
    
    def PurplePresenceGetLoginTime(self, arg_presence, *arg, **kw):
        """
        PurplePresenceGetLoginTime method:

        Parameters
        ----------

        presence:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceGetLoginTime( arg_presence, *arg, **kw)
    
    def PurplePresenceCompare(self, arg_presence1, arg_presence2, *arg, **kw):
        """
        PurplePresenceCompare method:

        Parameters
        ----------

        presence1:
            type: i,
            direction: in;
            presence2:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePresenceCompare( arg_presence1, arg_presence2, *arg, **kw)
    
    def PurpleStatusInit(self, *arg, **kw):
        """
        PurpleStatusInit method:
        """
        return self._dbus_object.PurpleStatusInit( *arg, **kw)
    
    def PurpleStatusUninit(self, *arg, **kw):
        """
        PurpleStatusUninit method:
        """
        return self._dbus_object.PurpleStatusUninit( *arg, **kw)
    
    def ServSendTyping(self, arg_gc, arg_name, arg_state, *arg, **kw):
        """
        ServSendTyping method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            state:
            type: i,
            direction: in;
            RESULT:
            type: u,
            direction: out;
            
        """
        return self._dbus_object.ServSendTyping( arg_gc, arg_name, arg_state, *arg, **kw)
    
    def ServMoveBuddy(self, arg_param0, arg_param1, arg_param2, *arg, **kw):
        """
        ServMoveBuddy method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: i,
            direction: in;
            param2:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServMoveBuddy( arg_param0, arg_param1, arg_param2, *arg, **kw)
    
    def ServSendIm(self, arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw):
        """
        ServSendIm method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            param2:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.ServSendIm( arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw)
    
    def PurpleGetAttentionTypeFromCode(self, arg_account, arg_type_code, *arg, **kw):
        """
        PurpleGetAttentionTypeFromCode method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            type_code:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetAttentionTypeFromCode( arg_account, arg_type_code, *arg, **kw)
    
    def ServSendAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
        """
        ServSendAttention method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type_code:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServSendAttention( arg_gc, arg_who, arg_type_code, *arg, **kw)
    
    def ServGotAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
        """
        ServGotAttention method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type_code:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServGotAttention( arg_gc, arg_who, arg_type_code, *arg, **kw)
    
    def ServGetInfo(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServGetInfo method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServGetInfo( arg_param0, arg_param1, *arg, **kw)
    
    def ServSetInfo(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServSetInfo method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServSetInfo( arg_param0, arg_param1, *arg, **kw)
    
    def ServAddPermit(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServAddPermit method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServAddPermit( arg_param0, arg_param1, *arg, **kw)
    
    def ServAddDeny(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServAddDeny method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServAddDeny( arg_param0, arg_param1, *arg, **kw)
    
    def ServRemPermit(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServRemPermit method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServRemPermit( arg_param0, arg_param1, *arg, **kw)
    
    def ServRemDeny(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServRemDeny method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServRemDeny( arg_param0, arg_param1, *arg, **kw)
    
    def ServSetPermitDeny(self, arg_param0, *arg, **kw):
        """
        ServSetPermitDeny method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServSetPermitDeny( arg_param0, *arg, **kw)
    
    def ServChatInvite(self, arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw):
        """
        ServChatInvite method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: i,
            direction: in;
            param2:
            type: s,
            direction: in;
            param3:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServChatInvite( arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw)
    
    def ServChatLeave(self, arg_param0, arg_param1, *arg, **kw):
        """
        ServChatLeave method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServChatLeave( arg_param0, arg_param1, *arg, **kw)
    
    def ServChatWhisper(self, arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw):
        """
        ServChatWhisper method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: i,
            direction: in;
            param2:
            type: s,
            direction: in;
            param3:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServChatWhisper( arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw)
    
    def ServChatSend(self, arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw):
        """
        ServChatSend method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            param1:
            type: i,
            direction: in;
            param2:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.ServChatSend( arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw)
    
    def ServAliasBuddy(self, arg_param0, *arg, **kw):
        """
        ServAliasBuddy method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServAliasBuddy( arg_param0, *arg, **kw)
    
    def ServGotAlias(self, arg_gc, arg_who, arg_alias, *arg, **kw):
        """
        ServGotAlias method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServGotAlias( arg_gc, arg_who, arg_alias, *arg, **kw)
    
    def PurpleServGotPrivateAlias(self, arg_gc, arg_who, arg_alias, *arg, **kw):
        """
        PurpleServGotPrivateAlias method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            alias:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleServGotPrivateAlias( arg_gc, arg_who, arg_alias, *arg, **kw)
    
    def ServGotTyping(self, arg_gc, arg_name, arg_timeout, arg_state, *arg, **kw):
        """
        ServGotTyping method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            timeout:
            type: i,
            direction: in;
            state:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServGotTyping( arg_gc, arg_name, arg_timeout, arg_state, *arg, **kw)
    
    def ServGotTypingStopped(self, arg_gc, arg_name, *arg, **kw):
        """
        ServGotTypingStopped method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServGotTypingStopped( arg_gc, arg_name, *arg, **kw)
    
    def ServGotIm(self, arg_gc, arg_who, arg_msg, arg_flags, arg_mtime, *arg, **kw):
        """
        ServGotIm method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            msg:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            mtime:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServGotIm( arg_gc, arg_who, arg_msg, arg_flags, arg_mtime, *arg, **kw)
    
    def ServJoinChat(self, arg_param0, arg_data, *arg, **kw):
        """
        ServJoinChat method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            data:
            type: a{ss},
            direction: in;
            
        """
        return self._dbus_object.ServJoinChat( arg_param0, arg_data, *arg, **kw)
    
    def ServRejectChat(self, arg_param0, arg_data, *arg, **kw):
        """
        ServRejectChat method:

        Parameters
        ----------

        param0:
            type: i,
            direction: in;
            data:
            type: a{ss},
            direction: in;
            
        """
        return self._dbus_object.ServRejectChat( arg_param0, arg_data, *arg, **kw)
    
    def ServGotChatInvite(self, arg_gc, arg_name, arg_who, arg_message, arg_data, *arg, **kw):
        """
        ServGotChatInvite method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            who:
            type: s,
            direction: in;
            message:
            type: s,
            direction: in;
            data:
            type: a{ss},
            direction: in;
            
        """
        return self._dbus_object.ServGotChatInvite( arg_gc, arg_name, arg_who, arg_message, arg_data, *arg, **kw)
    
    def ServGotJoinedChat(self, arg_gc, arg_id, arg_name, *arg, **kw):
        """
        ServGotJoinedChat method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.ServGotJoinedChat( arg_gc, arg_id, arg_name, *arg, **kw)
    
    def PurpleServGotJoinChatFailed(self, arg_gc, arg_data, *arg, **kw):
        """
        PurpleServGotJoinChatFailed method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            data:
            type: a{ss},
            direction: in;
            
        """
        return self._dbus_object.PurpleServGotJoinChatFailed( arg_gc, arg_data, *arg, **kw)
    
    def ServGotChatLeft(self, arg_g, arg_id, *arg, **kw):
        """
        ServGotChatLeft method:

        Parameters
        ----------

        g:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServGotChatLeft( arg_g, arg_id, *arg, **kw)
    
    def ServGotChatIn(self, arg_g, arg_id, arg_who, arg_flags, arg_message, arg_mtime, *arg, **kw):
        """
        ServGotChatIn method:

        Parameters
        ----------

        g:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            flags:
            type: i,
            direction: in;
            message:
            type: s,
            direction: in;
            mtime:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.ServGotChatIn( arg_g, arg_id, arg_who, arg_flags, arg_message, arg_mtime, *arg, **kw)
    
    def ServSendFile(self, arg_gc, arg_who, arg_file, *arg, **kw):
        """
        ServSendFile method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            file:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.ServSendFile( arg_gc, arg_who, arg_file, *arg, **kw)
    
    def PurpleMenuActionFree(self, arg_act, *arg, **kw):
        """
        PurpleMenuActionFree method:

        Parameters
        ----------

        act:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleMenuActionFree( arg_act, *arg, **kw)
    
    def PurpleUtilSetCurrentSong(self, arg_title, arg_artist, arg_album, *arg, **kw):
        """
        PurpleUtilSetCurrentSong method:

        Parameters
        ----------

        title:
            type: s,
            direction: in;
            artist:
            type: s,
            direction: in;
            album:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleUtilSetCurrentSong( arg_title, arg_artist, arg_album, *arg, **kw)
    
    def PurpleUtilInit(self, *arg, **kw):
        """
        PurpleUtilInit method:
        """
        return self._dbus_object.PurpleUtilInit( *arg, **kw)
    
    def PurpleUtilUninit(self, *arg, **kw):
        """
        PurpleUtilUninit method:
        """
        return self._dbus_object.PurpleUtilUninit( *arg, **kw)
    
    def PurpleMimeDecodeField(self, arg_str, *arg, **kw):
        """
        PurpleMimeDecodeField method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMimeDecodeField( arg_str, *arg, **kw)
    
    def PurpleTimeBuild(self, arg_year, arg_month, arg_day, arg_hour, arg_min, arg_sec, *arg, **kw):
        """
        PurpleTimeBuild method:

        Parameters
        ----------

        year:
            type: i,
            direction: in;
            month:
            type: i,
            direction: in;
            day:
            type: i,
            direction: in;
            hour:
            type: i,
            direction: in;
            min:
            type: i,
            direction: in;
            sec:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleTimeBuild( arg_year, arg_month, arg_day, arg_hour, arg_min, arg_sec, *arg, **kw)
    
    def PurpleMarkupEscapeText(self, arg_text, arg_length, *arg, **kw):
        """
        PurpleMarkupEscapeText method:

        Parameters
        ----------

        text:
            type: s,
            direction: in;
            length:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupEscapeText( arg_text, arg_length, *arg, **kw)
    
    def PurpleMarkupStripHtml(self, arg_str, *arg, **kw):
        """
        PurpleMarkupStripHtml method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupStripHtml( arg_str, *arg, **kw)
    
    def PurpleMarkupLinkify(self, arg_str, *arg, **kw):
        """
        PurpleMarkupLinkify method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupLinkify( arg_str, *arg, **kw)
    
    def PurpleUnescapeText(self, arg_text, *arg, **kw):
        """
        PurpleUnescapeText method:

        Parameters
        ----------

        text:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUnescapeText( arg_text, *arg, **kw)
    
    def PurpleUnescapeHtml(self, arg_html, *arg, **kw):
        """
        PurpleUnescapeHtml method:

        Parameters
        ----------

        html:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUnescapeHtml( arg_html, *arg, **kw)
    
    def PurpleMarkupSlice(self, arg_str, arg_x, arg_y, *arg, **kw):
        """
        PurpleMarkupSlice method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            x:
            type: i,
            direction: in;
            y:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupSlice( arg_str, arg_x, arg_y, *arg, **kw)
    
    def PurpleMarkupGetTagName(self, arg_tag, *arg, **kw):
        """
        PurpleMarkupGetTagName method:

        Parameters
        ----------

        tag:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupGetTagName( arg_tag, *arg, **kw)
    
    def PurpleMarkupUnescapeEntity(self, arg_text, arg_length, *arg, **kw):
        """
        PurpleMarkupUnescapeEntity method:

        Parameters
        ----------

        text:
            type: s,
            direction: in;
            length:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupUnescapeEntity( arg_text, arg_length, *arg, **kw)
    
    def PurpleMarkupGetCssProperty(self, arg_style, arg_opt, *arg, **kw):
        """
        PurpleMarkupGetCssProperty method:

        Parameters
        ----------

        style:
            type: s,
            direction: in;
            opt:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupGetCssProperty( arg_style, arg_opt, *arg, **kw)
    
    def PurpleMarkupIsRtl(self, arg_html, *arg, **kw):
        """
        PurpleMarkupIsRtl method:

        Parameters
        ----------

        html:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleMarkupIsRtl( arg_html, *arg, **kw)
    
    def PurpleHomeDir(self, *arg, **kw):
        """
        PurpleHomeDir method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleHomeDir( *arg, **kw)
    
    def PurpleUserDir(self, *arg, **kw):
        """
        PurpleUserDir method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUserDir( *arg, **kw)
    
    def PurpleUtilSetUserDir(self, arg_dir, *arg, **kw):
        """
        PurpleUtilSetUserDir method:

        Parameters
        ----------

        dir:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleUtilSetUserDir( arg_dir, *arg, **kw)
    
    def PurpleBuildDir(self, arg_path, arg_mode, *arg, **kw):
        """
        PurpleBuildDir method:

        Parameters
        ----------

        path:
            type: s,
            direction: in;
            mode:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleBuildDir( arg_path, arg_mode, *arg, **kw)
    
    def PurpleUtilWriteDataToFile(self, arg_filename, arg_data, arg_size, *arg, **kw):
        """
        PurpleUtilWriteDataToFile method:

        Parameters
        ----------

        filename:
            type: s,
            direction: in;
            data:
            type: s,
            direction: in;
            size:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtilWriteDataToFile( arg_filename, arg_data, arg_size, *arg, **kw)
    
    def PurpleUtilWriteDataToFileAbsolute(self, arg_filename_full, arg_data, arg_size, *arg, **kw):
        """
        PurpleUtilWriteDataToFileAbsolute method:

        Parameters
        ----------

        filename_full:
            type: s,
            direction: in;
            data:
            type: s,
            direction: in;
            size:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtilWriteDataToFileAbsolute( arg_filename_full, arg_data, arg_size, *arg, **kw)
    
    def PurpleProgramIsValid(self, arg_program, *arg, **kw):
        """
        PurpleProgramIsValid method:

        Parameters
        ----------

        program:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleProgramIsValid( arg_program, *arg, **kw)
    
    def PurpleRunningGnome(self, *arg, **kw):
        """
        PurpleRunningGnome method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRunningGnome( *arg, **kw)
    
    def PurpleRunningKde(self, *arg, **kw):
        """
        PurpleRunningKde method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRunningKde( *arg, **kw)
    
    def PurpleRunningOsx(self, *arg, **kw):
        """
        PurpleRunningOsx method:

        Parameters
        ----------

        RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleRunningOsx( *arg, **kw)
    
    def PurpleFdGetIp(self, arg_fd, *arg, **kw):
        """
        PurpleFdGetIp method:

        Parameters
        ----------

        fd:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleFdGetIp( arg_fd, *arg, **kw)
    
    def PurpleSocketGetFamily(self, arg_fd, *arg, **kw):
        """
        PurpleSocketGetFamily method:

        Parameters
        ----------

        fd:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSocketGetFamily( arg_fd, *arg, **kw)
    
    def PurpleSocketSpeaksIpv4(self, arg_fd, *arg, **kw):
        """
        PurpleSocketSpeaksIpv4 method:

        Parameters
        ----------

        fd:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleSocketSpeaksIpv4( arg_fd, *arg, **kw)
    
    def PurpleStrequal(self, arg_left, arg_right, *arg, **kw):
        """
        PurpleStrequal method:

        Parameters
        ----------

        left:
            type: s,
            direction: in;
            right:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrequal( arg_left, arg_right, *arg, **kw)
    
    def PurpleNormalize(self, arg_account, arg_str, *arg, **kw):
        """
        PurpleNormalize method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNormalize( arg_account, arg_str, *arg, **kw)
    
    def PurpleNormalizeNocase(self, arg_account, arg_str, *arg, **kw):
        """
        PurpleNormalizeNocase method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleNormalizeNocase( arg_account, arg_str, *arg, **kw)
    
    def PurpleStrHasPrefix(self, arg_s, arg_p, *arg, **kw):
        """
        PurpleStrHasPrefix method:

        Parameters
        ----------

        s:
            type: s,
            direction: in;
            p:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrHasPrefix( arg_s, arg_p, *arg, **kw)
    
    def PurpleStrHasSuffix(self, arg_s, arg_x, *arg, **kw):
        """
        PurpleStrHasSuffix method:

        Parameters
        ----------

        s:
            type: s,
            direction: in;
            x:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrHasSuffix( arg_s, arg_x, *arg, **kw)
    
    def PurpleStrdupWithhtml(self, arg_src, *arg, **kw):
        """
        PurpleStrdupWithhtml method:

        Parameters
        ----------

        src:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrdupWithhtml( arg_src, *arg, **kw)
    
    def PurpleStrAddCr(self, arg_str, *arg, **kw):
        """
        PurpleStrAddCr method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrAddCr( arg_str, *arg, **kw)
    
    def PurpleStrreplace(self, arg_string, arg_delimiter, arg_replacement, *arg, **kw):
        """
        PurpleStrreplace method:

        Parameters
        ----------

        string:
            type: s,
            direction: in;
            delimiter:
            type: s,
            direction: in;
            replacement:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrreplace( arg_string, arg_delimiter, arg_replacement, *arg, **kw)
    
    def PurpleUtf8NcrEncode(self, arg_in, *arg, **kw):
        """
        PurpleUtf8NcrEncode method:

        Parameters
        ----------

        in:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8NcrEncode( arg_in, *arg, **kw)
    
    def PurpleUtf8NcrDecode(self, arg_in, *arg, **kw):
        """
        PurpleUtf8NcrDecode method:

        Parameters
        ----------

        in:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8NcrDecode( arg_in, *arg, **kw)
    
    def PurpleStrcasereplace(self, arg_string, arg_delimiter, arg_replacement, *arg, **kw):
        """
        PurpleStrcasereplace method:

        Parameters
        ----------

        string:
            type: s,
            direction: in;
            delimiter:
            type: s,
            direction: in;
            replacement:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrcasereplace( arg_string, arg_delimiter, arg_replacement, *arg, **kw)
    
    def PurpleStrcasestr(self, arg_haystack, arg_needle, *arg, **kw):
        """
        PurpleStrcasestr method:

        Parameters
        ----------

        haystack:
            type: s,
            direction: in;
            needle:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrcasestr( arg_haystack, arg_needle, *arg, **kw)
    
    def PurpleStrSizeToUnits(self, arg_size, *arg, **kw):
        """
        PurpleStrSizeToUnits method:

        Parameters
        ----------

        size:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrSizeToUnits( arg_size, *arg, **kw)
    
    def PurpleStrSecondsToString(self, arg_sec, *arg, **kw):
        """
        PurpleStrSecondsToString method:

        Parameters
        ----------

        sec:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrSecondsToString( arg_sec, *arg, **kw)
    
    def PurpleStrBinaryToAscii(self, arg_binary, arg_len, *arg, **kw):
        """
        PurpleStrBinaryToAscii method:

        Parameters
        ----------

        binary:
            type: s,
            direction: in;
            len:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleStrBinaryToAscii( arg_binary, arg_len, *arg, **kw)
    
    def PurpleGotProtocolHandlerUri(self, arg_uri, *arg, **kw):
        """
        PurpleGotProtocolHandlerUri method:

        Parameters
        ----------

        uri:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleGotProtocolHandlerUri( arg_uri, *arg, **kw)
    
    def PurpleUtilFetchUrlCancel(self, arg_url_data, *arg, **kw):
        """
        PurpleUtilFetchUrlCancel method:

        Parameters
        ----------

        url_data:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurpleUtilFetchUrlCancel( arg_url_data, *arg, **kw)
    
    def PurpleUrlDecode(self, arg_str, *arg, **kw):
        """
        PurpleUrlDecode method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUrlDecode( arg_str, *arg, **kw)
    
    def PurpleUrlEncode(self, arg_str, *arg, **kw):
        """
        PurpleUrlEncode method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUrlEncode( arg_str, *arg, **kw)
    
    def PurpleEmailIsValid(self, arg_address, *arg, **kw):
        """
        PurpleEmailIsValid method:

        Parameters
        ----------

        address:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleEmailIsValid( arg_address, *arg, **kw)
    
    def PurpleIpAddressIsValid(self, arg_ip, *arg, **kw):
        """
        PurpleIpAddressIsValid method:

        Parameters
        ----------

        ip:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleIpAddressIsValid( arg_ip, *arg, **kw)
    
    def PurpleIpv4AddressIsValid(self, arg_ip, *arg, **kw):
        """
        PurpleIpv4AddressIsValid method:

        Parameters
        ----------

        ip:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleIpv4AddressIsValid( arg_ip, *arg, **kw)
    
    def PurpleIpv6AddressIsValid(self, arg_ip, *arg, **kw):
        """
        PurpleIpv6AddressIsValid method:

        Parameters
        ----------

        ip:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleIpv6AddressIsValid( arg_ip, *arg, **kw)
    
    def PurpleUriListExtractUris(self, arg_uri_list, *arg, **kw):
        """
        PurpleUriListExtractUris method:

        Parameters
        ----------

        uri_list:
            type: s,
            direction: in;
            RESULT:
            type: as,
            direction: out;
            
        """
        return self._dbus_object.PurpleUriListExtractUris( arg_uri_list, *arg, **kw)
    
    def PurpleUriListExtractFilenames(self, arg_uri_list, *arg, **kw):
        """
        PurpleUriListExtractFilenames method:

        Parameters
        ----------

        uri_list:
            type: s,
            direction: in;
            RESULT:
            type: as,
            direction: out;
            
        """
        return self._dbus_object.PurpleUriListExtractFilenames( arg_uri_list, *arg, **kw)
    
    def PurpleUtf8TryConvert(self, arg_str, *arg, **kw):
        """
        PurpleUtf8TryConvert method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8TryConvert( arg_str, *arg, **kw)
    
    def PurpleUtf8Salvage(self, arg_str, *arg, **kw):
        """
        PurpleUtf8Salvage method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8Salvage( arg_str, *arg, **kw)
    
    def PurpleUtf8StripUnprintables(self, arg_str, *arg, **kw):
        """
        PurpleUtf8StripUnprintables method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8StripUnprintables( arg_str, *arg, **kw)
    
    def PurpleUtf8Strcasecmp(self, arg_a, arg_b, *arg, **kw):
        """
        PurpleUtf8Strcasecmp method:

        Parameters
        ----------

        a:
            type: s,
            direction: in;
            b:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8Strcasecmp( arg_a, arg_b, *arg, **kw)
    
    def PurpleUtf8HasWord(self, arg_haystack, arg_needle, *arg, **kw):
        """
        PurpleUtf8HasWord method:

        Parameters
        ----------

        haystack:
            type: s,
            direction: in;
            needle:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleUtf8HasWord( arg_haystack, arg_needle, *arg, **kw)
    
    def PurpleTextStripMnemonic(self, arg_in, *arg, **kw):
        """
        PurpleTextStripMnemonic method:

        Parameters
        ----------

        in:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleTextStripMnemonic( arg_in, *arg, **kw)
    
    def PurpleUnescapeFilename(self, arg_str, *arg, **kw):
        """
        PurpleUnescapeFilename method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUnescapeFilename( arg_str, *arg, **kw)
    
    def PurpleEscapeFilename(self, arg_str, *arg, **kw):
        """
        PurpleEscapeFilename method:

        Parameters
        ----------

        str:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleEscapeFilename( arg_str, *arg, **kw)
    
    def PurpleOscarConvert(self, arg_act, arg_protocol, *arg, **kw):
        """
        PurpleOscarConvert method:

        Parameters
        ----------

        act:
            type: s,
            direction: in;
            protocol:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleOscarConvert( arg_act, arg_protocol, *arg, **kw)
    
    def PurpleRestoreDefaultSignalHandlers(self, *arg, **kw):
        """
        PurpleRestoreDefaultSignalHandlers method:
        """
        return self._dbus_object.PurpleRestoreDefaultSignalHandlers( *arg, **kw)
    
    def PurpleGetHostName(self, *arg, **kw):
        """
        PurpleGetHostName method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleGetHostName( *arg, **kw)
    
    def PurpleUuidRandom(self, *arg, **kw):
        """
        PurpleUuidRandom method:

        Parameters
        ----------

        RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleUuidRandom( *arg, **kw)
    
    def XmlnodeInsertChild(self, arg_parent, arg_child, *arg, **kw):
        """
        XmlnodeInsertChild method:

        Parameters
        ----------

        parent:
            type: i,
            direction: in;
            child:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeInsertChild( arg_parent, arg_child, *arg, **kw)
    
    def XmlnodeInsertData(self, arg_node, arg_data, arg_size, *arg, **kw):
        """
        XmlnodeInsertData method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            data:
            type: s,
            direction: in;
            size:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeInsertData( arg_node, arg_data, arg_size, *arg, **kw)
    
    def XmlnodeGetData(self, arg_node, *arg, **kw):
        """
        XmlnodeGetData method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetData( arg_node, *arg, **kw)
    
    def XmlnodeGetDataUnescaped(self, arg_node, *arg, **kw):
        """
        XmlnodeGetDataUnescaped method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetDataUnescaped( arg_node, *arg, **kw)
    
    def XmlnodeSetAttrib(self, arg_node, arg_attr, arg_value, *arg, **kw):
        """
        XmlnodeSetAttrib method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetAttrib( arg_node, arg_attr, arg_value, *arg, **kw)
    
    def XmlnodeSetAttribWithPrefix(self, arg_node, arg_attr, arg_prefix, arg_value, *arg, **kw):
        """
        XmlnodeSetAttribWithPrefix method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            prefix:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetAttribWithPrefix( arg_node, arg_attr, arg_prefix, arg_value, *arg, **kw)
    
    def XmlnodeSetAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, arg_value, *arg, **kw):
        """
        XmlnodeSetAttribWithNamespace method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            xmlns:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetAttribWithNamespace( arg_node, arg_attr, arg_xmlns, arg_value, *arg, **kw)
    
    def XmlnodeSetAttribFull(self, arg_node, arg_attr, arg_xmlns, arg_prefix, arg_value, *arg, **kw):
        """
        XmlnodeSetAttribFull method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            xmlns:
            type: s,
            direction: in;
            prefix:
            type: s,
            direction: in;
            value:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetAttribFull( arg_node, arg_attr, arg_xmlns, arg_prefix, arg_value, *arg, **kw)
    
    def XmlnodeGetAttrib(self, arg_node, arg_attr, *arg, **kw):
        """
        XmlnodeGetAttrib method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetAttrib( arg_node, arg_attr, *arg, **kw)
    
    def XmlnodeGetAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, *arg, **kw):
        """
        XmlnodeGetAttribWithNamespace method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            xmlns:
            type: s,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetAttribWithNamespace( arg_node, arg_attr, arg_xmlns, *arg, **kw)
    
    def XmlnodeRemoveAttrib(self, arg_node, arg_attr, *arg, **kw):
        """
        XmlnodeRemoveAttrib method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeRemoveAttrib( arg_node, arg_attr, *arg, **kw)
    
    def XmlnodeRemoveAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, *arg, **kw):
        """
        XmlnodeRemoveAttribWithNamespace method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            attr:
            type: s,
            direction: in;
            xmlns:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeRemoveAttribWithNamespace( arg_node, arg_attr, arg_xmlns, *arg, **kw)
    
    def XmlnodeSetNamespace(self, arg_node, arg_xmlns, *arg, **kw):
        """
        XmlnodeSetNamespace method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            xmlns:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetNamespace( arg_node, arg_xmlns, *arg, **kw)
    
    def XmlnodeGetNamespace(self, arg_node, *arg, **kw):
        """
        XmlnodeGetNamespace method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetNamespace( arg_node, *arg, **kw)
    
    def XmlnodeSetPrefix(self, arg_node, arg_prefix, *arg, **kw):
        """
        XmlnodeSetPrefix method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            prefix:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeSetPrefix( arg_node, arg_prefix, *arg, **kw)
    
    def XmlnodeGetPrefix(self, arg_node, *arg, **kw):
        """
        XmlnodeGetPrefix method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeGetPrefix( arg_node, *arg, **kw)
    
    def XmlnodeToStr(self, arg_node, arg_len, *arg, **kw):
        """
        XmlnodeToStr method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            len:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeToStr( arg_node, arg_len, *arg, **kw)
    
    def XmlnodeToFormattedStr(self, arg_node, arg_len, *arg, **kw):
        """
        XmlnodeToFormattedStr method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            len:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.XmlnodeToFormattedStr( arg_node, arg_len, *arg, **kw)
    
    def XmlnodeFree(self, arg_node, *arg, **kw):
        """
        XmlnodeFree method:

        Parameters
        ----------

        node:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.XmlnodeFree( arg_node, *arg, **kw)
    
    def PurpleAttentionTypeNew(self, arg_ulname, arg_name, arg_inc_desc, arg_out_desc, *arg, **kw):
        """
        PurpleAttentionTypeNew method:

        Parameters
        ----------

        ulname:
            type: s,
            direction: in;
            name:
            type: s,
            direction: in;
            inc_desc:
            type: s,
            direction: in;
            out_desc:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeNew( arg_ulname, arg_name, arg_inc_desc, arg_out_desc, *arg, **kw)
    
    def PurpleAttentionTypeSetName(self, arg_type, arg_name, *arg, **kw):
        """
        PurpleAttentionTypeSetName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAttentionTypeSetName( arg_type, arg_name, *arg, **kw)
    
    def PurpleAttentionTypeSetIncomingDesc(self, arg_type, arg_desc, *arg, **kw):
        """
        PurpleAttentionTypeSetIncomingDesc method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            desc:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAttentionTypeSetIncomingDesc( arg_type, arg_desc, *arg, **kw)
    
    def PurpleAttentionTypeSetOutgoingDesc(self, arg_type, arg_desc, *arg, **kw):
        """
        PurpleAttentionTypeSetOutgoingDesc method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            desc:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAttentionTypeSetOutgoingDesc( arg_type, arg_desc, *arg, **kw)
    
    def PurpleAttentionTypeSetIconName(self, arg_type, arg_name, *arg, **kw):
        """
        PurpleAttentionTypeSetIconName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAttentionTypeSetIconName( arg_type, arg_name, *arg, **kw)
    
    def PurpleAttentionTypeSetUnlocalizedName(self, arg_type, arg_ulname, *arg, **kw):
        """
        PurpleAttentionTypeSetUnlocalizedName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            ulname:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurpleAttentionTypeSetUnlocalizedName( arg_type, arg_ulname, *arg, **kw)
    
    def PurpleAttentionTypeGetName(self, arg_type, *arg, **kw):
        """
        PurpleAttentionTypeGetName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeGetName( arg_type, *arg, **kw)
    
    def PurpleAttentionTypeGetIncomingDesc(self, arg_type, *arg, **kw):
        """
        PurpleAttentionTypeGetIncomingDesc method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeGetIncomingDesc( arg_type, *arg, **kw)
    
    def PurpleAttentionTypeGetOutgoingDesc(self, arg_type, *arg, **kw):
        """
        PurpleAttentionTypeGetOutgoingDesc method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeGetOutgoingDesc( arg_type, *arg, **kw)
    
    def PurpleAttentionTypeGetIconName(self, arg_type, *arg, **kw):
        """
        PurpleAttentionTypeGetIconName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeGetIconName( arg_type, *arg, **kw)
    
    def PurpleAttentionTypeGetUnlocalizedName(self, arg_type, *arg, **kw):
        """
        PurpleAttentionTypeGetUnlocalizedName method:

        Parameters
        ----------

        type:
            type: i,
            direction: in;
            RESULT:
            type: s,
            direction: out;
            
        """
        return self._dbus_object.PurpleAttentionTypeGetUnlocalizedName( arg_type, *arg, **kw)
    
    def PurplePrplGotAccountIdle(self, arg_account, arg_idle, arg_idle_time, *arg, **kw):
        """
        PurplePrplGotAccountIdle method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            idle:
            type: i,
            direction: in;
            idle_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotAccountIdle( arg_account, arg_idle, arg_idle_time, *arg, **kw)
    
    def PurplePrplGotAccountLoginTime(self, arg_account, arg_login_time, *arg, **kw):
        """
        PurplePrplGotAccountLoginTime method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            login_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotAccountLoginTime( arg_account, arg_login_time, *arg, **kw)
    
    def PurplePrplGotAccountActions(self, arg_account, *arg, **kw):
        """
        PurplePrplGotAccountActions method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotAccountActions( arg_account, *arg, **kw)
    
    def PurplePrplGotUserIdle(self, arg_account, arg_name, arg_idle, arg_idle_time, *arg, **kw):
        """
        PurplePrplGotUserIdle method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            idle:
            type: i,
            direction: in;
            idle_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotUserIdle( arg_account, arg_name, arg_idle, arg_idle_time, *arg, **kw)
    
    def PurplePrplGotUserLoginTime(self, arg_account, arg_name, arg_login_time, *arg, **kw):
        """
        PurplePrplGotUserLoginTime method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            login_time:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotUserLoginTime( arg_account, arg_name, arg_login_time, *arg, **kw)
    
    def PurplePrplGotUserStatusDeactive(self, arg_account, arg_name, arg_status_id, *arg, **kw):
        """
        PurplePrplGotUserStatusDeactive method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            name:
            type: s,
            direction: in;
            status_id:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotUserStatusDeactive( arg_account, arg_name, arg_status_id, *arg, **kw)
    
    def PurplePrplChangeAccountStatus(self, arg_account, arg_old_status, arg_new_status, *arg, **kw):
        """
        PurplePrplChangeAccountStatus method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            old_status:
            type: i,
            direction: in;
            new_status:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplChangeAccountStatus( arg_account, arg_old_status, arg_new_status, *arg, **kw)
    
    def PurplePrplGetStatuses(self, arg_account, arg_presence, *arg, **kw):
        """
        PurplePrplGetStatuses method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            presence:
            type: i,
            direction: in;
            RESULT:
            type: ai,
            direction: out;
            
        """
        return self._dbus_object.PurplePrplGetStatuses( arg_account, arg_presence, *arg, **kw)
    
    def PurplePrplSendAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
        """
        PurplePrplSendAttention method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type_code:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplSendAttention( arg_gc, arg_who, arg_type_code, *arg, **kw)
    
    def PurplePrplGotAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
        """
        PurplePrplGotAttention method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type_code:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotAttention( arg_gc, arg_who, arg_type_code, *arg, **kw)
    
    def PurplePrplGotAttentionInChat(self, arg_gc, arg_id, arg_who, arg_type_code, *arg, **kw):
        """
        PurplePrplGotAttentionInChat method:

        Parameters
        ----------

        gc:
            type: i,
            direction: in;
            id:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type_code:
            type: i,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotAttentionInChat( arg_gc, arg_id, arg_who, arg_type_code, *arg, **kw)
    
    def PurplePrplGetMediaCaps(self, arg_account, arg_who, *arg, **kw):
        """
        PurplePrplGetMediaCaps method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrplGetMediaCaps( arg_account, arg_who, *arg, **kw)
    
    def PurplePrplInitiateMedia(self, arg_account, arg_who, arg_type, *arg, **kw):
        """
        PurplePrplInitiateMedia method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            type:
            type: i,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurplePrplInitiateMedia( arg_account, arg_who, arg_type, *arg, **kw)
    
    def PurplePrplGotMediaCaps(self, arg_account, arg_who, *arg, **kw):
        """
        PurplePrplGotMediaCaps method:

        Parameters
        ----------

        account:
            type: i,
            direction: in;
            who:
            type: s,
            direction: in;
            
        """
        return self._dbus_object.PurplePrplGotMediaCaps( arg_account, arg_who, *arg, **kw)
    
    def PurpleFindPrpl(self, arg_id, *arg, **kw):
        """
        PurpleFindPrpl method:

        Parameters
        ----------

        id:
            type: s,
            direction: in;
            RESULT:
            type: i,
            direction: out;
            
        """
        return self._dbus_object.PurpleFindPrpl( arg_id, *arg, **kw)
    
    @property
    def AccountConnecting(self, *arg, **kw):
        """

        AccountConnecting signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountConnecting.setter
    def AccountConnecting(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountConnecting", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountDisabled(self, *arg, **kw):
        """

        AccountDisabled signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountDisabled.setter
    def AccountDisabled(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountDisabled", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountEnabled(self, *arg, **kw):
        """

        AccountEnabled signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountEnabled.setter
    def AccountEnabled(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountEnabled", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountSettingInfo(self, *arg, **kw):
        """

        AccountSettingInfo signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountSettingInfo.setter
    def AccountSettingInfo(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountSettingInfo", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountSetInfo(self, *arg, **kw):
        """

        AccountSetInfo signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountSetInfo.setter
    def AccountSetInfo(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountSetInfo", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountCreated(self, *arg, **kw):
        """

        AccountCreated signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountCreated.setter
    def AccountCreated(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountCreated", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountDestroying(self, *arg, **kw):
        """

        AccountDestroying signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountDestroying.setter
    def AccountDestroying(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountDestroying", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAdded(self, *arg, **kw):
        """

        AccountAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAdded.setter
    def AccountAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountRemoved(self, *arg, **kw):
        """

        AccountRemoved signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountRemoved.setter
    def AccountRemoved(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountRemoved", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountStatusChanged(self, *arg, **kw):
        """

        AccountStatusChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @AccountStatusChanged.setter
    def AccountStatusChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountStatusChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountActionsChanged(self, *arg, **kw):
        """

        AccountActionsChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountActionsChanged.setter
    def AccountActionsChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountActionsChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAliasChanged(self, *arg, **kw):
        """

        AccountAliasChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAliasChanged.setter
    def AccountAliasChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAliasChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAuthorizationRequested(self, *arg, **kw):
        """

        AccountAuthorizationRequested signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAuthorizationRequested.setter
    def AccountAuthorizationRequested(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAuthorizationRequested", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAuthorizationRequestedWithMessage(self, *arg, **kw):
        """

        AccountAuthorizationRequestedWithMessage signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAuthorizationRequestedWithMessage.setter
    def AccountAuthorizationRequestedWithMessage(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAuthorizationRequestedWithMessage", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAuthorizationDenied(self, *arg, **kw):
        """

        AccountAuthorizationDenied signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAuthorizationDenied.setter
    def AccountAuthorizationDenied(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAuthorizationDenied", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountAuthorizationGranted(self, *arg, **kw):
        """

        AccountAuthorizationGranted signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @AccountAuthorizationGranted.setter
    def AccountAuthorizationGranted(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountAuthorizationGranted", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountErrorChanged(self, *arg, **kw):
        """

        AccountErrorChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @AccountErrorChanged.setter
    def AccountErrorChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountErrorChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountSignedOn(self, *arg, **kw):
        """

        AccountSignedOn signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountSignedOn.setter
    def AccountSignedOn(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountSignedOn", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountSignedOff(self, *arg, **kw):
        """

        AccountSignedOff signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @AccountSignedOff.setter
    def AccountSignedOff(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountSignedOff", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def AccountConnectionError(self, *arg, **kw):
        """

        AccountConnectionError signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @AccountConnectionError.setter
    def AccountConnectionError(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "AccountConnectionError", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyStatusChanged(self, *arg, **kw):
        """

        BuddyStatusChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyStatusChanged.setter
    def BuddyStatusChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyStatusChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyPrivacyChanged(self, *arg, **kw):
        """

        BuddyPrivacyChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyPrivacyChanged.setter
    def BuddyPrivacyChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyPrivacyChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyIdleChanged(self, *arg, **kw):
        """

        BuddyIdleChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyIdleChanged.setter
    def BuddyIdleChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyIdleChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddySignedOn(self, *arg, **kw):
        """

        BuddySignedOn signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddySignedOn.setter
    def BuddySignedOn(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddySignedOn", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddySignedOff(self, *arg, **kw):
        """

        BuddySignedOff signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddySignedOff.setter
    def BuddySignedOff(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddySignedOff", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyGotLoginTime(self, *arg, **kw):
        """

        BuddyGotLoginTime signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyGotLoginTime.setter
    def BuddyGotLoginTime(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyGotLoginTime", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BlistNodeAdded(self, *arg, **kw):
        """

        BlistNodeAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BlistNodeAdded.setter
    def BlistNodeAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BlistNodeAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BlistNodeRemoved(self, *arg, **kw):
        """

        BlistNodeRemoved signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BlistNodeRemoved.setter
    def BlistNodeRemoved(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BlistNodeRemoved", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyAdded(self, *arg, **kw):
        """

        BuddyAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyAdded.setter
    def BuddyAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyRemoved(self, *arg, **kw):
        """

        BuddyRemoved signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyRemoved.setter
    def BuddyRemoved(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyRemoved", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyIconChanged(self, *arg, **kw):
        """

        BuddyIconChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyIconChanged.setter
    def BuddyIconChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyIconChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def UpdateIdle(self, *arg, **kw):
        """

        UpdateIdle signal:
        """
        return None

    @UpdateIdle.setter
    def UpdateIdle(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "UpdateIdle", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BlistNodeExtendedMenu(self, *arg, **kw):
        """

        BlistNodeExtendedMenu signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @BlistNodeExtendedMenu.setter
    def BlistNodeExtendedMenu(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BlistNodeExtendedMenu", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BlistNodeAliased(self, *arg, **kw):
        """

        BlistNodeAliased signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @BlistNodeAliased.setter
    def BlistNodeAliased(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BlistNodeAliased", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyCapsChanged(self, *arg, **kw):
        """

        BuddyCapsChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyCapsChanged.setter
    def BuddyCapsChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyCapsChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CertificateStored(self, *arg, **kw):
        """

        CertificateStored signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @CertificateStored.setter
    def CertificateStored(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CertificateStored", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CertificateDeleted(self, *arg, **kw):
        """

        CertificateDeleted signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @CertificateDeleted.setter
    def CertificateDeleted(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CertificateDeleted", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CipherAdded(self, *arg, **kw):
        """

        CipherAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @CipherAdded.setter
    def CipherAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CipherAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CipherRemoved(self, *arg, **kw):
        """

        CipherRemoved signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @CipherRemoved.setter
    def CipherRemoved(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CipherRemoved", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CmdAdded(self, *arg, **kw):
        """

        CmdAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @CmdAdded.setter
    def CmdAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CmdAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def CmdRemoved(self, *arg, **kw):
        """

        CmdRemoved signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @CmdRemoved.setter
    def CmdRemoved(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "CmdRemoved", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SigningOn(self, *arg, **kw):
        """

        SigningOn signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SigningOn.setter
    def SigningOn(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SigningOn", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SignedOn(self, *arg, **kw):
        """

        SignedOn signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SignedOn.setter
    def SignedOn(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SignedOn", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SigningOff(self, *arg, **kw):
        """

        SigningOff signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SigningOff.setter
    def SigningOff(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SigningOff", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SignedOff(self, *arg, **kw):
        """

        SignedOff signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SignedOff.setter
    def SignedOff(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SignedOff", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ConnectionError(self, *arg, **kw):
        """

        ConnectionError signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ConnectionError.setter
    def ConnectionError(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ConnectionError", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def Autojoin(self, *arg, **kw):
        """

        Autojoin signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @Autojoin.setter
    def Autojoin(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "Autojoin", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def WritingImMsg(self, *arg, **kw):
        """

        WritingImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @WritingImMsg.setter
    def WritingImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "WritingImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def WroteImMsg(self, *arg, **kw):
        """

        WroteImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @WroteImMsg.setter
    def WroteImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "WroteImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SentAttention(self, *arg, **kw):
        """

        SentAttention signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: u,
            direction: in;
            
        """
        return None

    @SentAttention.setter
    def SentAttention(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SentAttention", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def GotAttention(self, *arg, **kw):
        """

        GotAttention signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: u,
            direction: in;
            
        """
        return None

    @GotAttention.setter
    def GotAttention(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "GotAttention", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SendingImMsg(self, *arg, **kw):
        """

        SendingImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @SendingImMsg.setter
    def SendingImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SendingImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SentImMsg(self, *arg, **kw):
        """

        SentImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @SentImMsg.setter
    def SentImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SentImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ReceivingImMsg(self, *arg, **kw):
        """

        ReceivingImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: i,
            direction: in;
            
        """
        return None

    @ReceivingImMsg.setter
    def ReceivingImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ReceivingImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ReceivedImMsg(self, *arg, **kw):
        """

        ReceivedImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @ReceivedImMsg.setter
    def ReceivedImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ReceivedImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BlockedImMsg(self, *arg, **kw):
        """

        BlockedImMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: u,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @BlockedImMsg.setter
    def BlockedImMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BlockedImMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def WritingChatMsg(self, *arg, **kw):
        """

        WritingChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @WritingChatMsg.setter
    def WritingChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "WritingChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def WroteChatMsg(self, *arg, **kw):
        """

        WroteChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @WroteChatMsg.setter
    def WroteChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "WroteChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SendingChatMsg(self, *arg, **kw):
        """

        SendingChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: u,
            direction: in;
            
        """
        return None

    @SendingChatMsg.setter
    def SendingChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SendingChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SentChatMsg(self, *arg, **kw):
        """

        SentChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: u,
            direction: in;
            
        """
        return None

    @SentChatMsg.setter
    def SentChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SentChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ReceivingChatMsg(self, *arg, **kw):
        """

        ReceivingChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: i,
            direction: in;
            
        """
        return None

    @ReceivingChatMsg.setter
    def ReceivingChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ReceivingChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ReceivedChatMsg(self, *arg, **kw):
        """

        ReceivedChatMsg signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @ReceivedChatMsg.setter
    def ReceivedChatMsg(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ReceivedChatMsg", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ConversationCreated(self, *arg, **kw):
        """

        ConversationCreated signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @ConversationCreated.setter
    def ConversationCreated(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ConversationCreated", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ConversationUpdated(self, *arg, **kw):
        """

        ConversationUpdated signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: u,
            direction: in;
            
        """
        return None

    @ConversationUpdated.setter
    def ConversationUpdated(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ConversationUpdated", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def DeletingConversation(self, *arg, **kw):
        """

        DeletingConversation signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @DeletingConversation.setter
    def DeletingConversation(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "DeletingConversation", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyTyping(self, *arg, **kw):
        """

        BuddyTyping signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyTyping.setter
    def BuddyTyping(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyTyping", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyTyped(self, *arg, **kw):
        """

        BuddyTyped signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyTyped.setter
    def BuddyTyped(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyTyped", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def BuddyTypingStopped(self, *arg, **kw):
        """

        BuddyTypingStopped signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @BuddyTypingStopped.setter
    def BuddyTypingStopped(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "BuddyTypingStopped", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatBuddyJoining(self, *arg, **kw):
        """

        ChatBuddyJoining signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: u,
            direction: in;
            
        """
        return None

    @ChatBuddyJoining.setter
    def ChatBuddyJoining(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatBuddyJoining", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatBuddyJoined(self, *arg, **kw):
        """

        ChatBuddyJoined signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: u,
            direction: in;
            arg4:
            type: u,
            direction: in;
            
        """
        return None

    @ChatBuddyJoined.setter
    def ChatBuddyJoined(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatBuddyJoined", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatBuddyFlags(self, *arg, **kw):
        """

        ChatBuddyFlags signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: u,
            direction: in;
            arg4:
            type: u,
            direction: in;
            
        """
        return None

    @ChatBuddyFlags.setter
    def ChatBuddyFlags(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatBuddyFlags", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatBuddyLeaving(self, *arg, **kw):
        """

        ChatBuddyLeaving signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ChatBuddyLeaving.setter
    def ChatBuddyLeaving(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatBuddyLeaving", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatBuddyLeft(self, *arg, **kw):
        """

        ChatBuddyLeft signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ChatBuddyLeft.setter
    def ChatBuddyLeft(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatBuddyLeft", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def DeletingChatBuddy(self, *arg, **kw):
        """

        DeletingChatBuddy signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @DeletingChatBuddy.setter
    def DeletingChatBuddy(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "DeletingChatBuddy", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatInvitingUser(self, *arg, **kw):
        """

        ChatInvitingUser signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ChatInvitingUser.setter
    def ChatInvitingUser(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatInvitingUser", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatInvitedUser(self, *arg, **kw):
        """

        ChatInvitedUser signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ChatInvitedUser.setter
    def ChatInvitedUser(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatInvitedUser", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatInvited(self, *arg, **kw):
        """

        ChatInvited signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: i,
            direction: in;
            
        """
        return None

    @ChatInvited.setter
    def ChatInvited(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatInvited", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatInviteBlocked(self, *arg, **kw):
        """

        ChatInviteBlocked signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: i,
            direction: in;
            
        """
        return None

    @ChatInviteBlocked.setter
    def ChatInviteBlocked(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatInviteBlocked", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatJoined(self, *arg, **kw):
        """

        ChatJoined signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @ChatJoined.setter
    def ChatJoined(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatJoined", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatJoinFailed(self, *arg, **kw):
        """

        ChatJoinFailed signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @ChatJoinFailed.setter
    def ChatJoinFailed(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatJoinFailed", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatLeft(self, *arg, **kw):
        """

        ChatLeft signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @ChatLeft.setter
    def ChatLeft(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatLeft", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ChatTopicChanged(self, *arg, **kw):
        """

        ChatTopicChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @ChatTopicChanged.setter
    def ChatTopicChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ChatTopicChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ClearedMessageHistory(self, *arg, **kw):
        """

        ClearedMessageHistory signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @ClearedMessageHistory.setter
    def ClearedMessageHistory(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ClearedMessageHistory", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ConversationExtendedMenu(self, *arg, **kw):
        """

        ConversationExtendedMenu signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @ConversationExtendedMenu.setter
    def ConversationExtendedMenu(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ConversationExtendedMenu", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def UriHandler(self, *arg, **kw):
        """

        UriHandler signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @UriHandler.setter
    def UriHandler(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "UriHandler", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def Quitting(self, *arg, **kw):
        """

        Quitting signal:
        """
        return None

    @Quitting.setter
    def Quitting(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "Quitting", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileRecvAccept(self, *arg, **kw):
        """

        FileRecvAccept signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileRecvAccept.setter
    def FileRecvAccept(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileRecvAccept", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileSendAccept(self, *arg, **kw):
        """

        FileSendAccept signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileSendAccept.setter
    def FileSendAccept(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileSendAccept", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileRecvStart(self, *arg, **kw):
        """

        FileRecvStart signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileRecvStart.setter
    def FileRecvStart(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileRecvStart", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileSendStart(self, *arg, **kw):
        """

        FileSendStart signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileSendStart.setter
    def FileSendStart(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileSendStart", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileSendCancel(self, *arg, **kw):
        """

        FileSendCancel signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileSendCancel.setter
    def FileSendCancel(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileSendCancel", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileRecvCancel(self, *arg, **kw):
        """

        FileRecvCancel signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileRecvCancel.setter
    def FileRecvCancel(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileRecvCancel", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileSendComplete(self, *arg, **kw):
        """

        FileSendComplete signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileSendComplete.setter
    def FileSendComplete(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileSendComplete", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileRecvComplete(self, *arg, **kw):
        """

        FileRecvComplete signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileRecvComplete.setter
    def FileRecvComplete(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileRecvComplete", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def FileRecvRequest(self, *arg, **kw):
        """

        FileRecvRequest signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @FileRecvRequest.setter
    def FileRecvRequest(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "FileRecvRequest", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def ImageDeleting(self, *arg, **kw):
        """

        ImageDeleting signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @ImageDeleting.setter
    def ImageDeleting(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "ImageDeleting", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def LogTimestamp(self, *arg, **kw):
        """

        LogTimestamp signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: x,
            direction: in;
            arg3:
            type: b,
            direction: in;
            
        """
        return None

    @LogTimestamp.setter
    def LogTimestamp(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "LogTimestamp", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def NetworkConfigurationChanged(self, *arg, **kw):
        """

        NetworkConfigurationChanged signal:
        """
        return None

    @NetworkConfigurationChanged.setter
    def NetworkConfigurationChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "NetworkConfigurationChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def DisplayingEmailNotification(self, *arg, **kw):
        """

        DisplayingEmailNotification signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            
        """
        return None

    @DisplayingEmailNotification.setter
    def DisplayingEmailNotification(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "DisplayingEmailNotification", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def DisplayingEmailsNotification(self, *arg, **kw):
        """

        DisplayingEmailsNotification signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            arg4:
            type: i,
            direction: in;
            arg5:
            type: u,
            direction: in;
            
        """
        return None

    @DisplayingEmailsNotification.setter
    def DisplayingEmailsNotification(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "DisplayingEmailsNotification", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def DisplayingUserinfo(self, *arg, **kw):
        """

        DisplayingUserinfo signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            arg3:
            type: i,
            direction: in;
            
        """
        return None

    @DisplayingUserinfo.setter
    def DisplayingUserinfo(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "DisplayingUserinfo", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def PluginLoad(self, *arg, **kw):
        """

        PluginLoad signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @PluginLoad.setter
    def PluginLoad(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "PluginLoad", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def PluginUnload(self, *arg, **kw):
        """

        PluginUnload signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @PluginUnload.setter
    def PluginUnload(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "PluginUnload", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SavedstatusChanged(self, *arg, **kw):
        """

        SavedstatusChanged signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @SavedstatusChanged.setter
    def SavedstatusChanged(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SavedstatusChanged", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SavedstatusAdded(self, *arg, **kw):
        """

        SavedstatusAdded signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SavedstatusAdded.setter
    def SavedstatusAdded(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SavedstatusAdded", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SavedstatusDeleted(self, *arg, **kw):
        """

        SavedstatusDeleted signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SavedstatusDeleted.setter
    def SavedstatusDeleted(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SavedstatusDeleted", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def SavedstatusModified(self, *arg, **kw):
        """

        SavedstatusModified signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            
        """
        return None

    @SavedstatusModified.setter
    def SavedstatusModified(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "SavedstatusModified", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def PlayingSoundEvent(self, *arg, **kw):
        """

        PlayingSoundEvent signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @PlayingSoundEvent.setter
    def PlayingSoundEvent(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "PlayingSoundEvent", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def IrcSendingText(self, *arg, **kw):
        """

        IrcSendingText signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @IrcSendingText.setter
    def IrcSendingText(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "IrcSendingText", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


    
    @property
    def IrcReceivingText(self, *arg, **kw):
        """

        IrcReceivingText signal:

        Parameters
        ----------

        arg1:
            type: i,
            direction: in;
            arg2:
            type: i,
            direction: in;
            
        """
        return None

    @IrcReceivingText.setter
    def IrcReceivingText(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "IrcReceivingText", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)


  
