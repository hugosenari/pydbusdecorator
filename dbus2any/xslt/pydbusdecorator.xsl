<?xml version="1.0" encoding="UTF-8" ?>
<!--
pydbusdecorator
Use this xslt to convert dbus into pydbusdecorator code

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
Created with dbus2any pydbusdecorator.xsl

https://github.com/hugosenari/pydbusdecorator/tree/master/dbus2any


This code require pydbusdecorator, see documentation for usage
https://github.com/hugosenari/pydbusdecorator

Parameters:

* <xsl:value-of select="$object_path"/>
* <xsl:value-of select="$bus_name"/>
* <xsl:value-of select="$interface"/>

'''
from pydbusdecorator import DbusInterface, DbusMethod, DbusSignal, DbusAttr
<xsl:for-each select="//interface">
class <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>(object):
    '''
    <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>
    
    Usage:
    ------
    
    >> my<xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/> = <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>()
    since this you can access any method, attribute or signal defined here.
    
    if this class (and dbus object) define
    >>> @DbusMethod
    >>> def foo (self, x): pass
    
    you can call
    >>> my<xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>.foo(x)
    and the program will be called by dbus
    
    if  something like
    >>> @DbusAttr
    >>> def bar(self): pass
    
    you can get or set (see __doc__ of attr to know if is read-only)
    >>> bar = my<xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>.bar
    >>> my<xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>.bar = bar
    
    and where is a
    >>> @DbusSignal
    >>> def spam(self, eggs): pass
    
    is possible do set handler of signal like
    >> my<xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>.spam = lambda eggs: do_something(eggs)
    every time that <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>
    dispatch one spam signal your lambda (or another function) will be called
    '''
    @DbusInterface("<xsl:value-of select="@name"/>", "<xsl:value-of select="$object_path"/>", "<xsl:value-of select="$bus_name"/>")
    def __init__(self, *arg, **kw):
        '''Constructor'''
        pass
    <xsl:apply-templates/>
</xsl:for-each>
</xsl:template>
<xsl:template match="method">@DbusMethod
    def <xsl:value-of select="@name"/>(self<xsl:apply-templates select="arg"/>, *arg, **kw):
        """
        <xsl:call-template name="doc"/>
        """
        pass
</xsl:template>

<xsl:template match="signal">@DbusSignal
    def <xsl:value-of select="@name"/>(self<xsl:apply-templates select="arg"/>, *arg, **kw):
        """

        <xsl:call-template name="doc"/>
        """
        pass
</xsl:template>

<xsl:template match="property">@DbusAttr
    def <xsl:value-of select="@name"/>(self, *arg, **kw):
        """
        <xsl:call-template name="doc"/>
        """
        pass
</xsl:template>

<xsl:template match="arg">
    <xsl:if test="(@direction = 'in' and name(..) = 'method')
        or (@direction = 'out' and name(..) = 'signal') or not(@direction)">
        <xsl:choose>
            <xsl:when test="@name">, arg_<xsl:value-of select="@name"/></xsl:when>
            <xsl:otherwise>, arg_<xsl:value-of select="position()"/></xsl:otherwise>
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
            type: <xsl:value-of select="dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(string(@type),'y', 'BYTE, '), 'b', 'BOOLEAN, '),'n', 'INT16, '),'q', 'UINT16, '),'i', 'INT32, '),'u', 'UINT32, '),'x', 'INT64, '),'t', 'UINT64, '),'d', 'DOUBLE, '),'s', 'STRING, '),'o', 'OBJECT_PATH, '),'g', 'SIGNATURE, '),'v','VARIANT, '),'e','DICT_ENTRY, '),'a', 'ARRAY:'),'r','STRUCT:'),'\(', 'STRUCT:( '),'\)', '), '),'{', 'KEY-VALUE:{ '),'}', '}, '),', }', ' }'),', \)' ,' )')"/>
            signature: <xsl:value-of select="@type"/>,
            direction: <xsl:value-of select="@direction"/>;
        </xsl:for-each>
        </xsl:when>
        <xsl:when test="name(.) = 'property'"> property:
            type: <xsl:value-of select="dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(dta:replace(string(@type),'y', 'BYTE, '), 'b', 'BOOLEAN, '),'n', 'INT16, '),'q', 'UINT16, '),'i', 'INT32, '),'u', 'UINT32, '),'x', 'INT64, '),'t', 'UINT64, '),'d', 'DOUBLE, '),'s', 'STRING, '),'o', 'OBJECT_PATH, '),'g', 'SIGNATURE, '),'v','VARIANT, '),'e','DICT_ENTRY, '),'a', 'ARRAY:'),'r','STRUCT:'),'\(', 'STRUCT:( '),'\)', '), '),'{', 'KEY-VALUE:{ '),'}', '}, '),', }', ' }'),', \)' ,' )')"/>
            signature: <xsl:value-of select="@type"/>,
            access: <xsl:value-of select="@access"/></xsl:when>
    </xsl:choose>
</xsl:template>

</xsl:stylesheet>