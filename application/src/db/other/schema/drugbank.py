# ./drugbank.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:bec9aba7331746bc78ae9501039c55dec5a831df
# Generated 2014-04-16 18:44:10.667947 by PyXB version 1.2.3
# Namespace http://drugbank.ca

import io
import sys

import pyxb
import pyxb.binding
import pyxb.binding.datatypes
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.utility


# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9ff807de-c5b8-11e3-a330-14109fd9e1c1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://drugbank.ca', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://drugbank.ca}EmptyStringType
class EmptyStringType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EmptyStringType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 16, 2)
    _Documentation = None
EmptyStringType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=EmptyStringType, enum_prefix=None)
EmptyStringType.emptyString = EmptyStringType._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
EmptyStringType._InitializeFacetMap(EmptyStringType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'EmptyStringType', EmptyStringType)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 37, 10)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.approved = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'approved', tag=u'approved')
STD_ANON.illicit = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'illicit', tag=u'illicit')
STD_ANON.experimental = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'experimental', tag=u'experimental')
STD_ANON.withdrawn = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'withdrawn', tag=u'withdrawn')
STD_ANON.nutraceutical = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'nutraceutical', tag=u'nutraceutical')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 372, 4)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Essential = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'Essential', tag=u'Essential')
STD_ANON_.Non_Essential = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'Non-Essential', tag=u'Non_Essential')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 385, 10)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.human = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'human', tag=u'human')
STD_ANON_2.bacterial = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'bacterial', tag=u'bacterial')
STD_ANON_2.fungal = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'fungal', tag=u'fungal')
STD_ANON_2.viral = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'viral', tag=u'viral')
STD_ANON_2.parasitic = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'parasitic', tag=u'parasitic')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 413, 8)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.logP = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'logP', tag=u'logP')
STD_ANON_3.logS = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'logS', tag=u'logS')
STD_ANON_3.logPhydrophobicity = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'logP/hydrophobicity', tag=u'logPhydrophobicity')
STD_ANON_3.Water_Solubility = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Water Solubility', tag=u'Water_Solubility')
STD_ANON_3.caco2_Permeability = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'caco2 Permeability', tag=u'caco2_Permeability')
STD_ANON_3.pKa_strongest_acidic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'pKa (strongest acidic)', tag=u'pKa_strongest_acidic')
STD_ANON_3.pKa_strongest_basic = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'pKa (strongest basic)', tag=u'pKa_strongest_basic')
STD_ANON_3.IUPAC_Name = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'IUPAC Name', tag=u'IUPAC_Name')
STD_ANON_3.Molecular_Weight = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Molecular Weight', tag=u'Molecular_Weight')
STD_ANON_3.Monoisotopic_Weight = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Monoisotopic Weight', tag=u'Monoisotopic_Weight')
STD_ANON_3.SMILES = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'SMILES', tag=u'SMILES')
STD_ANON_3.Molecular_Formula = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Molecular Formula', tag=u'Molecular_Formula')
STD_ANON_3.InChI = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'InChI', tag=u'InChI')
STD_ANON_3.InChIKey = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'InChIKey', tag=u'InChIKey')
STD_ANON_3.Polar_Surface_Area_PSA = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Polar Surface Area (PSA)', tag=u'Polar_Surface_Area_PSA')
STD_ANON_3.Refractivity = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Refractivity', tag=u'Refractivity')
STD_ANON_3.Polarizability = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Polarizability', tag=u'Polarizability')
STD_ANON_3.Rotatable_Bond_Count = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Rotatable Bond Count', tag=u'Rotatable_Bond_Count')
STD_ANON_3.H_Bond_Acceptor_Count = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'H Bond Acceptor Count', tag=u'H_Bond_Acceptor_Count')
STD_ANON_3.H_Bond_Donor_Count = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'H Bond Donor Count', tag=u'H_Bond_Donor_Count')
STD_ANON_3.Physiological_Charge = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'Physiological Charge', tag=u'Physiological_Charge')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 441, 8)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.JChem = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'JChem', tag=u'JChem')
STD_ANON_4.ALOGPS = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'ALOGPS', tag=u'ALOGPS')
STD_ANON_4.emptyString = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'', tag='emptyString')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 491, 12)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.yes = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'yes', tag=u'yes')
STD_ANON_5.no = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'no', tag=u'no')
STD_ANON_5.unknown = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 578, 6)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.small_molecule = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'small molecule', tag=u'small_molecule')
STD_ANON_6.biotech = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value=u'biotech', tag=u'biotech')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)

