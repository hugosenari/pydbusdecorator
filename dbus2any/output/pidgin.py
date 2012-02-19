'''
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* /im/pidgin/purple/PurpleObject
* im.pidgin.purple.PurpleService
* 

'''
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr
        
class Introspectable(object):
    '''
    Introspectable
    
    Usage:
    ------
    
    >> myIntrospectable = Introspectable()
    since this you can access any method, attribute or signal defined below this.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myIntrospectable.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myIntrospectable.bar
    >>> myIntrospectable.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myIntrospectable.spam = lambda eggs: do_something(eggs)
    
    '''
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/im/pidgin/purple/PurpleObject", "im.pidgin.purple.PurpleService")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:
		
		Parameters
		----------
		data: s, direction: out,
		
		"""
		pass
  
class PurpleInterface(object):
    '''
    PurpleInterface
    
    Usage:
    ------
    
    >> myPurpleInterface = PurpleInterface()
    since this you can access any method, attribute or signal defined below this.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> myPurpleInterface.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = myPurpleInterface.bar
    >>> myPurpleInterface.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> myPurpleInterface.spam = lambda eggs: do_something(eggs)
    
    '''
	@DbusInterface("im.pidgin.purple.PurpleInterface", "/im/pidgin/purple/PurpleObject", "im.pidgin.purple.PurpleService")
	def __init__(self, *arg, **kw):
		pass
    
        @DbusMethod
	def PurpleAccountsFindAny(self, arg_name, arg_protocol, *arg, **kw):
		"""
		PurpleAccountsFindAny method:
		
		Parameters
		----------
		name: s, direction: in,
		protocol: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsFindConnected(self, arg_name, arg_protocol, *arg, **kw):
		"""
		PurpleAccountsFindConnected method:
		
		Parameters
		----------
		name: s, direction: in,
		protocol: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeIsChat(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeIsChat method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeIsBuddy(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeIsBuddy method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeIsContact(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeIsContact method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeIsGroup(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeIsGroup method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIsOnline(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyIsOnline method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeHasFlag(self, arg_node, arg_flags, *arg, **kw):
		"""
		PurpleBlistNodeHasFlag method:
		
		Parameters
		----------
		node: i, direction: in,
		flags: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeShouldSave(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeShouldSave method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionIsConnected(self, arg_connection, *arg, **kw):
		"""
		PurpleConnectionIsConnected method:
		
		Parameters
		----------
		connection: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionIsValid(self, arg_connection, *arg, **kw):
		"""
		PurpleConnectionIsValid method:
		
		Parameters
		----------
		connection: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvIm(self, arg_conversation, *arg, **kw):
		"""
		PurpleConvIm method:
		
		Parameters
		----------
		conversation: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChat(self, arg_conversation, *arg, **kw):
		"""
		PurpleConvChat method:
		
		Parameters
		----------
		conversation: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountNew(self, arg_username, arg_protocol_id, *arg, **kw):
		"""
		PurpleAccountNew method:
		
		Parameters
		----------
		username: s, direction: in,
		protocol_id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountDestroy(self, arg_account, *arg, **kw):
		"""
		PurpleAccountDestroy method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountConnect(self, arg_account, *arg, **kw):
		"""
		PurpleAccountConnect method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRegister(self, arg_account, *arg, **kw):
		"""
		PurpleAccountRegister method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountDisconnect(self, arg_account, *arg, **kw):
		"""
		PurpleAccountDisconnect method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountNotifyAdded(self, arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw):
		"""
		PurpleAccountNotifyAdded method:
		
		Parameters
		----------
		account: i, direction: in,
		remote_user: s, direction: in,
		id: s, direction: in,
		alias: s, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRequestAdd(self, arg_account, arg_remote_user, arg_id, arg_alias, arg_message, *arg, **kw):
		"""
		PurpleAccountRequestAdd method:
		
		Parameters
		----------
		account: i, direction: in,
		remote_user: s, direction: in,
		id: s, direction: in,
		alias: s, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRequestCloseWithAccount(self, arg_account, *arg, **kw):
		"""
		PurpleAccountRequestCloseWithAccount method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRequestClose(self, arg_ui_handle, *arg, **kw):
		"""
		PurpleAccountRequestClose method:
		
		Parameters
		----------
		ui_handle: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRequestChangePassword(self, arg_account, *arg, **kw):
		"""
		PurpleAccountRequestChangePassword method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRequestChangeUserInfo(self, arg_account, *arg, **kw):
		"""
		PurpleAccountRequestChangeUserInfo method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetUsername(self, arg_account, arg_username, *arg, **kw):
		"""
		PurpleAccountSetUsername method:
		
		Parameters
		----------
		account: i, direction: in,
		username: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetPassword(self, arg_account, arg_password, *arg, **kw):
		"""
		PurpleAccountSetPassword method:
		
		Parameters
		----------
		account: i, direction: in,
		password: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetAlias(self, arg_account, arg_alias, *arg, **kw):
		"""
		PurpleAccountSetAlias method:
		
		Parameters
		----------
		account: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetUserInfo(self, arg_account, arg_user_info, *arg, **kw):
		"""
		PurpleAccountSetUserInfo method:
		
		Parameters
		----------
		account: i, direction: in,
		user_info: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetBuddyIconPath(self, arg_account, arg_path, *arg, **kw):
		"""
		PurpleAccountSetBuddyIconPath method:
		
		Parameters
		----------
		account: i, direction: in,
		path: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetProtocolId(self, arg_account, arg_protocol_id, *arg, **kw):
		"""
		PurpleAccountSetProtocolId method:
		
		Parameters
		----------
		account: i, direction: in,
		protocol_id: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetConnection(self, arg_account, arg_gc, *arg, **kw):
		"""
		PurpleAccountSetConnection method:
		
		Parameters
		----------
		account: i, direction: in,
		gc: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetRememberPassword(self, arg_account, arg_value, *arg, **kw):
		"""
		PurpleAccountSetRememberPassword method:
		
		Parameters
		----------
		account: i, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetCheckMail(self, arg_account, arg_value, *arg, **kw):
		"""
		PurpleAccountSetCheckMail method:
		
		Parameters
		----------
		account: i, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetEnabled(self, arg_account, arg_ui, arg_value, *arg, **kw):
		"""
		PurpleAccountSetEnabled method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetProxyInfo(self, arg_account, arg_info, *arg, **kw):
		"""
		PurpleAccountSetProxyInfo method:
		
		Parameters
		----------
		account: i, direction: in,
		info: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetPrivacyType(self, arg_account, arg_privacy_type, *arg, **kw):
		"""
		PurpleAccountSetPrivacyType method:
		
		Parameters
		----------
		account: i, direction: in,
		privacy_type: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetStatusTypes(self, arg_account, arg_status_types, *arg, **kw):
		"""
		PurpleAccountSetStatusTypes method:
		
		Parameters
		----------
		account: i, direction: in,
		status_types: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetStatusList(self, arg_account, arg_status_id, arg_active, arg_attrs, *arg, **kw):
		"""
		PurpleAccountSetStatusList method:
		
		Parameters
		----------
		account: i, direction: in,
		status_id: s, direction: in,
		active: i, direction: in,
		attrs: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetSilenceSuppression(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetSilenceSuppression method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetSilenceSuppression(self, arg_account, arg_value, *arg, **kw):
		"""
		PurpleAccountSetSilenceSuppression method:
		
		Parameters
		----------
		account: i, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountClearSettings(self, arg_account, *arg, **kw):
		"""
		PurpleAccountClearSettings method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRemoveSetting(self, arg_account, arg_setting, *arg, **kw):
		"""
		PurpleAccountRemoveSetting method:
		
		Parameters
		----------
		account: i, direction: in,
		setting: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetInt(self, arg_account, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetInt method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetString(self, arg_account, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetString method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetBool(self, arg_account, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetBool method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetUiInt(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetUiInt method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetUiString(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetUiString method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSetUiBool(self, arg_account, arg_ui, arg_name, arg_value, *arg, **kw):
		"""
		PurpleAccountSetUiBool method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountIsConnected(self, arg_account, *arg, **kw):
		"""
		PurpleAccountIsConnected method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountIsConnecting(self, arg_account, *arg, **kw):
		"""
		PurpleAccountIsConnecting method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountIsDisconnected(self, arg_account, *arg, **kw):
		"""
		PurpleAccountIsDisconnected method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetUsername(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetUsername method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetPassword(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetPassword method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetAlias(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetAlias method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetUserInfo(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetUserInfo method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetBuddyIconPath(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetBuddyIconPath method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetProtocolId(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetProtocolId method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetProtocolName(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetProtocolName method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetConnection(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetConnection method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetNameForDisplay(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetNameForDisplay method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetRememberPassword(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetRememberPassword method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetCheckMail(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetCheckMail method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetEnabled(self, arg_account, arg_ui, *arg, **kw):
		"""
		PurpleAccountGetEnabled method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetProxyInfo(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetProxyInfo method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetPrivacyType(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetPrivacyType method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetActiveStatus(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetActiveStatus method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetStatus(self, arg_account, arg_status_id, *arg, **kw):
		"""
		PurpleAccountGetStatus method:
		
		Parameters
		----------
		account: i, direction: in,
		status_id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetStatusType(self, arg_account, arg_id, *arg, **kw):
		"""
		PurpleAccountGetStatusType method:
		
		Parameters
		----------
		account: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetStatusTypeWithPrimitive(self, arg_account, arg_primitive, *arg, **kw):
		"""
		PurpleAccountGetStatusTypeWithPrimitive method:
		
		Parameters
		----------
		account: i, direction: in,
		primitive: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetPresence(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetPresence method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountIsStatusActive(self, arg_account, arg_status_id, *arg, **kw):
		"""
		PurpleAccountIsStatusActive method:
		
		Parameters
		----------
		account: i, direction: in,
		status_id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetStatusTypes(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetStatusTypes method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetInt(self, arg_account, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetInt method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		default_value: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetString(self, arg_account, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetString method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		default_value: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetBool(self, arg_account, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetBool method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		default_value: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetUiInt(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetUiInt method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		default_value: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetUiString(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetUiString method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		default_value: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetUiBool(self, arg_account, arg_ui, arg_name, arg_default_value, *arg, **kw):
		"""
		PurpleAccountGetUiBool method:
		
		Parameters
		----------
		account: i, direction: in,
		ui: s, direction: in,
		name: s, direction: in,
		default_value: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetLog(self, arg_account, arg_create, *arg, **kw):
		"""
		PurpleAccountGetLog method:
		
		Parameters
		----------
		account: i, direction: in,
		create: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountDestroyLog(self, arg_account, *arg, **kw):
		"""
		PurpleAccountDestroyLog method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountAddBuddy(self, arg_account, arg_buddy, *arg, **kw):
		"""
		PurpleAccountAddBuddy method:
		
		Parameters
		----------
		account: i, direction: in,
		buddy: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountAddBuddyWithInvite(self, arg_account, arg_buddy, arg_message, *arg, **kw):
		"""
		PurpleAccountAddBuddyWithInvite method:
		
		Parameters
		----------
		account: i, direction: in,
		buddy: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountAddBuddies(self, arg_account, arg_buddies, *arg, **kw):
		"""
		PurpleAccountAddBuddies method:
		
		Parameters
		----------
		account: i, direction: in,
		buddies: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountAddBuddiesWithInvite(self, arg_account, arg_buddies, arg_message, *arg, **kw):
		"""
		PurpleAccountAddBuddiesWithInvite method:
		
		Parameters
		----------
		account: i, direction: in,
		buddies: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRemoveBuddy(self, arg_account, arg_buddy, arg_group, *arg, **kw):
		"""
		PurpleAccountRemoveBuddy method:
		
		Parameters
		----------
		account: i, direction: in,
		buddy: i, direction: in,
		group: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRemoveBuddies(self, arg_account, arg_buddies, arg_groups, *arg, **kw):
		"""
		PurpleAccountRemoveBuddies method:
		
		Parameters
		----------
		account: i, direction: in,
		buddies: i, direction: in,
		groups: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountRemoveGroup(self, arg_account, arg_group, *arg, **kw):
		"""
		PurpleAccountRemoveGroup method:
		
		Parameters
		----------
		account: i, direction: in,
		group: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountChangePassword(self, arg_account, arg_orig_pw, arg_new_pw, *arg, **kw):
		"""
		PurpleAccountChangePassword method:
		
		Parameters
		----------
		account: i, direction: in,
		orig_pw: s, direction: in,
		new_pw: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountSupportsOfflineMessage(self, arg_account, arg_buddy, *arg, **kw):
		"""
		PurpleAccountSupportsOfflineMessage method:
		
		Parameters
		----------
		account: i, direction: in,
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountGetCurrentError(self, arg_account, *arg, **kw):
		"""
		PurpleAccountGetCurrentError method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountClearCurrentError(self, arg_account, *arg, **kw):
		"""
		PurpleAccountClearCurrentError method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsAdd(self, arg_account, *arg, **kw):
		"""
		PurpleAccountsAdd method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsRemove(self, arg_account, *arg, **kw):
		"""
		PurpleAccountsRemove method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsDelete(self, arg_account, *arg, **kw):
		"""
		PurpleAccountsDelete method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsReorder(self, arg_account, arg_new_index, *arg, **kw):
		"""
		PurpleAccountsReorder method:
		
		Parameters
		----------
		account: i, direction: in,
		new_index: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsGetAll(self, *arg, **kw):
		"""
		PurpleAccountsGetAll method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsGetAllActive(self, *arg, **kw):
		"""
		PurpleAccountsGetAllActive method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsFind(self, arg_name, arg_protocol, *arg, **kw):
		"""
		PurpleAccountsFind method:
		
		Parameters
		----------
		name: s, direction: in,
		protocol: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsRestoreCurrentStatuses(self, *arg, **kw):
		"""
		PurpleAccountsRestoreCurrentStatuses method:
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleAccountsSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsGetUiOps(self, *arg, **kw):
		"""
		PurpleAccountsGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsInit(self, *arg, **kw):
		"""
		PurpleAccountsInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleAccountsUninit(self, *arg, **kw):
		"""
		PurpleAccountsUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNew(self, *arg, **kw):
		"""
		PurpleBlistNew method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSetBlist(self, arg_blist, *arg, **kw):
		"""
		PurpleSetBlist method:
		
		Parameters
		----------
		blist: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetBlist(self, *arg, **kw):
		"""
		PurpleGetBlist method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistGetRoot(self, *arg, **kw):
		"""
		PurpleBlistGetRoot method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistGetBuddies(self, *arg, **kw):
		"""
		PurpleBlistGetBuddies method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeNext(self, arg_node, arg_offline, *arg, **kw):
		"""
		PurpleBlistNodeNext method:
		
		Parameters
		----------
		node: i, direction: in,
		offline: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetParent(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetParent method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetFirstChild(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetFirstChild method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetSiblingNext(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetSiblingNext method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetSiblingPrev(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetSiblingPrev method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistShow(self, *arg, **kw):
		"""
		PurpleBlistShow method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistDestroy(self, *arg, **kw):
		"""
		PurpleBlistDestroy method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistSetVisible(self, arg_show, *arg, **kw):
		"""
		PurpleBlistSetVisible method:
		
		Parameters
		----------
		show: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistUpdateBuddyStatus(self, arg_buddy, arg_old_status, *arg, **kw):
		"""
		PurpleBlistUpdateBuddyStatus method:
		
		Parameters
		----------
		buddy: i, direction: in,
		old_status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistUpdateNodeIcon(self, arg_node, *arg, **kw):
		"""
		PurpleBlistUpdateNodeIcon method:
		
		Parameters
		----------
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistUpdateBuddyIcon(self, arg_buddy, *arg, **kw):
		"""
		PurpleBlistUpdateBuddyIcon method:
		
		Parameters
		----------
		buddy: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRenameBuddy(self, arg_buddy, arg_name, *arg, **kw):
		"""
		PurpleBlistRenameBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAliasContact(self, arg_contact, arg_alias, *arg, **kw):
		"""
		PurpleBlistAliasContact method:
		
		Parameters
		----------
		contact: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAliasBuddy(self, arg_buddy, arg_alias, *arg, **kw):
		"""
		PurpleBlistAliasBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistServerAliasBuddy(self, arg_buddy, arg_alias, *arg, **kw):
		"""
		PurpleBlistServerAliasBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAliasChat(self, arg_chat, arg_alias, *arg, **kw):
		"""
		PurpleBlistAliasChat method:
		
		Parameters
		----------
		chat: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRenameGroup(self, arg_group, arg_name, *arg, **kw):
		"""
		PurpleBlistRenameGroup method:
		
		Parameters
		----------
		group: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleChatNew(self, arg_account, arg_alias, arg_components, *arg, **kw):
		"""
		PurpleChatNew method:
		
		Parameters
		----------
		account: i, direction: in,
		alias: s, direction: in,
		components: a{ss}, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleChatDestroy(self, arg_chat, *arg, **kw):
		"""
		PurpleChatDestroy method:
		
		Parameters
		----------
		chat: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAddChat(self, arg_chat, arg_group, arg_node, *arg, **kw):
		"""
		PurpleBlistAddChat method:
		
		Parameters
		----------
		chat: i, direction: in,
		group: i, direction: in,
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyNew(self, arg_account, arg_name, arg_alias, *arg, **kw):
		"""
		PurpleBuddyNew method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		alias: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyDestroy(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyDestroy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddySetIcon(self, arg_buddy, arg_icon, *arg, **kw):
		"""
		PurpleBuddySetIcon method:
		
		Parameters
		----------
		buddy: i, direction: in,
		icon: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetAccount(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetAccount method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetName(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetName method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetIcon(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetIcon method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetContact(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetContact method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetPresence(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetPresence method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetMediaCaps(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetMediaCaps method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddySetMediaCaps(self, arg_buddy, arg_media_caps, *arg, **kw):
		"""
		PurpleBuddySetMediaCaps method:
		
		Parameters
		----------
		buddy: i, direction: in,
		media_caps: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAddBuddy(self, arg_buddy, arg_contact, arg_group, arg_node, *arg, **kw):
		"""
		PurpleBlistAddBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		contact: i, direction: in,
		group: i, direction: in,
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGroupNew(self, arg_name, *arg, **kw):
		"""
		PurpleGroupNew method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGroupDestroy(self, arg_group, *arg, **kw):
		"""
		PurpleGroupDestroy method:
		
		Parameters
		----------
		group: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAddGroup(self, arg_group, arg_node, *arg, **kw):
		"""
		PurpleBlistAddGroup method:
		
		Parameters
		----------
		group: i, direction: in,
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactNew(self, *arg, **kw):
		"""
		PurpleContactNew method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactDestroy(self, arg_contact, *arg, **kw):
		"""
		PurpleContactDestroy method:
		
		Parameters
		----------
		contact: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactGetGroup(self, arg_contact, *arg, **kw):
		"""
		PurpleContactGetGroup method:
		
		Parameters
		----------
		contact: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAddContact(self, arg_contact, arg_group, arg_node, *arg, **kw):
		"""
		PurpleBlistAddContact method:
		
		Parameters
		----------
		contact: i, direction: in,
		group: i, direction: in,
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistMergeContact(self, arg_source, arg_node, *arg, **kw):
		"""
		PurpleBlistMergeContact method:
		
		Parameters
		----------
		source: i, direction: in,
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactGetPriorityBuddy(self, arg_contact, *arg, **kw):
		"""
		PurpleContactGetPriorityBuddy method:
		
		Parameters
		----------
		contact: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactSetAlias(self, arg_contact, arg_alias, *arg, **kw):
		"""
		PurpleContactSetAlias method:
		
		Parameters
		----------
		contact: i, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactGetAlias(self, arg_contact, *arg, **kw):
		"""
		PurpleContactGetAlias method:
		
		Parameters
		----------
		contact: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactOnAccount(self, arg_contact, arg_account, *arg, **kw):
		"""
		PurpleContactOnAccount method:
		
		Parameters
		----------
		contact: i, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleContactInvalidatePriorityBuddy(self, arg_contact, *arg, **kw):
		"""
		PurpleContactInvalidatePriorityBuddy method:
		
		Parameters
		----------
		contact: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRemoveBuddy(self, arg_buddy, *arg, **kw):
		"""
		PurpleBlistRemoveBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRemoveContact(self, arg_contact, *arg, **kw):
		"""
		PurpleBlistRemoveContact method:
		
		Parameters
		----------
		contact: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRemoveChat(self, arg_chat, *arg, **kw):
		"""
		PurpleBlistRemoveChat method:
		
		Parameters
		----------
		chat: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRemoveGroup(self, arg_group, *arg, **kw):
		"""
		PurpleBlistRemoveGroup method:
		
		Parameters
		----------
		group: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetAliasOnly(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetAliasOnly method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetServerAlias(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetServerAlias method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetContactAlias(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetContactAlias method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetLocalAlias(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetLocalAlias method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetAlias(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetAlias method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetLocalBuddyAlias(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetLocalBuddyAlias method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleChatGetName(self, arg_chat, *arg, **kw):
		"""
		PurpleChatGetName method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindBuddy(self, arg_account, arg_name, *arg, **kw):
		"""
		PurpleFindBuddy method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindBuddyInGroup(self, arg_account, arg_name, arg_group, *arg, **kw):
		"""
		PurpleFindBuddyInGroup method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		group: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindBuddies(self, arg_account, arg_name, *arg, **kw):
		"""
		PurpleFindBuddies method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindGroup(self, arg_name, *arg, **kw):
		"""
		PurpleFindGroup method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistFindChat(self, arg_account, arg_name, *arg, **kw):
		"""
		PurpleBlistFindChat method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleChatGetGroup(self, arg_chat, *arg, **kw):
		"""
		PurpleChatGetGroup method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleChatGetAccount(self, arg_chat, *arg, **kw):
		"""
		PurpleChatGetAccount method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyGetGroup(self, arg_buddy, *arg, **kw):
		"""
		PurpleBuddyGetGroup method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGroupGetAccounts(self, arg_g, *arg, **kw):
		"""
		PurpleGroupGetAccounts method:
		
		Parameters
		----------
		g: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGroupOnAccount(self, arg_g, arg_account, *arg, **kw):
		"""
		PurpleGroupOnAccount method:
		
		Parameters
		----------
		g: i, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGroupGetName(self, arg_group, *arg, **kw):
		"""
		PurpleGroupGetName method:
		
		Parameters
		----------
		group: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistAddAccount(self, arg_account, *arg, **kw):
		"""
		PurpleBlistAddAccount method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRemoveAccount(self, arg_account, *arg, **kw):
		"""
		PurpleBlistRemoveAccount method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistGetGroupSize(self, arg_group, arg_offline, *arg, **kw):
		"""
		PurpleBlistGetGroupSize method:
		
		Parameters
		----------
		group: i, direction: in,
		offline: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistGetGroupOnlineCount(self, arg_group, *arg, **kw):
		"""
		PurpleBlistGetGroupOnlineCount method:
		
		Parameters
		----------
		group: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistLoad(self, *arg, **kw):
		"""
		PurpleBlistLoad method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistScheduleSave(self, *arg, **kw):
		"""
		PurpleBlistScheduleSave method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRequestAddBuddy(self, arg_account, arg_username, arg_group, arg_alias, *arg, **kw):
		"""
		PurpleBlistRequestAddBuddy method:
		
		Parameters
		----------
		account: i, direction: in,
		username: s, direction: in,
		group: s, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRequestAddChat(self, arg_account, arg_group, arg_alias, arg_name, *arg, **kw):
		"""
		PurpleBlistRequestAddChat method:
		
		Parameters
		----------
		account: i, direction: in,
		group: i, direction: in,
		alias: s, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistRequestAddGroup(self, *arg, **kw):
		"""
		PurpleBlistRequestAddGroup method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeSetBool(self, arg_node, arg_key, arg_value, *arg, **kw):
		"""
		PurpleBlistNodeSetBool method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetBool(self, arg_node, arg_key, *arg, **kw):
		"""
		PurpleBlistNodeGetBool method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeSetInt(self, arg_node, arg_key, arg_value, *arg, **kw):
		"""
		PurpleBlistNodeSetInt method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetInt(self, arg_node, arg_key, *arg, **kw):
		"""
		PurpleBlistNodeGetInt method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeSetString(self, arg_node, arg_key, arg_value, *arg, **kw):
		"""
		PurpleBlistNodeSetString method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetString(self, arg_node, arg_key, *arg, **kw):
		"""
		PurpleBlistNodeGetString method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeRemoveSetting(self, arg_node, arg_key, *arg, **kw):
		"""
		PurpleBlistNodeRemoveSetting method:
		
		Parameters
		----------
		node: i, direction: in,
		key: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeSetFlags(self, arg_node, arg_flags, *arg, **kw):
		"""
		PurpleBlistNodeSetFlags method:
		
		Parameters
		----------
		node: i, direction: in,
		flags: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetFlags(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetFlags method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetType(self, arg_node, *arg, **kw):
		"""
		PurpleBlistNodeGetType method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistNodeGetExtendedMenu(self, arg_n, *arg, **kw):
		"""
		PurpleBlistNodeGetExtendedMenu method:
		
		Parameters
		----------
		n: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleBlistSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistGetUiOps(self, *arg, **kw):
		"""
		PurpleBlistGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBlistInit(self, *arg, **kw):
		"""
		PurpleBlistInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleBlistUninit(self, *arg, **kw):
		"""
		PurpleBlistUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconNew(self, arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw):
		"""
		PurpleBuddyIconNew method:
		
		Parameters
		----------
		account: i, direction: in,
		username: s, direction: in,
		icon_data: i, direction: in,
		icon_len: i, direction: in,
		checksum: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconRef(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconRef method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconUnref(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconUnref method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconUpdate(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconUpdate method:
		
		Parameters
		----------
		icon: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconSetData(self, arg_icon, arg_data, arg_len, arg_checksum, *arg, **kw):
		"""
		PurpleBuddyIconSetData method:
		
		Parameters
		----------
		icon: i, direction: in,
		data: i, direction: in,
		len: i, direction: in,
		checksum: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetAccount(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetAccount method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetUsername(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetUsername method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetChecksum(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetChecksum method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetData(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetData method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: ay, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetExtension(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetExtension method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetFullPath(self, arg_icon, *arg, **kw):
		"""
		PurpleBuddyIconGetFullPath method:
		
		Parameters
		----------
		icon: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsSetForUser(self, arg_account, arg_username, arg_icon_data, arg_icon_len, arg_checksum, *arg, **kw):
		"""
		PurpleBuddyIconsSetForUser method:
		
		Parameters
		----------
		account: i, direction: in,
		username: s, direction: in,
		icon_data: i, direction: in,
		icon_len: i, direction: in,
		checksum: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsFind(self, arg_account, arg_username, *arg, **kw):
		"""
		PurpleBuddyIconsFind method:
		
		Parameters
		----------
		account: i, direction: in,
		username: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsFindAccountIcon(self, arg_account, *arg, **kw):
		"""
		PurpleBuddyIconsFindAccountIcon method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsSetAccountIcon(self, arg_account, arg_icon_data, arg_icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsSetAccountIcon method:
		
		Parameters
		----------
		account: i, direction: in,
		icon_data: i, direction: in,
		icon_len: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsGetAccountIconTimestamp(self, arg_account, *arg, **kw):
		"""
		PurpleBuddyIconsGetAccountIconTimestamp method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsNodeHasCustomIcon(self, arg_node, *arg, **kw):
		"""
		PurpleBuddyIconsNodeHasCustomIcon method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsNodeFindCustomIcon(self, arg_node, *arg, **kw):
		"""
		PurpleBuddyIconsNodeFindCustomIcon method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsNodeSetCustomIcon(self, arg_node, arg_icon_data, arg_icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsNodeSetCustomIcon method:
		
		Parameters
		----------
		node: i, direction: in,
		icon_data: i, direction: in,
		icon_len: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsNodeSetCustomIconFromFile(self, arg_node, arg_filename, *arg, **kw):
		"""
		PurpleBuddyIconsNodeSetCustomIconFromFile method:
		
		Parameters
		----------
		node: i, direction: in,
		filename: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsHasCustomIcon(self, arg_contact, *arg, **kw):
		"""
		PurpleBuddyIconsHasCustomIcon method:
		
		Parameters
		----------
		contact: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsFindCustomIcon(self, arg_contact, *arg, **kw):
		"""
		PurpleBuddyIconsFindCustomIcon method:
		
		Parameters
		----------
		contact: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsSetCustomIcon(self, arg_contact, arg_icon_data, arg_icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsSetCustomIcon method:
		
		Parameters
		----------
		contact: i, direction: in,
		icon_data: i, direction: in,
		icon_len: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsSetCaching(self, arg_caching, *arg, **kw):
		"""
		PurpleBuddyIconsSetCaching method:
		
		Parameters
		----------
		caching: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsIsCaching(self, *arg, **kw):
		"""
		PurpleBuddyIconsIsCaching method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsSetCacheDir(self, arg_cache_dir, *arg, **kw):
		"""
		PurpleBuddyIconsSetCacheDir method:
		
		Parameters
		----------
		cache_dir: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsGetCacheDir(self, *arg, **kw):
		"""
		PurpleBuddyIconsGetCacheDir method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsInit(self, *arg, **kw):
		"""
		PurpleBuddyIconsInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconsUninit(self, *arg, **kw):
		"""
		PurpleBuddyIconsUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleBuddyIconGetScaleSize(self, arg_spec, arg_width, arg_height, *arg, **kw):
		"""
		PurpleBuddyIconGetScaleSize method:
		
		Parameters
		----------
		spec: i, direction: in,
		width: i, direction: in,
		height: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionNew(self, arg_account, arg_regist, arg_password, *arg, **kw):
		"""
		PurpleConnectionNew method:
		
		Parameters
		----------
		account: i, direction: in,
		regist: i, direction: in,
		password: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionDestroy(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionDestroy method:
		
		Parameters
		----------
		gc: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionSetState(self, arg_gc, arg_state, *arg, **kw):
		"""
		PurpleConnectionSetState method:
		
		Parameters
		----------
		gc: i, direction: in,
		state: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionSetAccount(self, arg_gc, arg_account, *arg, **kw):
		"""
		PurpleConnectionSetAccount method:
		
		Parameters
		----------
		gc: i, direction: in,
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionSetDisplayName(self, arg_gc, arg_name, *arg, **kw):
		"""
		PurpleConnectionSetDisplayName method:
		
		Parameters
		----------
		gc: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionSetProtocolData(self, arg_connection, arg_proto_data, *arg, **kw):
		"""
		PurpleConnectionSetProtocolData method:
		
		Parameters
		----------
		connection: i, direction: in,
		proto_data: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionGetState(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionGetState method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionGetAccount(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionGetAccount method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionGetPrpl(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionGetPrpl method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionGetPassword(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionGetPassword method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionGetDisplayName(self, arg_gc, *arg, **kw):
		"""
		PurpleConnectionGetDisplayName method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionUpdateProgress(self, arg_gc, arg_text, arg_step, arg_count, *arg, **kw):
		"""
		PurpleConnectionUpdateProgress method:
		
		Parameters
		----------
		gc: i, direction: in,
		text: s, direction: in,
		step: i, direction: in,
		count: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionNotice(self, arg_gc, arg_text, *arg, **kw):
		"""
		PurpleConnectionNotice method:
		
		Parameters
		----------
		gc: i, direction: in,
		text: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionError(self, arg_gc, arg_reason, *arg, **kw):
		"""
		PurpleConnectionError method:
		
		Parameters
		----------
		gc: i, direction: in,
		reason: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionErrorReason(self, arg_gc, arg_reason, arg_description, *arg, **kw):
		"""
		PurpleConnectionErrorReason method:
		
		Parameters
		----------
		gc: i, direction: in,
		reason: i, direction: in,
		description: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionSslError(self, arg_gc, arg_ssl_error, *arg, **kw):
		"""
		PurpleConnectionSslError method:
		
		Parameters
		----------
		gc: i, direction: in,
		ssl_error: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionErrorIsFatal(self, arg_reason, *arg, **kw):
		"""
		PurpleConnectionErrorIsFatal method:
		
		Parameters
		----------
		reason: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsDisconnectAll(self, *arg, **kw):
		"""
		PurpleConnectionsDisconnectAll method:
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsGetAll(self, *arg, **kw):
		"""
		PurpleConnectionsGetAll method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsGetConnecting(self, *arg, **kw):
		"""
		PurpleConnectionsGetConnecting method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleConnectionsSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsGetUiOps(self, *arg, **kw):
		"""
		PurpleConnectionsGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsInit(self, *arg, **kw):
		"""
		PurpleConnectionsInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleConnectionsUninit(self, *arg, **kw):
		"""
		PurpleConnectionsUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleConversationNew(self, arg_type, arg_account, arg_name, *arg, **kw):
		"""
		PurpleConversationNew method:
		
		Parameters
		----------
		type: i, direction: in,
		account: i, direction: in,
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationDestroy(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationDestroy method:
		
		Parameters
		----------
		conv: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationPresent(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationPresent method:
		
		Parameters
		----------
		conv: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetType(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetType method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetUiOps(self, arg_conv, arg_ops, *arg, **kw):
		"""
		PurpleConversationSetUiOps method:
		
		Parameters
		----------
		conv: i, direction: in,
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationsSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleConversationsSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetUiOps(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetUiOps method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetAccount(self, arg_conv, arg_account, *arg, **kw):
		"""
		PurpleConversationSetAccount method:
		
		Parameters
		----------
		conv: i, direction: in,
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetAccount(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetAccount method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetGc(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetGc method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetTitle(self, arg_conv, arg_title, *arg, **kw):
		"""
		PurpleConversationSetTitle method:
		
		Parameters
		----------
		conv: i, direction: in,
		title: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetTitle(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetTitle method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationAutosetTitle(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationAutosetTitle method:
		
		Parameters
		----------
		conv: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetName(self, arg_conv, arg_name, *arg, **kw):
		"""
		PurpleConversationSetName method:
		
		Parameters
		----------
		conv: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetName(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetName method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbGetAttribute(self, arg_cb, arg_key, *arg, **kw):
		"""
		PurpleConvChatCbGetAttribute method:
		
		Parameters
		----------
		cb: i, direction: in,
		key: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbGetAttributeKeys(self, arg_cb, *arg, **kw):
		"""
		PurpleConvChatCbGetAttributeKeys method:
		
		Parameters
		----------
		cb: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbSetAttribute(self, arg_chat, arg_cb, arg_key, arg_value, *arg, **kw):
		"""
		PurpleConvChatCbSetAttribute method:
		
		Parameters
		----------
		chat: i, direction: in,
		cb: i, direction: in,
		key: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbSetAttributes(self, arg_chat, arg_cb, arg_keys, arg_values, *arg, **kw):
		"""
		PurpleConvChatCbSetAttributes method:
		
		Parameters
		----------
		chat: i, direction: in,
		cb: i, direction: in,
		keys: i, direction: in,
		values: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetLogging(self, arg_conv, arg_log, *arg, **kw):
		"""
		PurpleConversationSetLogging method:
		
		Parameters
		----------
		conv: i, direction: in,
		log: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationIsLogging(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationIsLogging method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetImData(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetImData method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetChatData(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetChatData method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetConversations(self, *arg, **kw):
		"""
		PurpleGetConversations method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetIms(self, *arg, **kw):
		"""
		PurpleGetIms method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetChats(self, *arg, **kw):
		"""
		PurpleGetChats method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindConversationWithAccount(self, arg_type, arg_name, arg_account, *arg, **kw):
		"""
		PurpleFindConversationWithAccount method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationWrite(self, arg_conv, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
		"""
		PurpleConversationWrite method:
		
		Parameters
		----------
		conv: i, direction: in,
		who: s, direction: in,
		message: s, direction: in,
		flags: i, direction: in,
		mtime: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationSetFeatures(self, arg_conv, arg_features, *arg, **kw):
		"""
		PurpleConversationSetFeatures method:
		
		Parameters
		----------
		conv: i, direction: in,
		features: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetFeatures(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetFeatures method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationHasFocus(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationHasFocus method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationUpdate(self, arg_conv, arg_type, *arg, **kw):
		"""
		PurpleConversationUpdate method:
		
		Parameters
		----------
		conv: i, direction: in,
		type: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetMessageHistory(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetMessageHistory method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationClearMessageHistory(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationClearMessageHistory method:
		
		Parameters
		----------
		conv: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationMessageGetSender(self, arg_msg, *arg, **kw):
		"""
		PurpleConversationMessageGetSender method:
		
		Parameters
		----------
		msg: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationMessageGetMessage(self, arg_msg, *arg, **kw):
		"""
		PurpleConversationMessageGetMessage method:
		
		Parameters
		----------
		msg: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationMessageGetFlags(self, arg_msg, *arg, **kw):
		"""
		PurpleConversationMessageGetFlags method:
		
		Parameters
		----------
		msg: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationMessageGetTimestamp(self, arg_msg, *arg, **kw):
		"""
		PurpleConversationMessageGetTimestamp method:
		
		Parameters
		----------
		msg: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetConversation(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetConversation method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImSetIcon(self, arg_im, arg_icon, *arg, **kw):
		"""
		PurpleConvImSetIcon method:
		
		Parameters
		----------
		im: i, direction: in,
		icon: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetIcon(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetIcon method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImSetTypingState(self, arg_im, arg_state, *arg, **kw):
		"""
		PurpleConvImSetTypingState method:
		
		Parameters
		----------
		im: i, direction: in,
		state: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetTypingState(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetTypingState method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImStartTypingTimeout(self, arg_im, arg_timeout, *arg, **kw):
		"""
		PurpleConvImStartTypingTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		timeout: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImStopTypingTimeout(self, arg_im, *arg, **kw):
		"""
		PurpleConvImStopTypingTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetTypingTimeout(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetTypingTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImSetTypeAgain(self, arg_im, arg_val, *arg, **kw):
		"""
		PurpleConvImSetTypeAgain method:
		
		Parameters
		----------
		im: i, direction: in,
		val: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetTypeAgain(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetTypeAgain method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImStartSendTypedTimeout(self, arg_im, *arg, **kw):
		"""
		PurpleConvImStartSendTypedTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImStopSendTypedTimeout(self, arg_im, *arg, **kw):
		"""
		PurpleConvImStopSendTypedTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImGetSendTypedTimeout(self, arg_im, *arg, **kw):
		"""
		PurpleConvImGetSendTypedTimeout method:
		
		Parameters
		----------
		im: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImUpdateTyping(self, arg_im, *arg, **kw):
		"""
		PurpleConvImUpdateTyping method:
		
		Parameters
		----------
		im: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImWrite(self, arg_im, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
		"""
		PurpleConvImWrite method:
		
		Parameters
		----------
		im: i, direction: in,
		who: s, direction: in,
		message: s, direction: in,
		flags: i, direction: in,
		mtime: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvPresentError(self, arg_who, arg_account, arg_what, *arg, **kw):
		"""
		PurpleConvPresentError method:
		
		Parameters
		----------
		who: s, direction: in,
		account: i, direction: in,
		what: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImSend(self, arg_im, arg_message, *arg, **kw):
		"""
		PurpleConvImSend method:
		
		Parameters
		----------
		im: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvSendConfirm(self, arg_conv, arg_message, *arg, **kw):
		"""
		PurpleConvSendConfirm method:
		
		Parameters
		----------
		conv: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvImSendWithFlags(self, arg_im, arg_message, arg_flags, *arg, **kw):
		"""
		PurpleConvImSendWithFlags method:
		
		Parameters
		----------
		im: i, direction: in,
		message: s, direction: in,
		flags: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvCustomSmileyAdd(self, arg_conv, arg_smile, arg_cksum_type, arg_chksum, arg_remote, *arg, **kw):
		"""
		PurpleConvCustomSmileyAdd method:
		
		Parameters
		----------
		conv: i, direction: in,
		smile: s, direction: in,
		cksum_type: s, direction: in,
		chksum: s, direction: in,
		remote: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvCustomSmileyClose(self, arg_conv, arg_smile, *arg, **kw):
		"""
		PurpleConvCustomSmileyClose method:
		
		Parameters
		----------
		conv: i, direction: in,
		smile: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetConversation(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetConversation method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSetUsers(self, arg_chat, arg_users, *arg, **kw):
		"""
		PurpleConvChatSetUsers method:
		
		Parameters
		----------
		chat: i, direction: in,
		users: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetUsers(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetUsers method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatIgnore(self, arg_chat, arg_name, *arg, **kw):
		"""
		PurpleConvChatIgnore method:
		
		Parameters
		----------
		chat: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatUnignore(self, arg_chat, arg_name, *arg, **kw):
		"""
		PurpleConvChatUnignore method:
		
		Parameters
		----------
		chat: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSetIgnored(self, arg_chat, arg_ignored, *arg, **kw):
		"""
		PurpleConvChatSetIgnored method:
		
		Parameters
		----------
		chat: i, direction: in,
		ignored: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetIgnored(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetIgnored method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetIgnoredUser(self, arg_chat, arg_user, *arg, **kw):
		"""
		PurpleConvChatGetIgnoredUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatIsUserIgnored(self, arg_chat, arg_user, *arg, **kw):
		"""
		PurpleConvChatIsUserIgnored method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSetTopic(self, arg_chat, arg_who, arg_topic, *arg, **kw):
		"""
		PurpleConvChatSetTopic method:
		
		Parameters
		----------
		chat: i, direction: in,
		who: s, direction: in,
		topic: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetTopic(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetTopic method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSetId(self, arg_chat, arg_id, *arg, **kw):
		"""
		PurpleConvChatSetId method:
		
		Parameters
		----------
		chat: i, direction: in,
		id: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetId(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetId method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatWrite(self, arg_chat, arg_who, arg_message, arg_flags, arg_mtime, *arg, **kw):
		"""
		PurpleConvChatWrite method:
		
		Parameters
		----------
		chat: i, direction: in,
		who: s, direction: in,
		message: s, direction: in,
		flags: i, direction: in,
		mtime: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSend(self, arg_chat, arg_message, *arg, **kw):
		"""
		PurpleConvChatSend method:
		
		Parameters
		----------
		chat: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSendWithFlags(self, arg_chat, arg_message, arg_flags, *arg, **kw):
		"""
		PurpleConvChatSendWithFlags method:
		
		Parameters
		----------
		chat: i, direction: in,
		message: s, direction: in,
		flags: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatAddUser(self, arg_chat, arg_user, arg_extra_msg, arg_flags, arg_new_arrival, *arg, **kw):
		"""
		PurpleConvChatAddUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		extra_msg: s, direction: in,
		flags: i, direction: in,
		new_arrival: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatAddUsers(self, arg_chat, arg_users, arg_extra_msgs, arg_flags, arg_new_arrivals, *arg, **kw):
		"""
		PurpleConvChatAddUsers method:
		
		Parameters
		----------
		chat: i, direction: in,
		users: i, direction: in,
		extra_msgs: i, direction: in,
		flags: i, direction: in,
		new_arrivals: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatRenameUser(self, arg_chat, arg_old_user, arg_new_user, *arg, **kw):
		"""
		PurpleConvChatRenameUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		old_user: s, direction: in,
		new_user: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatRemoveUser(self, arg_chat, arg_user, arg_reason, *arg, **kw):
		"""
		PurpleConvChatRemoveUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		reason: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatRemoveUsers(self, arg_chat, arg_users, arg_reason, *arg, **kw):
		"""
		PurpleConvChatRemoveUsers method:
		
		Parameters
		----------
		chat: i, direction: in,
		users: i, direction: in,
		reason: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatFindUser(self, arg_chat, arg_user, *arg, **kw):
		"""
		PurpleConvChatFindUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatUserSetFlags(self, arg_chat, arg_user, arg_flags, *arg, **kw):
		"""
		PurpleConvChatUserSetFlags method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		flags: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatUserGetFlags(self, arg_chat, arg_user, *arg, **kw):
		"""
		PurpleConvChatUserGetFlags method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatClearUsers(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatClearUsers method:
		
		Parameters
		----------
		chat: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatSetNick(self, arg_chat, arg_nick, *arg, **kw):
		"""
		PurpleConvChatSetNick method:
		
		Parameters
		----------
		chat: i, direction: in,
		nick: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatGetNick(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatGetNick method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindChat(self, arg_gc, arg_id, *arg, **kw):
		"""
		PurpleFindChat method:
		
		Parameters
		----------
		gc: i, direction: in,
		id: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatLeft(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatLeft method:
		
		Parameters
		----------
		chat: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatInviteUser(self, arg_chat, arg_user, arg_message, arg_confirm, *arg, **kw):
		"""
		PurpleConvChatInviteUser method:
		
		Parameters
		----------
		chat: i, direction: in,
		user: s, direction: in,
		message: s, direction: in,
		confirm: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatHasLeft(self, arg_chat, *arg, **kw):
		"""
		PurpleConvChatHasLeft method:
		
		Parameters
		----------
		chat: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbNew(self, arg_name, arg_alias, arg_flags, *arg, **kw):
		"""
		PurpleConvChatCbNew method:
		
		Parameters
		----------
		name: s, direction: in,
		alias: s, direction: in,
		flags: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbFind(self, arg_chat, arg_name, *arg, **kw):
		"""
		PurpleConvChatCbFind method:
		
		Parameters
		----------
		chat: i, direction: in,
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbGetName(self, arg_cb, *arg, **kw):
		"""
		PurpleConvChatCbGetName method:
		
		Parameters
		----------
		cb: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConvChatCbDestroy(self, arg_cb, *arg, **kw):
		"""
		PurpleConvChatCbDestroy method:
		
		Parameters
		----------
		cb: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationGetExtendedMenu(self, arg_conv, *arg, **kw):
		"""
		PurpleConversationGetExtendedMenu method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleConversationsInit(self, *arg, **kw):
		"""
		PurpleConversationsInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleConversationsUninit(self, *arg, **kw):
		"""
		PurpleConversationsUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleCoreInit(self, arg_ui, *arg, **kw):
		"""
		PurpleCoreInit method:
		
		Parameters
		----------
		ui: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreQuit(self, *arg, **kw):
		"""
		PurpleCoreQuit method:
		"""
		pass
    
        @DbusMethod
	def PurpleCoreGetVersion(self, *arg, **kw):
		"""
		PurpleCoreGetVersion method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreGetUi(self, *arg, **kw):
		"""
		PurpleCoreGetUi method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetCore(self, *arg, **kw):
		"""
		PurpleGetCore method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleCoreSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreGetUiOps(self, *arg, **kw):
		"""
		PurpleCoreGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreMigrate(self, *arg, **kw):
		"""
		PurpleCoreMigrate method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleCoreEnsureSingleInstance(self, *arg, **kw):
		"""
		PurpleCoreEnsureSingleInstance method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferNew(self, arg_account, arg_type, arg_who, *arg, **kw):
		"""
		PurpleXferNew method:
		
		Parameters
		----------
		account: i, direction: in,
		type: i, direction: in,
		who: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXfersGetAll(self, *arg, **kw):
		"""
		PurpleXfersGetAll method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferRef(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferRef method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferUnref(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferUnref method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferRequest(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferRequest method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferRequestAccepted(self, arg_xfer, arg_filename, *arg, **kw):
		"""
		PurpleXferRequestAccepted method:
		
		Parameters
		----------
		xfer: i, direction: in,
		filename: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferRequestDenied(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferRequestDenied method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetType(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetType method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetAccount(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetAccount method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetRemoteUser(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetRemoteUser method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetStatus(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetStatus method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferIsCanceled(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferIsCanceled method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferIsCompleted(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferIsCompleted method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetFilename(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetFilename method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetLocalFilename(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetLocalFilename method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetBytesSent(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetBytesSent method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetBytesRemaining(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetBytesRemaining method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetSize(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetSize method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetLocalPort(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetLocalPort method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: u, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetRemoteIp(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetRemoteIp method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetRemotePort(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetRemotePort method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: u, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetStartTime(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetStartTime method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetEndTime(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetEndTime method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetCompleted(self, arg_xfer, arg_completed, *arg, **kw):
		"""
		PurpleXferSetCompleted method:
		
		Parameters
		----------
		xfer: i, direction: in,
		completed: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetMessage(self, arg_xfer, arg_message, *arg, **kw):
		"""
		PurpleXferSetMessage method:
		
		Parameters
		----------
		xfer: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetFilename(self, arg_xfer, arg_filename, *arg, **kw):
		"""
		PurpleXferSetFilename method:
		
		Parameters
		----------
		xfer: i, direction: in,
		filename: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetLocalFilename(self, arg_xfer, arg_filename, *arg, **kw):
		"""
		PurpleXferSetLocalFilename method:
		
		Parameters
		----------
		xfer: i, direction: in,
		filename: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetSize(self, arg_xfer, arg_size, *arg, **kw):
		"""
		PurpleXferSetSize method:
		
		Parameters
		----------
		xfer: i, direction: in,
		size: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferSetBytesSent(self, arg_xfer, arg_bytes_sent, *arg, **kw):
		"""
		PurpleXferSetBytesSent method:
		
		Parameters
		----------
		xfer: i, direction: in,
		bytes_sent: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetUiOps(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetUiOps method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferStart(self, arg_xfer, arg_fd, arg_ip, arg_port, *arg, **kw):
		"""
		PurpleXferStart method:
		
		Parameters
		----------
		xfer: i, direction: in,
		fd: i, direction: in,
		ip: s, direction: in,
		port: u, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferEnd(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferEnd method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferAdd(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferAdd method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferCancelLocal(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferCancelLocal method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferCancelRemote(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferCancelRemote method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferError(self, arg_type, arg_account, arg_who, arg_msg, *arg, **kw):
		"""
		PurpleXferError method:
		
		Parameters
		----------
		type: i, direction: in,
		account: i, direction: in,
		who: s, direction: in,
		msg: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferUpdateProgress(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferUpdateProgress method:
		
		Parameters
		----------
		xfer: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetThumbnail(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetThumbnail method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: ay, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferGetThumbnailMimetype(self, arg_xfer, *arg, **kw):
		"""
		PurpleXferGetThumbnailMimetype method:
		
		Parameters
		----------
		xfer: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXferPrepareThumbnail(self, arg_xfer, arg_formats, *arg, **kw):
		"""
		PurpleXferPrepareThumbnail method:
		
		Parameters
		----------
		xfer: i, direction: in,
		formats: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXfersInit(self, *arg, **kw):
		"""
		PurpleXfersInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleXfersUninit(self, *arg, **kw):
		"""
		PurpleXfersUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleXfersSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleXfersSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleXfersGetUiOps(self, *arg, **kw):
		"""
		PurpleXfersGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogFree(self, arg_log, *arg, **kw):
		"""
		PurpleLogFree method:
		
		Parameters
		----------
		log: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogWrite(self, arg_log, arg_type, arg_from, arg_time, arg_message, *arg, **kw):
		"""
		PurpleLogWrite method:
		
		Parameters
		----------
		log: i, direction: in,
		type: i, direction: in,
		from: s, direction: in,
		time: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetLogs(self, arg_type, arg_name, arg_account, *arg, **kw):
		"""
		PurpleLogGetLogs method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetSystemLogs(self, arg_account, *arg, **kw):
		"""
		PurpleLogGetSystemLogs method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetSize(self, arg_log, *arg, **kw):
		"""
		PurpleLogGetSize method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetTotalSize(self, arg_type, arg_name, arg_account, *arg, **kw):
		"""
		PurpleLogGetTotalSize method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetActivityScore(self, arg_type, arg_name, arg_account, *arg, **kw):
		"""
		PurpleLogGetActivityScore method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogIsDeletable(self, arg_log, *arg, **kw):
		"""
		PurpleLogIsDeletable method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogDelete(self, arg_log, *arg, **kw):
		"""
		PurpleLogDelete method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogGetLogDir(self, arg_type, arg_name, arg_account, *arg, **kw):
		"""
		PurpleLogGetLogDir method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogSetFree(self, arg_set, *arg, **kw):
		"""
		PurpleLogSetFree method:
		
		Parameters
		----------
		set: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonWriter(self, arg_log, arg_ext, *arg, **kw):
		"""
		PurpleLogCommonWriter method:
		
		Parameters
		----------
		log: i, direction: in,
		ext: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonLister(self, arg_type, arg_name, arg_account, arg_ext, arg_logger, *arg, **kw):
		"""
		PurpleLogCommonLister method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		ext: s, direction: in,
		logger: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonTotalSizer(self, arg_type, arg_name, arg_account, arg_ext, *arg, **kw):
		"""
		PurpleLogCommonTotalSizer method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		account: i, direction: in,
		ext: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonSizer(self, arg_log, *arg, **kw):
		"""
		PurpleLogCommonSizer method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonDeleter(self, arg_log, *arg, **kw):
		"""
		PurpleLogCommonDeleter method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogCommonIsDeletable(self, arg_log, *arg, **kw):
		"""
		PurpleLogCommonIsDeletable method:
		
		Parameters
		----------
		log: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerFree(self, arg_logger, *arg, **kw):
		"""
		PurpleLogLoggerFree method:
		
		Parameters
		----------
		logger: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerAdd(self, arg_logger, *arg, **kw):
		"""
		PurpleLogLoggerAdd method:
		
		Parameters
		----------
		logger: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerRemove(self, arg_logger, *arg, **kw):
		"""
		PurpleLogLoggerRemove method:
		
		Parameters
		----------
		logger: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerSet(self, arg_logger, *arg, **kw):
		"""
		PurpleLogLoggerSet method:
		
		Parameters
		----------
		logger: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerGet(self, *arg, **kw):
		"""
		PurpleLogLoggerGet method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogLoggerGetOptions(self, *arg, **kw):
		"""
		PurpleLogLoggerGetOptions method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleLogInit(self, *arg, **kw):
		"""
		PurpleLogInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleLogUninit(self, *arg, **kw):
		"""
		PurpleLogUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsFree(self, arg_results, *arg, **kw):
		"""
		PurpleNotifySearchresultsFree method:
		
		Parameters
		----------
		results: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsNewRows(self, arg_gc, arg_results, arg_data, *arg, **kw):
		"""
		PurpleNotifySearchresultsNewRows method:
		
		Parameters
		----------
		gc: i, direction: in,
		results: i, direction: in,
		data: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsNew(self, *arg, **kw):
		"""
		PurpleNotifySearchresultsNew method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsColumnNew(self, arg_title, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnNew method:
		
		Parameters
		----------
		title: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsColumnAdd(self, arg_results, arg_column, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnAdd method:
		
		Parameters
		----------
		results: i, direction: in,
		column: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsRowAdd(self, arg_results, arg_row, *arg, **kw):
		"""
		PurpleNotifySearchresultsRowAdd method:
		
		Parameters
		----------
		results: i, direction: in,
		row: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsGetRowsCount(self, arg_results, *arg, **kw):
		"""
		PurpleNotifySearchresultsGetRowsCount method:
		
		Parameters
		----------
		results: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsGetColumnsCount(self, arg_results, *arg, **kw):
		"""
		PurpleNotifySearchresultsGetColumnsCount method:
		
		Parameters
		----------
		results: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsRowGet(self, arg_results, arg_row_id, *arg, **kw):
		"""
		PurpleNotifySearchresultsRowGet method:
		
		Parameters
		----------
		results: i, direction: in,
		row_id: u, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySearchresultsColumnGetTitle(self, arg_results, arg_column_id, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnGetTitle method:
		
		Parameters
		----------
		results: i, direction: in,
		column_id: u, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoNew(self, *arg, **kw):
		"""
		PurpleNotifyUserInfoNew method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoDestroy(self, arg_user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoDestroy method:
		
		Parameters
		----------
		user_info: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoGetEntries(self, arg_user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoGetEntries method:
		
		Parameters
		----------
		user_info: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoGetTextWithNewline(self, arg_user_info, arg_newline, *arg, **kw):
		"""
		PurpleNotifyUserInfoGetTextWithNewline method:
		
		Parameters
		----------
		user_info: i, direction: in,
		newline: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoAddPair(self, arg_user_info, arg_label, arg_value, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddPair method:
		
		Parameters
		----------
		user_info: i, direction: in,
		label: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoAddPairPlaintext(self, arg_user_info, arg_label, arg_value, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddPairPlaintext method:
		
		Parameters
		----------
		user_info: i, direction: in,
		label: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoPrependPair(self, arg_user_info, arg_label, arg_value, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependPair method:
		
		Parameters
		----------
		user_info: i, direction: in,
		label: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoRemoveEntry(self, arg_user_info, arg_user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoRemoveEntry method:
		
		Parameters
		----------
		user_info: i, direction: in,
		user_info_entry: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntryNew(self, arg_label, arg_value, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryNew method:
		
		Parameters
		----------
		label: s, direction: in,
		value: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoAddSectionBreak(self, arg_user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddSectionBreak method:
		
		Parameters
		----------
		user_info: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoPrependSectionBreak(self, arg_user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependSectionBreak method:
		
		Parameters
		----------
		user_info: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoAddSectionHeader(self, arg_user_info, arg_label, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddSectionHeader method:
		
		Parameters
		----------
		user_info: i, direction: in,
		label: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoPrependSectionHeader(self, arg_user_info, arg_label, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependSectionHeader method:
		
		Parameters
		----------
		user_info: i, direction: in,
		label: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoRemoveLastItem(self, arg_user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoRemoveLastItem method:
		
		Parameters
		----------
		user_info: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntryGetLabel(self, arg_user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetLabel method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntrySetLabel(self, arg_user_info_entry, arg_label, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetLabel method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		label: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntryGetValue(self, arg_user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetValue method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntrySetValue(self, arg_user_info_entry, arg_value, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetValue method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntryGetType(self, arg_user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetType method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUserInfoEntrySetType(self, arg_user_info_entry, arg_type, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetType method:
		
		Parameters
		----------
		user_info_entry: i, direction: in,
		type: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyClose(self, arg_type, arg_ui_handle, *arg, **kw):
		"""
		PurpleNotifyClose method:
		
		Parameters
		----------
		type: i, direction: in,
		ui_handle: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyCloseWithHandle(self, arg_handle, *arg, **kw):
		"""
		PurpleNotifyCloseWithHandle method:
		
		Parameters
		----------
		handle: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifySetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleNotifySetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyGetUiOps(self, *arg, **kw):
		"""
		PurpleNotifyGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyInit(self, *arg, **kw):
		"""
		PurpleNotifyInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleNotifyUninit(self, *arg, **kw):
		"""
		PurpleNotifyUninit method:
		"""
		pass
    
        @DbusMethod
	def PurplePrefsInit(self, *arg, **kw):
		"""
		PurplePrefsInit method:
		"""
		pass
    
        @DbusMethod
	def PurplePrefsUninit(self, *arg, **kw):
		"""
		PurplePrefsUninit method:
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddNone(self, arg_name, *arg, **kw):
		"""
		PurplePrefsAddNone method:
		
		Parameters
		----------
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddBool(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddBool method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddInt(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddInt method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddString(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddString method:
		
		Parameters
		----------
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddStringList(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddStringList method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddPath(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddPath method:
		
		Parameters
		----------
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsAddPathList(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsAddPathList method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsRemove(self, arg_name, *arg, **kw):
		"""
		PurplePrefsRemove method:
		
		Parameters
		----------
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsRename(self, arg_oldname, arg_newname, *arg, **kw):
		"""
		PurplePrefsRename method:
		
		Parameters
		----------
		oldname: s, direction: in,
		newname: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsRenameBooleanToggle(self, arg_oldname, arg_newname, *arg, **kw):
		"""
		PurplePrefsRenameBooleanToggle method:
		
		Parameters
		----------
		oldname: s, direction: in,
		newname: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsDestroy(self, *arg, **kw):
		"""
		PurplePrefsDestroy method:
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetBool(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetBool method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetInt(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetInt method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetString(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetString method:
		
		Parameters
		----------
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetStringList(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetStringList method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetPath(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetPath method:
		
		Parameters
		----------
		name: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsSetPathList(self, arg_name, arg_value, *arg, **kw):
		"""
		PurplePrefsSetPathList method:
		
		Parameters
		----------
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsExists(self, arg_name, *arg, **kw):
		"""
		PurplePrefsExists method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetType(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetType method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetBool(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetBool method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetInt(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetInt method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetString(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetString method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetStringList(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetStringList method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetPath(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetPath method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetPathList(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetPathList method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsGetChildrenNames(self, arg_name, *arg, **kw):
		"""
		PurplePrefsGetChildrenNames method:
		
		Parameters
		----------
		name: s, direction: in,
		RESULT: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsDisconnectCallback(self, arg_callback_id, *arg, **kw):
		"""
		PurplePrefsDisconnectCallback method:
		
		Parameters
		----------
		callback_id: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsDisconnectByHandle(self, arg_handle, *arg, **kw):
		"""
		PurplePrefsDisconnectByHandle method:
		
		Parameters
		----------
		handle: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsTriggerCallback(self, arg_name, *arg, **kw):
		"""
		PurplePrefsTriggerCallback method:
		
		Parameters
		----------
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsLoad(self, *arg, **kw):
		"""
		PurplePrefsLoad method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrefsUpdateOld(self, *arg, **kw):
		"""
		PurplePrefsUpdateOld method:
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistShowWithAccount(self, arg_account, *arg, **kw):
		"""
		PurpleRoomlistShowWithAccount method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistNew(self, arg_account, *arg, **kw):
		"""
		PurpleRoomlistNew method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRef(self, arg_list, *arg, **kw):
		"""
		PurpleRoomlistRef method:
		
		Parameters
		----------
		list: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistUnref(self, arg_list, *arg, **kw):
		"""
		PurpleRoomlistUnref method:
		
		Parameters
		----------
		list: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistSetFields(self, arg_list, arg_fields, *arg, **kw):
		"""
		PurpleRoomlistSetFields method:
		
		Parameters
		----------
		list: i, direction: in,
		fields: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistSetInProgress(self, arg_list, arg_in_progress, *arg, **kw):
		"""
		PurpleRoomlistSetInProgress method:
		
		Parameters
		----------
		list: i, direction: in,
		in_progress: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistGetInProgress(self, arg_list, *arg, **kw):
		"""
		PurpleRoomlistGetInProgress method:
		
		Parameters
		----------
		list: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomAdd(self, arg_list, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomAdd method:
		
		Parameters
		----------
		list: i, direction: in,
		room: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistGetList(self, arg_gc, *arg, **kw):
		"""
		PurpleRoomlistGetList method:
		
		Parameters
		----------
		gc: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistCancelGetList(self, arg_list, *arg, **kw):
		"""
		PurpleRoomlistCancelGetList method:
		
		Parameters
		----------
		list: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistExpandCategory(self, arg_list, arg_category, *arg, **kw):
		"""
		PurpleRoomlistExpandCategory method:
		
		Parameters
		----------
		list: i, direction: in,
		category: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistGetFields(self, arg_roomlist, *arg, **kw):
		"""
		PurpleRoomlistGetFields method:
		
		Parameters
		----------
		roomlist: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomNew(self, arg_type, arg_name, arg_parent, *arg, **kw):
		"""
		PurpleRoomlistRoomNew method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		parent: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomJoin(self, arg_list, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomJoin method:
		
		Parameters
		----------
		list: i, direction: in,
		room: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomGetType(self, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetType method:
		
		Parameters
		----------
		room: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomGetName(self, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetName method:
		
		Parameters
		----------
		room: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomGetParent(self, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetParent method:
		
		Parameters
		----------
		room: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistRoomGetFields(self, arg_room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetFields method:
		
		Parameters
		----------
		room: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistFieldNew(self, arg_type, arg_label, arg_name, arg_hidden, *arg, **kw):
		"""
		PurpleRoomlistFieldNew method:
		
		Parameters
		----------
		type: i, direction: in,
		label: s, direction: in,
		name: s, direction: in,
		hidden: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistFieldGetType(self, arg_field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetType method:
		
		Parameters
		----------
		field: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistFieldGetLabel(self, arg_field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetLabel method:
		
		Parameters
		----------
		field: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistFieldGetHidden(self, arg_field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetHidden method:
		
		Parameters
		----------
		field: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistSetUiOps(self, arg_ops, *arg, **kw):
		"""
		PurpleRoomlistSetUiOps method:
		
		Parameters
		----------
		ops: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRoomlistGetUiOps(self, *arg, **kw):
		"""
		PurpleRoomlistGetUiOps method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusNew(self, arg_title, arg_type, *arg, **kw):
		"""
		PurpleSavedstatusNew method:
		
		Parameters
		----------
		title: s, direction: in,
		type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSetTitle(self, arg_status, arg_title, *arg, **kw):
		"""
		PurpleSavedstatusSetTitle method:
		
		Parameters
		----------
		status: i, direction: in,
		title: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSetType(self, arg_status, arg_type, *arg, **kw):
		"""
		PurpleSavedstatusSetType method:
		
		Parameters
		----------
		status: i, direction: in,
		type: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSetMessage(self, arg_status, arg_message, *arg, **kw):
		"""
		PurpleSavedstatusSetMessage method:
		
		Parameters
		----------
		status: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSetSubstatus(self, arg_status, arg_account, arg_type, arg_message, *arg, **kw):
		"""
		PurpleSavedstatusSetSubstatus method:
		
		Parameters
		----------
		status: i, direction: in,
		account: i, direction: in,
		type: i, direction: in,
		message: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusUnsetSubstatus(self, arg_saved_status, arg_account, *arg, **kw):
		"""
		PurpleSavedstatusUnsetSubstatus method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusDelete(self, arg_title, *arg, **kw):
		"""
		PurpleSavedstatusDelete method:
		
		Parameters
		----------
		title: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusDeleteByStatus(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusDeleteByStatus method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusesGetAll(self, *arg, **kw):
		"""
		PurpleSavedstatusesGetAll method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusesGetPopular(self, arg_how_many, *arg, **kw):
		"""
		PurpleSavedstatusesGetPopular method:
		
		Parameters
		----------
		how_many: u, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetCurrent(self, *arg, **kw):
		"""
		PurpleSavedstatusGetCurrent method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetDefault(self, *arg, **kw):
		"""
		PurpleSavedstatusGetDefault method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetIdleaway(self, *arg, **kw):
		"""
		PurpleSavedstatusGetIdleaway method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusIsIdleaway(self, *arg, **kw):
		"""
		PurpleSavedstatusIsIdleaway method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSetIdleaway(self, arg_idleaway, *arg, **kw):
		"""
		PurpleSavedstatusSetIdleaway method:
		
		Parameters
		----------
		idleaway: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetStartup(self, *arg, **kw):
		"""
		PurpleSavedstatusGetStartup method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusFind(self, arg_title, *arg, **kw):
		"""
		PurpleSavedstatusFind method:
		
		Parameters
		----------
		title: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusFindByCreationTime(self, arg_creation_time, *arg, **kw):
		"""
		PurpleSavedstatusFindByCreationTime method:
		
		Parameters
		----------
		creation_time: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusFindTransientByTypeAndMessage(self, arg_type, arg_message, *arg, **kw):
		"""
		PurpleSavedstatusFindTransientByTypeAndMessage method:
		
		Parameters
		----------
		type: i, direction: in,
		message: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusIsTransient(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusIsTransient method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetTitle(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetTitle method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetType(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetType method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetMessage(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetMessage method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetCreationTime(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetCreationTime method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusHasSubstatuses(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusHasSubstatuses method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusGetSubstatus(self, arg_saved_status, arg_account, *arg, **kw):
		"""
		PurpleSavedstatusGetSubstatus method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSubstatusGetType(self, arg_substatus, *arg, **kw):
		"""
		PurpleSavedstatusSubstatusGetType method:
		
		Parameters
		----------
		substatus: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusSubstatusGetMessage(self, arg_substatus, *arg, **kw):
		"""
		PurpleSavedstatusSubstatusGetMessage method:
		
		Parameters
		----------
		substatus: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusActivate(self, arg_saved_status, *arg, **kw):
		"""
		PurpleSavedstatusActivate method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusActivateForAccount(self, arg_saved_status, arg_account, *arg, **kw):
		"""
		PurpleSavedstatusActivateForAccount method:
		
		Parameters
		----------
		saved_status: i, direction: in,
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusesInit(self, *arg, **kw):
		"""
		PurpleSavedstatusesInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleSavedstatusesUninit(self, *arg, **kw):
		"""
		PurpleSavedstatusesUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyNew(self, arg_img, arg_shortcut, *arg, **kw):
		"""
		PurpleSmileyNew method:
		
		Parameters
		----------
		img: i, direction: in,
		shortcut: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyNewFromFile(self, arg_shortcut, arg_filepath, *arg, **kw):
		"""
		PurpleSmileyNewFromFile method:
		
		Parameters
		----------
		shortcut: s, direction: in,
		filepath: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyDelete(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyDelete method:
		
		Parameters
		----------
		smiley: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileySetShortcut(self, arg_smiley, arg_shortcut, *arg, **kw):
		"""
		PurpleSmileySetShortcut method:
		
		Parameters
		----------
		smiley: i, direction: in,
		shortcut: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileySetData(self, arg_smiley, arg_smiley_data, arg_smiley_data_len, *arg, **kw):
		"""
		PurpleSmileySetData method:
		
		Parameters
		----------
		smiley: i, direction: in,
		smiley_data: i, direction: in,
		smiley_data_len: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetShortcut(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetShortcut method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetChecksum(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetChecksum method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetStoredImage(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetStoredImage method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetData(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetData method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: ay, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetExtension(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetExtension method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileyGetFullPath(self, arg_smiley, *arg, **kw):
		"""
		PurpleSmileyGetFullPath method:
		
		Parameters
		----------
		smiley: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysGetAll(self, *arg, **kw):
		"""
		PurpleSmileysGetAll method:
		
		Parameters
		----------
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysFindByShortcut(self, arg_shortcut, *arg, **kw):
		"""
		PurpleSmileysFindByShortcut method:
		
		Parameters
		----------
		shortcut: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysFindByChecksum(self, arg_checksum, *arg, **kw):
		"""
		PurpleSmileysFindByChecksum method:
		
		Parameters
		----------
		checksum: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysGetStoringDir(self, *arg, **kw):
		"""
		PurpleSmileysGetStoringDir method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysInit(self, *arg, **kw):
		"""
		PurpleSmileysInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleSmileysUninit(self, *arg, **kw):
		"""
		PurpleSmileysUninit method:
		"""
		pass
    
        @DbusMethod
	def PurplePrimitiveGetIdFromType(self, arg_type, *arg, **kw):
		"""
		PurplePrimitiveGetIdFromType method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrimitiveGetNameFromType(self, arg_type, *arg, **kw):
		"""
		PurplePrimitiveGetNameFromType method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrimitiveGetTypeFromId(self, arg_id, *arg, **kw):
		"""
		PurplePrimitiveGetTypeFromId method:
		
		Parameters
		----------
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeNewFull(self, arg_primitive, arg_id, arg_name, arg_saveable, arg_user_settable, arg_independent, *arg, **kw):
		"""
		PurpleStatusTypeNewFull method:
		
		Parameters
		----------
		primitive: i, direction: in,
		id: s, direction: in,
		name: s, direction: in,
		saveable: i, direction: in,
		user_settable: i, direction: in,
		independent: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeNew(self, arg_primitive, arg_id, arg_name, arg_user_settable, *arg, **kw):
		"""
		PurpleStatusTypeNew method:
		
		Parameters
		----------
		primitive: i, direction: in,
		id: s, direction: in,
		name: s, direction: in,
		user_settable: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeDestroy(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeDestroy method:
		
		Parameters
		----------
		status_type: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeSetPrimaryAttr(self, arg_status_type, arg_attr_id, *arg, **kw):
		"""
		PurpleStatusTypeSetPrimaryAttr method:
		
		Parameters
		----------
		status_type: i, direction: in,
		attr_id: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeAddAttr(self, arg_status_type, arg_id, arg_name, arg_value, *arg, **kw):
		"""
		PurpleStatusTypeAddAttr method:
		
		Parameters
		----------
		status_type: i, direction: in,
		id: s, direction: in,
		name: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetPrimitive(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetPrimitive method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetId(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetId method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetName(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetName method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeIsSaveable(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsSaveable method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeIsUserSettable(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsUserSettable method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeIsIndependent(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsIndependent method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeIsExclusive(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsExclusive method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeIsAvailable(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsAvailable method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetPrimaryAttr(self, arg_type, *arg, **kw):
		"""
		PurpleStatusTypeGetPrimaryAttr method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetAttr(self, arg_status_type, arg_id, *arg, **kw):
		"""
		PurpleStatusTypeGetAttr method:
		
		Parameters
		----------
		status_type: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeGetAttrs(self, arg_status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetAttrs method:
		
		Parameters
		----------
		status_type: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusTypeFindWithId(self, arg_status_types, arg_id, *arg, **kw):
		"""
		PurpleStatusTypeFindWithId method:
		
		Parameters
		----------
		status_types: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusAttrNew(self, arg_id, arg_name, arg_value_type, *arg, **kw):
		"""
		PurpleStatusAttrNew method:
		
		Parameters
		----------
		id: s, direction: in,
		name: s, direction: in,
		value_type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusAttrDestroy(self, arg_attr, *arg, **kw):
		"""
		PurpleStatusAttrDestroy method:
		
		Parameters
		----------
		attr: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusAttrGetId(self, arg_attr, *arg, **kw):
		"""
		PurpleStatusAttrGetId method:
		
		Parameters
		----------
		attr: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusAttrGetName(self, arg_attr, *arg, **kw):
		"""
		PurpleStatusAttrGetName method:
		
		Parameters
		----------
		attr: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusAttrGetValue(self, arg_attr, *arg, **kw):
		"""
		PurpleStatusAttrGetValue method:
		
		Parameters
		----------
		attr: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusNew(self, arg_status_type, arg_presence, *arg, **kw):
		"""
		PurpleStatusNew method:
		
		Parameters
		----------
		status_type: i, direction: in,
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusDestroy(self, arg_status, *arg, **kw):
		"""
		PurpleStatusDestroy method:
		
		Parameters
		----------
		status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusSetActive(self, arg_status, arg_active, *arg, **kw):
		"""
		PurpleStatusSetActive method:
		
		Parameters
		----------
		status: i, direction: in,
		active: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusSetActiveWithAttrsList(self, arg_status, arg_active, arg_attrs, *arg, **kw):
		"""
		PurpleStatusSetActiveWithAttrsList method:
		
		Parameters
		----------
		status: i, direction: in,
		active: i, direction: in,
		attrs: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusSetAttrBoolean(self, arg_status, arg_id, arg_value, *arg, **kw):
		"""
		PurpleStatusSetAttrBoolean method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusSetAttrInt(self, arg_status, arg_id, arg_value, *arg, **kw):
		"""
		PurpleStatusSetAttrInt method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		value: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusSetAttrString(self, arg_status, arg_id, arg_value, *arg, **kw):
		"""
		PurpleStatusSetAttrString method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetType(self, arg_status, *arg, **kw):
		"""
		PurpleStatusGetType method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetPresence(self, arg_status, *arg, **kw):
		"""
		PurpleStatusGetPresence method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetId(self, arg_status, *arg, **kw):
		"""
		PurpleStatusGetId method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetName(self, arg_status, *arg, **kw):
		"""
		PurpleStatusGetName method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusIsIndependent(self, arg_status, *arg, **kw):
		"""
		PurpleStatusIsIndependent method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusIsExclusive(self, arg_status, *arg, **kw):
		"""
		PurpleStatusIsExclusive method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusIsAvailable(self, arg_status, *arg, **kw):
		"""
		PurpleStatusIsAvailable method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusIsActive(self, arg_status, *arg, **kw):
		"""
		PurpleStatusIsActive method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusIsOnline(self, arg_status, *arg, **kw):
		"""
		PurpleStatusIsOnline method:
		
		Parameters
		----------
		status: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetAttrValue(self, arg_status, arg_id, *arg, **kw):
		"""
		PurpleStatusGetAttrValue method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetAttrBoolean(self, arg_status, arg_id, *arg, **kw):
		"""
		PurpleStatusGetAttrBoolean method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetAttrInt(self, arg_status, arg_id, *arg, **kw):
		"""
		PurpleStatusGetAttrInt method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusGetAttrString(self, arg_status, arg_id, *arg, **kw):
		"""
		PurpleStatusGetAttrString method:
		
		Parameters
		----------
		status: i, direction: in,
		id: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusCompare(self, arg_status1, arg_status2, *arg, **kw):
		"""
		PurpleStatusCompare method:
		
		Parameters
		----------
		status1: i, direction: in,
		status2: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceNew(self, arg_context, *arg, **kw):
		"""
		PurplePresenceNew method:
		
		Parameters
		----------
		context: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceNewForAccount(self, arg_account, *arg, **kw):
		"""
		PurplePresenceNewForAccount method:
		
		Parameters
		----------
		account: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceNewForConv(self, arg_conv, *arg, **kw):
		"""
		PurplePresenceNewForConv method:
		
		Parameters
		----------
		conv: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceNewForBuddy(self, arg_buddy, *arg, **kw):
		"""
		PurplePresenceNewForBuddy method:
		
		Parameters
		----------
		buddy: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceDestroy(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceDestroy method:
		
		Parameters
		----------
		presence: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceAddStatus(self, arg_presence, arg_status, *arg, **kw):
		"""
		PurplePresenceAddStatus method:
		
		Parameters
		----------
		presence: i, direction: in,
		status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceSetStatusActive(self, arg_presence, arg_status_id, arg_active, *arg, **kw):
		"""
		PurplePresenceSetStatusActive method:
		
		Parameters
		----------
		presence: i, direction: in,
		status_id: s, direction: in,
		active: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceSwitchStatus(self, arg_presence, arg_status_id, *arg, **kw):
		"""
		PurplePresenceSwitchStatus method:
		
		Parameters
		----------
		presence: i, direction: in,
		status_id: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceSetIdle(self, arg_presence, arg_idle, arg_idle_time, *arg, **kw):
		"""
		PurplePresenceSetIdle method:
		
		Parameters
		----------
		presence: i, direction: in,
		idle: i, direction: in,
		idle_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceSetLoginTime(self, arg_presence, arg_login_time, *arg, **kw):
		"""
		PurplePresenceSetLoginTime method:
		
		Parameters
		----------
		presence: i, direction: in,
		login_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetContext(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetContext method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetAccount(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetAccount method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetConversation(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetConversation method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetChatUser(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetChatUser method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetBuddy(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetBuddy method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetStatuses(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetStatuses method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetStatus(self, arg_presence, arg_status_id, *arg, **kw):
		"""
		PurplePresenceGetStatus method:
		
		Parameters
		----------
		presence: i, direction: in,
		status_id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetActiveStatus(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetActiveStatus method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceIsAvailable(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceIsAvailable method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceIsOnline(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceIsOnline method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceIsStatusActive(self, arg_presence, arg_status_id, *arg, **kw):
		"""
		PurplePresenceIsStatusActive method:
		
		Parameters
		----------
		presence: i, direction: in,
		status_id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceIsStatusPrimitiveActive(self, arg_presence, arg_primitive, *arg, **kw):
		"""
		PurplePresenceIsStatusPrimitiveActive method:
		
		Parameters
		----------
		presence: i, direction: in,
		primitive: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceIsIdle(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceIsIdle method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetIdleTime(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetIdleTime method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceGetLoginTime(self, arg_presence, *arg, **kw):
		"""
		PurplePresenceGetLoginTime method:
		
		Parameters
		----------
		presence: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePresenceCompare(self, arg_presence1, arg_presence2, *arg, **kw):
		"""
		PurplePresenceCompare method:
		
		Parameters
		----------
		presence1: i, direction: in,
		presence2: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStatusInit(self, *arg, **kw):
		"""
		PurpleStatusInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleStatusUninit(self, *arg, **kw):
		"""
		PurpleStatusUninit method:
		"""
		pass
    
        @DbusMethod
	def ServSendTyping(self, arg_gc, arg_name, arg_state, *arg, **kw):
		"""
		ServSendTyping method:
		
		Parameters
		----------
		gc: i, direction: in,
		name: s, direction: in,
		state: i, direction: in,
		RESULT: u, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ServMoveBuddy(self, arg_param0, arg_param1, arg_param2, *arg, **kw):
		"""
		ServMoveBuddy method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: i, direction: in,
		param2: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServSendIm(self, arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw):
		"""
		ServSendIm method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		param2: s, direction: in,
		flags: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGetAttentionTypeFromCode(self, arg_account, arg_type_code, *arg, **kw):
		"""
		PurpleGetAttentionTypeFromCode method:
		
		Parameters
		----------
		account: i, direction: in,
		type_code: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ServSendAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
		"""
		ServSendAttention method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		type_code: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
		"""
		ServGotAttention method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		type_code: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGetInfo(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServGetInfo method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServSetInfo(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServSetInfo method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServAddPermit(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServAddPermit method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServAddDeny(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServAddDeny method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServRemPermit(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServRemPermit method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServRemDeny(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServRemDeny method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServSetPermitDeny(self, arg_param0, *arg, **kw):
		"""
		ServSetPermitDeny method:
		
		Parameters
		----------
		param0: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServChatInvite(self, arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw):
		"""
		ServChatInvite method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: i, direction: in,
		param2: s, direction: in,
		param3: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServChatLeave(self, arg_param0, arg_param1, *arg, **kw):
		"""
		ServChatLeave method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServChatWhisper(self, arg_param0, arg_param1, arg_param2, arg_param3, *arg, **kw):
		"""
		ServChatWhisper method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: i, direction: in,
		param2: s, direction: in,
		param3: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServChatSend(self, arg_param0, arg_param1, arg_param2, arg_flags, *arg, **kw):
		"""
		ServChatSend method:
		
		Parameters
		----------
		param0: i, direction: in,
		param1: i, direction: in,
		param2: s, direction: in,
		flags: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def ServAliasBuddy(self, arg_param0, *arg, **kw):
		"""
		ServAliasBuddy method:
		
		Parameters
		----------
		param0: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotAlias(self, arg_gc, arg_who, arg_alias, *arg, **kw):
		"""
		ServGotAlias method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleServGotPrivateAlias(self, arg_gc, arg_who, arg_alias, *arg, **kw):
		"""
		PurpleServGotPrivateAlias method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		alias: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotTyping(self, arg_gc, arg_name, arg_timeout, arg_state, *arg, **kw):
		"""
		ServGotTyping method:
		
		Parameters
		----------
		gc: i, direction: in,
		name: s, direction: in,
		timeout: i, direction: in,
		state: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotTypingStopped(self, arg_gc, arg_name, *arg, **kw):
		"""
		ServGotTypingStopped method:
		
		Parameters
		----------
		gc: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotIm(self, arg_gc, arg_who, arg_msg, arg_flags, arg_mtime, *arg, **kw):
		"""
		ServGotIm method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		msg: s, direction: in,
		flags: i, direction: in,
		mtime: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServJoinChat(self, arg_param0, arg_data, *arg, **kw):
		"""
		ServJoinChat method:
		
		Parameters
		----------
		param0: i, direction: in,
		data: a{ss}, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServRejectChat(self, arg_param0, arg_data, *arg, **kw):
		"""
		ServRejectChat method:
		
		Parameters
		----------
		param0: i, direction: in,
		data: a{ss}, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotChatInvite(self, arg_gc, arg_name, arg_who, arg_message, arg_data, *arg, **kw):
		"""
		ServGotChatInvite method:
		
		Parameters
		----------
		gc: i, direction: in,
		name: s, direction: in,
		who: s, direction: in,
		message: s, direction: in,
		data: a{ss}, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotJoinedChat(self, arg_gc, arg_id, arg_name, *arg, **kw):
		"""
		ServGotJoinedChat method:
		
		Parameters
		----------
		gc: i, direction: in,
		id: i, direction: in,
		name: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleServGotJoinChatFailed(self, arg_gc, arg_data, *arg, **kw):
		"""
		PurpleServGotJoinChatFailed method:
		
		Parameters
		----------
		gc: i, direction: in,
		data: a{ss}, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotChatLeft(self, arg_g, arg_id, *arg, **kw):
		"""
		ServGotChatLeft method:
		
		Parameters
		----------
		g: i, direction: in,
		id: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServGotChatIn(self, arg_g, arg_id, arg_who, arg_flags, arg_message, arg_mtime, *arg, **kw):
		"""
		ServGotChatIn method:
		
		Parameters
		----------
		g: i, direction: in,
		id: i, direction: in,
		who: s, direction: in,
		flags: i, direction: in,
		message: s, direction: in,
		mtime: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def ServSendFile(self, arg_gc, arg_who, arg_file, *arg, **kw):
		"""
		ServSendFile method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		file: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMenuActionFree(self, arg_act, *arg, **kw):
		"""
		PurpleMenuActionFree method:
		
		Parameters
		----------
		act: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilSetCurrentSong(self, arg_title, arg_artist, arg_album, *arg, **kw):
		"""
		PurpleUtilSetCurrentSong method:
		
		Parameters
		----------
		title: s, direction: in,
		artist: s, direction: in,
		album: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilInit(self, *arg, **kw):
		"""
		PurpleUtilInit method:
		"""
		pass
    
        @DbusMethod
	def PurpleUtilUninit(self, *arg, **kw):
		"""
		PurpleUtilUninit method:
		"""
		pass
    
        @DbusMethod
	def PurpleMimeDecodeField(self, arg_str, *arg, **kw):
		"""
		PurpleMimeDecodeField method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleTimeBuild(self, arg_year, arg_month, arg_day, arg_hour, arg_min, arg_sec, *arg, **kw):
		"""
		PurpleTimeBuild method:
		
		Parameters
		----------
		year: i, direction: in,
		month: i, direction: in,
		day: i, direction: in,
		hour: i, direction: in,
		min: i, direction: in,
		sec: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupEscapeText(self, arg_text, arg_length, *arg, **kw):
		"""
		PurpleMarkupEscapeText method:
		
		Parameters
		----------
		text: s, direction: in,
		length: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupStripHtml(self, arg_str, *arg, **kw):
		"""
		PurpleMarkupStripHtml method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupLinkify(self, arg_str, *arg, **kw):
		"""
		PurpleMarkupLinkify method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUnescapeText(self, arg_text, *arg, **kw):
		"""
		PurpleUnescapeText method:
		
		Parameters
		----------
		text: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUnescapeHtml(self, arg_html, *arg, **kw):
		"""
		PurpleUnescapeHtml method:
		
		Parameters
		----------
		html: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupSlice(self, arg_str, arg_x, arg_y, *arg, **kw):
		"""
		PurpleMarkupSlice method:
		
		Parameters
		----------
		str: s, direction: in,
		x: i, direction: in,
		y: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupGetTagName(self, arg_tag, *arg, **kw):
		"""
		PurpleMarkupGetTagName method:
		
		Parameters
		----------
		tag: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupUnescapeEntity(self, arg_text, arg_length, *arg, **kw):
		"""
		PurpleMarkupUnescapeEntity method:
		
		Parameters
		----------
		text: s, direction: in,
		length: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupGetCssProperty(self, arg_style, arg_opt, *arg, **kw):
		"""
		PurpleMarkupGetCssProperty method:
		
		Parameters
		----------
		style: s, direction: in,
		opt: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleMarkupIsRtl(self, arg_html, *arg, **kw):
		"""
		PurpleMarkupIsRtl method:
		
		Parameters
		----------
		html: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleHomeDir(self, *arg, **kw):
		"""
		PurpleHomeDir method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUserDir(self, *arg, **kw):
		"""
		PurpleUserDir method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilSetUserDir(self, arg_dir, *arg, **kw):
		"""
		PurpleUtilSetUserDir method:
		
		Parameters
		----------
		dir: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleBuildDir(self, arg_path, arg_mode, *arg, **kw):
		"""
		PurpleBuildDir method:
		
		Parameters
		----------
		path: s, direction: in,
		mode: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilWriteDataToFile(self, arg_filename, arg_data, arg_size, *arg, **kw):
		"""
		PurpleUtilWriteDataToFile method:
		
		Parameters
		----------
		filename: s, direction: in,
		data: s, direction: in,
		size: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilWriteDataToFileAbsolute(self, arg_filename_full, arg_data, arg_size, *arg, **kw):
		"""
		PurpleUtilWriteDataToFileAbsolute method:
		
		Parameters
		----------
		filename_full: s, direction: in,
		data: s, direction: in,
		size: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleProgramIsValid(self, arg_program, *arg, **kw):
		"""
		PurpleProgramIsValid method:
		
		Parameters
		----------
		program: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRunningGnome(self, *arg, **kw):
		"""
		PurpleRunningGnome method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRunningKde(self, *arg, **kw):
		"""
		PurpleRunningKde method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRunningOsx(self, *arg, **kw):
		"""
		PurpleRunningOsx method:
		
		Parameters
		----------
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFdGetIp(self, arg_fd, *arg, **kw):
		"""
		PurpleFdGetIp method:
		
		Parameters
		----------
		fd: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSocketGetFamily(self, arg_fd, *arg, **kw):
		"""
		PurpleSocketGetFamily method:
		
		Parameters
		----------
		fd: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleSocketSpeaksIpv4(self, arg_fd, *arg, **kw):
		"""
		PurpleSocketSpeaksIpv4 method:
		
		Parameters
		----------
		fd: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrequal(self, arg_left, arg_right, *arg, **kw):
		"""
		PurpleStrequal method:
		
		Parameters
		----------
		left: s, direction: in,
		right: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNormalize(self, arg_account, arg_str, *arg, **kw):
		"""
		PurpleNormalize method:
		
		Parameters
		----------
		account: i, direction: in,
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleNormalizeNocase(self, arg_account, arg_str, *arg, **kw):
		"""
		PurpleNormalizeNocase method:
		
		Parameters
		----------
		account: i, direction: in,
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrHasPrefix(self, arg_s, arg_p, *arg, **kw):
		"""
		PurpleStrHasPrefix method:
		
		Parameters
		----------
		s: s, direction: in,
		p: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrHasSuffix(self, arg_s, arg_x, *arg, **kw):
		"""
		PurpleStrHasSuffix method:
		
		Parameters
		----------
		s: s, direction: in,
		x: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrdupWithhtml(self, arg_src, *arg, **kw):
		"""
		PurpleStrdupWithhtml method:
		
		Parameters
		----------
		src: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrAddCr(self, arg_str, *arg, **kw):
		"""
		PurpleStrAddCr method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrreplace(self, arg_string, arg_delimiter, arg_replacement, *arg, **kw):
		"""
		PurpleStrreplace method:
		
		Parameters
		----------
		string: s, direction: in,
		delimiter: s, direction: in,
		replacement: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8NcrEncode(self, arg_in, *arg, **kw):
		"""
		PurpleUtf8NcrEncode method:
		
		Parameters
		----------
		in: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8NcrDecode(self, arg_in, *arg, **kw):
		"""
		PurpleUtf8NcrDecode method:
		
		Parameters
		----------
		in: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrcasereplace(self, arg_string, arg_delimiter, arg_replacement, *arg, **kw):
		"""
		PurpleStrcasereplace method:
		
		Parameters
		----------
		string: s, direction: in,
		delimiter: s, direction: in,
		replacement: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrcasestr(self, arg_haystack, arg_needle, *arg, **kw):
		"""
		PurpleStrcasestr method:
		
		Parameters
		----------
		haystack: s, direction: in,
		needle: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrSizeToUnits(self, arg_size, *arg, **kw):
		"""
		PurpleStrSizeToUnits method:
		
		Parameters
		----------
		size: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrSecondsToString(self, arg_sec, *arg, **kw):
		"""
		PurpleStrSecondsToString method:
		
		Parameters
		----------
		sec: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleStrBinaryToAscii(self, arg_binary, arg_len, *arg, **kw):
		"""
		PurpleStrBinaryToAscii method:
		
		Parameters
		----------
		binary: s, direction: in,
		len: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleGotProtocolHandlerUri(self, arg_uri, *arg, **kw):
		"""
		PurpleGotProtocolHandlerUri method:
		
		Parameters
		----------
		uri: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtilFetchUrlCancel(self, arg_url_data, *arg, **kw):
		"""
		PurpleUtilFetchUrlCancel method:
		
		Parameters
		----------
		url_data: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUrlDecode(self, arg_str, *arg, **kw):
		"""
		PurpleUrlDecode method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUrlEncode(self, arg_str, *arg, **kw):
		"""
		PurpleUrlEncode method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleEmailIsValid(self, arg_address, *arg, **kw):
		"""
		PurpleEmailIsValid method:
		
		Parameters
		----------
		address: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleIpAddressIsValid(self, arg_ip, *arg, **kw):
		"""
		PurpleIpAddressIsValid method:
		
		Parameters
		----------
		ip: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleIpv4AddressIsValid(self, arg_ip, *arg, **kw):
		"""
		PurpleIpv4AddressIsValid method:
		
		Parameters
		----------
		ip: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleIpv6AddressIsValid(self, arg_ip, *arg, **kw):
		"""
		PurpleIpv6AddressIsValid method:
		
		Parameters
		----------
		ip: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUriListExtractUris(self, arg_uri_list, *arg, **kw):
		"""
		PurpleUriListExtractUris method:
		
		Parameters
		----------
		uri_list: s, direction: in,
		RESULT: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUriListExtractFilenames(self, arg_uri_list, *arg, **kw):
		"""
		PurpleUriListExtractFilenames method:
		
		Parameters
		----------
		uri_list: s, direction: in,
		RESULT: as, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8TryConvert(self, arg_str, *arg, **kw):
		"""
		PurpleUtf8TryConvert method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8Salvage(self, arg_str, *arg, **kw):
		"""
		PurpleUtf8Salvage method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8StripUnprintables(self, arg_str, *arg, **kw):
		"""
		PurpleUtf8StripUnprintables method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8Strcasecmp(self, arg_a, arg_b, *arg, **kw):
		"""
		PurpleUtf8Strcasecmp method:
		
		Parameters
		----------
		a: s, direction: in,
		b: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUtf8HasWord(self, arg_haystack, arg_needle, *arg, **kw):
		"""
		PurpleUtf8HasWord method:
		
		Parameters
		----------
		haystack: s, direction: in,
		needle: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleTextStripMnemonic(self, arg_in, *arg, **kw):
		"""
		PurpleTextStripMnemonic method:
		
		Parameters
		----------
		in: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUnescapeFilename(self, arg_str, *arg, **kw):
		"""
		PurpleUnescapeFilename method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleEscapeFilename(self, arg_str, *arg, **kw):
		"""
		PurpleEscapeFilename method:
		
		Parameters
		----------
		str: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleOscarConvert(self, arg_act, arg_protocol, *arg, **kw):
		"""
		PurpleOscarConvert method:
		
		Parameters
		----------
		act: s, direction: in,
		protocol: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleRestoreDefaultSignalHandlers(self, *arg, **kw):
		"""
		PurpleRestoreDefaultSignalHandlers method:
		"""
		pass
    
        @DbusMethod
	def PurpleGetHostName(self, *arg, **kw):
		"""
		PurpleGetHostName method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleUuidRandom(self, *arg, **kw):
		"""
		PurpleUuidRandom method:
		
		Parameters
		----------
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeInsertChild(self, arg_parent, arg_child, *arg, **kw):
		"""
		XmlnodeInsertChild method:
		
		Parameters
		----------
		parent: i, direction: in,
		child: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeInsertData(self, arg_node, arg_data, arg_size, *arg, **kw):
		"""
		XmlnodeInsertData method:
		
		Parameters
		----------
		node: i, direction: in,
		data: s, direction: in,
		size: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetData(self, arg_node, *arg, **kw):
		"""
		XmlnodeGetData method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetDataUnescaped(self, arg_node, *arg, **kw):
		"""
		XmlnodeGetDataUnescaped method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetAttrib(self, arg_node, arg_attr, arg_value, *arg, **kw):
		"""
		XmlnodeSetAttrib method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetAttribWithPrefix(self, arg_node, arg_attr, arg_prefix, arg_value, *arg, **kw):
		"""
		XmlnodeSetAttribWithPrefix method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		prefix: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, arg_value, *arg, **kw):
		"""
		XmlnodeSetAttribWithNamespace method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		xmlns: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetAttribFull(self, arg_node, arg_attr, arg_xmlns, arg_prefix, arg_value, *arg, **kw):
		"""
		XmlnodeSetAttribFull method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		xmlns: s, direction: in,
		prefix: s, direction: in,
		value: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetAttrib(self, arg_node, arg_attr, *arg, **kw):
		"""
		XmlnodeGetAttrib method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, *arg, **kw):
		"""
		XmlnodeGetAttribWithNamespace method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		xmlns: s, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeRemoveAttrib(self, arg_node, arg_attr, *arg, **kw):
		"""
		XmlnodeRemoveAttrib method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeRemoveAttribWithNamespace(self, arg_node, arg_attr, arg_xmlns, *arg, **kw):
		"""
		XmlnodeRemoveAttribWithNamespace method:
		
		Parameters
		----------
		node: i, direction: in,
		attr: s, direction: in,
		xmlns: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetNamespace(self, arg_node, arg_xmlns, *arg, **kw):
		"""
		XmlnodeSetNamespace method:
		
		Parameters
		----------
		node: i, direction: in,
		xmlns: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetNamespace(self, arg_node, *arg, **kw):
		"""
		XmlnodeGetNamespace method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeSetPrefix(self, arg_node, arg_prefix, *arg, **kw):
		"""
		XmlnodeSetPrefix method:
		
		Parameters
		----------
		node: i, direction: in,
		prefix: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeGetPrefix(self, arg_node, *arg, **kw):
		"""
		XmlnodeGetPrefix method:
		
		Parameters
		----------
		node: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeToStr(self, arg_node, arg_len, *arg, **kw):
		"""
		XmlnodeToStr method:
		
		Parameters
		----------
		node: i, direction: in,
		len: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeToFormattedStr(self, arg_node, arg_len, *arg, **kw):
		"""
		XmlnodeToFormattedStr method:
		
		Parameters
		----------
		node: i, direction: in,
		len: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def XmlnodeFree(self, arg_node, *arg, **kw):
		"""
		XmlnodeFree method:
		
		Parameters
		----------
		node: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeNew(self, arg_ulname, arg_name, arg_inc_desc, arg_out_desc, *arg, **kw):
		"""
		PurpleAttentionTypeNew method:
		
		Parameters
		----------
		ulname: s, direction: in,
		name: s, direction: in,
		inc_desc: s, direction: in,
		out_desc: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeSetName(self, arg_type, arg_name, *arg, **kw):
		"""
		PurpleAttentionTypeSetName method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeSetIncomingDesc(self, arg_type, arg_desc, *arg, **kw):
		"""
		PurpleAttentionTypeSetIncomingDesc method:
		
		Parameters
		----------
		type: i, direction: in,
		desc: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeSetOutgoingDesc(self, arg_type, arg_desc, *arg, **kw):
		"""
		PurpleAttentionTypeSetOutgoingDesc method:
		
		Parameters
		----------
		type: i, direction: in,
		desc: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeSetIconName(self, arg_type, arg_name, *arg, **kw):
		"""
		PurpleAttentionTypeSetIconName method:
		
		Parameters
		----------
		type: i, direction: in,
		name: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeSetUnlocalizedName(self, arg_type, arg_ulname, *arg, **kw):
		"""
		PurpleAttentionTypeSetUnlocalizedName method:
		
		Parameters
		----------
		type: i, direction: in,
		ulname: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeGetName(self, arg_type, *arg, **kw):
		"""
		PurpleAttentionTypeGetName method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeGetIncomingDesc(self, arg_type, *arg, **kw):
		"""
		PurpleAttentionTypeGetIncomingDesc method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeGetOutgoingDesc(self, arg_type, *arg, **kw):
		"""
		PurpleAttentionTypeGetOutgoingDesc method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeGetIconName(self, arg_type, *arg, **kw):
		"""
		PurpleAttentionTypeGetIconName method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurpleAttentionTypeGetUnlocalizedName(self, arg_type, *arg, **kw):
		"""
		PurpleAttentionTypeGetUnlocalizedName method:
		
		Parameters
		----------
		type: i, direction: in,
		RESULT: s, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotAccountIdle(self, arg_account, arg_idle, arg_idle_time, *arg, **kw):
		"""
		PurplePrplGotAccountIdle method:
		
		Parameters
		----------
		account: i, direction: in,
		idle: i, direction: in,
		idle_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotAccountLoginTime(self, arg_account, arg_login_time, *arg, **kw):
		"""
		PurplePrplGotAccountLoginTime method:
		
		Parameters
		----------
		account: i, direction: in,
		login_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotAccountActions(self, arg_account, *arg, **kw):
		"""
		PurplePrplGotAccountActions method:
		
		Parameters
		----------
		account: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotUserIdle(self, arg_account, arg_name, arg_idle, arg_idle_time, *arg, **kw):
		"""
		PurplePrplGotUserIdle method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		idle: i, direction: in,
		idle_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotUserLoginTime(self, arg_account, arg_name, arg_login_time, *arg, **kw):
		"""
		PurplePrplGotUserLoginTime method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		login_time: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotUserStatusDeactive(self, arg_account, arg_name, arg_status_id, *arg, **kw):
		"""
		PurplePrplGotUserStatusDeactive method:
		
		Parameters
		----------
		account: i, direction: in,
		name: s, direction: in,
		status_id: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplChangeAccountStatus(self, arg_account, arg_old_status, arg_new_status, *arg, **kw):
		"""
		PurplePrplChangeAccountStatus method:
		
		Parameters
		----------
		account: i, direction: in,
		old_status: i, direction: in,
		new_status: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGetStatuses(self, arg_account, arg_presence, *arg, **kw):
		"""
		PurplePrplGetStatuses method:
		
		Parameters
		----------
		account: i, direction: in,
		presence: i, direction: in,
		RESULT: ai, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplSendAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
		"""
		PurplePrplSendAttention method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		type_code: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotAttention(self, arg_gc, arg_who, arg_type_code, *arg, **kw):
		"""
		PurplePrplGotAttention method:
		
		Parameters
		----------
		gc: i, direction: in,
		who: s, direction: in,
		type_code: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotAttentionInChat(self, arg_gc, arg_id, arg_who, arg_type_code, *arg, **kw):
		"""
		PurplePrplGotAttentionInChat method:
		
		Parameters
		----------
		gc: i, direction: in,
		id: i, direction: in,
		who: s, direction: in,
		type_code: i, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGetMediaCaps(self, arg_account, arg_who, *arg, **kw):
		"""
		PurplePrplGetMediaCaps method:
		
		Parameters
		----------
		account: i, direction: in,
		who: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplInitiateMedia(self, arg_account, arg_who, arg_type, *arg, **kw):
		"""
		PurplePrplInitiateMedia method:
		
		Parameters
		----------
		account: i, direction: in,
		who: s, direction: in,
		type: i, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusMethod
	def PurplePrplGotMediaCaps(self, arg_account, arg_who, *arg, **kw):
		"""
		PurplePrplGotMediaCaps method:
		
		Parameters
		----------
		account: i, direction: in,
		who: s, direction: in,
		
		"""
		pass
    
        @DbusMethod
	def PurpleFindPrpl(self, arg_id, *arg, **kw):
		"""
		PurpleFindPrpl method:
		
		Parameters
		----------
		id: s, direction: in,
		RESULT: i, direction: out,
		
		"""
		pass
    
        @DbusSignal
	def AccountConnecting(self, *arg, **kw):
		"""
		AccountConnecting signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountDisabled(self, *arg, **kw):
		"""
		AccountDisabled signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountEnabled(self, *arg, **kw):
		"""
		AccountEnabled signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountSettingInfo(self, *arg, **kw):
		"""
		AccountSettingInfo signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountSetInfo(self, *arg, **kw):
		"""
		AccountSetInfo signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountCreated(self, *arg, **kw):
		"""
		AccountCreated signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountDestroying(self, *arg, **kw):
		"""
		AccountDestroying signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAdded(self, *arg, **kw):
		"""
		AccountAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountRemoved(self, *arg, **kw):
		"""
		AccountRemoved signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountStatusChanged(self, *arg, **kw):
		"""
		AccountStatusChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountActionsChanged(self, *arg, **kw):
		"""
		AccountActionsChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAliasChanged(self, *arg, **kw):
		"""
		AccountAliasChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAuthorizationRequested(self, *arg, **kw):
		"""
		AccountAuthorizationRequested signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAuthorizationRequestedWithMessage(self, *arg, **kw):
		"""
		AccountAuthorizationRequestedWithMessage signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAuthorizationDenied(self, *arg, **kw):
		"""
		AccountAuthorizationDenied signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountAuthorizationGranted(self, *arg, **kw):
		"""
		AccountAuthorizationGranted signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountErrorChanged(self, *arg, **kw):
		"""
		AccountErrorChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountSignedOn(self, *arg, **kw):
		"""
		AccountSignedOn signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountSignedOff(self, *arg, **kw):
		"""
		AccountSignedOff signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def AccountConnectionError(self, *arg, **kw):
		"""
		AccountConnectionError signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyStatusChanged(self, *arg, **kw):
		"""
		BuddyStatusChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyPrivacyChanged(self, *arg, **kw):
		"""
		BuddyPrivacyChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyIdleChanged(self, *arg, **kw):
		"""
		BuddyIdleChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddySignedOn(self, *arg, **kw):
		"""
		BuddySignedOn signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddySignedOff(self, *arg, **kw):
		"""
		BuddySignedOff signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyGotLoginTime(self, *arg, **kw):
		"""
		BuddyGotLoginTime signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BlistNodeAdded(self, *arg, **kw):
		"""
		BlistNodeAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BlistNodeRemoved(self, *arg, **kw):
		"""
		BlistNodeRemoved signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyAdded(self, *arg, **kw):
		"""
		BuddyAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyRemoved(self, *arg, **kw):
		"""
		BuddyRemoved signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyIconChanged(self, *arg, **kw):
		"""
		BuddyIconChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def UpdateIdle(self, *arg, **kw):
		"""
		UpdateIdle signal:
		"""
		pass
    
        @DbusSignal
	def BlistNodeExtendedMenu(self, *arg, **kw):
		"""
		BlistNodeExtendedMenu signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BlistNodeAliased(self, *arg, **kw):
		"""
		BlistNodeAliased signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyCapsChanged(self, *arg, **kw):
		"""
		BuddyCapsChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CertificateStored(self, *arg, **kw):
		"""
		CertificateStored signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CertificateDeleted(self, *arg, **kw):
		"""
		CertificateDeleted signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CipherAdded(self, *arg, **kw):
		"""
		CipherAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CipherRemoved(self, *arg, **kw):
		"""
		CipherRemoved signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CmdAdded(self, *arg, **kw):
		"""
		CmdAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def CmdRemoved(self, *arg, **kw):
		"""
		CmdRemoved signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SigningOn(self, *arg, **kw):
		"""
		SigningOn signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SignedOn(self, *arg, **kw):
		"""
		SignedOn signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SigningOff(self, *arg, **kw):
		"""
		SigningOff signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SignedOff(self, *arg, **kw):
		"""
		SignedOff signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ConnectionError(self, *arg, **kw):
		"""
		ConnectionError signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def Autojoin(self, *arg, **kw):
		"""
		Autojoin signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def WritingImMsg(self, *arg, **kw):
		"""
		WritingImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def WroteImMsg(self, *arg, **kw):
		"""
		WroteImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SentAttention(self, *arg, **kw):
		"""
		SentAttention signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def GotAttention(self, *arg, **kw):
		"""
		GotAttention signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SendingImMsg(self, *arg, **kw):
		"""
		SendingImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SentImMsg(self, *arg, **kw):
		"""
		SentImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ReceivingImMsg(self, *arg, **kw):
		"""
		ReceivingImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ReceivedImMsg(self, *arg, **kw):
		"""
		ReceivedImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BlockedImMsg(self, *arg, **kw):
		"""
		BlockedImMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: u, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def WritingChatMsg(self, *arg, **kw):
		"""
		WritingChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def WroteChatMsg(self, *arg, **kw):
		"""
		WroteChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SendingChatMsg(self, *arg, **kw):
		"""
		SendingChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SentChatMsg(self, *arg, **kw):
		"""
		SentChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ReceivingChatMsg(self, *arg, **kw):
		"""
		ReceivingChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ReceivedChatMsg(self, *arg, **kw):
		"""
		ReceivedChatMsg signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ConversationCreated(self, *arg, **kw):
		"""
		ConversationCreated signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ConversationUpdated(self, *arg, **kw):
		"""
		ConversationUpdated signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def DeletingConversation(self, *arg, **kw):
		"""
		DeletingConversation signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyTyping(self, *arg, **kw):
		"""
		BuddyTyping signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyTyped(self, *arg, **kw):
		"""
		BuddyTyped signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def BuddyTypingStopped(self, *arg, **kw):
		"""
		BuddyTypingStopped signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatBuddyJoining(self, *arg, **kw):
		"""
		ChatBuddyJoining signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatBuddyJoined(self, *arg, **kw):
		"""
		ChatBuddyJoined signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: u, direction: in,
		
		    arg4: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatBuddyFlags(self, *arg, **kw):
		"""
		ChatBuddyFlags signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: u, direction: in,
		
		    arg4: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatBuddyLeaving(self, *arg, **kw):
		"""
		ChatBuddyLeaving signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatBuddyLeft(self, *arg, **kw):
		"""
		ChatBuddyLeft signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def DeletingChatBuddy(self, *arg, **kw):
		"""
		DeletingChatBuddy signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatInvitingUser(self, *arg, **kw):
		"""
		ChatInvitingUser signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatInvitedUser(self, *arg, **kw):
		"""
		ChatInvitedUser signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatInvited(self, *arg, **kw):
		"""
		ChatInvited signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatInviteBlocked(self, *arg, **kw):
		"""
		ChatInviteBlocked signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatJoined(self, *arg, **kw):
		"""
		ChatJoined signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatJoinFailed(self, *arg, **kw):
		"""
		ChatJoinFailed signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatLeft(self, *arg, **kw):
		"""
		ChatLeft signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ChatTopicChanged(self, *arg, **kw):
		"""
		ChatTopicChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ClearedMessageHistory(self, *arg, **kw):
		"""
		ClearedMessageHistory signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ConversationExtendedMenu(self, *arg, **kw):
		"""
		ConversationExtendedMenu signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def UriHandler(self, *arg, **kw):
		"""
		UriHandler signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def Quitting(self, *arg, **kw):
		"""
		Quitting signal:
		"""
		pass
    
        @DbusSignal
	def FileRecvAccept(self, *arg, **kw):
		"""
		FileRecvAccept signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileSendAccept(self, *arg, **kw):
		"""
		FileSendAccept signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileRecvStart(self, *arg, **kw):
		"""
		FileRecvStart signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileSendStart(self, *arg, **kw):
		"""
		FileSendStart signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileSendCancel(self, *arg, **kw):
		"""
		FileSendCancel signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileRecvCancel(self, *arg, **kw):
		"""
		FileRecvCancel signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileSendComplete(self, *arg, **kw):
		"""
		FileSendComplete signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileRecvComplete(self, *arg, **kw):
		"""
		FileRecvComplete signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def FileRecvRequest(self, *arg, **kw):
		"""
		FileRecvRequest signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def ImageDeleting(self, *arg, **kw):
		"""
		ImageDeleting signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def LogTimestamp(self, *arg, **kw):
		"""
		LogTimestamp signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: x, direction: in,
		
		    arg3: b, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def NetworkConfigurationChanged(self, *arg, **kw):
		"""
		NetworkConfigurationChanged signal:
		"""
		pass
    
        @DbusSignal
	def DisplayingEmailNotification(self, *arg, **kw):
		"""
		DisplayingEmailNotification signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def DisplayingEmailsNotification(self, *arg, **kw):
		"""
		DisplayingEmailsNotification signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		    arg4: i, direction: in,
		
		    arg5: u, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def DisplayingUserinfo(self, *arg, **kw):
		"""
		DisplayingUserinfo signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		    arg3: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PluginLoad(self, *arg, **kw):
		"""
		PluginLoad signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PluginUnload(self, *arg, **kw):
		"""
		PluginUnload signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SavedstatusChanged(self, *arg, **kw):
		"""
		SavedstatusChanged signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SavedstatusAdded(self, *arg, **kw):
		"""
		SavedstatusAdded signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SavedstatusDeleted(self, *arg, **kw):
		"""
		SavedstatusDeleted signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def SavedstatusModified(self, *arg, **kw):
		"""
		SavedstatusModified signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def PlayingSoundEvent(self, *arg, **kw):
		"""
		PlayingSoundEvent signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def IrcSendingText(self, *arg, **kw):
		"""
		IrcSendingText signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
    
        @DbusSignal
	def IrcReceivingText(self, *arg, **kw):
		"""
		IrcReceivingText signal:
		
		Parameters
		----------
		
		    arg1: i, direction: in,
		
		    arg2: i, direction: in,
		
		"""
		pass
  
