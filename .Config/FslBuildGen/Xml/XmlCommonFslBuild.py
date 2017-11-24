#!/usr/bin/env python3

#****************************************************************************************************************************************************
# Copyright (c) 2014 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
#    * Neither the name of the Freescale Semiconductor, Inc. nor the names of
#      its contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#****************************************************************************************************************************************************

from typing import List
import xml.etree.ElementTree as ET
from FslBuildGen.BasicConfig import BasicConfig
from FslBuildGen.Config import Config
from FslBuildGen.Xml.Exceptions import XmlUnsupportedTag
from FslBuildGen.Xml.SubPackageSupportConfig import SubPackageSupportConfig
from FslBuildGen.Xml.XmlGenFileRequirement import XmlGenFileRequirement
from FslBuildGen.Xml.XmlBase import XmlBase
from FslBuildGen.Xml.XmlBase2 import XmlBase2


class XmlGenFileUsesFeature(XmlBase):
    def __init__(self, basicConfig: BasicConfig, xmlElement: ET.Element) -> None:
        super(XmlGenFileUsesFeature, self).__init__(basicConfig, xmlElement)
        self.Name = self._ReadAttrib(xmlElement, 'Name')


class XmlCommonFslBuild(XmlBase2):
    def __init__(self, config: Config, xmlElement: ET.Element, subPackageSupport: SubPackageSupportConfig) -> None:
        super(XmlCommonFslBuild, self).__init__(config, xmlElement, subPackageSupport)
        self.__Config = config


    def _GetXMLRequirements(self, elem: ET.Element) -> List[XmlGenFileRequirement]:
        elements = []  # List[XmlGenFileRequirement]
        for child in elem:
            if child.tag == 'Requirement':
                elements.append(XmlGenFileRequirement(self.__Config, child))
            if child.tag == 'UsesFeature':
                legacyElement = XmlGenFileUsesFeature(self.BasicConfig, child)
                raise XmlUnsupportedTag(legacyElement.XMLElement, "The tag <UsesFeature Name='{0}'> has been replaced by <Requirement Name=\"{0}\" Type=\"feature\"> please update".format(legacyElement.Name))
        return elements