# Union simple type: {http://drugbank.ca}DecimalOrEmptyType
# superclasses pyxb.binding.datatypes.anySimpleType
class DecimalOrEmptyType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.decimal, EmptyStringType."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DecimalOrEmptyType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 13, 2)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.decimal, EmptyStringType, )
DecimalOrEmptyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=DecimalOrEmptyType)
DecimalOrEmptyType._CF_pattern = pyxb.binding.facets.CF_pattern()
DecimalOrEmptyType.emptyString = u''              # originally EmptyStringType.emptyString
DecimalOrEmptyType._InitializeFacetMap(DecimalOrEmptyType._CF_enumeration,
   DecimalOrEmptyType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'DecimalOrEmptyType', DecimalOrEmptyType)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 25, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}secondary-accession-number uses Python identifier secondary_accession_number
    __secondary_accession_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-number'), 'secondary_accession_number', '__httpdrugbank_ca_CTD_ANON_httpdrugbank_casecondary_accession_number', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 27, 8), )

    
    secondary_accession_number = property(__secondary_accession_number.value, __secondary_accession_number.set, None, None)

    _ElementMap.update({
        __secondary_accession_number.name() : __secondary_accession_number
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 34, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'group'), 'group', '__httpdrugbank_ca_CTD_ANON__httpdrugbank_cagroup', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 36, 8), )

    
    group = property(__group.value, __group.set, None, None)

    _ElementMap.update({
        __group.name() : __group
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 53, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'class'), 'class_', '__httpdrugbank_ca_CTD_ANON_2_class', pyxb.binding.datatypes.string, required=True)
    __class._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 56, 10)
    __class._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 56, 10)
    
    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __class.name() : __class
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 62, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}substructure uses Python identifier substructure
    __substructure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'substructure'), 'substructure', '__httpdrugbank_ca_CTD_ANON_3_httpdrugbank_casubstructure', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 52, 2), )

    
    substructure = property(__substructure.value, __substructure.set, None, None)

    _ElementMap.update({
        __substructure.name() : __substructure
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 69, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}substructures uses Python identifier substructures
    __substructures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'substructures'), 'substructures', '__httpdrugbank_ca_CTD_ANON_4_httpdrugbank_casubstructures', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 61, 2), )

    
    substructures = property(__substructures.value, __substructures.set, None, None)

    
    # Element {http://drugbank.ca}kingdom uses Python identifier kingdom
    __kingdom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'kingdom'), 'kingdom', '__httpdrugbank_ca_CTD_ANON_4_httpdrugbank_cakingdom', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 71, 8), )

    
    kingdom = property(__kingdom.value, __kingdom.set, None, None)

    _ElementMap.update({
        __substructures.name() : __substructures,
        __kingdom.name() : __kingdom
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 79, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}brand uses Python identifier brand
    __brand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'brand'), 'brand', '__httpdrugbank_ca_CTD_ANON_5_httpdrugbank_cabrand', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 81, 8), )

    
    brand = property(__brand.value, __brand.set, None, None)

    _ElementMap.update({
        __brand.name() : __brand
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 88, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}salt uses Python identifier salt
    __salt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'salt'), 'salt', '__httpdrugbank_ca_CTD_ANON_6_httpdrugbank_casalt', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 90, 8), )

    
    salt = property(__salt.value, __salt.set, None, None)

    _ElementMap.update({
        __salt.name() : __salt
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 97, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_CTD_ANON_7_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 99, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}ingredients uses Python identifier ingredients
    __ingredients = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ingredients'), 'ingredients', '__httpdrugbank_ca_CTD_ANON_7_httpdrugbank_caingredients', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 100, 8), )

    
    ingredients = property(__ingredients.value, __ingredients.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __ingredients.name() : __ingredients
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 105, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}mixture uses Python identifier mixture
    __mixture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mixture'), 'mixture', '__httpdrugbank_ca_CTD_ANON_8_httpdrugbank_camixture', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 96, 2), )

    
    mixture = property(__mixture.value, __mixture.set, None, None)

    _ElementMap.update({
        __mixture.name() : __mixture
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 114, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_CTD_ANON_9_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 116, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpdrugbank_ca_CTD_ANON_9_httpdrugbank_caurl', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 117, 8), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 122, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}packager uses Python identifier packager
    __packager = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'packager'), 'packager', '__httpdrugbank_ca_CTD_ANON_10_httpdrugbank_capackager', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 113, 2), )

    
    packager = property(__packager.value, __packager.set, None, None)

    _ElementMap.update({
        __packager.name() : __packager
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 131, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute generic uses Python identifier generic
    __generic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'generic'), 'generic', '__httpdrugbank_ca_CTD_ANON_11_generic', pyxb.binding.datatypes.string, required=True)
    __generic._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 134, 10)
    __generic._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 134, 10)
    
    generic = property(__generic.value, __generic.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __generic.name() : __generic
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 140, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}manufacturer uses Python identifier manufacturer
    __manufacturer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'manufacturer'), 'manufacturer', '__httpdrugbank_ca_CTD_ANON_12_httpdrugbank_camanufacturer', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 130, 2), )

    
    manufacturer = property(__manufacturer.value, __manufacturer.set, None, None)

    _ElementMap.update({
        __manufacturer.name() : __manufacturer
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute currency uses Python identifier currency
    __currency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'currency'), 'currency', '__httpdrugbank_ca_CTD_ANON_13_currency', pyxb.binding.datatypes.string, required=True)
    __currency._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 152, 10)
    __currency._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 152, 10)
    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __currency.name() : __currency
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 158, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}cost uses Python identifier cost
    __cost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cost'), 'cost', '__httpdrugbank_ca_CTD_ANON_14_httpdrugbank_cacost', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 148, 2), )

    
    cost = property(__cost.value, __cost.set, None, None)

    
    # Element {http://drugbank.ca}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpdrugbank_ca_CTD_ANON_14_httpdrugbank_cadescription', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 160, 8), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://drugbank.ca}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'unit'), 'unit', '__httpdrugbank_ca_CTD_ANON_14_httpdrugbank_caunit', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 162, 8), )

    
    unit = property(__unit.value, __unit.set, None, None)

    _ElementMap.update({
        __cost.name() : __cost,
        __description.name() : __description,
        __unit.name() : __unit
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 167, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}price uses Python identifier price
    __price = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'price'), 'price', '__httpdrugbank_ca_CTD_ANON_15_httpdrugbank_caprice', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 157, 2), )

    
    price = property(__price.value, __price.set, None, None)

    _ElementMap.update({
        __price.name() : __price
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 176, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpdrugbank_ca_CTD_ANON_16_httpdrugbank_cacategory', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 178, 8), )

    
    category = property(__category.value, __category.set, None, None)

    _ElementMap.update({
        __category.name() : __category
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 185, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}affected-organism uses Python identifier affected_organism
    __affected_organism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'affected-organism'), 'affected_organism', '__httpdrugbank_ca_CTD_ANON_17_httpdrugbank_caaffected_organism', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 187, 8), )

    
    affected_organism = property(__affected_organism.value, __affected_organism.set, None, None)

    _ElementMap.update({
        __affected_organism.name() : __affected_organism
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 194, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}form uses Python identifier form
    __form = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'form'), 'form', '__httpdrugbank_ca_CTD_ANON_18_httpdrugbank_caform', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 196, 8), )

    
    form = property(__form.value, __form.set, None, None)

    
    # Element {http://drugbank.ca}route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'route'), 'route', '__httpdrugbank_ca_CTD_ANON_18_httpdrugbank_caroute', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 197, 8), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Element {http://drugbank.ca}strength uses Python identifier strength
    __strength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'strength'), 'strength', '__httpdrugbank_ca_CTD_ANON_18_httpdrugbank_castrength', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 198, 8), )

    
    strength = property(__strength.value, __strength.set, None, None)

    _ElementMap.update({
        __form.name() : __form,
        __route.name() : __route,
        __strength.name() : __strength
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 203, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}dosage uses Python identifier dosage
    __dosage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dosage'), 'dosage', '__httpdrugbank_ca_CTD_ANON_19_httpdrugbank_cadosage', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 193, 2), )

    
    dosage = property(__dosage.value, __dosage.set, None, None)

    _ElementMap.update({
        __dosage.name() : __dosage
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 212, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}atc-code uses Python identifier atc_code
    __atc_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'atc-code'), 'atc_code', '__httpdrugbank_ca_CTD_ANON_20_httpdrugbank_caatc_code', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 214, 8), )

    
    atc_code = property(__atc_code.value, __atc_code.set, None, None)

    _ElementMap.update({
        __atc_code.name() : __atc_code
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 221, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}ahfs-code uses Python identifier ahfs_code
    __ahfs_code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ahfs-code'), 'ahfs_code', '__httpdrugbank_ca_CTD_ANON_21_httpdrugbank_caahfs_code', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 223, 8), )

    
    ahfs_code = property(__ahfs_code.value, __ahfs_code.set, None, None)

    _ElementMap.update({
        __ahfs_code.name() : __ahfs_code
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 230, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}number uses Python identifier number
    __number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'number'), 'number', '__httpdrugbank_ca_CTD_ANON_22_httpdrugbank_canumber', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 232, 8), )

    
    number = property(__number.value, __number.set, None, None)

    
    # Element {http://drugbank.ca}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpdrugbank_ca_CTD_ANON_22_httpdrugbank_cacountry', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 233, 8), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element {http://drugbank.ca}approved uses Python identifier approved
    __approved = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'approved'), 'approved', '__httpdrugbank_ca_CTD_ANON_22_httpdrugbank_caapproved', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 234, 8), )

    
    approved = property(__approved.value, __approved.set, None, None)

    
    # Element {http://drugbank.ca}expires uses Python identifier expires
    __expires = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'expires'), 'expires', '__httpdrugbank_ca_CTD_ANON_22_httpdrugbank_caexpires', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 235, 8), )

    
    expires = property(__expires.value, __expires.set, None, None)

    _ElementMap.update({
        __number.name() : __number,
        __country.name() : __country,
        __approved.name() : __approved,
        __expires.name() : __expires
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 240, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}patent uses Python identifier patent
    __patent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'patent'), 'patent', '__httpdrugbank_ca_CTD_ANON_23_httpdrugbank_capatent', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 229, 2), )

    
    patent = property(__patent.value, __patent.set, None, None)

    _ElementMap.update({
        __patent.name() : __patent
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 249, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}food-interaction uses Python identifier food_interaction
    __food_interaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'food-interaction'), 'food_interaction', '__httpdrugbank_ca_CTD_ANON_24_httpdrugbank_cafood_interaction', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 251, 8), )

    
    food_interaction = property(__food_interaction.value, __food_interaction.set, None, None)

    _ElementMap.update({
        __food_interaction.name() : __food_interaction
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}drug uses Python identifier drug
    __drug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'drug'), 'drug', '__httpdrugbank_ca_CTD_ANON_25_httpdrugbank_cadrug', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 260, 8), )

    
    drug = property(__drug.value, __drug.set, None, None)

    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_CTD_ANON_25_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 261, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpdrugbank_ca_CTD_ANON_25_httpdrugbank_cadescription', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 262, 8), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __drug.name() : __drug,
        __name.name() : __name,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 267, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}drug-interaction uses Python identifier drug_interaction
    __drug_interaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'drug-interaction'), 'drug_interaction', '__httpdrugbank_ca_CTD_ANON_26_httpdrugbank_cadrug_interaction', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 257, 2), )

    
    drug_interaction = property(__drug_interaction.value, __drug_interaction.set, None, None)

    _ElementMap.update({
        __drug_interaction.name() : __drug_interaction
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 276, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}protein-sequence uses Python identifier protein_sequence
    __protein_sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence'), 'protein_sequence', '__httpdrugbank_ca_CTD_ANON_27_httpdrugbank_caprotein_sequence', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 278, 8), )

    
    protein_sequence = property(__protein_sequence.value, __protein_sequence.set, None, None)

    _ElementMap.update({
        __protein_sequence.name() : __protein_sequence
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 285, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpdrugbank_ca_CTD_ANON_28_httpdrugbank_caresource', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 287, 8), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {http://drugbank.ca}url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'url'), 'url', '__httpdrugbank_ca_CTD_ANON_28_httpdrugbank_caurl', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 288, 8), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __resource.name() : __resource,
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 293, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}external-link uses Python identifier external_link
    __external_link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'external-link'), 'external_link', '__httpdrugbank_ca_CTD_ANON_29_httpdrugbank_caexternal_link', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 284, 2), )

    
    external_link = property(__external_link.value, __external_link.set, None, None)

    _ElementMap.update({
        __external_link.name() : __external_link
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 302, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'target'), 'target', '__httpdrugbank_ca_CTD_ANON_30_httpdrugbank_catarget', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 304, 8), )

    
    target = property(__target.value, __target.set, None, None)

    _ElementMap.update({
        __target.name() : __target
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 311, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}enzyme uses Python identifier enzyme
    __enzyme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'enzyme'), 'enzyme', '__httpdrugbank_ca_CTD_ANON_31_httpdrugbank_caenzyme', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 313, 8), )

    
    enzyme = property(__enzyme.value, __enzyme.set, None, None)

    _ElementMap.update({
        __enzyme.name() : __enzyme
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 320, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}transporter uses Python identifier transporter
    __transporter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transporter'), 'transporter', '__httpdrugbank_ca_CTD_ANON_32_httpdrugbank_catransporter', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 322, 8), )

    
    transporter = property(__transporter.value, __transporter.set, None, None)

    _ElementMap.update({
        __transporter.name() : __transporter
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 329, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}carrier uses Python identifier carrier
    __carrier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'carrier'), 'carrier', '__httpdrugbank_ca_CTD_ANON_33_httpdrugbank_cacarrier', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 331, 8), )

    
    carrier = property(__carrier.value, __carrier.set, None, None)

    _ElementMap.update({
        __carrier.name() : __carrier
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 338, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'identifier'), 'identifier', '__httpdrugbank_ca_CTD_ANON_34_httpdrugbank_caidentifier', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 340, 8), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_CTD_ANON_34_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 341, 8), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __identifier.name() : __identifier,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 346, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}pfam uses Python identifier pfam
    __pfam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pfam'), 'pfam', '__httpdrugbank_ca_CTD_ANON_35_httpdrugbank_capfam', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 337, 2), )

    
    pfam = property(__pfam.value, __pfam.set, None, None)

    _ElementMap.update({
        __pfam.name() : __pfam
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 355, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpdrugbank_ca_CTD_ANON_36_httpdrugbank_cacategory', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 357, 8), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://drugbank.ca}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpdrugbank_ca_CTD_ANON_36_httpdrugbank_cadescription', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 358, 8), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __category.name() : __category,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 363, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}go-classifier uses Python identifier go_classifier
    __go_classifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'go-classifier'), 'go_classifier', '__httpdrugbank_ca_CTD_ANON_37_httpdrugbank_cago_classifier', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 354, 2), )

    
    go_classifier = property(__go_classifier.value, __go_classifier.set, None, None)

    _ElementMap.update({
        __go_classifier.name() : __go_classifier
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 382, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'category'), 'category', '__httpdrugbank_ca_CTD_ANON_38_httpdrugbank_cacategory', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 384, 8), )

    
    category = property(__category.value, __category.set, None, None)

    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_CTD_ANON_38_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 395, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}uniprot-name uses Python identifier uniprot_name
    __uniprot_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uniprot-name'), 'uniprot_name', '__httpdrugbank_ca_CTD_ANON_38_httpdrugbank_cauniprot_name', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 396, 8), )

    
    uniprot_name = property(__uniprot_name.value, __uniprot_name.set, None, None)

    
    # Element {http://drugbank.ca}uniprot-taxon-id uses Python identifier uniprot_taxon_id
    __uniprot_taxon_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'uniprot-taxon-id'), 'uniprot_taxon_id', '__httpdrugbank_ca_CTD_ANON_38_httpdrugbank_cauniprot_taxon_id', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 397, 8), )

    
    uniprot_taxon_id = property(__uniprot_taxon_id.value, __uniprot_taxon_id.set, None, None)

    _ElementMap.update({
        __category.name() : __category,
        __name.name() : __name,
        __uniprot_name.name() : __uniprot_name,
        __uniprot_taxon_id.name() : __uniprot_taxon_id
    })
    _AttributeMap.update({
        
    })



