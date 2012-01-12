<?xml version="1.0" encoding="UTF-8" ?>
<!--
    pydbusdecorator
    Use this xslt to convert dbus into pydbusdecorator code
    
    Generated code require pydbusdecorator to work
-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"  
	xmlns:dta='https://github.com/hugosenari'
    xsl:exclude-result-prefixes='dbustoany'>
<xsl:output encoding="UTF-8" indent="yes" method="text" />
	
	<xsl:param name='interface'></xsl:param>
	<xsl:param name='object_path'></xsl:param>
	<xsl:param name='bus_name'></xsl:param>
	
    <xsl:template match="/">
from pydbusdecorator import DbusInterface
        <xsl:for-each select="//interface">
class <xsl:value-of select="dta:replace(string(@name), '^.+\.([^\.]+)$', '\1')"/>(object):
	@DbusInterface("<xsl:value-of select="@name"/>", "<xsl:value-of select="$object_path"/>", "<xsl:value-of select="$bus_name"/>")
	def __init__(self, *arg, **kw):
		pass<xsl:apply-templates/>
        </xsl:for-each>
    </xsl:template>
    
    <xsl:template match="method">
	@DbusMethod
	def <xsl:value-of select="@name"/>(self<xsl:apply-templates select="arg"/>, *arg, **kw):
		"""
		<xsl:call-template name="doc"/>
		"""
		pass</xsl:template>
    
    <xsl:template match="signal">
	@DbusSignal
	def <xsl:value-of select="@name"/>(self<xsl:apply-templates select="arg"/>, *arg, **kw):
		"""
		<xsl:call-template name="doc"/>
		"""
		pass</xsl:template>
    
    <xsl:template match="property">
	@DbusAttr
	def <xsl:value-of select="@name"/>(self, *arg, **kw):
		"""
		<xsl:call-template name="doc"/>
		"""
		pass</xsl:template>
    
    <xsl:template match="arg">
	<xsl:if test="(@direction = 'in' and name(..) = 'method')
	    or (@direction = 'out' and name(..) = 'signal') or not(@direction)">
	    <xsl:choose>
		<xsl:when test="@name">, <xsl:value-of select="@name"/></xsl:when>
		<xsl:otherwise>, arg<xsl:value-of select="position()"/></xsl:otherwise>
	    </xsl:choose>
	</xsl:if></xsl:template>
    
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
		    </xsl:if>
		    <xsl:choose>
			<xsl:when test="@name">
		<xsl:value-of select="@name"/>: </xsl:when>
			<xsl:otherwise>
		arg<xsl:value-of select="position()"/>: </xsl:otherwise>
		    </xsl:choose>
		    <xsl:value-of select="@type"/>, <xsl:value-of select="@direction"/>
		</xsl:for-each>
		</xsl:when>
		<xsl:when test="name(.) = 'property'"> property: <xsl:value-of select="@type"/>, <xsl:value-of select="@access"/>
		</xsl:when>
	    </xsl:choose>
    </xsl:template>
</xsl:stylesheet>