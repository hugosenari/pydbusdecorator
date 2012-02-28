<?xml version="1.0" encoding="UTF-8" ?>
<!--
pydbusclient
Use this xslt to convert dbus into pydbusclient code

Generated code require pydbusdecorator to work
-->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  
xmlns:dta='https://github.com/hugosenari'
xsl:exclude-result-prefixes='dbustoany'>
<xsl:output encoding="UTF-8" method="text" />
<xsl:param name='interface'></xsl:param>
<xsl:param name='object_path'></xsl:param>
<xsl:param name='bus_name'></xsl:param>
<xsl:template match="/">'''
Created with dbus2any pydbusclient.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require python dbus

Parameters:

* <xsl:value-of select="$object_path"/>
* <xsl:value-of select="$bus_name"/>
* <xsl:value-of select="$interface"/>

'''

import dbus

<xsl:for-each select="//interface">
def get_<xsl:value-of select="dta:replace(dta:lower-case(string(@name)), '^.+\.([^\.]+)$', '\1')"/>_dbus_client():
    session_bus = dbus.SessionBus()
    return session_bus.get_object('<xsl:value-of select="$bus_name"/>',
                                  '<xsl:value-of select="$object_path"/>')
    
class <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>(object):
    '''
    <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>
    
    Usage:
    ------
    
    Instantiate this class and access the instance members and methods
    '''
    def __init__(self, interface=None, object_path=None, bus_name=None, *arg, **kw):
        '''Constructor'''
        self._dbus_interface = interface or "<xsl:value-of select="@name"/>"
        self._dbus_object_path = object_path or "<xsl:value-of select="$object_path"/>"
        self._dbus_name = bus_name or "<xsl:value-of select="$bus_name"/>"
        self._dbus_object = get_<xsl:value-of select="dta:replace(dta:lower-case(string(@name)), '^.+\.([^\.]+)$', '\1')"/>_dbus_client()

    <xsl:apply-templates/>
</xsl:for-each>
</xsl:template>
<xsl:template match="method">
    def <xsl:value-of select="@name"/>(self,<xsl:apply-templates select="arg"/> *arg, **kw):
        """
        <xsl:call-template name="doc"/>
        """
        return self._dbus_object.<xsl:value-of select="@name"/>(<xsl:apply-templates select="arg"/> *arg, **kw)</xsl:template>

<xsl:template match="signal">
    @property
    def <xsl:value-of select="@name"/>(self, *arg, **kw):
        """

        <xsl:call-template name="doc"/>
        """
        return None

    @<xsl:value-of select="@name"/>.setter
    def <xsl:value-of select="@name"/>(self, callback, *arg, **kw):
        def _callback(*args, **kw): callback(self, *args, **kw)
        dbus.SessionBus().add_signal_receiver(
            _callback,
            "<xsl:value-of select="@name"/>", self._dbus_interface,
            self._dbus_name, self._dbus_object_path)

</xsl:template>

<xsl:template match="property">
    @property
    def <xsl:value-of select="@name"/>(self, *arg, **kw):
        """
        <xsl:call-template name="doc"/>
        """
        properties = dbus.Interface(self._dbus_object,
            dbus_interface=kw.get('dbus_interface',
                self._dbus_interface))
        return properties.Get(iface, "<xsl:value-of select="@name"/>")

    @<xsl:value-of select="@name"/>.setter
    def <xsl:value-of select="@name"/>(self, value, *arg, **kw):
        """
        <xsl:call-template name="doc"/>
        """
        properties = dbus.Interface(self._dbus_object,
            dbus_interface=kw.get('dbus_interface',
                self._dbus_interface))
        properties.Set(iface, "<xsl:value-of select="@name"/>", value)</xsl:template>

<xsl:template match="arg">
    <xsl:if test="(@direction = 'in' and name(..) = 'method')
        or (@direction = 'out' and name(..) = 'signal') or not(@direction)">
        <xsl:choose>
            <xsl:when test="@name"> arg_<xsl:value-of select="@name"/>,</xsl:when>
            <xsl:otherwise> arg_<xsl:value-of select="position()"/>,</xsl:otherwise>
        </xsl:choose>
    </xsl:if>
</xsl:template>

<xsl:template name="doc">
    <xsl:value-of select="@name"/>
    <xsl:choose>
        <xsl:when test="name(.) = 'method' or name(.) = 'signal'">
            <xsl:choose>
                <xsl:when test="name(.) = 'method'"> method:</xsl:when>
                <xsl:when test="name(.) = 'signal'"> signal:</xsl:when>
            </xsl:choose>
            <xsl:for-each select="arg">
                <xsl:if test="position() = 1">

        Parameters
        ----------

        </xsl:if><xsl:choose><xsl:when test="@name"><xsl:value-of select="@name"/>:</xsl:when><xsl:otherwise>arg<xsl:value-of select="position()"/>:</xsl:otherwise></xsl:choose>
            type: <xsl:value-of select="@type"/>,
            direction: <xsl:value-of select="@direction"/>;
            </xsl:for-each>
        </xsl:when>
        <xsl:when test="name(.) = 'property'"> property:
        <xsl:value-of select="@type"/>,<xsl:value-of select="@access"/></xsl:when>
    </xsl:choose>
</xsl:template>
</xsl:stylesheet>