# Complex type {http://drugbank.ca}SequenceType with content type ELEMENT_ONLY
class SequenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}SequenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SequenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 404, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'header'), 'header', '__httpdrugbank_ca_SequenceType_httpdrugbank_caheader', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 406, 6), )

    
    header = property(__header.value, __header.set, None, None)

    
    # Element {http://drugbank.ca}chain uses Python identifier chain
    __chain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'chain'), 'chain', '__httpdrugbank_ca_SequenceType_httpdrugbank_cachain', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 407, 6), )

    
    chain = property(__chain.value, __chain.set, None, None)

    _ElementMap.update({
        __header.name() : __header,
        __chain.name() : __chain
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SequenceType', SequenceType)


# Complex type {http://drugbank.ca}PropertyType with content type ELEMENT_ONLY
class PropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}PropertyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 410, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}kind uses Python identifier kind
    __kind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'kind'), 'kind', '__httpdrugbank_ca_PropertyType_httpdrugbank_cakind', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 412, 6), )

    
    kind = property(__kind.value, __kind.set, None, None)

    
    # Element {http://drugbank.ca}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpdrugbank_ca_PropertyType_httpdrugbank_cavalue', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 439, 6), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element {http://drugbank.ca}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpdrugbank_ca_PropertyType_httpdrugbank_casource', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 440, 6), )

    
    source = property(__source.value, __source.set, None, None)

    _ElementMap.update({
        __kind.name() : __kind,
        __value.name() : __value,
        __source.name() : __source
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PropertyType', PropertyType)


# Complex type {http://drugbank.ca}PropertiesType with content type ELEMENT_ONLY
class PropertiesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}PropertiesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PropertiesType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 451, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'property'), 'property_', '__httpdrugbank_ca_PropertiesType_httpdrugbank_caproperty', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 453, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PropertiesType', PropertiesType)


# Complex type {http://drugbank.ca}SynonymsType with content type ELEMENT_ONLY
class SynonymsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}SynonymsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SynonymsType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 456, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}synonym uses Python identifier synonym
    __synonym = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synonym'), 'synonym', '__httpdrugbank_ca_SynonymsType_httpdrugbank_casynonym', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 458, 6), )

    
    synonym = property(__synonym.value, __synonym.set, None, None)

    _ElementMap.update({
        __synonym.name() : __synonym
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SynonymsType', SynonymsType)


# Complex type {http://drugbank.ca}IdentifiersType with content type ELEMENT_ONLY
class IdentifiersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}IdentifiersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IdentifiersType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 461, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}external-identifier uses Python identifier external_identifier
    __external_identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'external-identifier'), 'external_identifier', '__httpdrugbank_ca_IdentifiersType_httpdrugbank_caexternal_identifier', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 463, 6), )

    
    external_identifier = property(__external_identifier.value, __external_identifier.set, None, None)

    _ElementMap.update({
        __external_identifier.name() : __external_identifier
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'IdentifiersType', IdentifiersType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 464, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpdrugbank_ca_CTD_ANON_39_httpdrugbank_caresource', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 466, 12), )

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {http://drugbank.ca}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'identifier'), 'identifier', '__httpdrugbank_ca_CTD_ANON_39_httpdrugbank_caidentifier', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 467, 12), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    _ElementMap.update({
        __resource.name() : __resource,
        __identifier.name() : __identifier
    })
    _AttributeMap.update({
        
    })



# Complex type {http://drugbank.ca}BondActionsType with content type ELEMENT_ONLY
class BondActionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}BondActionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BondActionsType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 473, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}action uses Python identifier action
    __action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'action'), 'action', '__httpdrugbank_ca_BondActionsType_httpdrugbank_caaction', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 475, 6), )

    
    action = property(__action.value, __action.set, None, None)

    _ElementMap.update({
        __action.name() : __action
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'BondActionsType', BondActionsType)


# Complex type {http://drugbank.ca}BondType with content type ELEMENT_ONLY
class BondType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}BondType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BondType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 478, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}actions uses Python identifier actions
    __actions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'actions'), 'actions', '__httpdrugbank_ca_BondType_httpdrugbank_caactions', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 480, 6), )

    
    actions = property(__actions.value, __actions.set, None, None)

    
    # Element {http://drugbank.ca}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'references'), 'references', '__httpdrugbank_ca_BondType_httpdrugbank_careferences', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 481, 6), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'position'), 'position', '__httpdrugbank_ca_BondType_position', pyxb.binding.datatypes.integer)
    __position._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 483, 4)
    __position._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 483, 4)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute partner uses Python identifier partner
    __partner = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'partner'), 'partner', '__httpdrugbank_ca_BondType_partner', pyxb.binding.datatypes.integer)
    __partner._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 484, 4)
    __partner._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 484, 4)
    
    partner = property(__partner.value, __partner.set, None, None)

    _ElementMap.update({
        __actions.name() : __actions,
        __references.name() : __references
    })
    _AttributeMap.update({
        __position.name() : __position,
        __partner.name() : __partner
    })
Namespace.addCategoryObject('typeBinding', u'BondType', BondType)


