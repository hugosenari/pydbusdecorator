<?xml version="1.0" encoding="UTF-8" ?>
<!--
    node2nodes
    Convert one node with all interfaces to one node to every interface
-->

<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output encoding="UTF-8" indent="yes" method="xml" />
    <xsl:variable name="linebreak">
<xsl:text>
</xsl:text>
    </xsl:variable>
    
	<xsl:param name="xpath">//interface</xsl:param>
	<xsl:param name="tplname">node2nodes</xsl:param>
	
    <xsl:template match="/">
    	<xsl:call-template name="$tplname">
			<xsl:with-param name="interface" select="$xpath"/>		
    	</xsl:call-template>
    </xsl:template>
	
    <xsl:template name="node2nodes">
    	<xsl:param name="interface">//interface</xsl:param>
    	<node>
        <xsl:for-each select="$interface">
        	<node>
		    	<xsl:call-template name="nodefilter">
					<xsl:with-param name="interface" select="."/>		
		    	</xsl:call-template>
            </node>
        </xsl:for-each>
        </node>
    </xsl:template>
    
    <xsl:template name="nodefilter">
    	<xsl:param name="interface">//interface</xsl:param>
        <xsl:for-each select="$interface">
        	<node>
            	<xsl:copy-of select="."/>
            </node>
        </xsl:for-each>
    </xsl:template>
    
</xsl:stylesheet>