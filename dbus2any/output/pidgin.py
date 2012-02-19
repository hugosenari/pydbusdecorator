All class:  
from pydbusdecorator import DbusInterface
        
class Introspectable(object):
	@DbusInterface("org.freedesktop.DBus.Introspectable", "/im/pidgin/purple/PurpleObject", "im.pidgin.purple.PurpleService")
	def __init__(self, *arg, **kw):
		pass
    
	@DbusMethod
	def Introspect(self, *arg, **kw):
		"""
		Introspect method:

		Parameters
		----------
		    data: s, out
		"""
		pass
  
class PurpleInterface(object):
	@DbusInterface("im.pidgin.purple.PurpleInterface", "/im/pidgin/purple/PurpleObject", "im.pidgin.purple.PurpleService")
	def __init__(self, *arg, **kw):
		pass
    
	@DbusMethod
	def PurpleAccountsFindAny(self, name, protocol, *arg, **kw):
		"""
		PurpleAccountsFindAny method:

		Parameters
		----------
		    name: s, inprotocol: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsFindConnected(self, name, protocol, *arg, **kw):
		"""
		PurpleAccountsFindConnected method:

		Parameters
		----------
		    name: s, inprotocol: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeIsChat(self, node, *arg, **kw):
		"""
		PurpleBlistNodeIsChat method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeIsBuddy(self, node, *arg, **kw):
		"""
		PurpleBlistNodeIsBuddy method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeIsContact(self, node, *arg, **kw):
		"""
		PurpleBlistNodeIsContact method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeIsGroup(self, node, *arg, **kw):
		"""
		PurpleBlistNodeIsGroup method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIsOnline(self, buddy, *arg, **kw):
		"""
		PurpleBuddyIsOnline method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeHasFlag(self, node, flags, *arg, **kw):
		"""
		PurpleBlistNodeHasFlag method:

		Parameters
		----------
		    node: i, inflags: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeShouldSave(self, node, *arg, **kw):
		"""
		PurpleBlistNodeShouldSave method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionIsConnected(self, connection, *arg, **kw):
		"""
		PurpleConnectionIsConnected method:

		Parameters
		----------
		    connection: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionIsValid(self, connection, *arg, **kw):
		"""
		PurpleConnectionIsValid method:

		Parameters
		----------
		    connection: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvIm(self, conversation, *arg, **kw):
		"""
		PurpleConvIm method:

		Parameters
		----------
		    conversation: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChat(self, conversation, *arg, **kw):
		"""
		PurpleConvChat method:

		Parameters
		----------
		    conversation: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountNew(self, username, protocol_id, *arg, **kw):
		"""
		PurpleAccountNew method:

		Parameters
		----------
		    username: s, inprotocol_id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountDestroy(self, account, *arg, **kw):
		"""
		PurpleAccountDestroy method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountConnect(self, account, *arg, **kw):
		"""
		PurpleAccountConnect method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRegister(self, account, *arg, **kw):
		"""
		PurpleAccountRegister method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountDisconnect(self, account, *arg, **kw):
		"""
		PurpleAccountDisconnect method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountNotifyAdded(self, account, remote_user, id, alias, message, *arg, **kw):
		"""
		PurpleAccountNotifyAdded method:

		Parameters
		----------
		    account: i, inremote_user: s, inid: s, inalias: s, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRequestAdd(self, account, remote_user, id, alias, message, *arg, **kw):
		"""
		PurpleAccountRequestAdd method:

		Parameters
		----------
		    account: i, inremote_user: s, inid: s, inalias: s, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRequestCloseWithAccount(self, account, *arg, **kw):
		"""
		PurpleAccountRequestCloseWithAccount method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRequestClose(self, ui_handle, *arg, **kw):
		"""
		PurpleAccountRequestClose method:

		Parameters
		----------
		    ui_handle: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRequestChangePassword(self, account, *arg, **kw):
		"""
		PurpleAccountRequestChangePassword method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRequestChangeUserInfo(self, account, *arg, **kw):
		"""
		PurpleAccountRequestChangeUserInfo method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetUsername(self, account, username, *arg, **kw):
		"""
		PurpleAccountSetUsername method:

		Parameters
		----------
		    account: i, inusername: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetPassword(self, account, password, *arg, **kw):
		"""
		PurpleAccountSetPassword method:

		Parameters
		----------
		    account: i, inpassword: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetAlias(self, account, alias, *arg, **kw):
		"""
		PurpleAccountSetAlias method:

		Parameters
		----------
		    account: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetUserInfo(self, account, user_info, *arg, **kw):
		"""
		PurpleAccountSetUserInfo method:

		Parameters
		----------
		    account: i, inuser_info: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetBuddyIconPath(self, account, path, *arg, **kw):
		"""
		PurpleAccountSetBuddyIconPath method:

		Parameters
		----------
		    account: i, inpath: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetProtocolId(self, account, protocol_id, *arg, **kw):
		"""
		PurpleAccountSetProtocolId method:

		Parameters
		----------
		    account: i, inprotocol_id: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetConnection(self, account, gc, *arg, **kw):
		"""
		PurpleAccountSetConnection method:

		Parameters
		----------
		    account: i, ingc: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetRememberPassword(self, account, value, *arg, **kw):
		"""
		PurpleAccountSetRememberPassword method:

		Parameters
		----------
		    account: i, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetCheckMail(self, account, value, *arg, **kw):
		"""
		PurpleAccountSetCheckMail method:

		Parameters
		----------
		    account: i, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetEnabled(self, account, ui, value, *arg, **kw):
		"""
		PurpleAccountSetEnabled method:

		Parameters
		----------
		    account: i, inui: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetProxyInfo(self, account, info, *arg, **kw):
		"""
		PurpleAccountSetProxyInfo method:

		Parameters
		----------
		    account: i, ininfo: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetPrivacyType(self, account, privacy_type, *arg, **kw):
		"""
		PurpleAccountSetPrivacyType method:

		Parameters
		----------
		    account: i, inprivacy_type: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetStatusTypes(self, account, status_types, *arg, **kw):
		"""
		PurpleAccountSetStatusTypes method:

		Parameters
		----------
		    account: i, instatus_types: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetStatusList(self, account, status_id, active, attrs, *arg, **kw):
		"""
		PurpleAccountSetStatusList method:

		Parameters
		----------
		    account: i, instatus_id: s, inactive: i, inattrs: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetSilenceSuppression(self, account, *arg, **kw):
		"""
		PurpleAccountGetSilenceSuppression method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetSilenceSuppression(self, account, value, *arg, **kw):
		"""
		PurpleAccountSetSilenceSuppression method:

		Parameters
		----------
		    account: i, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountClearSettings(self, account, *arg, **kw):
		"""
		PurpleAccountClearSettings method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRemoveSetting(self, account, setting, *arg, **kw):
		"""
		PurpleAccountRemoveSetting method:

		Parameters
		----------
		    account: i, insetting: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetInt(self, account, name, value, *arg, **kw):
		"""
		PurpleAccountSetInt method:

		Parameters
		----------
		    account: i, inname: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetString(self, account, name, value, *arg, **kw):
		"""
		PurpleAccountSetString method:

		Parameters
		----------
		    account: i, inname: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetBool(self, account, name, value, *arg, **kw):
		"""
		PurpleAccountSetBool method:

		Parameters
		----------
		    account: i, inname: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetUiInt(self, account, ui, name, value, *arg, **kw):
		"""
		PurpleAccountSetUiInt method:

		Parameters
		----------
		    account: i, inui: s, inname: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetUiString(self, account, ui, name, value, *arg, **kw):
		"""
		PurpleAccountSetUiString method:

		Parameters
		----------
		    account: i, inui: s, inname: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSetUiBool(self, account, ui, name, value, *arg, **kw):
		"""
		PurpleAccountSetUiBool method:

		Parameters
		----------
		    account: i, inui: s, inname: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountIsConnected(self, account, *arg, **kw):
		"""
		PurpleAccountIsConnected method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountIsConnecting(self, account, *arg, **kw):
		"""
		PurpleAccountIsConnecting method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountIsDisconnected(self, account, *arg, **kw):
		"""
		PurpleAccountIsDisconnected method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetUsername(self, account, *arg, **kw):
		"""
		PurpleAccountGetUsername method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetPassword(self, account, *arg, **kw):
		"""
		PurpleAccountGetPassword method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetAlias(self, account, *arg, **kw):
		"""
		PurpleAccountGetAlias method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetUserInfo(self, account, *arg, **kw):
		"""
		PurpleAccountGetUserInfo method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetBuddyIconPath(self, account, *arg, **kw):
		"""
		PurpleAccountGetBuddyIconPath method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetProtocolId(self, account, *arg, **kw):
		"""
		PurpleAccountGetProtocolId method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetProtocolName(self, account, *arg, **kw):
		"""
		PurpleAccountGetProtocolName method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetConnection(self, account, *arg, **kw):
		"""
		PurpleAccountGetConnection method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetNameForDisplay(self, account, *arg, **kw):
		"""
		PurpleAccountGetNameForDisplay method:

		Parameters
		----------
		    account: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetRememberPassword(self, account, *arg, **kw):
		"""
		PurpleAccountGetRememberPassword method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetCheckMail(self, account, *arg, **kw):
		"""
		PurpleAccountGetCheckMail method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetEnabled(self, account, ui, *arg, **kw):
		"""
		PurpleAccountGetEnabled method:

		Parameters
		----------
		    account: i, inui: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetProxyInfo(self, account, *arg, **kw):
		"""
		PurpleAccountGetProxyInfo method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetPrivacyType(self, account, *arg, **kw):
		"""
		PurpleAccountGetPrivacyType method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetActiveStatus(self, account, *arg, **kw):
		"""
		PurpleAccountGetActiveStatus method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetStatus(self, account, status_id, *arg, **kw):
		"""
		PurpleAccountGetStatus method:

		Parameters
		----------
		    account: i, instatus_id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetStatusType(self, account, id, *arg, **kw):
		"""
		PurpleAccountGetStatusType method:

		Parameters
		----------
		    account: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetStatusTypeWithPrimitive(self, account, primitive, *arg, **kw):
		"""
		PurpleAccountGetStatusTypeWithPrimitive method:

		Parameters
		----------
		    account: i, inprimitive: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetPresence(self, account, *arg, **kw):
		"""
		PurpleAccountGetPresence method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountIsStatusActive(self, account, status_id, *arg, **kw):
		"""
		PurpleAccountIsStatusActive method:

		Parameters
		----------
		    account: i, instatus_id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetStatusTypes(self, account, *arg, **kw):
		"""
		PurpleAccountGetStatusTypes method:

		Parameters
		----------
		    account: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetInt(self, account, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetInt method:

		Parameters
		----------
		    account: i, inname: s, indefault_value: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetString(self, account, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetString method:

		Parameters
		----------
		    account: i, inname: s, indefault_value: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetBool(self, account, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetBool method:

		Parameters
		----------
		    account: i, inname: s, indefault_value: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetUiInt(self, account, ui, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetUiInt method:

		Parameters
		----------
		    account: i, inui: s, inname: s, indefault_value: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetUiString(self, account, ui, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetUiString method:

		Parameters
		----------
		    account: i, inui: s, inname: s, indefault_value: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetUiBool(self, account, ui, name, default_value, *arg, **kw):
		"""
		PurpleAccountGetUiBool method:

		Parameters
		----------
		    account: i, inui: s, inname: s, indefault_value: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetLog(self, account, create, *arg, **kw):
		"""
		PurpleAccountGetLog method:

		Parameters
		----------
		    account: i, increate: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountDestroyLog(self, account, *arg, **kw):
		"""
		PurpleAccountDestroyLog method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountAddBuddy(self, account, buddy, *arg, **kw):
		"""
		PurpleAccountAddBuddy method:

		Parameters
		----------
		    account: i, inbuddy: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountAddBuddyWithInvite(self, account, buddy, message, *arg, **kw):
		"""
		PurpleAccountAddBuddyWithInvite method:

		Parameters
		----------
		    account: i, inbuddy: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountAddBuddies(self, account, buddies, *arg, **kw):
		"""
		PurpleAccountAddBuddies method:

		Parameters
		----------
		    account: i, inbuddies: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountAddBuddiesWithInvite(self, account, buddies, message, *arg, **kw):
		"""
		PurpleAccountAddBuddiesWithInvite method:

		Parameters
		----------
		    account: i, inbuddies: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRemoveBuddy(self, account, buddy, group, *arg, **kw):
		"""
		PurpleAccountRemoveBuddy method:

		Parameters
		----------
		    account: i, inbuddy: i, ingroup: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRemoveBuddies(self, account, buddies, groups, *arg, **kw):
		"""
		PurpleAccountRemoveBuddies method:

		Parameters
		----------
		    account: i, inbuddies: i, ingroups: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountRemoveGroup(self, account, group, *arg, **kw):
		"""
		PurpleAccountRemoveGroup method:

		Parameters
		----------
		    account: i, ingroup: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountChangePassword(self, account, orig_pw, new_pw, *arg, **kw):
		"""
		PurpleAccountChangePassword method:

		Parameters
		----------
		    account: i, inorig_pw: s, innew_pw: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountSupportsOfflineMessage(self, account, buddy, *arg, **kw):
		"""
		PurpleAccountSupportsOfflineMessage method:

		Parameters
		----------
		    account: i, inbuddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountGetCurrentError(self, account, *arg, **kw):
		"""
		PurpleAccountGetCurrentError method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountClearCurrentError(self, account, *arg, **kw):
		"""
		PurpleAccountClearCurrentError method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsAdd(self, account, *arg, **kw):
		"""
		PurpleAccountsAdd method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsRemove(self, account, *arg, **kw):
		"""
		PurpleAccountsRemove method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsDelete(self, account, *arg, **kw):
		"""
		PurpleAccountsDelete method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsReorder(self, account, new_index, *arg, **kw):
		"""
		PurpleAccountsReorder method:

		Parameters
		----------
		    account: i, innew_index: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsGetAll(self, *arg, **kw):
		"""
		PurpleAccountsGetAll method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsGetAllActive(self, *arg, **kw):
		"""
		PurpleAccountsGetAllActive method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsFind(self, name, protocol, *arg, **kw):
		"""
		PurpleAccountsFind method:

		Parameters
		----------
		    name: s, inprotocol: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsRestoreCurrentStatuses(self, *arg, **kw):
		"""
		PurpleAccountsRestoreCurrentStatuses method:
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleAccountsSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAccountsGetUiOps(self, *arg, **kw):
		"""
		PurpleAccountsGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
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
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSetBlist(self, blist, *arg, **kw):
		"""
		PurpleSetBlist method:

		Parameters
		----------
		    blist: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleGetBlist(self, *arg, **kw):
		"""
		PurpleGetBlist method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistGetRoot(self, *arg, **kw):
		"""
		PurpleBlistGetRoot method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistGetBuddies(self, *arg, **kw):
		"""
		PurpleBlistGetBuddies method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeNext(self, node, offline, *arg, **kw):
		"""
		PurpleBlistNodeNext method:

		Parameters
		----------
		    node: i, inoffline: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetParent(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetParent method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetFirstChild(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetFirstChild method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetSiblingNext(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetSiblingNext method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetSiblingPrev(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetSiblingPrev method:

		Parameters
		----------
		    node: i, inRESULT: i, out
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
	def PurpleBlistSetVisible(self, show, *arg, **kw):
		"""
		PurpleBlistSetVisible method:

		Parameters
		----------
		    show: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistUpdateBuddyStatus(self, buddy, old_status, *arg, **kw):
		"""
		PurpleBlistUpdateBuddyStatus method:

		Parameters
		----------
		    buddy: i, inold_status: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistUpdateNodeIcon(self, node, *arg, **kw):
		"""
		PurpleBlistUpdateNodeIcon method:

		Parameters
		----------
		    node: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistUpdateBuddyIcon(self, buddy, *arg, **kw):
		"""
		PurpleBlistUpdateBuddyIcon method:

		Parameters
		----------
		    buddy: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRenameBuddy(self, buddy, name, *arg, **kw):
		"""
		PurpleBlistRenameBuddy method:

		Parameters
		----------
		    buddy: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAliasContact(self, contact, alias, *arg, **kw):
		"""
		PurpleBlistAliasContact method:

		Parameters
		----------
		    contact: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAliasBuddy(self, buddy, alias, *arg, **kw):
		"""
		PurpleBlistAliasBuddy method:

		Parameters
		----------
		    buddy: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistServerAliasBuddy(self, buddy, alias, *arg, **kw):
		"""
		PurpleBlistServerAliasBuddy method:

		Parameters
		----------
		    buddy: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAliasChat(self, chat, alias, *arg, **kw):
		"""
		PurpleBlistAliasChat method:

		Parameters
		----------
		    chat: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRenameGroup(self, group, name, *arg, **kw):
		"""
		PurpleBlistRenameGroup method:

		Parameters
		----------
		    group: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleChatNew(self, account, alias, components, *arg, **kw):
		"""
		PurpleChatNew method:

		Parameters
		----------
		    account: i, inalias: s, incomponents: a{ss}, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleChatDestroy(self, chat, *arg, **kw):
		"""
		PurpleChatDestroy method:

		Parameters
		----------
		    chat: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAddChat(self, chat, group, node, *arg, **kw):
		"""
		PurpleBlistAddChat method:

		Parameters
		----------
		    chat: i, ingroup: i, innode: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyNew(self, account, name, alias, *arg, **kw):
		"""
		PurpleBuddyNew method:

		Parameters
		----------
		    account: i, inname: s, inalias: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyDestroy(self, buddy, *arg, **kw):
		"""
		PurpleBuddyDestroy method:

		Parameters
		----------
		    buddy: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddySetIcon(self, buddy, icon, *arg, **kw):
		"""
		PurpleBuddySetIcon method:

		Parameters
		----------
		    buddy: i, inicon: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetAccount(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetAccount method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetName(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetName method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetIcon(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetIcon method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetContact(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetContact method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetPresence(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetPresence method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetMediaCaps(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetMediaCaps method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddySetMediaCaps(self, buddy, media_caps, *arg, **kw):
		"""
		PurpleBuddySetMediaCaps method:

		Parameters
		----------
		    buddy: i, inmedia_caps: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAddBuddy(self, buddy, contact, group, node, *arg, **kw):
		"""
		PurpleBlistAddBuddy method:

		Parameters
		----------
		    buddy: i, incontact: i, ingroup: i, innode: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleGroupNew(self, name, *arg, **kw):
		"""
		PurpleGroupNew method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleGroupDestroy(self, group, *arg, **kw):
		"""
		PurpleGroupDestroy method:

		Parameters
		----------
		    group: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAddGroup(self, group, node, *arg, **kw):
		"""
		PurpleBlistAddGroup method:

		Parameters
		----------
		    group: i, innode: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleContactNew(self, *arg, **kw):
		"""
		PurpleContactNew method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleContactDestroy(self, contact, *arg, **kw):
		"""
		PurpleContactDestroy method:

		Parameters
		----------
		    contact: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleContactGetGroup(self, contact, *arg, **kw):
		"""
		PurpleContactGetGroup method:

		Parameters
		----------
		    contact: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAddContact(self, contact, group, node, *arg, **kw):
		"""
		PurpleBlistAddContact method:

		Parameters
		----------
		    contact: i, ingroup: i, innode: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistMergeContact(self, source, node, *arg, **kw):
		"""
		PurpleBlistMergeContact method:

		Parameters
		----------
		    source: i, innode: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleContactGetPriorityBuddy(self, contact, *arg, **kw):
		"""
		PurpleContactGetPriorityBuddy method:

		Parameters
		----------
		    contact: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleContactSetAlias(self, contact, alias, *arg, **kw):
		"""
		PurpleContactSetAlias method:

		Parameters
		----------
		    contact: i, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleContactGetAlias(self, contact, *arg, **kw):
		"""
		PurpleContactGetAlias method:

		Parameters
		----------
		    contact: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleContactOnAccount(self, contact, account, *arg, **kw):
		"""
		PurpleContactOnAccount method:

		Parameters
		----------
		    contact: i, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleContactInvalidatePriorityBuddy(self, contact, *arg, **kw):
		"""
		PurpleContactInvalidatePriorityBuddy method:

		Parameters
		----------
		    contact: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRemoveBuddy(self, buddy, *arg, **kw):
		"""
		PurpleBlistRemoveBuddy method:

		Parameters
		----------
		    buddy: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRemoveContact(self, contact, *arg, **kw):
		"""
		PurpleBlistRemoveContact method:

		Parameters
		----------
		    contact: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRemoveChat(self, chat, *arg, **kw):
		"""
		PurpleBlistRemoveChat method:

		Parameters
		----------
		    chat: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRemoveGroup(self, group, *arg, **kw):
		"""
		PurpleBlistRemoveGroup method:

		Parameters
		----------
		    group: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetAliasOnly(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetAliasOnly method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetServerAlias(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetServerAlias method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetContactAlias(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetContactAlias method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetLocalAlias(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetLocalAlias method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetAlias(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetAlias method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetLocalBuddyAlias(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetLocalBuddyAlias method:

		Parameters
		----------
		    buddy: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleChatGetName(self, chat, *arg, **kw):
		"""
		PurpleChatGetName method:

		Parameters
		----------
		    chat: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindBuddy(self, account, name, *arg, **kw):
		"""
		PurpleFindBuddy method:

		Parameters
		----------
		    account: i, inname: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindBuddyInGroup(self, account, name, group, *arg, **kw):
		"""
		PurpleFindBuddyInGroup method:

		Parameters
		----------
		    account: i, inname: s, ingroup: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindBuddies(self, account, name, *arg, **kw):
		"""
		PurpleFindBuddies method:

		Parameters
		----------
		    account: i, inname: s, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindGroup(self, name, *arg, **kw):
		"""
		PurpleFindGroup method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistFindChat(self, account, name, *arg, **kw):
		"""
		PurpleBlistFindChat method:

		Parameters
		----------
		    account: i, inname: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleChatGetGroup(self, chat, *arg, **kw):
		"""
		PurpleChatGetGroup method:

		Parameters
		----------
		    chat: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleChatGetAccount(self, chat, *arg, **kw):
		"""
		PurpleChatGetAccount method:

		Parameters
		----------
		    chat: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyGetGroup(self, buddy, *arg, **kw):
		"""
		PurpleBuddyGetGroup method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleGroupGetAccounts(self, g, *arg, **kw):
		"""
		PurpleGroupGetAccounts method:

		Parameters
		----------
		    g: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleGroupOnAccount(self, g, account, *arg, **kw):
		"""
		PurpleGroupOnAccount method:

		Parameters
		----------
		    g: i, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleGroupGetName(self, group, *arg, **kw):
		"""
		PurpleGroupGetName method:

		Parameters
		----------
		    group: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistAddAccount(self, account, *arg, **kw):
		"""
		PurpleBlistAddAccount method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRemoveAccount(self, account, *arg, **kw):
		"""
		PurpleBlistRemoveAccount method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistGetGroupSize(self, group, offline, *arg, **kw):
		"""
		PurpleBlistGetGroupSize method:

		Parameters
		----------
		    group: i, inoffline: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistGetGroupOnlineCount(self, group, *arg, **kw):
		"""
		PurpleBlistGetGroupOnlineCount method:

		Parameters
		----------
		    group: i, inRESULT: i, out
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
	def PurpleBlistRequestAddBuddy(self, account, username, group, alias, *arg, **kw):
		"""
		PurpleBlistRequestAddBuddy method:

		Parameters
		----------
		    account: i, inusername: s, ingroup: s, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRequestAddChat(self, account, group, alias, name, *arg, **kw):
		"""
		PurpleBlistRequestAddChat method:

		Parameters
		----------
		    account: i, ingroup: i, inalias: s, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistRequestAddGroup(self, *arg, **kw):
		"""
		PurpleBlistRequestAddGroup method:
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeSetBool(self, node, key, value, *arg, **kw):
		"""
		PurpleBlistNodeSetBool method:

		Parameters
		----------
		    node: i, inkey: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetBool(self, node, key, *arg, **kw):
		"""
		PurpleBlistNodeGetBool method:

		Parameters
		----------
		    node: i, inkey: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeSetInt(self, node, key, value, *arg, **kw):
		"""
		PurpleBlistNodeSetInt method:

		Parameters
		----------
		    node: i, inkey: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetInt(self, node, key, *arg, **kw):
		"""
		PurpleBlistNodeGetInt method:

		Parameters
		----------
		    node: i, inkey: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeSetString(self, node, key, value, *arg, **kw):
		"""
		PurpleBlistNodeSetString method:

		Parameters
		----------
		    node: i, inkey: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetString(self, node, key, *arg, **kw):
		"""
		PurpleBlistNodeGetString method:

		Parameters
		----------
		    node: i, inkey: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeRemoveSetting(self, node, key, *arg, **kw):
		"""
		PurpleBlistNodeRemoveSetting method:

		Parameters
		----------
		    node: i, inkey: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeSetFlags(self, node, flags, *arg, **kw):
		"""
		PurpleBlistNodeSetFlags method:

		Parameters
		----------
		    node: i, inflags: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetFlags(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetFlags method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetType(self, node, *arg, **kw):
		"""
		PurpleBlistNodeGetType method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistNodeGetExtendedMenu(self, n, *arg, **kw):
		"""
		PurpleBlistNodeGetExtendedMenu method:

		Parameters
		----------
		    n: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleBlistSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleBlistSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBlistGetUiOps(self, *arg, **kw):
		"""
		PurpleBlistGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
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
	def PurpleBuddyIconNew(self, account, username, icon_data, icon_len, checksum, *arg, **kw):
		"""
		PurpleBuddyIconNew method:

		Parameters
		----------
		    account: i, inusername: s, inicon_data: i, inicon_len: i, inchecksum: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconRef(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconRef method:

		Parameters
		----------
		    icon: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconUnref(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconUnref method:

		Parameters
		----------
		    icon: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconUpdate(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconUpdate method:

		Parameters
		----------
		    icon: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconSetData(self, icon, data, len, checksum, *arg, **kw):
		"""
		PurpleBuddyIconSetData method:

		Parameters
		----------
		    icon: i, indata: i, inlen: i, inchecksum: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetAccount(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetAccount method:

		Parameters
		----------
		    icon: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetUsername(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetUsername method:

		Parameters
		----------
		    icon: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetChecksum(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetChecksum method:

		Parameters
		----------
		    icon: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetData(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetData method:

		Parameters
		----------
		    icon: i, inRESULT: ay, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetExtension(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetExtension method:

		Parameters
		----------
		    icon: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconGetFullPath(self, icon, *arg, **kw):
		"""
		PurpleBuddyIconGetFullPath method:

		Parameters
		----------
		    icon: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsSetForUser(self, account, username, icon_data, icon_len, checksum, *arg, **kw):
		"""
		PurpleBuddyIconsSetForUser method:

		Parameters
		----------
		    account: i, inusername: s, inicon_data: i, inicon_len: i, inchecksum: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsFind(self, account, username, *arg, **kw):
		"""
		PurpleBuddyIconsFind method:

		Parameters
		----------
		    account: i, inusername: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsFindAccountIcon(self, account, *arg, **kw):
		"""
		PurpleBuddyIconsFindAccountIcon method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsSetAccountIcon(self, account, icon_data, icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsSetAccountIcon method:

		Parameters
		----------
		    account: i, inicon_data: i, inicon_len: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsGetAccountIconTimestamp(self, account, *arg, **kw):
		"""
		PurpleBuddyIconsGetAccountIconTimestamp method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsNodeHasCustomIcon(self, node, *arg, **kw):
		"""
		PurpleBuddyIconsNodeHasCustomIcon method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsNodeFindCustomIcon(self, node, *arg, **kw):
		"""
		PurpleBuddyIconsNodeFindCustomIcon method:

		Parameters
		----------
		    node: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsNodeSetCustomIcon(self, node, icon_data, icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsNodeSetCustomIcon method:

		Parameters
		----------
		    node: i, inicon_data: i, inicon_len: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsNodeSetCustomIconFromFile(self, node, filename, *arg, **kw):
		"""
		PurpleBuddyIconsNodeSetCustomIconFromFile method:

		Parameters
		----------
		    node: i, infilename: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsHasCustomIcon(self, contact, *arg, **kw):
		"""
		PurpleBuddyIconsHasCustomIcon method:

		Parameters
		----------
		    contact: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsFindCustomIcon(self, contact, *arg, **kw):
		"""
		PurpleBuddyIconsFindCustomIcon method:

		Parameters
		----------
		    contact: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsSetCustomIcon(self, contact, icon_data, icon_len, *arg, **kw):
		"""
		PurpleBuddyIconsSetCustomIcon method:

		Parameters
		----------
		    contact: i, inicon_data: i, inicon_len: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsSetCaching(self, caching, *arg, **kw):
		"""
		PurpleBuddyIconsSetCaching method:

		Parameters
		----------
		    caching: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsIsCaching(self, *arg, **kw):
		"""
		PurpleBuddyIconsIsCaching method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsSetCacheDir(self, cache_dir, *arg, **kw):
		"""
		PurpleBuddyIconsSetCacheDir method:

		Parameters
		----------
		    cache_dir: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuddyIconsGetCacheDir(self, *arg, **kw):
		"""
		PurpleBuddyIconsGetCacheDir method:

		Parameters
		----------
		    RESULT: s, out
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
	def PurpleBuddyIconGetScaleSize(self, spec, width, height, *arg, **kw):
		"""
		PurpleBuddyIconGetScaleSize method:

		Parameters
		----------
		    spec: i, inwidth: i, inheight: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionNew(self, account, regist, password, *arg, **kw):
		"""
		PurpleConnectionNew method:

		Parameters
		----------
		    account: i, inregist: i, inpassword: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionDestroy(self, gc, *arg, **kw):
		"""
		PurpleConnectionDestroy method:

		Parameters
		----------
		    gc: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionSetState(self, gc, state, *arg, **kw):
		"""
		PurpleConnectionSetState method:

		Parameters
		----------
		    gc: i, instate: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionSetAccount(self, gc, account, *arg, **kw):
		"""
		PurpleConnectionSetAccount method:

		Parameters
		----------
		    gc: i, inaccount: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionSetDisplayName(self, gc, name, *arg, **kw):
		"""
		PurpleConnectionSetDisplayName method:

		Parameters
		----------
		    gc: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionSetProtocolData(self, connection, proto_data, *arg, **kw):
		"""
		PurpleConnectionSetProtocolData method:

		Parameters
		----------
		    connection: i, inproto_data: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionGetState(self, gc, *arg, **kw):
		"""
		PurpleConnectionGetState method:

		Parameters
		----------
		    gc: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionGetAccount(self, gc, *arg, **kw):
		"""
		PurpleConnectionGetAccount method:

		Parameters
		----------
		    gc: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionGetPrpl(self, gc, *arg, **kw):
		"""
		PurpleConnectionGetPrpl method:

		Parameters
		----------
		    gc: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionGetPassword(self, gc, *arg, **kw):
		"""
		PurpleConnectionGetPassword method:

		Parameters
		----------
		    gc: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionGetDisplayName(self, gc, *arg, **kw):
		"""
		PurpleConnectionGetDisplayName method:

		Parameters
		----------
		    gc: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionUpdateProgress(self, gc, text, step, count, *arg, **kw):
		"""
		PurpleConnectionUpdateProgress method:

		Parameters
		----------
		    gc: i, intext: s, instep: i, incount: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionNotice(self, gc, text, *arg, **kw):
		"""
		PurpleConnectionNotice method:

		Parameters
		----------
		    gc: i, intext: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionError(self, gc, reason, *arg, **kw):
		"""
		PurpleConnectionError method:

		Parameters
		----------
		    gc: i, inreason: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionErrorReason(self, gc, reason, description, *arg, **kw):
		"""
		PurpleConnectionErrorReason method:

		Parameters
		----------
		    gc: i, inreason: i, indescription: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionSslError(self, gc, ssl_error, *arg, **kw):
		"""
		PurpleConnectionSslError method:

		Parameters
		----------
		    gc: i, inssl_error: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionErrorIsFatal(self, reason, *arg, **kw):
		"""
		PurpleConnectionErrorIsFatal method:

		Parameters
		----------
		    reason: i, inRESULT: i, out
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
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionsGetConnecting(self, *arg, **kw):
		"""
		PurpleConnectionsGetConnecting method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionsSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleConnectionsSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConnectionsGetUiOps(self, *arg, **kw):
		"""
		PurpleConnectionsGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
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
	def PurpleConversationNew(self, type, account, name, *arg, **kw):
		"""
		PurpleConversationNew method:

		Parameters
		----------
		    type: i, inaccount: i, inname: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationDestroy(self, conv, *arg, **kw):
		"""
		PurpleConversationDestroy method:

		Parameters
		----------
		    conv: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationPresent(self, conv, *arg, **kw):
		"""
		PurpleConversationPresent method:

		Parameters
		----------
		    conv: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetType(self, conv, *arg, **kw):
		"""
		PurpleConversationGetType method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetUiOps(self, conv, ops, *arg, **kw):
		"""
		PurpleConversationSetUiOps method:

		Parameters
		----------
		    conv: i, inops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationsSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleConversationsSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetUiOps(self, conv, *arg, **kw):
		"""
		PurpleConversationGetUiOps method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetAccount(self, conv, account, *arg, **kw):
		"""
		PurpleConversationSetAccount method:

		Parameters
		----------
		    conv: i, inaccount: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetAccount(self, conv, *arg, **kw):
		"""
		PurpleConversationGetAccount method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetGc(self, conv, *arg, **kw):
		"""
		PurpleConversationGetGc method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetTitle(self, conv, title, *arg, **kw):
		"""
		PurpleConversationSetTitle method:

		Parameters
		----------
		    conv: i, intitle: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetTitle(self, conv, *arg, **kw):
		"""
		PurpleConversationGetTitle method:

		Parameters
		----------
		    conv: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationAutosetTitle(self, conv, *arg, **kw):
		"""
		PurpleConversationAutosetTitle method:

		Parameters
		----------
		    conv: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetName(self, conv, name, *arg, **kw):
		"""
		PurpleConversationSetName method:

		Parameters
		----------
		    conv: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetName(self, conv, *arg, **kw):
		"""
		PurpleConversationGetName method:

		Parameters
		----------
		    conv: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbGetAttribute(self, cb, key, *arg, **kw):
		"""
		PurpleConvChatCbGetAttribute method:

		Parameters
		----------
		    cb: i, inkey: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbGetAttributeKeys(self, cb, *arg, **kw):
		"""
		PurpleConvChatCbGetAttributeKeys method:

		Parameters
		----------
		    cb: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbSetAttribute(self, chat, cb, key, value, *arg, **kw):
		"""
		PurpleConvChatCbSetAttribute method:

		Parameters
		----------
		    chat: i, incb: i, inkey: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbSetAttributes(self, chat, cb, keys, values, *arg, **kw):
		"""
		PurpleConvChatCbSetAttributes method:

		Parameters
		----------
		    chat: i, incb: i, inkeys: i, invalues: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetLogging(self, conv, log, *arg, **kw):
		"""
		PurpleConversationSetLogging method:

		Parameters
		----------
		    conv: i, inlog: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationIsLogging(self, conv, *arg, **kw):
		"""
		PurpleConversationIsLogging method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetImData(self, conv, *arg, **kw):
		"""
		PurpleConversationGetImData method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetChatData(self, conv, *arg, **kw):
		"""
		PurpleConversationGetChatData method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleGetConversations(self, *arg, **kw):
		"""
		PurpleGetConversations method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleGetIms(self, *arg, **kw):
		"""
		PurpleGetIms method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleGetChats(self, *arg, **kw):
		"""
		PurpleGetChats method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindConversationWithAccount(self, type, name, account, *arg, **kw):
		"""
		PurpleFindConversationWithAccount method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationWrite(self, conv, who, message, flags, mtime, *arg, **kw):
		"""
		PurpleConversationWrite method:

		Parameters
		----------
		    conv: i, inwho: s, inmessage: s, inflags: i, inmtime: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationSetFeatures(self, conv, features, *arg, **kw):
		"""
		PurpleConversationSetFeatures method:

		Parameters
		----------
		    conv: i, infeatures: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetFeatures(self, conv, *arg, **kw):
		"""
		PurpleConversationGetFeatures method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationHasFocus(self, conv, *arg, **kw):
		"""
		PurpleConversationHasFocus method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationUpdate(self, conv, type, *arg, **kw):
		"""
		PurpleConversationUpdate method:

		Parameters
		----------
		    conv: i, intype: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetMessageHistory(self, conv, *arg, **kw):
		"""
		PurpleConversationGetMessageHistory method:

		Parameters
		----------
		    conv: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationClearMessageHistory(self, conv, *arg, **kw):
		"""
		PurpleConversationClearMessageHistory method:

		Parameters
		----------
		    conv: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationMessageGetSender(self, msg, *arg, **kw):
		"""
		PurpleConversationMessageGetSender method:

		Parameters
		----------
		    msg: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationMessageGetMessage(self, msg, *arg, **kw):
		"""
		PurpleConversationMessageGetMessage method:

		Parameters
		----------
		    msg: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationMessageGetFlags(self, msg, *arg, **kw):
		"""
		PurpleConversationMessageGetFlags method:

		Parameters
		----------
		    msg: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConversationMessageGetTimestamp(self, msg, *arg, **kw):
		"""
		PurpleConversationMessageGetTimestamp method:

		Parameters
		----------
		    msg: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetConversation(self, im, *arg, **kw):
		"""
		PurpleConvImGetConversation method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImSetIcon(self, im, icon, *arg, **kw):
		"""
		PurpleConvImSetIcon method:

		Parameters
		----------
		    im: i, inicon: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetIcon(self, im, *arg, **kw):
		"""
		PurpleConvImGetIcon method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImSetTypingState(self, im, state, *arg, **kw):
		"""
		PurpleConvImSetTypingState method:

		Parameters
		----------
		    im: i, instate: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetTypingState(self, im, *arg, **kw):
		"""
		PurpleConvImGetTypingState method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImStartTypingTimeout(self, im, timeout, *arg, **kw):
		"""
		PurpleConvImStartTypingTimeout method:

		Parameters
		----------
		    im: i, intimeout: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImStopTypingTimeout(self, im, *arg, **kw):
		"""
		PurpleConvImStopTypingTimeout method:

		Parameters
		----------
		    im: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetTypingTimeout(self, im, *arg, **kw):
		"""
		PurpleConvImGetTypingTimeout method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImSetTypeAgain(self, im, val, *arg, **kw):
		"""
		PurpleConvImSetTypeAgain method:

		Parameters
		----------
		    im: i, inval: u, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetTypeAgain(self, im, *arg, **kw):
		"""
		PurpleConvImGetTypeAgain method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImStartSendTypedTimeout(self, im, *arg, **kw):
		"""
		PurpleConvImStartSendTypedTimeout method:

		Parameters
		----------
		    im: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImStopSendTypedTimeout(self, im, *arg, **kw):
		"""
		PurpleConvImStopSendTypedTimeout method:

		Parameters
		----------
		    im: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImGetSendTypedTimeout(self, im, *arg, **kw):
		"""
		PurpleConvImGetSendTypedTimeout method:

		Parameters
		----------
		    im: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImUpdateTyping(self, im, *arg, **kw):
		"""
		PurpleConvImUpdateTyping method:

		Parameters
		----------
		    im: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImWrite(self, im, who, message, flags, mtime, *arg, **kw):
		"""
		PurpleConvImWrite method:

		Parameters
		----------
		    im: i, inwho: s, inmessage: s, inflags: i, inmtime: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvPresentError(self, who, account, what, *arg, **kw):
		"""
		PurpleConvPresentError method:

		Parameters
		----------
		    who: s, inaccount: i, inwhat: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvImSend(self, im, message, *arg, **kw):
		"""
		PurpleConvImSend method:

		Parameters
		----------
		    im: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvSendConfirm(self, conv, message, *arg, **kw):
		"""
		PurpleConvSendConfirm method:

		Parameters
		----------
		    conv: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvImSendWithFlags(self, im, message, flags, *arg, **kw):
		"""
		PurpleConvImSendWithFlags method:

		Parameters
		----------
		    im: i, inmessage: s, inflags: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvCustomSmileyAdd(self, conv, smile, cksum_type, chksum, remote, *arg, **kw):
		"""
		PurpleConvCustomSmileyAdd method:

		Parameters
		----------
		    conv: i, insmile: s, incksum_type: s, inchksum: s, inremote: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvCustomSmileyClose(self, conv, smile, *arg, **kw):
		"""
		PurpleConvCustomSmileyClose method:

		Parameters
		----------
		    conv: i, insmile: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetConversation(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetConversation method:

		Parameters
		----------
		    chat: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSetUsers(self, chat, users, *arg, **kw):
		"""
		PurpleConvChatSetUsers method:

		Parameters
		----------
		    chat: i, inusers: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetUsers(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetUsers method:

		Parameters
		----------
		    chat: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatIgnore(self, chat, name, *arg, **kw):
		"""
		PurpleConvChatIgnore method:

		Parameters
		----------
		    chat: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatUnignore(self, chat, name, *arg, **kw):
		"""
		PurpleConvChatUnignore method:

		Parameters
		----------
		    chat: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSetIgnored(self, chat, ignored, *arg, **kw):
		"""
		PurpleConvChatSetIgnored method:

		Parameters
		----------
		    chat: i, inignored: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetIgnored(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetIgnored method:

		Parameters
		----------
		    chat: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetIgnoredUser(self, chat, user, *arg, **kw):
		"""
		PurpleConvChatGetIgnoredUser method:

		Parameters
		----------
		    chat: i, inuser: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatIsUserIgnored(self, chat, user, *arg, **kw):
		"""
		PurpleConvChatIsUserIgnored method:

		Parameters
		----------
		    chat: i, inuser: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSetTopic(self, chat, who, topic, *arg, **kw):
		"""
		PurpleConvChatSetTopic method:

		Parameters
		----------
		    chat: i, inwho: s, intopic: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetTopic(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetTopic method:

		Parameters
		----------
		    chat: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSetId(self, chat, id, *arg, **kw):
		"""
		PurpleConvChatSetId method:

		Parameters
		----------
		    chat: i, inid: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetId(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetId method:

		Parameters
		----------
		    chat: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatWrite(self, chat, who, message, flags, mtime, *arg, **kw):
		"""
		PurpleConvChatWrite method:

		Parameters
		----------
		    chat: i, inwho: s, inmessage: s, inflags: i, inmtime: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSend(self, chat, message, *arg, **kw):
		"""
		PurpleConvChatSend method:

		Parameters
		----------
		    chat: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSendWithFlags(self, chat, message, flags, *arg, **kw):
		"""
		PurpleConvChatSendWithFlags method:

		Parameters
		----------
		    chat: i, inmessage: s, inflags: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatAddUser(self, chat, user, extra_msg, flags, new_arrival, *arg, **kw):
		"""
		PurpleConvChatAddUser method:

		Parameters
		----------
		    chat: i, inuser: s, inextra_msg: s, inflags: i, innew_arrival: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatAddUsers(self, chat, users, extra_msgs, flags, new_arrivals, *arg, **kw):
		"""
		PurpleConvChatAddUsers method:

		Parameters
		----------
		    chat: i, inusers: i, inextra_msgs: i, inflags: i, innew_arrivals: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatRenameUser(self, chat, old_user, new_user, *arg, **kw):
		"""
		PurpleConvChatRenameUser method:

		Parameters
		----------
		    chat: i, inold_user: s, innew_user: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatRemoveUser(self, chat, user, reason, *arg, **kw):
		"""
		PurpleConvChatRemoveUser method:

		Parameters
		----------
		    chat: i, inuser: s, inreason: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatRemoveUsers(self, chat, users, reason, *arg, **kw):
		"""
		PurpleConvChatRemoveUsers method:

		Parameters
		----------
		    chat: i, inusers: i, inreason: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatFindUser(self, chat, user, *arg, **kw):
		"""
		PurpleConvChatFindUser method:

		Parameters
		----------
		    chat: i, inuser: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatUserSetFlags(self, chat, user, flags, *arg, **kw):
		"""
		PurpleConvChatUserSetFlags method:

		Parameters
		----------
		    chat: i, inuser: s, inflags: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatUserGetFlags(self, chat, user, *arg, **kw):
		"""
		PurpleConvChatUserGetFlags method:

		Parameters
		----------
		    chat: i, inuser: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatClearUsers(self, chat, *arg, **kw):
		"""
		PurpleConvChatClearUsers method:

		Parameters
		----------
		    chat: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatSetNick(self, chat, nick, *arg, **kw):
		"""
		PurpleConvChatSetNick method:

		Parameters
		----------
		    chat: i, innick: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatGetNick(self, chat, *arg, **kw):
		"""
		PurpleConvChatGetNick method:

		Parameters
		----------
		    chat: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleFindChat(self, gc, id, *arg, **kw):
		"""
		PurpleFindChat method:

		Parameters
		----------
		    gc: i, inid: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatLeft(self, chat, *arg, **kw):
		"""
		PurpleConvChatLeft method:

		Parameters
		----------
		    chat: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatInviteUser(self, chat, user, message, confirm, *arg, **kw):
		"""
		PurpleConvChatInviteUser method:

		Parameters
		----------
		    chat: i, inuser: s, inmessage: s, inconfirm: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatHasLeft(self, chat, *arg, **kw):
		"""
		PurpleConvChatHasLeft method:

		Parameters
		----------
		    chat: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbNew(self, name, alias, flags, *arg, **kw):
		"""
		PurpleConvChatCbNew method:

		Parameters
		----------
		    name: s, inalias: s, inflags: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbFind(self, chat, name, *arg, **kw):
		"""
		PurpleConvChatCbFind method:

		Parameters
		----------
		    chat: i, inname: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbGetName(self, cb, *arg, **kw):
		"""
		PurpleConvChatCbGetName method:

		Parameters
		----------
		    cb: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleConvChatCbDestroy(self, cb, *arg, **kw):
		"""
		PurpleConvChatCbDestroy method:

		Parameters
		----------
		    cb: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleConversationGetExtendedMenu(self, conv, *arg, **kw):
		"""
		PurpleConversationGetExtendedMenu method:

		Parameters
		----------
		    conv: i, inRESULT: ai, out
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
	def PurpleCoreInit(self, ui, *arg, **kw):
		"""
		PurpleCoreInit method:

		Parameters
		----------
		    ui: s, inRESULT: i, out
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
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleCoreGetUi(self, *arg, **kw):
		"""
		PurpleCoreGetUi method:

		Parameters
		----------
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleGetCore(self, *arg, **kw):
		"""
		PurpleGetCore method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleCoreSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleCoreSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleCoreGetUiOps(self, *arg, **kw):
		"""
		PurpleCoreGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleCoreMigrate(self, *arg, **kw):
		"""
		PurpleCoreMigrate method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleCoreEnsureSingleInstance(self, *arg, **kw):
		"""
		PurpleCoreEnsureSingleInstance method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferNew(self, account, type, who, *arg, **kw):
		"""
		PurpleXferNew method:

		Parameters
		----------
		    account: i, intype: i, inwho: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXfersGetAll(self, *arg, **kw):
		"""
		PurpleXfersGetAll method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferRef(self, xfer, *arg, **kw):
		"""
		PurpleXferRef method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferUnref(self, xfer, *arg, **kw):
		"""
		PurpleXferUnref method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferRequest(self, xfer, *arg, **kw):
		"""
		PurpleXferRequest method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferRequestAccepted(self, xfer, filename, *arg, **kw):
		"""
		PurpleXferRequestAccepted method:

		Parameters
		----------
		    xfer: i, infilename: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferRequestDenied(self, xfer, *arg, **kw):
		"""
		PurpleXferRequestDenied method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetType(self, xfer, *arg, **kw):
		"""
		PurpleXferGetType method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetAccount(self, xfer, *arg, **kw):
		"""
		PurpleXferGetAccount method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetRemoteUser(self, xfer, *arg, **kw):
		"""
		PurpleXferGetRemoteUser method:

		Parameters
		----------
		    xfer: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetStatus(self, xfer, *arg, **kw):
		"""
		PurpleXferGetStatus method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferIsCanceled(self, xfer, *arg, **kw):
		"""
		PurpleXferIsCanceled method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferIsCompleted(self, xfer, *arg, **kw):
		"""
		PurpleXferIsCompleted method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetFilename(self, xfer, *arg, **kw):
		"""
		PurpleXferGetFilename method:

		Parameters
		----------
		    xfer: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetLocalFilename(self, xfer, *arg, **kw):
		"""
		PurpleXferGetLocalFilename method:

		Parameters
		----------
		    xfer: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetBytesSent(self, xfer, *arg, **kw):
		"""
		PurpleXferGetBytesSent method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetBytesRemaining(self, xfer, *arg, **kw):
		"""
		PurpleXferGetBytesRemaining method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetSize(self, xfer, *arg, **kw):
		"""
		PurpleXferGetSize method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetLocalPort(self, xfer, *arg, **kw):
		"""
		PurpleXferGetLocalPort method:

		Parameters
		----------
		    xfer: i, inRESULT: u, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetRemoteIp(self, xfer, *arg, **kw):
		"""
		PurpleXferGetRemoteIp method:

		Parameters
		----------
		    xfer: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetRemotePort(self, xfer, *arg, **kw):
		"""
		PurpleXferGetRemotePort method:

		Parameters
		----------
		    xfer: i, inRESULT: u, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetStartTime(self, xfer, *arg, **kw):
		"""
		PurpleXferGetStartTime method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetEndTime(self, xfer, *arg, **kw):
		"""
		PurpleXferGetEndTime method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetCompleted(self, xfer, completed, *arg, **kw):
		"""
		PurpleXferSetCompleted method:

		Parameters
		----------
		    xfer: i, incompleted: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetMessage(self, xfer, message, *arg, **kw):
		"""
		PurpleXferSetMessage method:

		Parameters
		----------
		    xfer: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetFilename(self, xfer, filename, *arg, **kw):
		"""
		PurpleXferSetFilename method:

		Parameters
		----------
		    xfer: i, infilename: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetLocalFilename(self, xfer, filename, *arg, **kw):
		"""
		PurpleXferSetLocalFilename method:

		Parameters
		----------
		    xfer: i, infilename: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetSize(self, xfer, size, *arg, **kw):
		"""
		PurpleXferSetSize method:

		Parameters
		----------
		    xfer: i, insize: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferSetBytesSent(self, xfer, bytes_sent, *arg, **kw):
		"""
		PurpleXferSetBytesSent method:

		Parameters
		----------
		    xfer: i, inbytes_sent: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetUiOps(self, xfer, *arg, **kw):
		"""
		PurpleXferGetUiOps method:

		Parameters
		----------
		    xfer: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferStart(self, xfer, fd, ip, port, *arg, **kw):
		"""
		PurpleXferStart method:

		Parameters
		----------
		    xfer: i, infd: i, inip: s, inport: u, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferEnd(self, xfer, *arg, **kw):
		"""
		PurpleXferEnd method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferAdd(self, xfer, *arg, **kw):
		"""
		PurpleXferAdd method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferCancelLocal(self, xfer, *arg, **kw):
		"""
		PurpleXferCancelLocal method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferCancelRemote(self, xfer, *arg, **kw):
		"""
		PurpleXferCancelRemote method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferError(self, type, account, who, msg, *arg, **kw):
		"""
		PurpleXferError method:

		Parameters
		----------
		    type: i, inaccount: i, inwho: s, inmsg: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferUpdateProgress(self, xfer, *arg, **kw):
		"""
		PurpleXferUpdateProgress method:

		Parameters
		----------
		    xfer: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetThumbnail(self, xfer, *arg, **kw):
		"""
		PurpleXferGetThumbnail method:

		Parameters
		----------
		    xfer: i, inRESULT: ay, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferGetThumbnailMimetype(self, xfer, *arg, **kw):
		"""
		PurpleXferGetThumbnailMimetype method:

		Parameters
		----------
		    xfer: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleXferPrepareThumbnail(self, xfer, formats, *arg, **kw):
		"""
		PurpleXferPrepareThumbnail method:

		Parameters
		----------
		    xfer: i, informats: s, in
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
	def PurpleXfersSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleXfersSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleXfersGetUiOps(self, *arg, **kw):
		"""
		PurpleXfersGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogFree(self, log, *arg, **kw):
		"""
		PurpleLogFree method:

		Parameters
		----------
		    log: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogWrite(self, log, type, from, time, message, *arg, **kw):
		"""
		PurpleLogWrite method:

		Parameters
		----------
		    log: i, intype: i, infrom: s, intime: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetLogs(self, type, name, account, *arg, **kw):
		"""
		PurpleLogGetLogs method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetSystemLogs(self, account, *arg, **kw):
		"""
		PurpleLogGetSystemLogs method:

		Parameters
		----------
		    account: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetSize(self, log, *arg, **kw):
		"""
		PurpleLogGetSize method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetTotalSize(self, type, name, account, *arg, **kw):
		"""
		PurpleLogGetTotalSize method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetActivityScore(self, type, name, account, *arg, **kw):
		"""
		PurpleLogGetActivityScore method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogIsDeletable(self, log, *arg, **kw):
		"""
		PurpleLogIsDeletable method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogDelete(self, log, *arg, **kw):
		"""
		PurpleLogDelete method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogGetLogDir(self, type, name, account, *arg, **kw):
		"""
		PurpleLogGetLogDir method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogSetFree(self, set, *arg, **kw):
		"""
		PurpleLogSetFree method:

		Parameters
		----------
		    set: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonWriter(self, log, ext, *arg, **kw):
		"""
		PurpleLogCommonWriter method:

		Parameters
		----------
		    log: i, inext: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonLister(self, type, name, account, ext, logger, *arg, **kw):
		"""
		PurpleLogCommonLister method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inext: s, inlogger: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonTotalSizer(self, type, name, account, ext, *arg, **kw):
		"""
		PurpleLogCommonTotalSizer method:

		Parameters
		----------
		    type: i, inname: s, inaccount: i, inext: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonSizer(self, log, *arg, **kw):
		"""
		PurpleLogCommonSizer method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonDeleter(self, log, *arg, **kw):
		"""
		PurpleLogCommonDeleter method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogCommonIsDeletable(self, log, *arg, **kw):
		"""
		PurpleLogCommonIsDeletable method:

		Parameters
		----------
		    log: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerFree(self, logger, *arg, **kw):
		"""
		PurpleLogLoggerFree method:

		Parameters
		----------
		    logger: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerAdd(self, logger, *arg, **kw):
		"""
		PurpleLogLoggerAdd method:

		Parameters
		----------
		    logger: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerRemove(self, logger, *arg, **kw):
		"""
		PurpleLogLoggerRemove method:

		Parameters
		----------
		    logger: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerSet(self, logger, *arg, **kw):
		"""
		PurpleLogLoggerSet method:

		Parameters
		----------
		    logger: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerGet(self, *arg, **kw):
		"""
		PurpleLogLoggerGet method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleLogLoggerGetOptions(self, *arg, **kw):
		"""
		PurpleLogLoggerGetOptions method:

		Parameters
		----------
		    RESULT: ai, out
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
	def PurpleNotifySearchresultsFree(self, results, *arg, **kw):
		"""
		PurpleNotifySearchresultsFree method:

		Parameters
		----------
		    results: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsNewRows(self, gc, results, data, *arg, **kw):
		"""
		PurpleNotifySearchresultsNewRows method:

		Parameters
		----------
		    gc: i, inresults: i, indata: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsNew(self, *arg, **kw):
		"""
		PurpleNotifySearchresultsNew method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsColumnNew(self, title, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnNew method:

		Parameters
		----------
		    title: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsColumnAdd(self, results, column, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnAdd method:

		Parameters
		----------
		    results: i, incolumn: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsRowAdd(self, results, row, *arg, **kw):
		"""
		PurpleNotifySearchresultsRowAdd method:

		Parameters
		----------
		    results: i, inrow: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsGetRowsCount(self, results, *arg, **kw):
		"""
		PurpleNotifySearchresultsGetRowsCount method:

		Parameters
		----------
		    results: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsGetColumnsCount(self, results, *arg, **kw):
		"""
		PurpleNotifySearchresultsGetColumnsCount method:

		Parameters
		----------
		    results: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsRowGet(self, results, row_id, *arg, **kw):
		"""
		PurpleNotifySearchresultsRowGet method:

		Parameters
		----------
		    results: i, inrow_id: u, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySearchresultsColumnGetTitle(self, results, column_id, *arg, **kw):
		"""
		PurpleNotifySearchresultsColumnGetTitle method:

		Parameters
		----------
		    results: i, incolumn_id: u, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoNew(self, *arg, **kw):
		"""
		PurpleNotifyUserInfoNew method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoDestroy(self, user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoDestroy method:

		Parameters
		----------
		    user_info: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoGetEntries(self, user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoGetEntries method:

		Parameters
		----------
		    user_info: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoGetTextWithNewline(self, user_info, newline, *arg, **kw):
		"""
		PurpleNotifyUserInfoGetTextWithNewline method:

		Parameters
		----------
		    user_info: i, innewline: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoAddPair(self, user_info, label, value, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddPair method:

		Parameters
		----------
		    user_info: i, inlabel: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoAddPairPlaintext(self, user_info, label, value, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddPairPlaintext method:

		Parameters
		----------
		    user_info: i, inlabel: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoPrependPair(self, user_info, label, value, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependPair method:

		Parameters
		----------
		    user_info: i, inlabel: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoRemoveEntry(self, user_info, user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoRemoveEntry method:

		Parameters
		----------
		    user_info: i, inuser_info_entry: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntryNew(self, label, value, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryNew method:

		Parameters
		----------
		    label: s, invalue: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoAddSectionBreak(self, user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddSectionBreak method:

		Parameters
		----------
		    user_info: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoPrependSectionBreak(self, user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependSectionBreak method:

		Parameters
		----------
		    user_info: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoAddSectionHeader(self, user_info, label, *arg, **kw):
		"""
		PurpleNotifyUserInfoAddSectionHeader method:

		Parameters
		----------
		    user_info: i, inlabel: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoPrependSectionHeader(self, user_info, label, *arg, **kw):
		"""
		PurpleNotifyUserInfoPrependSectionHeader method:

		Parameters
		----------
		    user_info: i, inlabel: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoRemoveLastItem(self, user_info, *arg, **kw):
		"""
		PurpleNotifyUserInfoRemoveLastItem method:

		Parameters
		----------
		    user_info: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntryGetLabel(self, user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetLabel method:

		Parameters
		----------
		    user_info_entry: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntrySetLabel(self, user_info_entry, label, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetLabel method:

		Parameters
		----------
		    user_info_entry: i, inlabel: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntryGetValue(self, user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetValue method:

		Parameters
		----------
		    user_info_entry: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntrySetValue(self, user_info_entry, value, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetValue method:

		Parameters
		----------
		    user_info_entry: i, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntryGetType(self, user_info_entry, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntryGetType method:

		Parameters
		----------
		    user_info_entry: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyUserInfoEntrySetType(self, user_info_entry, type, *arg, **kw):
		"""
		PurpleNotifyUserInfoEntrySetType method:

		Parameters
		----------
		    user_info_entry: i, intype: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyClose(self, type, ui_handle, *arg, **kw):
		"""
		PurpleNotifyClose method:

		Parameters
		----------
		    type: i, inui_handle: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyCloseWithHandle(self, handle, *arg, **kw):
		"""
		PurpleNotifyCloseWithHandle method:

		Parameters
		----------
		    handle: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifySetUiOps(self, ops, *arg, **kw):
		"""
		PurpleNotifySetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleNotifyGetUiOps(self, *arg, **kw):
		"""
		PurpleNotifyGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
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
	def PurplePrefsAddNone(self, name, *arg, **kw):
		"""
		PurplePrefsAddNone method:

		Parameters
		----------
		    name: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddBool(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddBool method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddInt(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddInt method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddString(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddString method:

		Parameters
		----------
		    name: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddStringList(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddStringList method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddPath(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddPath method:

		Parameters
		----------
		    name: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsAddPathList(self, name, value, *arg, **kw):
		"""
		PurplePrefsAddPathList method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsRemove(self, name, *arg, **kw):
		"""
		PurplePrefsRemove method:

		Parameters
		----------
		    name: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsRename(self, oldname, newname, *arg, **kw):
		"""
		PurplePrefsRename method:

		Parameters
		----------
		    oldname: s, innewname: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsRenameBooleanToggle(self, oldname, newname, *arg, **kw):
		"""
		PurplePrefsRenameBooleanToggle method:

		Parameters
		----------
		    oldname: s, innewname: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsDestroy(self, *arg, **kw):
		"""
		PurplePrefsDestroy method:
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetBool(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetBool method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetInt(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetInt method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetString(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetString method:

		Parameters
		----------
		    name: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetStringList(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetStringList method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetPath(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetPath method:

		Parameters
		----------
		    name: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsSetPathList(self, name, value, *arg, **kw):
		"""
		PurplePrefsSetPathList method:

		Parameters
		----------
		    name: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsExists(self, name, *arg, **kw):
		"""
		PurplePrefsExists method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetType(self, name, *arg, **kw):
		"""
		PurplePrefsGetType method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetBool(self, name, *arg, **kw):
		"""
		PurplePrefsGetBool method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetInt(self, name, *arg, **kw):
		"""
		PurplePrefsGetInt method:

		Parameters
		----------
		    name: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetString(self, name, *arg, **kw):
		"""
		PurplePrefsGetString method:

		Parameters
		----------
		    name: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetStringList(self, name, *arg, **kw):
		"""
		PurplePrefsGetStringList method:

		Parameters
		----------
		    name: s, inRESULT: as, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetPath(self, name, *arg, **kw):
		"""
		PurplePrefsGetPath method:

		Parameters
		----------
		    name: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetPathList(self, name, *arg, **kw):
		"""
		PurplePrefsGetPathList method:

		Parameters
		----------
		    name: s, inRESULT: as, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsGetChildrenNames(self, name, *arg, **kw):
		"""
		PurplePrefsGetChildrenNames method:

		Parameters
		----------
		    name: s, inRESULT: as, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsDisconnectCallback(self, callback_id, *arg, **kw):
		"""
		PurplePrefsDisconnectCallback method:

		Parameters
		----------
		    callback_id: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsDisconnectByHandle(self, handle, *arg, **kw):
		"""
		PurplePrefsDisconnectByHandle method:

		Parameters
		----------
		    handle: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsTriggerCallback(self, name, *arg, **kw):
		"""
		PurplePrefsTriggerCallback method:

		Parameters
		----------
		    name: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrefsLoad(self, *arg, **kw):
		"""
		PurplePrefsLoad method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrefsUpdateOld(self, *arg, **kw):
		"""
		PurplePrefsUpdateOld method:
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistShowWithAccount(self, account, *arg, **kw):
		"""
		PurpleRoomlistShowWithAccount method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistNew(self, account, *arg, **kw):
		"""
		PurpleRoomlistNew method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRef(self, list, *arg, **kw):
		"""
		PurpleRoomlistRef method:

		Parameters
		----------
		    list: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistUnref(self, list, *arg, **kw):
		"""
		PurpleRoomlistUnref method:

		Parameters
		----------
		    list: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistSetFields(self, list, fields, *arg, **kw):
		"""
		PurpleRoomlistSetFields method:

		Parameters
		----------
		    list: i, infields: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistSetInProgress(self, list, in_progress, *arg, **kw):
		"""
		PurpleRoomlistSetInProgress method:

		Parameters
		----------
		    list: i, inin_progress: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistGetInProgress(self, list, *arg, **kw):
		"""
		PurpleRoomlistGetInProgress method:

		Parameters
		----------
		    list: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomAdd(self, list, room, *arg, **kw):
		"""
		PurpleRoomlistRoomAdd method:

		Parameters
		----------
		    list: i, inroom: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistGetList(self, gc, *arg, **kw):
		"""
		PurpleRoomlistGetList method:

		Parameters
		----------
		    gc: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistCancelGetList(self, list, *arg, **kw):
		"""
		PurpleRoomlistCancelGetList method:

		Parameters
		----------
		    list: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistExpandCategory(self, list, category, *arg, **kw):
		"""
		PurpleRoomlistExpandCategory method:

		Parameters
		----------
		    list: i, incategory: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistGetFields(self, roomlist, *arg, **kw):
		"""
		PurpleRoomlistGetFields method:

		Parameters
		----------
		    roomlist: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomNew(self, type, name, parent, *arg, **kw):
		"""
		PurpleRoomlistRoomNew method:

		Parameters
		----------
		    type: i, inname: s, inparent: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomJoin(self, list, room, *arg, **kw):
		"""
		PurpleRoomlistRoomJoin method:

		Parameters
		----------
		    list: i, inroom: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomGetType(self, room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetType method:

		Parameters
		----------
		    room: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomGetName(self, room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetName method:

		Parameters
		----------
		    room: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomGetParent(self, room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetParent method:

		Parameters
		----------
		    room: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistRoomGetFields(self, room, *arg, **kw):
		"""
		PurpleRoomlistRoomGetFields method:

		Parameters
		----------
		    room: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistFieldNew(self, type, label, name, hidden, *arg, **kw):
		"""
		PurpleRoomlistFieldNew method:

		Parameters
		----------
		    type: i, inlabel: s, inname: s, inhidden: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistFieldGetType(self, field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetType method:

		Parameters
		----------
		    field: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistFieldGetLabel(self, field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetLabel method:

		Parameters
		----------
		    field: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistFieldGetHidden(self, field, *arg, **kw):
		"""
		PurpleRoomlistFieldGetHidden method:

		Parameters
		----------
		    field: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistSetUiOps(self, ops, *arg, **kw):
		"""
		PurpleRoomlistSetUiOps method:

		Parameters
		----------
		    ops: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleRoomlistGetUiOps(self, *arg, **kw):
		"""
		PurpleRoomlistGetUiOps method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusNew(self, title, type, *arg, **kw):
		"""
		PurpleSavedstatusNew method:

		Parameters
		----------
		    title: s, intype: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSetTitle(self, status, title, *arg, **kw):
		"""
		PurpleSavedstatusSetTitle method:

		Parameters
		----------
		    status: i, intitle: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSetType(self, status, type, *arg, **kw):
		"""
		PurpleSavedstatusSetType method:

		Parameters
		----------
		    status: i, intype: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSetMessage(self, status, message, *arg, **kw):
		"""
		PurpleSavedstatusSetMessage method:

		Parameters
		----------
		    status: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSetSubstatus(self, status, account, type, message, *arg, **kw):
		"""
		PurpleSavedstatusSetSubstatus method:

		Parameters
		----------
		    status: i, inaccount: i, intype: i, inmessage: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusUnsetSubstatus(self, saved_status, account, *arg, **kw):
		"""
		PurpleSavedstatusUnsetSubstatus method:

		Parameters
		----------
		    saved_status: i, inaccount: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusDelete(self, title, *arg, **kw):
		"""
		PurpleSavedstatusDelete method:

		Parameters
		----------
		    title: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusDeleteByStatus(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusDeleteByStatus method:

		Parameters
		----------
		    saved_status: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusesGetAll(self, *arg, **kw):
		"""
		PurpleSavedstatusesGetAll method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusesGetPopular(self, how_many, *arg, **kw):
		"""
		PurpleSavedstatusesGetPopular method:

		Parameters
		----------
		    how_many: u, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetCurrent(self, *arg, **kw):
		"""
		PurpleSavedstatusGetCurrent method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetDefault(self, *arg, **kw):
		"""
		PurpleSavedstatusGetDefault method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetIdleaway(self, *arg, **kw):
		"""
		PurpleSavedstatusGetIdleaway method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusIsIdleaway(self, *arg, **kw):
		"""
		PurpleSavedstatusIsIdleaway method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSetIdleaway(self, idleaway, *arg, **kw):
		"""
		PurpleSavedstatusSetIdleaway method:

		Parameters
		----------
		    idleaway: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetStartup(self, *arg, **kw):
		"""
		PurpleSavedstatusGetStartup method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusFind(self, title, *arg, **kw):
		"""
		PurpleSavedstatusFind method:

		Parameters
		----------
		    title: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusFindByCreationTime(self, creation_time, *arg, **kw):
		"""
		PurpleSavedstatusFindByCreationTime method:

		Parameters
		----------
		    creation_time: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusFindTransientByTypeAndMessage(self, type, message, *arg, **kw):
		"""
		PurpleSavedstatusFindTransientByTypeAndMessage method:

		Parameters
		----------
		    type: i, inmessage: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusIsTransient(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusIsTransient method:

		Parameters
		----------
		    saved_status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetTitle(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetTitle method:

		Parameters
		----------
		    saved_status: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetType(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetType method:

		Parameters
		----------
		    saved_status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetMessage(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetMessage method:

		Parameters
		----------
		    saved_status: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetCreationTime(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusGetCreationTime method:

		Parameters
		----------
		    saved_status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusHasSubstatuses(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusHasSubstatuses method:

		Parameters
		----------
		    saved_status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusGetSubstatus(self, saved_status, account, *arg, **kw):
		"""
		PurpleSavedstatusGetSubstatus method:

		Parameters
		----------
		    saved_status: i, inaccount: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSubstatusGetType(self, substatus, *arg, **kw):
		"""
		PurpleSavedstatusSubstatusGetType method:

		Parameters
		----------
		    substatus: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusSubstatusGetMessage(self, substatus, *arg, **kw):
		"""
		PurpleSavedstatusSubstatusGetMessage method:

		Parameters
		----------
		    substatus: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusActivate(self, saved_status, *arg, **kw):
		"""
		PurpleSavedstatusActivate method:

		Parameters
		----------
		    saved_status: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSavedstatusActivateForAccount(self, saved_status, account, *arg, **kw):
		"""
		PurpleSavedstatusActivateForAccount method:

		Parameters
		----------
		    saved_status: i, inaccount: i, in
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
	def PurpleSmileyNew(self, img, shortcut, *arg, **kw):
		"""
		PurpleSmileyNew method:

		Parameters
		----------
		    img: i, inshortcut: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyNewFromFile(self, shortcut, filepath, *arg, **kw):
		"""
		PurpleSmileyNewFromFile method:

		Parameters
		----------
		    shortcut: s, infilepath: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyDelete(self, smiley, *arg, **kw):
		"""
		PurpleSmileyDelete method:

		Parameters
		----------
		    smiley: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSmileySetShortcut(self, smiley, shortcut, *arg, **kw):
		"""
		PurpleSmileySetShortcut method:

		Parameters
		----------
		    smiley: i, inshortcut: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileySetData(self, smiley, smiley_data, smiley_data_len, *arg, **kw):
		"""
		PurpleSmileySetData method:

		Parameters
		----------
		    smiley: i, insmiley_data: i, insmiley_data_len: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetShortcut(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetShortcut method:

		Parameters
		----------
		    smiley: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetChecksum(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetChecksum method:

		Parameters
		----------
		    smiley: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetStoredImage(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetStoredImage method:

		Parameters
		----------
		    smiley: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetData(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetData method:

		Parameters
		----------
		    smiley: i, inRESULT: ay, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetExtension(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetExtension method:

		Parameters
		----------
		    smiley: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileyGetFullPath(self, smiley, *arg, **kw):
		"""
		PurpleSmileyGetFullPath method:

		Parameters
		----------
		    smiley: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileysGetAll(self, *arg, **kw):
		"""
		PurpleSmileysGetAll method:

		Parameters
		----------
		    RESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileysFindByShortcut(self, shortcut, *arg, **kw):
		"""
		PurpleSmileysFindByShortcut method:

		Parameters
		----------
		    shortcut: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileysFindByChecksum(self, checksum, *arg, **kw):
		"""
		PurpleSmileysFindByChecksum method:

		Parameters
		----------
		    checksum: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSmileysGetStoringDir(self, *arg, **kw):
		"""
		PurpleSmileysGetStoringDir method:

		Parameters
		----------
		    RESULT: s, out
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
	def PurplePrimitiveGetIdFromType(self, type, *arg, **kw):
		"""
		PurplePrimitiveGetIdFromType method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePrimitiveGetNameFromType(self, type, *arg, **kw):
		"""
		PurplePrimitiveGetNameFromType method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePrimitiveGetTypeFromId(self, id, *arg, **kw):
		"""
		PurplePrimitiveGetTypeFromId method:

		Parameters
		----------
		    id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeNewFull(self, primitive, id, name, saveable, user_settable, independent, *arg, **kw):
		"""
		PurpleStatusTypeNewFull method:

		Parameters
		----------
		    primitive: i, inid: s, inname: s, insaveable: i, inuser_settable: i, inindependent: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeNew(self, primitive, id, name, user_settable, *arg, **kw):
		"""
		PurpleStatusTypeNew method:

		Parameters
		----------
		    primitive: i, inid: s, inname: s, inuser_settable: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeDestroy(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeDestroy method:

		Parameters
		----------
		    status_type: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeSetPrimaryAttr(self, status_type, attr_id, *arg, **kw):
		"""
		PurpleStatusTypeSetPrimaryAttr method:

		Parameters
		----------
		    status_type: i, inattr_id: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeAddAttr(self, status_type, id, name, value, *arg, **kw):
		"""
		PurpleStatusTypeAddAttr method:

		Parameters
		----------
		    status_type: i, inid: s, inname: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetPrimitive(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetPrimitive method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetId(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetId method:

		Parameters
		----------
		    status_type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetName(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetName method:

		Parameters
		----------
		    status_type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeIsSaveable(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsSaveable method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeIsUserSettable(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsUserSettable method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeIsIndependent(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsIndependent method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeIsExclusive(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsExclusive method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeIsAvailable(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeIsAvailable method:

		Parameters
		----------
		    status_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetPrimaryAttr(self, type, *arg, **kw):
		"""
		PurpleStatusTypeGetPrimaryAttr method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetAttr(self, status_type, id, *arg, **kw):
		"""
		PurpleStatusTypeGetAttr method:

		Parameters
		----------
		    status_type: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeGetAttrs(self, status_type, *arg, **kw):
		"""
		PurpleStatusTypeGetAttrs method:

		Parameters
		----------
		    status_type: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusTypeFindWithId(self, status_types, id, *arg, **kw):
		"""
		PurpleStatusTypeFindWithId method:

		Parameters
		----------
		    status_types: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusAttrNew(self, id, name, value_type, *arg, **kw):
		"""
		PurpleStatusAttrNew method:

		Parameters
		----------
		    id: s, inname: s, invalue_type: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusAttrDestroy(self, attr, *arg, **kw):
		"""
		PurpleStatusAttrDestroy method:

		Parameters
		----------
		    attr: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusAttrGetId(self, attr, *arg, **kw):
		"""
		PurpleStatusAttrGetId method:

		Parameters
		----------
		    attr: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusAttrGetName(self, attr, *arg, **kw):
		"""
		PurpleStatusAttrGetName method:

		Parameters
		----------
		    attr: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusAttrGetValue(self, attr, *arg, **kw):
		"""
		PurpleStatusAttrGetValue method:

		Parameters
		----------
		    attr: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusNew(self, status_type, presence, *arg, **kw):
		"""
		PurpleStatusNew method:

		Parameters
		----------
		    status_type: i, inpresence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusDestroy(self, status, *arg, **kw):
		"""
		PurpleStatusDestroy method:

		Parameters
		----------
		    status: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusSetActive(self, status, active, *arg, **kw):
		"""
		PurpleStatusSetActive method:

		Parameters
		----------
		    status: i, inactive: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusSetActiveWithAttrsList(self, status, active, attrs, *arg, **kw):
		"""
		PurpleStatusSetActiveWithAttrsList method:

		Parameters
		----------
		    status: i, inactive: i, inattrs: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusSetAttrBoolean(self, status, id, value, *arg, **kw):
		"""
		PurpleStatusSetAttrBoolean method:

		Parameters
		----------
		    status: i, inid: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusSetAttrInt(self, status, id, value, *arg, **kw):
		"""
		PurpleStatusSetAttrInt method:

		Parameters
		----------
		    status: i, inid: s, invalue: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusSetAttrString(self, status, id, value, *arg, **kw):
		"""
		PurpleStatusSetAttrString method:

		Parameters
		----------
		    status: i, inid: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetType(self, status, *arg, **kw):
		"""
		PurpleStatusGetType method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetPresence(self, status, *arg, **kw):
		"""
		PurpleStatusGetPresence method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetId(self, status, *arg, **kw):
		"""
		PurpleStatusGetId method:

		Parameters
		----------
		    status: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetName(self, status, *arg, **kw):
		"""
		PurpleStatusGetName method:

		Parameters
		----------
		    status: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusIsIndependent(self, status, *arg, **kw):
		"""
		PurpleStatusIsIndependent method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusIsExclusive(self, status, *arg, **kw):
		"""
		PurpleStatusIsExclusive method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusIsAvailable(self, status, *arg, **kw):
		"""
		PurpleStatusIsAvailable method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusIsActive(self, status, *arg, **kw):
		"""
		PurpleStatusIsActive method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusIsOnline(self, status, *arg, **kw):
		"""
		PurpleStatusIsOnline method:

		Parameters
		----------
		    status: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetAttrValue(self, status, id, *arg, **kw):
		"""
		PurpleStatusGetAttrValue method:

		Parameters
		----------
		    status: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetAttrBoolean(self, status, id, *arg, **kw):
		"""
		PurpleStatusGetAttrBoolean method:

		Parameters
		----------
		    status: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetAttrInt(self, status, id, *arg, **kw):
		"""
		PurpleStatusGetAttrInt method:

		Parameters
		----------
		    status: i, inid: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusGetAttrString(self, status, id, *arg, **kw):
		"""
		PurpleStatusGetAttrString method:

		Parameters
		----------
		    status: i, inid: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStatusCompare(self, status1, status2, *arg, **kw):
		"""
		PurpleStatusCompare method:

		Parameters
		----------
		    status1: i, instatus2: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceNew(self, context, *arg, **kw):
		"""
		PurplePresenceNew method:

		Parameters
		----------
		    context: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceNewForAccount(self, account, *arg, **kw):
		"""
		PurplePresenceNewForAccount method:

		Parameters
		----------
		    account: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceNewForConv(self, conv, *arg, **kw):
		"""
		PurplePresenceNewForConv method:

		Parameters
		----------
		    conv: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceNewForBuddy(self, buddy, *arg, **kw):
		"""
		PurplePresenceNewForBuddy method:

		Parameters
		----------
		    buddy: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceDestroy(self, presence, *arg, **kw):
		"""
		PurplePresenceDestroy method:

		Parameters
		----------
		    presence: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceAddStatus(self, presence, status, *arg, **kw):
		"""
		PurplePresenceAddStatus method:

		Parameters
		----------
		    presence: i, instatus: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceSetStatusActive(self, presence, status_id, active, *arg, **kw):
		"""
		PurplePresenceSetStatusActive method:

		Parameters
		----------
		    presence: i, instatus_id: s, inactive: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceSwitchStatus(self, presence, status_id, *arg, **kw):
		"""
		PurplePresenceSwitchStatus method:

		Parameters
		----------
		    presence: i, instatus_id: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceSetIdle(self, presence, idle, idle_time, *arg, **kw):
		"""
		PurplePresenceSetIdle method:

		Parameters
		----------
		    presence: i, inidle: i, inidle_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceSetLoginTime(self, presence, login_time, *arg, **kw):
		"""
		PurplePresenceSetLoginTime method:

		Parameters
		----------
		    presence: i, inlogin_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetContext(self, presence, *arg, **kw):
		"""
		PurplePresenceGetContext method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetAccount(self, presence, *arg, **kw):
		"""
		PurplePresenceGetAccount method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetConversation(self, presence, *arg, **kw):
		"""
		PurplePresenceGetConversation method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetChatUser(self, presence, *arg, **kw):
		"""
		PurplePresenceGetChatUser method:

		Parameters
		----------
		    presence: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetBuddy(self, presence, *arg, **kw):
		"""
		PurplePresenceGetBuddy method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetStatuses(self, presence, *arg, **kw):
		"""
		PurplePresenceGetStatuses method:

		Parameters
		----------
		    presence: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetStatus(self, presence, status_id, *arg, **kw):
		"""
		PurplePresenceGetStatus method:

		Parameters
		----------
		    presence: i, instatus_id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetActiveStatus(self, presence, *arg, **kw):
		"""
		PurplePresenceGetActiveStatus method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceIsAvailable(self, presence, *arg, **kw):
		"""
		PurplePresenceIsAvailable method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceIsOnline(self, presence, *arg, **kw):
		"""
		PurplePresenceIsOnline method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceIsStatusActive(self, presence, status_id, *arg, **kw):
		"""
		PurplePresenceIsStatusActive method:

		Parameters
		----------
		    presence: i, instatus_id: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceIsStatusPrimitiveActive(self, presence, primitive, *arg, **kw):
		"""
		PurplePresenceIsStatusPrimitiveActive method:

		Parameters
		----------
		    presence: i, inprimitive: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceIsIdle(self, presence, *arg, **kw):
		"""
		PurplePresenceIsIdle method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetIdleTime(self, presence, *arg, **kw):
		"""
		PurplePresenceGetIdleTime method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceGetLoginTime(self, presence, *arg, **kw):
		"""
		PurplePresenceGetLoginTime method:

		Parameters
		----------
		    presence: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePresenceCompare(self, presence1, presence2, *arg, **kw):
		"""
		PurplePresenceCompare method:

		Parameters
		----------
		    presence1: i, inpresence2: i, inRESULT: i, out
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
	def ServSendTyping(self, gc, name, state, *arg, **kw):
		"""
		ServSendTyping method:

		Parameters
		----------
		    gc: i, inname: s, instate: i, inRESULT: u, out
		"""
		pass
    
	@DbusMethod
	def ServMoveBuddy(self, param0, param1, param2, *arg, **kw):
		"""
		ServMoveBuddy method:

		Parameters
		----------
		    param0: i, inparam1: i, inparam2: i, in
		"""
		pass
    
	@DbusMethod
	def ServSendIm(self, param0, param1, param2, flags, *arg, **kw):
		"""
		ServSendIm method:

		Parameters
		----------
		    param0: i, inparam1: s, inparam2: s, inflags: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleGetAttentionTypeFromCode(self, account, type_code, *arg, **kw):
		"""
		PurpleGetAttentionTypeFromCode method:

		Parameters
		----------
		    account: i, intype_code: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def ServSendAttention(self, gc, who, type_code, *arg, **kw):
		"""
		ServSendAttention method:

		Parameters
		----------
		    gc: i, inwho: s, intype_code: i, in
		"""
		pass
    
	@DbusMethod
	def ServGotAttention(self, gc, who, type_code, *arg, **kw):
		"""
		ServGotAttention method:

		Parameters
		----------
		    gc: i, inwho: s, intype_code: i, in
		"""
		pass
    
	@DbusMethod
	def ServGetInfo(self, param0, param1, *arg, **kw):
		"""
		ServGetInfo method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServSetInfo(self, param0, param1, *arg, **kw):
		"""
		ServSetInfo method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServAddPermit(self, param0, param1, *arg, **kw):
		"""
		ServAddPermit method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServAddDeny(self, param0, param1, *arg, **kw):
		"""
		ServAddDeny method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServRemPermit(self, param0, param1, *arg, **kw):
		"""
		ServRemPermit method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServRemDeny(self, param0, param1, *arg, **kw):
		"""
		ServRemDeny method:

		Parameters
		----------
		    param0: i, inparam1: s, in
		"""
		pass
    
	@DbusMethod
	def ServSetPermitDeny(self, param0, *arg, **kw):
		"""
		ServSetPermitDeny method:

		Parameters
		----------
		    param0: i, in
		"""
		pass
    
	@DbusMethod
	def ServChatInvite(self, param0, param1, param2, param3, *arg, **kw):
		"""
		ServChatInvite method:

		Parameters
		----------
		    param0: i, inparam1: i, inparam2: s, inparam3: s, in
		"""
		pass
    
	@DbusMethod
	def ServChatLeave(self, param0, param1, *arg, **kw):
		"""
		ServChatLeave method:

		Parameters
		----------
		    param0: i, inparam1: i, in
		"""
		pass
    
	@DbusMethod
	def ServChatWhisper(self, param0, param1, param2, param3, *arg, **kw):
		"""
		ServChatWhisper method:

		Parameters
		----------
		    param0: i, inparam1: i, inparam2: s, inparam3: s, in
		"""
		pass
    
	@DbusMethod
	def ServChatSend(self, param0, param1, param2, flags, *arg, **kw):
		"""
		ServChatSend method:

		Parameters
		----------
		    param0: i, inparam1: i, inparam2: s, inflags: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def ServAliasBuddy(self, param0, *arg, **kw):
		"""
		ServAliasBuddy method:

		Parameters
		----------
		    param0: i, in
		"""
		pass
    
	@DbusMethod
	def ServGotAlias(self, gc, who, alias, *arg, **kw):
		"""
		ServGotAlias method:

		Parameters
		----------
		    gc: i, inwho: s, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleServGotPrivateAlias(self, gc, who, alias, *arg, **kw):
		"""
		PurpleServGotPrivateAlias method:

		Parameters
		----------
		    gc: i, inwho: s, inalias: s, in
		"""
		pass
    
	@DbusMethod
	def ServGotTyping(self, gc, name, timeout, state, *arg, **kw):
		"""
		ServGotTyping method:

		Parameters
		----------
		    gc: i, inname: s, intimeout: i, instate: i, in
		"""
		pass
    
	@DbusMethod
	def ServGotTypingStopped(self, gc, name, *arg, **kw):
		"""
		ServGotTypingStopped method:

		Parameters
		----------
		    gc: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def ServGotIm(self, gc, who, msg, flags, mtime, *arg, **kw):
		"""
		ServGotIm method:

		Parameters
		----------
		    gc: i, inwho: s, inmsg: s, inflags: i, inmtime: i, in
		"""
		pass
    
	@DbusMethod
	def ServJoinChat(self, param0, data, *arg, **kw):
		"""
		ServJoinChat method:

		Parameters
		----------
		    param0: i, indata: a{ss}, in
		"""
		pass
    
	@DbusMethod
	def ServRejectChat(self, param0, data, *arg, **kw):
		"""
		ServRejectChat method:

		Parameters
		----------
		    param0: i, indata: a{ss}, in
		"""
		pass
    
	@DbusMethod
	def ServGotChatInvite(self, gc, name, who, message, data, *arg, **kw):
		"""
		ServGotChatInvite method:

		Parameters
		----------
		    gc: i, inname: s, inwho: s, inmessage: s, indata: a{ss}, in
		"""
		pass
    
	@DbusMethod
	def ServGotJoinedChat(self, gc, id, name, *arg, **kw):
		"""
		ServGotJoinedChat method:

		Parameters
		----------
		    gc: i, inid: i, inname: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleServGotJoinChatFailed(self, gc, data, *arg, **kw):
		"""
		PurpleServGotJoinChatFailed method:

		Parameters
		----------
		    gc: i, indata: a{ss}, in
		"""
		pass
    
	@DbusMethod
	def ServGotChatLeft(self, g, id, *arg, **kw):
		"""
		ServGotChatLeft method:

		Parameters
		----------
		    g: i, inid: i, in
		"""
		pass
    
	@DbusMethod
	def ServGotChatIn(self, g, id, who, flags, message, mtime, *arg, **kw):
		"""
		ServGotChatIn method:

		Parameters
		----------
		    g: i, inid: i, inwho: s, inflags: i, inmessage: s, inmtime: i, in
		"""
		pass
    
	@DbusMethod
	def ServSendFile(self, gc, who, file, *arg, **kw):
		"""
		ServSendFile method:

		Parameters
		----------
		    gc: i, inwho: s, infile: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleMenuActionFree(self, act, *arg, **kw):
		"""
		PurpleMenuActionFree method:

		Parameters
		----------
		    act: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleUtilSetCurrentSong(self, title, artist, album, *arg, **kw):
		"""
		PurpleUtilSetCurrentSong method:

		Parameters
		----------
		    title: s, inartist: s, inalbum: s, in
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
	def PurpleMimeDecodeField(self, str, *arg, **kw):
		"""
		PurpleMimeDecodeField method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleTimeBuild(self, year, month, day, hour, min, sec, *arg, **kw):
		"""
		PurpleTimeBuild method:

		Parameters
		----------
		    year: i, inmonth: i, inday: i, inhour: i, inmin: i, insec: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupEscapeText(self, text, length, *arg, **kw):
		"""
		PurpleMarkupEscapeText method:

		Parameters
		----------
		    text: s, inlength: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupStripHtml(self, str, *arg, **kw):
		"""
		PurpleMarkupStripHtml method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupLinkify(self, str, *arg, **kw):
		"""
		PurpleMarkupLinkify method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUnescapeText(self, text, *arg, **kw):
		"""
		PurpleUnescapeText method:

		Parameters
		----------
		    text: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUnescapeHtml(self, html, *arg, **kw):
		"""
		PurpleUnescapeHtml method:

		Parameters
		----------
		    html: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupSlice(self, str, x, y, *arg, **kw):
		"""
		PurpleMarkupSlice method:

		Parameters
		----------
		    str: s, inx: i, iny: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupGetTagName(self, tag, *arg, **kw):
		"""
		PurpleMarkupGetTagName method:

		Parameters
		----------
		    tag: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupUnescapeEntity(self, text, length, *arg, **kw):
		"""
		PurpleMarkupUnescapeEntity method:

		Parameters
		----------
		    text: s, inlength: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupGetCssProperty(self, style, opt, *arg, **kw):
		"""
		PurpleMarkupGetCssProperty method:

		Parameters
		----------
		    style: s, inopt: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleMarkupIsRtl(self, html, *arg, **kw):
		"""
		PurpleMarkupIsRtl method:

		Parameters
		----------
		    html: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleHomeDir(self, *arg, **kw):
		"""
		PurpleHomeDir method:

		Parameters
		----------
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUserDir(self, *arg, **kw):
		"""
		PurpleUserDir method:

		Parameters
		----------
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtilSetUserDir(self, dir, *arg, **kw):
		"""
		PurpleUtilSetUserDir method:

		Parameters
		----------
		    dir: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleBuildDir(self, path, mode, *arg, **kw):
		"""
		PurpleBuildDir method:

		Parameters
		----------
		    path: s, inmode: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtilWriteDataToFile(self, filename, data, size, *arg, **kw):
		"""
		PurpleUtilWriteDataToFile method:

		Parameters
		----------
		    filename: s, indata: s, insize: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtilWriteDataToFileAbsolute(self, filename_full, data, size, *arg, **kw):
		"""
		PurpleUtilWriteDataToFileAbsolute method:

		Parameters
		----------
		    filename_full: s, indata: s, insize: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleProgramIsValid(self, program, *arg, **kw):
		"""
		PurpleProgramIsValid method:

		Parameters
		----------
		    program: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRunningGnome(self, *arg, **kw):
		"""
		PurpleRunningGnome method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRunningKde(self, *arg, **kw):
		"""
		PurpleRunningKde method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleRunningOsx(self, *arg, **kw):
		"""
		PurpleRunningOsx method:

		Parameters
		----------
		    RESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleFdGetIp(self, fd, *arg, **kw):
		"""
		PurpleFdGetIp method:

		Parameters
		----------
		    fd: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleSocketGetFamily(self, fd, *arg, **kw):
		"""
		PurpleSocketGetFamily method:

		Parameters
		----------
		    fd: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleSocketSpeaksIpv4(self, fd, *arg, **kw):
		"""
		PurpleSocketSpeaksIpv4 method:

		Parameters
		----------
		    fd: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrequal(self, left, right, *arg, **kw):
		"""
		PurpleStrequal method:

		Parameters
		----------
		    left: s, inright: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleNormalize(self, account, str, *arg, **kw):
		"""
		PurpleNormalize method:

		Parameters
		----------
		    account: i, instr: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleNormalizeNocase(self, account, str, *arg, **kw):
		"""
		PurpleNormalizeNocase method:

		Parameters
		----------
		    account: i, instr: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrHasPrefix(self, s, p, *arg, **kw):
		"""
		PurpleStrHasPrefix method:

		Parameters
		----------
		    s: s, inp: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrHasSuffix(self, s, x, *arg, **kw):
		"""
		PurpleStrHasSuffix method:

		Parameters
		----------
		    s: s, inx: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrdupWithhtml(self, src, *arg, **kw):
		"""
		PurpleStrdupWithhtml method:

		Parameters
		----------
		    src: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrAddCr(self, str, *arg, **kw):
		"""
		PurpleStrAddCr method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrreplace(self, string, delimiter, replacement, *arg, **kw):
		"""
		PurpleStrreplace method:

		Parameters
		----------
		    string: s, indelimiter: s, inreplacement: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8NcrEncode(self, in, *arg, **kw):
		"""
		PurpleUtf8NcrEncode method:

		Parameters
		----------
		    in: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8NcrDecode(self, in, *arg, **kw):
		"""
		PurpleUtf8NcrDecode method:

		Parameters
		----------
		    in: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrcasereplace(self, string, delimiter, replacement, *arg, **kw):
		"""
		PurpleStrcasereplace method:

		Parameters
		----------
		    string: s, indelimiter: s, inreplacement: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrcasestr(self, haystack, needle, *arg, **kw):
		"""
		PurpleStrcasestr method:

		Parameters
		----------
		    haystack: s, inneedle: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrSizeToUnits(self, size, *arg, **kw):
		"""
		PurpleStrSizeToUnits method:

		Parameters
		----------
		    size: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrSecondsToString(self, sec, *arg, **kw):
		"""
		PurpleStrSecondsToString method:

		Parameters
		----------
		    sec: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleStrBinaryToAscii(self, binary, len, *arg, **kw):
		"""
		PurpleStrBinaryToAscii method:

		Parameters
		----------
		    binary: s, inlen: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleGotProtocolHandlerUri(self, uri, *arg, **kw):
		"""
		PurpleGotProtocolHandlerUri method:

		Parameters
		----------
		    uri: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleUtilFetchUrlCancel(self, url_data, *arg, **kw):
		"""
		PurpleUtilFetchUrlCancel method:

		Parameters
		----------
		    url_data: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleUrlDecode(self, str, *arg, **kw):
		"""
		PurpleUrlDecode method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUrlEncode(self, str, *arg, **kw):
		"""
		PurpleUrlEncode method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleEmailIsValid(self, address, *arg, **kw):
		"""
		PurpleEmailIsValid method:

		Parameters
		----------
		    address: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleIpAddressIsValid(self, ip, *arg, **kw):
		"""
		PurpleIpAddressIsValid method:

		Parameters
		----------
		    ip: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleIpv4AddressIsValid(self, ip, *arg, **kw):
		"""
		PurpleIpv4AddressIsValid method:

		Parameters
		----------
		    ip: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleIpv6AddressIsValid(self, ip, *arg, **kw):
		"""
		PurpleIpv6AddressIsValid method:

		Parameters
		----------
		    ip: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleUriListExtractUris(self, uri_list, *arg, **kw):
		"""
		PurpleUriListExtractUris method:

		Parameters
		----------
		    uri_list: s, inRESULT: as, out
		"""
		pass
    
	@DbusMethod
	def PurpleUriListExtractFilenames(self, uri_list, *arg, **kw):
		"""
		PurpleUriListExtractFilenames method:

		Parameters
		----------
		    uri_list: s, inRESULT: as, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8TryConvert(self, str, *arg, **kw):
		"""
		PurpleUtf8TryConvert method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8Salvage(self, str, *arg, **kw):
		"""
		PurpleUtf8Salvage method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8StripUnprintables(self, str, *arg, **kw):
		"""
		PurpleUtf8StripUnprintables method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8Strcasecmp(self, a, b, *arg, **kw):
		"""
		PurpleUtf8Strcasecmp method:

		Parameters
		----------
		    a: s, inb: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleUtf8HasWord(self, haystack, needle, *arg, **kw):
		"""
		PurpleUtf8HasWord method:

		Parameters
		----------
		    haystack: s, inneedle: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleTextStripMnemonic(self, in, *arg, **kw):
		"""
		PurpleTextStripMnemonic method:

		Parameters
		----------
		    in: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUnescapeFilename(self, str, *arg, **kw):
		"""
		PurpleUnescapeFilename method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleEscapeFilename(self, str, *arg, **kw):
		"""
		PurpleEscapeFilename method:

		Parameters
		----------
		    str: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleOscarConvert(self, act, protocol, *arg, **kw):
		"""
		PurpleOscarConvert method:

		Parameters
		----------
		    act: s, inprotocol: s, inRESULT: s, out
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
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleUuidRandom(self, *arg, **kw):
		"""
		PurpleUuidRandom method:

		Parameters
		----------
		    RESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeInsertChild(self, parent, child, *arg, **kw):
		"""
		XmlnodeInsertChild method:

		Parameters
		----------
		    parent: i, inchild: i, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeInsertData(self, node, data, size, *arg, **kw):
		"""
		XmlnodeInsertData method:

		Parameters
		----------
		    node: i, indata: s, insize: i, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetData(self, node, *arg, **kw):
		"""
		XmlnodeGetData method:

		Parameters
		----------
		    node: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetDataUnescaped(self, node, *arg, **kw):
		"""
		XmlnodeGetDataUnescaped method:

		Parameters
		----------
		    node: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetAttrib(self, node, attr, value, *arg, **kw):
		"""
		XmlnodeSetAttrib method:

		Parameters
		----------
		    node: i, inattr: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetAttribWithPrefix(self, node, attr, prefix, value, *arg, **kw):
		"""
		XmlnodeSetAttribWithPrefix method:

		Parameters
		----------
		    node: i, inattr: s, inprefix: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetAttribWithNamespace(self, node, attr, xmlns, value, *arg, **kw):
		"""
		XmlnodeSetAttribWithNamespace method:

		Parameters
		----------
		    node: i, inattr: s, inxmlns: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetAttribFull(self, node, attr, xmlns, prefix, value, *arg, **kw):
		"""
		XmlnodeSetAttribFull method:

		Parameters
		----------
		    node: i, inattr: s, inxmlns: s, inprefix: s, invalue: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetAttrib(self, node, attr, *arg, **kw):
		"""
		XmlnodeGetAttrib method:

		Parameters
		----------
		    node: i, inattr: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetAttribWithNamespace(self, node, attr, xmlns, *arg, **kw):
		"""
		XmlnodeGetAttribWithNamespace method:

		Parameters
		----------
		    node: i, inattr: s, inxmlns: s, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeRemoveAttrib(self, node, attr, *arg, **kw):
		"""
		XmlnodeRemoveAttrib method:

		Parameters
		----------
		    node: i, inattr: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeRemoveAttribWithNamespace(self, node, attr, xmlns, *arg, **kw):
		"""
		XmlnodeRemoveAttribWithNamespace method:

		Parameters
		----------
		    node: i, inattr: s, inxmlns: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetNamespace(self, node, xmlns, *arg, **kw):
		"""
		XmlnodeSetNamespace method:

		Parameters
		----------
		    node: i, inxmlns: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetNamespace(self, node, *arg, **kw):
		"""
		XmlnodeGetNamespace method:

		Parameters
		----------
		    node: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeSetPrefix(self, node, prefix, *arg, **kw):
		"""
		XmlnodeSetPrefix method:

		Parameters
		----------
		    node: i, inprefix: s, in
		"""
		pass
    
	@DbusMethod
	def XmlnodeGetPrefix(self, node, *arg, **kw):
		"""
		XmlnodeGetPrefix method:

		Parameters
		----------
		    node: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeToStr(self, node, len, *arg, **kw):
		"""
		XmlnodeToStr method:

		Parameters
		----------
		    node: i, inlen: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeToFormattedStr(self, node, len, *arg, **kw):
		"""
		XmlnodeToFormattedStr method:

		Parameters
		----------
		    node: i, inlen: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def XmlnodeFree(self, node, *arg, **kw):
		"""
		XmlnodeFree method:

		Parameters
		----------
		    node: i, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeNew(self, ulname, name, inc_desc, out_desc, *arg, **kw):
		"""
		PurpleAttentionTypeNew method:

		Parameters
		----------
		    ulname: s, inname: s, ininc_desc: s, inout_desc: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeSetName(self, type, name, *arg, **kw):
		"""
		PurpleAttentionTypeSetName method:

		Parameters
		----------
		    type: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeSetIncomingDesc(self, type, desc, *arg, **kw):
		"""
		PurpleAttentionTypeSetIncomingDesc method:

		Parameters
		----------
		    type: i, indesc: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeSetOutgoingDesc(self, type, desc, *arg, **kw):
		"""
		PurpleAttentionTypeSetOutgoingDesc method:

		Parameters
		----------
		    type: i, indesc: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeSetIconName(self, type, name, *arg, **kw):
		"""
		PurpleAttentionTypeSetIconName method:

		Parameters
		----------
		    type: i, inname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeSetUnlocalizedName(self, type, ulname, *arg, **kw):
		"""
		PurpleAttentionTypeSetUnlocalizedName method:

		Parameters
		----------
		    type: i, inulname: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeGetName(self, type, *arg, **kw):
		"""
		PurpleAttentionTypeGetName method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeGetIncomingDesc(self, type, *arg, **kw):
		"""
		PurpleAttentionTypeGetIncomingDesc method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeGetOutgoingDesc(self, type, *arg, **kw):
		"""
		PurpleAttentionTypeGetOutgoingDesc method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeGetIconName(self, type, *arg, **kw):
		"""
		PurpleAttentionTypeGetIconName method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurpleAttentionTypeGetUnlocalizedName(self, type, *arg, **kw):
		"""
		PurpleAttentionTypeGetUnlocalizedName method:

		Parameters
		----------
		    type: i, inRESULT: s, out
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotAccountIdle(self, account, idle, idle_time, *arg, **kw):
		"""
		PurplePrplGotAccountIdle method:

		Parameters
		----------
		    account: i, inidle: i, inidle_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotAccountLoginTime(self, account, login_time, *arg, **kw):
		"""
		PurplePrplGotAccountLoginTime method:

		Parameters
		----------
		    account: i, inlogin_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotAccountActions(self, account, *arg, **kw):
		"""
		PurplePrplGotAccountActions method:

		Parameters
		----------
		    account: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotUserIdle(self, account, name, idle, idle_time, *arg, **kw):
		"""
		PurplePrplGotUserIdle method:

		Parameters
		----------
		    account: i, inname: s, inidle: i, inidle_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotUserLoginTime(self, account, name, login_time, *arg, **kw):
		"""
		PurplePrplGotUserLoginTime method:

		Parameters
		----------
		    account: i, inname: s, inlogin_time: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotUserStatusDeactive(self, account, name, status_id, *arg, **kw):
		"""
		PurplePrplGotUserStatusDeactive method:

		Parameters
		----------
		    account: i, inname: s, instatus_id: s, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplChangeAccountStatus(self, account, old_status, new_status, *arg, **kw):
		"""
		PurplePrplChangeAccountStatus method:

		Parameters
		----------
		    account: i, inold_status: i, innew_status: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGetStatuses(self, account, presence, *arg, **kw):
		"""
		PurplePrplGetStatuses method:

		Parameters
		----------
		    account: i, inpresence: i, inRESULT: ai, out
		"""
		pass
    
	@DbusMethod
	def PurplePrplSendAttention(self, gc, who, type_code, *arg, **kw):
		"""
		PurplePrplSendAttention method:

		Parameters
		----------
		    gc: i, inwho: s, intype_code: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotAttention(self, gc, who, type_code, *arg, **kw):
		"""
		PurplePrplGotAttention method:

		Parameters
		----------
		    gc: i, inwho: s, intype_code: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotAttentionInChat(self, gc, id, who, type_code, *arg, **kw):
		"""
		PurplePrplGotAttentionInChat method:

		Parameters
		----------
		    gc: i, inid: i, inwho: s, intype_code: i, in
		"""
		pass
    
	@DbusMethod
	def PurplePrplGetMediaCaps(self, account, who, *arg, **kw):
		"""
		PurplePrplGetMediaCaps method:

		Parameters
		----------
		    account: i, inwho: s, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrplInitiateMedia(self, account, who, type, *arg, **kw):
		"""
		PurplePrplInitiateMedia method:

		Parameters
		----------
		    account: i, inwho: s, intype: i, inRESULT: i, out
		"""
		pass
    
	@DbusMethod
	def PurplePrplGotMediaCaps(self, account, who, *arg, **kw):
		"""
		PurplePrplGotMediaCaps method:

		Parameters
		----------
		    account: i, inwho: s, in
		"""
		pass
    
	@DbusMethod
	def PurpleFindPrpl(self, id, *arg, **kw):
		"""
		PurpleFindPrpl method:

		Parameters
		----------
		    id: s, inRESULT: i, out
		"""
		pass
    
	@DbusSignal
	def AccountConnecting(self, *arg, **kw):
		"""
		AccountConnecting signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountDisabled(self, *arg, **kw):
		"""
		AccountDisabled signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountEnabled(self, *arg, **kw):
		"""
		AccountEnabled signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountSettingInfo(self, *arg, **kw):
		"""
		AccountSettingInfo signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountSetInfo(self, *arg, **kw):
		"""
		AccountSetInfo signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountCreated(self, *arg, **kw):
		"""
		AccountCreated signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountDestroying(self, *arg, **kw):
		"""
		AccountDestroying signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAdded(self, *arg, **kw):
		"""
		AccountAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountRemoved(self, *arg, **kw):
		"""
		AccountRemoved signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountStatusChanged(self, *arg, **kw):
		"""
		AccountStatusChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def AccountActionsChanged(self, *arg, **kw):
		"""
		AccountActionsChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAliasChanged(self, *arg, **kw):
		"""
		AccountAliasChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAuthorizationRequested(self, *arg, **kw):
		"""
		AccountAuthorizationRequested signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAuthorizationRequestedWithMessage(self, *arg, **kw):
		"""
		AccountAuthorizationRequestedWithMessage signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAuthorizationDenied(self, *arg, **kw):
		"""
		AccountAuthorizationDenied signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountAuthorizationGranted(self, *arg, **kw):
		"""
		AccountAuthorizationGranted signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def AccountErrorChanged(self, *arg, **kw):
		"""
		AccountErrorChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def AccountSignedOn(self, *arg, **kw):
		"""
		AccountSignedOn signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountSignedOff(self, *arg, **kw):
		"""
		AccountSignedOff signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def AccountConnectionError(self, *arg, **kw):
		"""
		AccountConnectionError signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyStatusChanged(self, *arg, **kw):
		"""
		BuddyStatusChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyPrivacyChanged(self, *arg, **kw):
		"""
		BuddyPrivacyChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyIdleChanged(self, *arg, **kw):
		"""
		BuddyIdleChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def BuddySignedOn(self, *arg, **kw):
		"""
		BuddySignedOn signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddySignedOff(self, *arg, **kw):
		"""
		BuddySignedOff signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyGotLoginTime(self, *arg, **kw):
		"""
		BuddyGotLoginTime signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BlistNodeAdded(self, *arg, **kw):
		"""
		BlistNodeAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BlistNodeRemoved(self, *arg, **kw):
		"""
		BlistNodeRemoved signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyAdded(self, *arg, **kw):
		"""
		BuddyAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyRemoved(self, *arg, **kw):
		"""
		BuddyRemoved signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyIconChanged(self, *arg, **kw):
		"""
		BuddyIconChanged signal:

		Parameters
		----------
		    
		arg1: i, in
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
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def BlistNodeAliased(self, *arg, **kw):
		"""
		BlistNodeAliased signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyCapsChanged(self, *arg, **kw):
		"""
		BuddyCapsChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def CertificateStored(self, *arg, **kw):
		"""
		CertificateStored signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def CertificateDeleted(self, *arg, **kw):
		"""
		CertificateDeleted signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def CipherAdded(self, *arg, **kw):
		"""
		CipherAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def CipherRemoved(self, *arg, **kw):
		"""
		CipherRemoved signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def CmdAdded(self, *arg, **kw):
		"""
		CmdAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def CmdRemoved(self, *arg, **kw):
		"""
		CmdRemoved signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SigningOn(self, *arg, **kw):
		"""
		SigningOn signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SignedOn(self, *arg, **kw):
		"""
		SignedOn signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SigningOff(self, *arg, **kw):
		"""
		SigningOff signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SignedOff(self, *arg, **kw):
		"""
		SignedOff signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ConnectionError(self, *arg, **kw):
		"""
		ConnectionError signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def Autojoin(self, *arg, **kw):
		"""
		Autojoin signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def WritingImMsg(self, *arg, **kw):
		"""
		WritingImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def WroteImMsg(self, *arg, **kw):
		"""
		WroteImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def SentAttention(self, *arg, **kw):
		"""
		SentAttention signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: u, in
		"""
		pass
    
	@DbusSignal
	def GotAttention(self, *arg, **kw):
		"""
		GotAttention signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: u, in
		"""
		pass
    
	@DbusSignal
	def SendingImMsg(self, *arg, **kw):
		"""
		SendingImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def SentImMsg(self, *arg, **kw):
		"""
		SentImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def ReceivingImMsg(self, *arg, **kw):
		"""
		ReceivingImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: i, in
		"""
		pass
    
	@DbusSignal
	def ReceivedImMsg(self, *arg, **kw):
		"""
		ReceivedImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def BlockedImMsg(self, *arg, **kw):
		"""
		BlockedImMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: u, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def WritingChatMsg(self, *arg, **kw):
		"""
		WritingChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def WroteChatMsg(self, *arg, **kw):
		"""
		WroteChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def SendingChatMsg(self, *arg, **kw):
		"""
		SendingChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: u, in
		"""
		pass
    
	@DbusSignal
	def SentChatMsg(self, *arg, **kw):
		"""
		SentChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: u, in
		"""
		pass
    
	@DbusSignal
	def ReceivingChatMsg(self, *arg, **kw):
		"""
		ReceivingChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: i, in
		"""
		pass
    
	@DbusSignal
	def ReceivedChatMsg(self, *arg, **kw):
		"""
		ReceivedChatMsg signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def ConversationCreated(self, *arg, **kw):
		"""
		ConversationCreated signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ConversationUpdated(self, *arg, **kw):
		"""
		ConversationUpdated signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: u, in
		"""
		pass
    
	@DbusSignal
	def DeletingConversation(self, *arg, **kw):
		"""
		DeletingConversation signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyTyping(self, *arg, **kw):
		"""
		BuddyTyping signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyTyped(self, *arg, **kw):
		"""
		BuddyTyped signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def BuddyTypingStopped(self, *arg, **kw):
		"""
		BuddyTypingStopped signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def ChatBuddyJoining(self, *arg, **kw):
		"""
		ChatBuddyJoining signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: u, in
		"""
		pass
    
	@DbusSignal
	def ChatBuddyJoined(self, *arg, **kw):
		"""
		ChatBuddyJoined signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: u, in
		arg4: u, in
		"""
		pass
    
	@DbusSignal
	def ChatBuddyFlags(self, *arg, **kw):
		"""
		ChatBuddyFlags signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: u, in
		arg4: u, in
		"""
		pass
    
	@DbusSignal
	def ChatBuddyLeaving(self, *arg, **kw):
		"""
		ChatBuddyLeaving signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def ChatBuddyLeft(self, *arg, **kw):
		"""
		ChatBuddyLeft signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def DeletingChatBuddy(self, *arg, **kw):
		"""
		DeletingChatBuddy signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ChatInvitingUser(self, *arg, **kw):
		"""
		ChatInvitingUser signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def ChatInvitedUser(self, *arg, **kw):
		"""
		ChatInvitedUser signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def ChatInvited(self, *arg, **kw):
		"""
		ChatInvited signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: i, in
		"""
		pass
    
	@DbusSignal
	def ChatInviteBlocked(self, *arg, **kw):
		"""
		ChatInviteBlocked signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: i, in
		"""
		pass
    
	@DbusSignal
	def ChatJoined(self, *arg, **kw):
		"""
		ChatJoined signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ChatJoinFailed(self, *arg, **kw):
		"""
		ChatJoinFailed signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def ChatLeft(self, *arg, **kw):
		"""
		ChatLeft signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ChatTopicChanged(self, *arg, **kw):
		"""
		ChatTopicChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def ClearedMessageHistory(self, *arg, **kw):
		"""
		ClearedMessageHistory signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ConversationExtendedMenu(self, *arg, **kw):
		"""
		ConversationExtendedMenu signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def UriHandler(self, *arg, **kw):
		"""
		UriHandler signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
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
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileSendAccept(self, *arg, **kw):
		"""
		FileSendAccept signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileRecvStart(self, *arg, **kw):
		"""
		FileRecvStart signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileSendStart(self, *arg, **kw):
		"""
		FileSendStart signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileSendCancel(self, *arg, **kw):
		"""
		FileSendCancel signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileRecvCancel(self, *arg, **kw):
		"""
		FileRecvCancel signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileSendComplete(self, *arg, **kw):
		"""
		FileSendComplete signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileRecvComplete(self, *arg, **kw):
		"""
		FileRecvComplete signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def FileRecvRequest(self, *arg, **kw):
		"""
		FileRecvRequest signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def ImageDeleting(self, *arg, **kw):
		"""
		ImageDeleting signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def LogTimestamp(self, *arg, **kw):
		"""
		LogTimestamp signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: x, in
		arg3: b, in
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
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		"""
		pass
    
	@DbusSignal
	def DisplayingEmailsNotification(self, *arg, **kw):
		"""
		DisplayingEmailsNotification signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		arg4: i, in
		arg5: u, in
		"""
		pass
    
	@DbusSignal
	def DisplayingUserinfo(self, *arg, **kw):
		"""
		DisplayingUserinfo signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		arg3: i, in
		"""
		pass
    
	@DbusSignal
	def PluginLoad(self, *arg, **kw):
		"""
		PluginLoad signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def PluginUnload(self, *arg, **kw):
		"""
		PluginUnload signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SavedstatusChanged(self, *arg, **kw):
		"""
		SavedstatusChanged signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def SavedstatusAdded(self, *arg, **kw):
		"""
		SavedstatusAdded signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SavedstatusDeleted(self, *arg, **kw):
		"""
		SavedstatusDeleted signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def SavedstatusModified(self, *arg, **kw):
		"""
		SavedstatusModified signal:

		Parameters
		----------
		    
		arg1: i, in
		"""
		pass
    
	@DbusSignal
	def PlayingSoundEvent(self, *arg, **kw):
		"""
		PlayingSoundEvent signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def IrcSendingText(self, *arg, **kw):
		"""
		IrcSendingText signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
    
	@DbusSignal
	def IrcReceivingText(self, *arg, **kw):
		"""
		IrcReceivingText signal:

		Parameters
		----------
		    
		arg1: i, in
		arg2: i, in
		"""
		pass
  