# Complex type {http://drugbank.ca}PartnerType with content type ELEMENT_ONLY
class PartnerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}PartnerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PartnerType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 504, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}pfams uses Python identifier pfams
    __pfams = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pfams'), 'pfams', '__httpdrugbank_ca_PartnerType_httpdrugbank_capfams', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 345, 2), )

    
    pfams = property(__pfams.value, __pfams.set, None, None)

    
    # Element {http://drugbank.ca}go-classifiers uses Python identifier go_classifiers
    __go_classifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'go-classifiers'), 'go_classifiers', '__httpdrugbank_ca_PartnerType_httpdrugbank_cago_classifiers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 362, 2), )

    
    go_classifiers = property(__go_classifiers.value, __go_classifiers.set, None, None)

    
    # Element {http://drugbank.ca}essentiality uses Python identifier essentiality
    __essentiality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'essentiality'), 'essentiality', '__httpdrugbank_ca_PartnerType_httpdrugbank_caessentiality', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 371, 2), )

    
    essentiality = property(__essentiality.value, __essentiality.set, None, None)

    
    # Element {http://drugbank.ca}species uses Python identifier species
    __species = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'species'), 'species', '__httpdrugbank_ca_PartnerType_httpdrugbank_caspecies', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 381, 2), )

    
    species = property(__species.value, __species.set, None, None)

    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_PartnerType_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 506, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}general-function uses Python identifier general_function
    __general_function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'general-function'), 'general_function', '__httpdrugbank_ca_PartnerType_httpdrugbank_cageneral_function', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 507, 6), )

    
    general_function = property(__general_function.value, __general_function.set, None, None)

    
    # Element {http://drugbank.ca}specific-function uses Python identifier specific_function
    __specific_function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'specific-function'), 'specific_function', '__httpdrugbank_ca_PartnerType_httpdrugbank_caspecific_function', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 508, 6), )

    
    specific_function = property(__specific_function.value, __specific_function.set, None, None)

    
    # Element {http://drugbank.ca}gene-name uses Python identifier gene_name
    __gene_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gene-name'), 'gene_name', '__httpdrugbank_ca_PartnerType_httpdrugbank_cagene_name', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 509, 6), )

    
    gene_name = property(__gene_name.value, __gene_name.set, None, None)

    
    # Element {http://drugbank.ca}locus uses Python identifier locus
    __locus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'locus'), 'locus', '__httpdrugbank_ca_PartnerType_httpdrugbank_calocus', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 510, 6), )

    
    locus = property(__locus.value, __locus.set, None, None)

    
    # Element {http://drugbank.ca}reaction uses Python identifier reaction
    __reaction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reaction'), 'reaction', '__httpdrugbank_ca_PartnerType_httpdrugbank_careaction', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 511, 6), )

    
    reaction = property(__reaction.value, __reaction.set, None, None)

    
    # Element {http://drugbank.ca}signals uses Python identifier signals
    __signals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'signals'), 'signals', '__httpdrugbank_ca_PartnerType_httpdrugbank_casignals', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 512, 6), )

    
    signals = property(__signals.value, __signals.set, None, None)

    
    # Element {http://drugbank.ca}cellular-location uses Python identifier cellular_location
    __cellular_location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cellular-location'), 'cellular_location', '__httpdrugbank_ca_PartnerType_httpdrugbank_cacellular_location', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 513, 6), )

    
    cellular_location = property(__cellular_location.value, __cellular_location.set, None, None)

    
    # Element {http://drugbank.ca}transmembrane-regions uses Python identifier transmembrane_regions
    __transmembrane_regions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transmembrane-regions'), 'transmembrane_regions', '__httpdrugbank_ca_PartnerType_httpdrugbank_catransmembrane_regions', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 514, 6), )

    
    transmembrane_regions = property(__transmembrane_regions.value, __transmembrane_regions.set, None, None)

    
    # Element {http://drugbank.ca}theoretical-pi uses Python identifier theoretical_pi
    __theoretical_pi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'theoretical-pi'), 'theoretical_pi', '__httpdrugbank_ca_PartnerType_httpdrugbank_catheoretical_pi', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 515, 6), )

    
    theoretical_pi = property(__theoretical_pi.value, __theoretical_pi.set, None, None)

    
    # Element {http://drugbank.ca}molecular-weight uses Python identifier molecular_weight
    __molecular_weight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'molecular-weight'), 'molecular_weight', '__httpdrugbank_ca_PartnerType_httpdrugbank_camolecular_weight', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 516, 6), )

    
    molecular_weight = property(__molecular_weight.value, __molecular_weight.set, None, None)

    
    # Element {http://drugbank.ca}chromosome uses Python identifier chromosome
    __chromosome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'chromosome'), 'chromosome', '__httpdrugbank_ca_PartnerType_httpdrugbank_cachromosome', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 517, 6), )

    
    chromosome = property(__chromosome.value, __chromosome.set, None, None)

    
    # Element {http://drugbank.ca}references uses Python identifier references
    __references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'references'), 'references', '__httpdrugbank_ca_PartnerType_httpdrugbank_careferences', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 520, 6), )

    
    references = property(__references.value, __references.set, None, None)

    
    # Element {http://drugbank.ca}external-identifiers uses Python identifier external_identifiers
    __external_identifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers'), 'external_identifiers', '__httpdrugbank_ca_PartnerType_httpdrugbank_caexternal_identifiers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 521, 6), )

    
    external_identifiers = property(__external_identifiers.value, __external_identifiers.set, None, None)

    
    # Element {http://drugbank.ca}synonyms uses Python identifier synonyms
    __synonyms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synonyms'), 'synonyms', '__httpdrugbank_ca_PartnerType_httpdrugbank_casynonyms', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 522, 6), )

    
    synonyms = property(__synonyms.value, __synonyms.set, None, None)

    
    # Element {http://drugbank.ca}protein-sequence uses Python identifier protein_sequence
    __protein_sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence'), 'protein_sequence', '__httpdrugbank_ca_PartnerType_httpdrugbank_caprotein_sequence', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 523, 6), )

    
    protein_sequence = property(__protein_sequence.value, __protein_sequence.set, None, None)

    
    # Element {http://drugbank.ca}gene-sequence uses Python identifier gene_sequence
    __gene_sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gene-sequence'), 'gene_sequence', '__httpdrugbank_ca_PartnerType_httpdrugbank_cagene_sequence', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 524, 6), )

    
    gene_sequence = property(__gene_sequence.value, __gene_sequence.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpdrugbank_ca_PartnerType_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 528, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 528, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __pfams.name() : __pfams,
        __go_classifiers.name() : __go_classifiers,
        __essentiality.name() : __essentiality,
        __species.name() : __species,
        __name.name() : __name,
        __general_function.name() : __general_function,
        __specific_function.name() : __specific_function,
        __gene_name.name() : __gene_name,
        __locus.name() : __locus,
        __reaction.name() : __reaction,
        __signals.name() : __signals,
        __cellular_location.name() : __cellular_location,
        __transmembrane_regions.name() : __transmembrane_regions,
        __theoretical_pi.name() : __theoretical_pi,
        __molecular_weight.name() : __molecular_weight,
        __chromosome.name() : __chromosome,
        __references.name() : __references,
        __external_identifiers.name() : __external_identifiers,
        __synonyms.name() : __synonyms,
        __protein_sequence.name() : __protein_sequence,
        __gene_sequence.name() : __gene_sequence
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'PartnerType', PartnerType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 591, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}drug uses Python identifier drug
    __drug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'drug'), 'drug', '__httpdrugbank_ca_CTD_ANON_40_httpdrugbank_cadrug', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 593, 8), )

    
    drug = property(__drug.value, __drug.set, None, None)

    
    # Element {http://drugbank.ca}partners uses Python identifier partners
    __partners = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'partners'), 'partners', '__httpdrugbank_ca_CTD_ANON_40_httpdrugbank_capartners', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 594, 8), )

    
    partners = property(__partners.value, __partners.set, None, None)

    
    # Attribute schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'schemaVersion'), 'schemaVersion', '__httpdrugbank_ca_CTD_ANON_40_schemaVersion', pyxb.binding.datatypes.decimal, required=True)
    __schemaVersion._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 602, 6)
    __schemaVersion._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 602, 6)
    
    schemaVersion = property(__schemaVersion.value, __schemaVersion.set, None, None)

    _ElementMap.update({
        __drug.name() : __drug,
        __partners.name() : __partners
    })
    _AttributeMap.update({
        __schemaVersion.name() : __schemaVersion
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 595, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}partner uses Python identifier partner
    __partner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'partner'), 'partner', '__httpdrugbank_ca_CTD_ANON_41_httpdrugbank_capartner', True, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 597, 14), )

    
    partner = property(__partner.value, __partner.set, None, None)

    _ElementMap.update({
        __partner.name() : __partner
    })
    _AttributeMap.update({
        
    })



# Complex type {http://drugbank.ca}TargetBondType with content type ELEMENT_ONLY
class TargetBondType (BondType):
    """Complex type {http://drugbank.ca}TargetBondType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TargetBondType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 486, 2)
    _ElementMap = BondType._ElementMap.copy()
    _AttributeMap = BondType._AttributeMap.copy()
    # Base type is BondType
    
    # Element actions ({http://drugbank.ca}actions) inherited from {http://drugbank.ca}BondType
    
    # Element references ({http://drugbank.ca}references) inherited from {http://drugbank.ca}BondType
    
    # Element {http://drugbank.ca}known-action uses Python identifier known_action
    __known_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'known-action'), 'known_action', '__httpdrugbank_ca_TargetBondType_httpdrugbank_caknown_action', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 490, 10), )

    
    known_action = property(__known_action.value, __known_action.set, None, None)

    
    # Attribute position inherited from {http://drugbank.ca}BondType
    
    # Attribute partner inherited from {http://drugbank.ca}BondType
    _ElementMap.update({
        __known_action.name() : __known_action
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TargetBondType', TargetBondType)


# Complex type {http://drugbank.ca}DrugType with content type ELEMENT_ONLY
class DrugType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://drugbank.ca}DrugType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DrugType')
    _XSDLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 530, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://drugbank.ca}secondary-accession-numbers uses Python identifier secondary_accession_numbers
    __secondary_accession_numbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-numbers'), 'secondary_accession_numbers', '__httpdrugbank_ca_DrugType_httpdrugbank_casecondary_accession_numbers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 24, 2), )

    
    secondary_accession_numbers = property(__secondary_accession_numbers.value, __secondary_accession_numbers.set, None, None)

    
    # Element {http://drugbank.ca}groups uses Python identifier groups
    __groups = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'groups'), 'groups', '__httpdrugbank_ca_DrugType_httpdrugbank_cagroups', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 33, 2), )

    
    groups = property(__groups.value, __groups.set, None, None)

    
    # Element {http://drugbank.ca}taxonomy uses Python identifier taxonomy
    __taxonomy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'taxonomy'), 'taxonomy', '__httpdrugbank_ca_DrugType_httpdrugbank_cataxonomy', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 68, 2), )

    
    taxonomy = property(__taxonomy.value, __taxonomy.set, None, None)

    
    # Element {http://drugbank.ca}brands uses Python identifier brands
    __brands = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'brands'), 'brands', '__httpdrugbank_ca_DrugType_httpdrugbank_cabrands', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 78, 2), )

    
    brands = property(__brands.value, __brands.set, None, None)

    
    # Element {http://drugbank.ca}salts uses Python identifier salts
    __salts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'salts'), 'salts', '__httpdrugbank_ca_DrugType_httpdrugbank_casalts', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 87, 2), )

    
    salts = property(__salts.value, __salts.set, None, None)

    
    # Element {http://drugbank.ca}mixtures uses Python identifier mixtures
    __mixtures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mixtures'), 'mixtures', '__httpdrugbank_ca_DrugType_httpdrugbank_camixtures', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 104, 2), )

    
    mixtures = property(__mixtures.value, __mixtures.set, None, None)

    
    # Element {http://drugbank.ca}packagers uses Python identifier packagers
    __packagers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'packagers'), 'packagers', '__httpdrugbank_ca_DrugType_httpdrugbank_capackagers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 121, 2), )

    
    packagers = property(__packagers.value, __packagers.set, None, None)

    
    # Element {http://drugbank.ca}manufacturers uses Python identifier manufacturers
    __manufacturers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'manufacturers'), 'manufacturers', '__httpdrugbank_ca_DrugType_httpdrugbank_camanufacturers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 139, 2), )

    
    manufacturers = property(__manufacturers.value, __manufacturers.set, None, None)

    
    # Element {http://drugbank.ca}prices uses Python identifier prices
    __prices = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'prices'), 'prices', '__httpdrugbank_ca_DrugType_httpdrugbank_caprices', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 166, 2), )

    
    prices = property(__prices.value, __prices.set, None, None)

    
    # Element {http://drugbank.ca}categories uses Python identifier categories
    __categories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'categories'), 'categories', '__httpdrugbank_ca_DrugType_httpdrugbank_cacategories', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 175, 2), )

    
    categories = property(__categories.value, __categories.set, None, None)

    
    # Element {http://drugbank.ca}affected-organisms uses Python identifier affected_organisms
    __affected_organisms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'affected-organisms'), 'affected_organisms', '__httpdrugbank_ca_DrugType_httpdrugbank_caaffected_organisms', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 184, 2), )

    
    affected_organisms = property(__affected_organisms.value, __affected_organisms.set, None, None)

    
    # Element {http://drugbank.ca}dosages uses Python identifier dosages
    __dosages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dosages'), 'dosages', '__httpdrugbank_ca_DrugType_httpdrugbank_cadosages', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 202, 2), )

    
    dosages = property(__dosages.value, __dosages.set, None, None)

    
    # Element {http://drugbank.ca}atc-codes uses Python identifier atc_codes
    __atc_codes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'atc-codes'), 'atc_codes', '__httpdrugbank_ca_DrugType_httpdrugbank_caatc_codes', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 211, 2), )

    
    atc_codes = property(__atc_codes.value, __atc_codes.set, None, None)

    
    # Element {http://drugbank.ca}ahfs-codes uses Python identifier ahfs_codes
    __ahfs_codes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ahfs-codes'), 'ahfs_codes', '__httpdrugbank_ca_DrugType_httpdrugbank_caahfs_codes', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 220, 2), )

    
    ahfs_codes = property(__ahfs_codes.value, __ahfs_codes.set, None, None)

    
    # Element {http://drugbank.ca}patents uses Python identifier patents
    __patents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'patents'), 'patents', '__httpdrugbank_ca_DrugType_httpdrugbank_capatents', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 239, 2), )

    
    patents = property(__patents.value, __patents.set, None, None)

    
    # Element {http://drugbank.ca}food-interactions uses Python identifier food_interactions
    __food_interactions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'food-interactions'), 'food_interactions', '__httpdrugbank_ca_DrugType_httpdrugbank_cafood_interactions', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 248, 2), )

    
    food_interactions = property(__food_interactions.value, __food_interactions.set, None, None)

    
    # Element {http://drugbank.ca}drug-interactions uses Python identifier drug_interactions
    __drug_interactions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'drug-interactions'), 'drug_interactions', '__httpdrugbank_ca_DrugType_httpdrugbank_cadrug_interactions', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 266, 2), )

    
    drug_interactions = property(__drug_interactions.value, __drug_interactions.set, None, None)

    
    # Element {http://drugbank.ca}protein-sequences uses Python identifier protein_sequences
    __protein_sequences = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'protein-sequences'), 'protein_sequences', '__httpdrugbank_ca_DrugType_httpdrugbank_caprotein_sequences', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 275, 2), )

    
    protein_sequences = property(__protein_sequences.value, __protein_sequences.set, None, None)

    
    # Element {http://drugbank.ca}external-links uses Python identifier external_links
    __external_links = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'external-links'), 'external_links', '__httpdrugbank_ca_DrugType_httpdrugbank_caexternal_links', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 292, 2), )

    
    external_links = property(__external_links.value, __external_links.set, None, None)

    
    # Element {http://drugbank.ca}targets uses Python identifier targets
    __targets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targets'), 'targets', '__httpdrugbank_ca_DrugType_httpdrugbank_catargets', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 301, 2), )

    
    targets = property(__targets.value, __targets.set, None, None)

    
    # Element {http://drugbank.ca}enzymes uses Python identifier enzymes
    __enzymes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'enzymes'), 'enzymes', '__httpdrugbank_ca_DrugType_httpdrugbank_caenzymes', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 310, 2), )

    
    enzymes = property(__enzymes.value, __enzymes.set, None, None)

    
    # Element {http://drugbank.ca}transporters uses Python identifier transporters
    __transporters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transporters'), 'transporters', '__httpdrugbank_ca_DrugType_httpdrugbank_catransporters', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 319, 2), )

    
    transporters = property(__transporters.value, __transporters.set, None, None)

    
    # Element {http://drugbank.ca}carriers uses Python identifier carriers
    __carriers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'carriers'), 'carriers', '__httpdrugbank_ca_DrugType_httpdrugbank_cacarriers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 328, 2), )

    
    carriers = property(__carriers.value, __carriers.set, None, None)

    
    # Element {http://drugbank.ca}drugbank-id uses Python identifier drugbank_id
    __drugbank_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'drugbank-id'), 'drugbank_id', '__httpdrugbank_ca_DrugType_httpdrugbank_cadrugbank_id', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 532, 6), )

    
    drugbank_id = property(__drugbank_id.value, __drugbank_id.set, None, None)

    
    # Element {http://drugbank.ca}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpdrugbank_ca_DrugType_httpdrugbank_caname', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 533, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://drugbank.ca}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpdrugbank_ca_DrugType_httpdrugbank_cadescription', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 534, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://drugbank.ca}cas-number uses Python identifier cas_number
    __cas_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cas-number'), 'cas_number', '__httpdrugbank_ca_DrugType_httpdrugbank_cacas_number', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 535, 6), )

    
    cas_number = property(__cas_number.value, __cas_number.set, None, None)

    
    # Element {http://drugbank.ca}general-references uses Python identifier general_references
    __general_references = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'general-references'), 'general_references', '__httpdrugbank_ca_DrugType_httpdrugbank_cageneral_references', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 536, 6), )

    
    general_references = property(__general_references.value, __general_references.set, None, None)

    
    # Element {http://drugbank.ca}synthesis-reference uses Python identifier synthesis_reference
    __synthesis_reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synthesis-reference'), 'synthesis_reference', '__httpdrugbank_ca_DrugType_httpdrugbank_casynthesis_reference', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 537, 6), )

    
    synthesis_reference = property(__synthesis_reference.value, __synthesis_reference.set, None, None)

    
    # Element {http://drugbank.ca}indication uses Python identifier indication
    __indication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'indication'), 'indication', '__httpdrugbank_ca_DrugType_httpdrugbank_caindication', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 538, 6), )

    
    indication = property(__indication.value, __indication.set, None, None)

    
    # Element {http://drugbank.ca}pharmacology uses Python identifier pharmacology
    __pharmacology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pharmacology'), 'pharmacology', '__httpdrugbank_ca_DrugType_httpdrugbank_capharmacology', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 539, 6), )

    
    pharmacology = property(__pharmacology.value, __pharmacology.set, None, None)

    
    # Element {http://drugbank.ca}mechanism-of-action uses Python identifier mechanism_of_action
    __mechanism_of_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mechanism-of-action'), 'mechanism_of_action', '__httpdrugbank_ca_DrugType_httpdrugbank_camechanism_of_action', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 540, 6), )

    
    mechanism_of_action = property(__mechanism_of_action.value, __mechanism_of_action.set, None, None)

    
    # Element {http://drugbank.ca}toxicity uses Python identifier toxicity
    __toxicity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'toxicity'), 'toxicity', '__httpdrugbank_ca_DrugType_httpdrugbank_catoxicity', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 541, 6), )

    
    toxicity = property(__toxicity.value, __toxicity.set, None, None)

    
    # Element {http://drugbank.ca}biotransformation uses Python identifier biotransformation
    __biotransformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biotransformation'), 'biotransformation', '__httpdrugbank_ca_DrugType_httpdrugbank_cabiotransformation', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 542, 6), )

    
    biotransformation = property(__biotransformation.value, __biotransformation.set, None, None)

    
    # Element {http://drugbank.ca}absorption uses Python identifier absorption
    __absorption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'absorption'), 'absorption', '__httpdrugbank_ca_DrugType_httpdrugbank_caabsorption', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 543, 6), )

    
    absorption = property(__absorption.value, __absorption.set, None, None)

    
    # Element {http://drugbank.ca}half-life uses Python identifier half_life
    __half_life = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'half-life'), 'half_life', '__httpdrugbank_ca_DrugType_httpdrugbank_cahalf_life', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 544, 6), )

    
    half_life = property(__half_life.value, __half_life.set, None, None)

    
    # Element {http://drugbank.ca}protein-binding uses Python identifier protein_binding
    __protein_binding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'protein-binding'), 'protein_binding', '__httpdrugbank_ca_DrugType_httpdrugbank_caprotein_binding', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 545, 6), )

    
    protein_binding = property(__protein_binding.value, __protein_binding.set, None, None)

    
    # Element {http://drugbank.ca}route-of-elimination uses Python identifier route_of_elimination
    __route_of_elimination = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'route-of-elimination'), 'route_of_elimination', '__httpdrugbank_ca_DrugType_httpdrugbank_caroute_of_elimination', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 546, 6), )

    
    route_of_elimination = property(__route_of_elimination.value, __route_of_elimination.set, None, None)

    
    # Element {http://drugbank.ca}volume-of-distribution uses Python identifier volume_of_distribution
    __volume_of_distribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'volume-of-distribution'), 'volume_of_distribution', '__httpdrugbank_ca_DrugType_httpdrugbank_cavolume_of_distribution', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 547, 6), )

    
    volume_of_distribution = property(__volume_of_distribution.value, __volume_of_distribution.set, None, None)

    
    # Element {http://drugbank.ca}clearance uses Python identifier clearance
    __clearance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'clearance'), 'clearance', '__httpdrugbank_ca_DrugType_httpdrugbank_caclearance', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 548, 6), )

    
    clearance = property(__clearance.value, __clearance.set, None, None)

    
    # Element {http://drugbank.ca}synonyms uses Python identifier synonyms
    __synonyms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'synonyms'), 'synonyms', '__httpdrugbank_ca_DrugType_httpdrugbank_casynonyms', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 552, 6), )

    
    synonyms = property(__synonyms.value, __synonyms.set, None, None)

    
    # Element {http://drugbank.ca}calculated-properties uses Python identifier calculated_properties
    __calculated_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'calculated-properties'), 'calculated_properties', '__httpdrugbank_ca_DrugType_httpdrugbank_cacalculated_properties', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 568, 6), )

    
    calculated_properties = property(__calculated_properties.value, __calculated_properties.set, None, None)

    
    # Element {http://drugbank.ca}experimental-properties uses Python identifier experimental_properties
    __experimental_properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'experimental-properties'), 'experimental_properties', '__httpdrugbank_ca_DrugType_httpdrugbank_caexperimental_properties', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 569, 6), )

    
    experimental_properties = property(__experimental_properties.value, __experimental_properties.set, None, None)

    
    # Element {http://drugbank.ca}external-identifiers uses Python identifier external_identifiers
    __external_identifiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers'), 'external_identifiers', '__httpdrugbank_ca_DrugType_httpdrugbank_caexternal_identifiers', False, pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 570, 6), )

    
    external_identifiers = property(__external_identifiers.value, __external_identifiers.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpdrugbank_ca_DrugType_type', STD_ANON_6, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 577, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 577, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute updated uses Python identifier updated
    __updated = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updated'), 'updated', '__httpdrugbank_ca_DrugType_updated', pyxb.binding.datatypes.string, required=True)
    __updated._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 585, 4)
    __updated._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 585, 4)
    
    updated = property(__updated.value, __updated.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpdrugbank_ca_DrugType_created', pyxb.binding.datatypes.string, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 586, 4)
    __created._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 586, 4)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpdrugbank_ca_DrugType_version', pyxb.binding.datatypes.decimal, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 587, 4)
    __version._UseLocation = pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 587, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __secondary_accession_numbers.name() : __secondary_accession_numbers,
        __groups.name() : __groups,
        __taxonomy.name() : __taxonomy,
        __brands.name() : __brands,
        __salts.name() : __salts,
        __mixtures.name() : __mixtures,
        __packagers.name() : __packagers,
        __manufacturers.name() : __manufacturers,
        __prices.name() : __prices,
        __categories.name() : __categories,
        __affected_organisms.name() : __affected_organisms,
        __dosages.name() : __dosages,
        __atc_codes.name() : __atc_codes,
        __ahfs_codes.name() : __ahfs_codes,
        __patents.name() : __patents,
        __food_interactions.name() : __food_interactions,
        __drug_interactions.name() : __drug_interactions,
        __protein_sequences.name() : __protein_sequences,
        __external_links.name() : __external_links,
        __targets.name() : __targets,
        __enzymes.name() : __enzymes,
        __transporters.name() : __transporters,
        __carriers.name() : __carriers,
        __drugbank_id.name() : __drugbank_id,
        __name.name() : __name,
        __description.name() : __description,
        __cas_number.name() : __cas_number,
        __general_references.name() : __general_references,
        __synthesis_reference.name() : __synthesis_reference,
        __indication.name() : __indication,
        __pharmacology.name() : __pharmacology,
        __mechanism_of_action.name() : __mechanism_of_action,
        __toxicity.name() : __toxicity,
        __biotransformation.name() : __biotransformation,
        __absorption.name() : __absorption,
        __half_life.name() : __half_life,
        __protein_binding.name() : __protein_binding,
        __route_of_elimination.name() : __route_of_elimination,
        __volume_of_distribution.name() : __volume_of_distribution,
        __clearance.name() : __clearance,
        __synonyms.name() : __synonyms,
        __calculated_properties.name() : __calculated_properties,
        __experimental_properties.name() : __experimental_properties,
        __external_identifiers.name() : __external_identifiers
    })
    _AttributeMap.update({
        __type.name() : __type,
        __updated.name() : __updated,
        __created.name() : __created,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'DrugType', DrugType)


secondary_accession_numbers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-numbers'), CTD_ANON, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 24, 2))
Namespace.addCategoryObject('elementBinding', secondary_accession_numbers.name().localName(), secondary_accession_numbers)

groups = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'groups'), CTD_ANON_, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', groups.name().localName(), groups)

substructure = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'substructure'), CTD_ANON_2, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', substructure.name().localName(), substructure)

substructures = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'substructures'), CTD_ANON_3, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 61, 2))
Namespace.addCategoryObject('elementBinding', substructures.name().localName(), substructures)

taxonomy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxonomy'), CTD_ANON_4, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 68, 2))
Namespace.addCategoryObject('elementBinding', taxonomy.name().localName(), taxonomy)

brands = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'brands'), CTD_ANON_5, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 78, 2))
Namespace.addCategoryObject('elementBinding', brands.name().localName(), brands)

salts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'salts'), CTD_ANON_6, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 87, 2))
Namespace.addCategoryObject('elementBinding', salts.name().localName(), salts)

mixture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mixture'), CTD_ANON_7, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 96, 2))
Namespace.addCategoryObject('elementBinding', mixture.name().localName(), mixture)

mixtures = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mixtures'), CTD_ANON_8, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 104, 2))
Namespace.addCategoryObject('elementBinding', mixtures.name().localName(), mixtures)

packager = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'packager'), CTD_ANON_9, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 113, 2))
Namespace.addCategoryObject('elementBinding', packager.name().localName(), packager)

packagers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'packagers'), CTD_ANON_10, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 121, 2))
Namespace.addCategoryObject('elementBinding', packagers.name().localName(), packagers)

manufacturer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'manufacturer'), CTD_ANON_11, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 130, 2))
Namespace.addCategoryObject('elementBinding', manufacturer.name().localName(), manufacturer)

manufacturers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'manufacturers'), CTD_ANON_12, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 139, 2))
Namespace.addCategoryObject('elementBinding', manufacturers.name().localName(), manufacturers)

cost = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cost'), CTD_ANON_13, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 148, 2))
Namespace.addCategoryObject('elementBinding', cost.name().localName(), cost)

price = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'price'), CTD_ANON_14, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 157, 2))
Namespace.addCategoryObject('elementBinding', price.name().localName(), price)

prices = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prices'), CTD_ANON_15, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 166, 2))
Namespace.addCategoryObject('elementBinding', prices.name().localName(), prices)

categories = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'categories'), CTD_ANON_16, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 175, 2))
Namespace.addCategoryObject('elementBinding', categories.name().localName(), categories)

affected_organisms = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affected-organisms'), CTD_ANON_17, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 184, 2))
Namespace.addCategoryObject('elementBinding', affected_organisms.name().localName(), affected_organisms)

dosage = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dosage'), CTD_ANON_18, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 193, 2))
Namespace.addCategoryObject('elementBinding', dosage.name().localName(), dosage)

dosages = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dosages'), CTD_ANON_19, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 202, 2))
Namespace.addCategoryObject('elementBinding', dosages.name().localName(), dosages)

atc_codes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'atc-codes'), CTD_ANON_20, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 211, 2))
Namespace.addCategoryObject('elementBinding', atc_codes.name().localName(), atc_codes)

ahfs_codes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ahfs-codes'), CTD_ANON_21, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 220, 2))
Namespace.addCategoryObject('elementBinding', ahfs_codes.name().localName(), ahfs_codes)

patent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'patent'), CTD_ANON_22, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 229, 2))
Namespace.addCategoryObject('elementBinding', patent.name().localName(), patent)

patents = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'patents'), CTD_ANON_23, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 239, 2))
Namespace.addCategoryObject('elementBinding', patents.name().localName(), patents)

food_interactions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'food-interactions'), CTD_ANON_24, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 248, 2))
Namespace.addCategoryObject('elementBinding', food_interactions.name().localName(), food_interactions)

drug_interaction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug-interaction'), CTD_ANON_25, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 257, 2))
Namespace.addCategoryObject('elementBinding', drug_interaction.name().localName(), drug_interaction)

drug_interactions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug-interactions'), CTD_ANON_26, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 266, 2))
Namespace.addCategoryObject('elementBinding', drug_interactions.name().localName(), drug_interactions)

protein_sequences = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein-sequences'), CTD_ANON_27, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 275, 2))
Namespace.addCategoryObject('elementBinding', protein_sequences.name().localName(), protein_sequences)

external_link = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-link'), CTD_ANON_28, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 284, 2))
Namespace.addCategoryObject('elementBinding', external_link.name().localName(), external_link)

external_links = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-links'), CTD_ANON_29, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 292, 2))
Namespace.addCategoryObject('elementBinding', external_links.name().localName(), external_links)

targets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targets'), CTD_ANON_30, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 301, 2))
Namespace.addCategoryObject('elementBinding', targets.name().localName(), targets)

enzymes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enzymes'), CTD_ANON_31, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 310, 2))
Namespace.addCategoryObject('elementBinding', enzymes.name().localName(), enzymes)

transporters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transporters'), CTD_ANON_32, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 319, 2))
Namespace.addCategoryObject('elementBinding', transporters.name().localName(), transporters)

carriers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'carriers'), CTD_ANON_33, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 328, 2))
Namespace.addCategoryObject('elementBinding', carriers.name().localName(), carriers)

pfam = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pfam'), CTD_ANON_34, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 337, 2))
Namespace.addCategoryObject('elementBinding', pfam.name().localName(), pfam)

pfams = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pfams'), CTD_ANON_35, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 345, 2))
Namespace.addCategoryObject('elementBinding', pfams.name().localName(), pfams)

go_classifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'go-classifier'), CTD_ANON_36, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 354, 2))
Namespace.addCategoryObject('elementBinding', go_classifier.name().localName(), go_classifier)

go_classifiers = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'go-classifiers'), CTD_ANON_37, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 362, 2))
Namespace.addCategoryObject('elementBinding', go_classifiers.name().localName(), go_classifiers)

essentiality = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'essentiality'), STD_ANON_, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 371, 2))
Namespace.addCategoryObject('elementBinding', essentiality.name().localName(), essentiality)

species = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'species'), CTD_ANON_38, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 381, 2))
Namespace.addCategoryObject('elementBinding', species.name().localName(), species)

drugs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drugs'), CTD_ANON_40, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 590, 2))
Namespace.addCategoryObject('elementBinding', drugs.name().localName(), drugs)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-number'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 27, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 26, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-number')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 27, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'group'), STD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 36, 8)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 35, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'group')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 36, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'substructure'), CTD_ANON_2, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 52, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'substructure')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 64, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_2()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'substructures'), CTD_ANON_3, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 61, 2)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'kingdom'), pyxb.binding.datatypes.string, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 71, 8)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'kingdom')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 71, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'substructures')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 72, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_3()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'brand'), pyxb.binding.datatypes.string, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 81, 8)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 80, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'brand')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 81, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_4()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'salt'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 90, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 89, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'salt')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 90, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_5()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 99, 8)))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ingredients'), pyxb.binding.datatypes.string, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 100, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 99, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ingredients')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 100, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_6()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mixture'), CTD_ANON_7, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 96, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 106, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mixture')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 107, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_7()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 116, 8)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 117, 8)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 116, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 117, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_8()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'packager'), CTD_ANON_9, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 113, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 123, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'packager')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 124, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_9()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'manufacturer'), CTD_ANON_11, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 130, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 141, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'manufacturer')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 142, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_10()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cost'), CTD_ANON_13, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 148, 2)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 160, 8)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unit'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 162, 8)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 160, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cost')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 161, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unit')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 162, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_11()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'price'), CTD_ANON_14, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 157, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 168, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'price')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 169, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_12()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), pyxb.binding.datatypes.string, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 178, 8)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 177, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 178, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_13()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affected-organism'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 187, 8)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 186, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'affected-organism')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 187, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_14()




CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'form'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 196, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'route'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 197, 8)))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strength'), pyxb.binding.datatypes.string, scope=CTD_ANON_18, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 198, 8)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'form')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 196, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'route')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 197, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strength')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 198, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_15()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dosage'), CTD_ANON_18, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 193, 2)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 204, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dosage')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 205, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_16()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'atc-code'), pyxb.binding.datatypes.string, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 214, 8)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 213, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'atc-code')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 214, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_17()




CTD_ANON_21._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ahfs-code'), pyxb.binding.datatypes.string, scope=CTD_ANON_21, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 223, 8)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 222, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_21._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ahfs-code')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 223, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_18()




CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'number'), pyxb.binding.datatypes.string, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 232, 8)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), pyxb.binding.datatypes.string, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 233, 8)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'approved'), pyxb.binding.datatypes.string, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 234, 8)))

CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'expires'), pyxb.binding.datatypes.string, scope=CTD_ANON_22, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 235, 8)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'number')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 232, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 233, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'approved')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 234, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'expires')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 235, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_19()




CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'patent'), CTD_ANON_22, scope=CTD_ANON_23, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 229, 2)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 241, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'patent')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 242, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_20()




CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'food-interaction'), pyxb.binding.datatypes.string, scope=CTD_ANON_24, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 251, 8)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 251, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'food-interaction')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 251, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_21()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 260, 8)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 261, 8)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 262, 8)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'drug')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 260, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 261, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 262, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_22()




CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug-interaction'), CTD_ANON_25, scope=CTD_ANON_26, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 257, 2)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 268, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'drug-interaction')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 269, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_23()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence'), SequenceType, scope=CTD_ANON_27, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 278, 8)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 277, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 278, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_24()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 287, 8)))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'url'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 288, 8)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 287, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'url')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 288, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_25()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-link'), CTD_ANON_28, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 284, 2)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 294, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'external-link')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 295, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_26()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target'), TargetBondType, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 304, 8)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 304, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'target')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 304, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_27()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enzyme'), BondType, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 313, 8)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 313, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enzyme')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 313, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_28()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transporter'), BondType, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 322, 8)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 322, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transporter')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 322, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_29()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'carrier'), BondType, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 331, 8)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 331, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'carrier')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 331, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_30()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'identifier'), pyxb.binding.datatypes.string, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 340, 8)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 341, 8)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'identifier')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 340, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 341, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_31()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pfam'), CTD_ANON_34, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 337, 2)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 347, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pfam')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 348, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_32()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), pyxb.binding.datatypes.string, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 357, 8)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 358, 8)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 357, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 358, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_33()




CTD_ANON_37._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'go-classifier'), CTD_ANON_36, scope=CTD_ANON_37, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 354, 2)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 364, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_37._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'go-classifier')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 365, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_34()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'category'), STD_ANON_2, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 384, 8)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 395, 8)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uniprot-name'), pyxb.binding.datatypes.string, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 396, 8)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uniprot-taxon-id'), pyxb.binding.datatypes.string, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 397, 8)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 383, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'category')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 384, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 395, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uniprot-name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 396, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'uniprot-taxon-id')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 397, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_35()




SequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'header'), pyxb.binding.datatypes.string, scope=SequenceType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 406, 6)))

SequenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chain'), pyxb.binding.datatypes.string, scope=SequenceType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 407, 6)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SequenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'header')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 406, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SequenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chain')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 407, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SequenceType._Automaton = _BuildAutomaton_36()




PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'kind'), STD_ANON_3, scope=PropertyType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 412, 6)))

PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), pyxb.binding.datatypes.string, scope=PropertyType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 439, 6)))

PropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), STD_ANON_4, scope=PropertyType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 440, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'kind')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 412, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 439, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 440, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PropertyType._Automaton = _BuildAutomaton_37()




PropertiesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'property'), PropertyType, scope=PropertiesType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 453, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 453, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertiesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'property')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 453, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PropertiesType._Automaton = _BuildAutomaton_38()




SynonymsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synonym'), pyxb.binding.datatypes.string, scope=SynonymsType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 458, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 457, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SynonymsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synonym')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 458, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SynonymsType._Automaton = _BuildAutomaton_39()




IdentifiersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-identifier'), CTD_ANON_39, scope=IdentifiersType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 463, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 462, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IdentifiersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'external-identifier')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 463, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IdentifiersType._Automaton = _BuildAutomaton_40()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), pyxb.binding.datatypes.string, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 466, 12)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'identifier'), pyxb.binding.datatypes.string, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 467, 12)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 466, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'identifier')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 467, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_41()




BondActionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'action'), pyxb.binding.datatypes.string, scope=BondActionsType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 475, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 474, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BondActionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'action')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 475, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BondActionsType._Automaton = _BuildAutomaton_42()




BondType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'actions'), BondActionsType, scope=BondType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 480, 6)))

BondType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'references'), pyxb.binding.datatypes.string, scope=BondType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 481, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BondType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'actions')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 480, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BondType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'references')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 481, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BondType._Automaton = _BuildAutomaton_43()




PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pfams'), CTD_ANON_35, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 345, 2)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'go-classifiers'), CTD_ANON_37, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 362, 2)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'essentiality'), STD_ANON_, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 371, 2)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'species'), CTD_ANON_38, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 381, 2)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 506, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'general-function'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 507, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'specific-function'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 508, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gene-name'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 509, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locus'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 510, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reaction'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 511, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'signals'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 512, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cellular-location'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 513, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transmembrane-regions'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 514, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'theoretical-pi'), DecimalOrEmptyType, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 515, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'molecular-weight'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 516, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chromosome'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 517, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'references'), pyxb.binding.datatypes.string, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 520, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers'), IdentifiersType, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 521, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synonyms'), SynonymsType, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 522, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence'), SequenceType, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 523, 6)))

PartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gene-sequence'), SequenceType, scope=PartnerType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 524, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 523, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 524, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 506, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'general-function')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 507, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'specific-function')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 508, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gene-name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 509, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locus')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 510, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reaction')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 511, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'signals')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 512, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cellular-location')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 513, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transmembrane-regions')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 514, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'theoretical-pi')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 515, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'molecular-weight')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 516, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chromosome')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 517, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'species')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 518, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'essentiality')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 519, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'references')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 520, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 521, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synonyms')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 522, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protein-sequence')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 523, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gene-sequence')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 524, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pfams')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 525, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'go-classifiers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 526, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    st_20._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PartnerType._Automaton = _BuildAutomaton_44()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug'), DrugType, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 593, 8)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'partners'), CTD_ANON_41, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 594, 8)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 593, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'drug')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 593, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'partners')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 594, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_45()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'partner'), PartnerType, scope=CTD_ANON_41, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 597, 14)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 597, 14))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'partner')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 597, 14))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_46()




TargetBondType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'known-action'), STD_ANON_5, scope=TargetBondType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 490, 10)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TargetBondType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'actions')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 480, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TargetBondType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'references')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 481, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TargetBondType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'known-action')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 490, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TargetBondType._Automaton = _BuildAutomaton_47()




DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-numbers'), CTD_ANON, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 24, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'groups'), CTD_ANON_, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 33, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxonomy'), CTD_ANON_4, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 68, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'brands'), CTD_ANON_5, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 78, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'salts'), CTD_ANON_6, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 87, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mixtures'), CTD_ANON_8, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 104, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'packagers'), CTD_ANON_10, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 121, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'manufacturers'), CTD_ANON_12, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 139, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prices'), CTD_ANON_15, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 166, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'categories'), CTD_ANON_16, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 175, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'affected-organisms'), CTD_ANON_17, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 184, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dosages'), CTD_ANON_19, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 202, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'atc-codes'), CTD_ANON_20, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 211, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ahfs-codes'), CTD_ANON_21, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 220, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'patents'), CTD_ANON_23, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 239, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'food-interactions'), CTD_ANON_24, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 248, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drug-interactions'), CTD_ANON_26, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 266, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein-sequences'), CTD_ANON_27, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 275, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-links'), CTD_ANON_29, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 292, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targets'), CTD_ANON_30, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 301, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'enzymes'), CTD_ANON_31, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 310, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transporters'), CTD_ANON_32, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 319, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'carriers'), CTD_ANON_33, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 328, 2)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'drugbank-id'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 532, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 533, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 534, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cas-number'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 535, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'general-references'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 536, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synthesis-reference'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 537, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'indication'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 538, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pharmacology'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 539, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mechanism-of-action'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 540, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'toxicity'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 541, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biotransformation'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 542, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absorption'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 543, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'half-life'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 544, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein-binding'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 545, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'route-of-elimination'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 546, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'volume-of-distribution'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 547, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clearance'), pyxb.binding.datatypes.string, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 548, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'synonyms'), SynonymsType, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 552, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'calculated-properties'), PropertiesType, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 568, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'experimental-properties'), PropertiesType, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 569, 6)))

DrugType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers'), IdentifiersType, scope=DrugType, location=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 570, 6)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 567, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 568, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'drugbank-id')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 532, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 533, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 534, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cas-number')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 535, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'general-references')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 536, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synthesis-reference')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 537, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'indication')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 538, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pharmacology')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 539, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mechanism-of-action')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 540, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'toxicity')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 541, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biotransformation')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 542, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absorption')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 543, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'half-life')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 544, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protein-binding')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 545, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'route-of-elimination')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 546, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'volume-of-distribution')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 547, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clearance')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 548, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secondary-accession-numbers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 549, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'groups')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 550, 6))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxonomy')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 551, 6))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'synonyms')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 552, 6))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'salts')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 553, 6))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'brands')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 554, 6))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mixtures')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 555, 6))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'packagers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 556, 6))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'manufacturers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 557, 6))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prices')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 558, 6))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'categories')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 559, 6))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'affected-organisms')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 560, 6))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dosages')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 561, 6))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'atc-codes')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 562, 6))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ahfs-codes')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 563, 6))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'patents')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 564, 6))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'food-interactions')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 565, 6))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'drug-interactions')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 566, 6))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protein-sequences')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 567, 6))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'calculated-properties')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 568, 6))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'experimental-properties')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 569, 6))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'external-identifiers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 570, 6))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'external-links')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 571, 6))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targets')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 572, 6))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'enzymes')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 573, 6))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transporters')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 574, 6))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DrugType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'carriers')), pyxb.utils.utility.Location('http://v3.drugbank.ca/docs/drugbank.xsd', 575, 6))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
         ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
         ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
         ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
         ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
         ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
         ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
         ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
         ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
         ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
         ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
         ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
         ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
         ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
         ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
         ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
         ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
         ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
         ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    st_43._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DrugType._Automaton = _BuildAutomaton_48()

