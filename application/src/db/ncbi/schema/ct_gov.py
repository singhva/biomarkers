# ./ncbi/ct_gov.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2014-04-21 10:08:41.532668 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import io
import sys

import pyxb
import pyxb.binding
import pyxb.binding.datatypes
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.utility


# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7116f0de-c95e-11e3-b469-14109fd9e1c1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# Complex type required_header_struct with content type ELEMENT_ONLY
class required_header_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type required_header_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'required_header_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element download_date uses Python identifier download_date
    __download_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'download_date'), 'download_date', '__AbsentNamespace0_required_header_struct_download_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 115, 6), )

    
    download_date = property(__download_date.value, __download_date.set, None, None)

    
    # Element link_text uses Python identifier link_text
    __link_text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link_text'), 'link_text', '__AbsentNamespace0_required_header_struct_link_text', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 116, 6), )

    
    link_text = property(__link_text.value, __link_text.set, None, None)

    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'url'), 'url', '__AbsentNamespace0_required_header_struct_url', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 117, 6), )

    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        __download_date.name() : __download_date,
        __link_text.name() : __link_text,
        __url.name() : __url
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'required_header_struct', required_header_struct)


# Complex type id_info_struct with content type ELEMENT_ONLY
class id_info_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type id_info_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'id_info_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 123, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element org_study_id uses Python identifier org_study_id
    __org_study_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'org_study_id'), 'org_study_id', '__AbsentNamespace0_id_info_struct_org_study_id', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 125, 6), )

    
    org_study_id = property(__org_study_id.value, __org_study_id.set, None, None)

    
    # Element secondary_id uses Python identifier secondary_id
    __secondary_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'secondary_id'), 'secondary_id', '__AbsentNamespace0_id_info_struct_secondary_id', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 126, 6), )

    
    secondary_id = property(__secondary_id.value, __secondary_id.set, None, None)

    
    # Element nct_id uses Python identifier nct_id
    __nct_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'nct_id'), 'nct_id', '__AbsentNamespace0_id_info_struct_nct_id', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 127, 6), )

    
    nct_id = property(__nct_id.value, __nct_id.set, None, None)

    
    # Element nct_alias uses Python identifier nct_alias
    __nct_alias = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'nct_alias'), 'nct_alias', '__AbsentNamespace0_id_info_struct_nct_alias', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 128, 6), )

    
    nct_alias = property(__nct_alias.value, __nct_alias.set, None, None)

    _ElementMap.update({
        __org_study_id.name() : __org_study_id,
        __secondary_id.name() : __secondary_id,
        __nct_id.name() : __nct_id,
        __nct_alias.name() : __nct_alias
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'id_info_struct', id_info_struct)


# Complex type sponsor_struct with content type ELEMENT_ONLY
class sponsor_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type sponsor_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sponsor_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 134, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element agency uses Python identifier agency
    __agency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'agency'), 'agency', '__AbsentNamespace0_sponsor_struct_agency', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 136, 6), )

    
    agency = property(__agency.value, __agency.set, None, None)

    
    # Element agency_class uses Python identifier agency_class
    __agency_class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'agency_class'), 'agency_class', '__AbsentNamespace0_sponsor_struct_agency_class', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 137, 6), )

    
    agency_class = property(__agency_class.value, __agency_class.set, None, None)

    _ElementMap.update({
        __agency.name() : __agency,
        __agency_class.name() : __agency_class
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sponsor_struct', sponsor_struct)


# Complex type sponsors_struct with content type ELEMENT_ONLY
class sponsors_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type sponsors_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sponsors_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 143, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lead_sponsor uses Python identifier lead_sponsor
    __lead_sponsor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'lead_sponsor'), 'lead_sponsor', '__AbsentNamespace0_sponsors_struct_lead_sponsor', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 145, 6), )

    
    lead_sponsor = property(__lead_sponsor.value, __lead_sponsor.set, None, None)

    
    # Element collaborator uses Python identifier collaborator
    __collaborator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'collaborator'), 'collaborator', '__AbsentNamespace0_sponsors_struct_collaborator', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 146, 6), )

    
    collaborator = property(__collaborator.value, __collaborator.set, None, None)

    _ElementMap.update({
        __lead_sponsor.name() : __lead_sponsor,
        __collaborator.name() : __collaborator
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sponsors_struct', sponsors_struct)


# Complex type oversight_info_struct with content type ELEMENT_ONLY
class oversight_info_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type oversight_info_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'oversight_info_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 152, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element authority uses Python identifier authority
    __authority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'authority'), 'authority', '__AbsentNamespace0_oversight_info_struct_authority', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 154, 6), )

    
    authority = property(__authority.value, __authority.set, None, None)

    
    # Element has_dmc uses Python identifier has_dmc
    __has_dmc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'has_dmc'), 'has_dmc', '__AbsentNamespace0_oversight_info_struct_has_dmc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 155, 6), )

    
    has_dmc = property(__has_dmc.value, __has_dmc.set, None, None)

    _ElementMap.update({
        __authority.name() : __authority,
        __has_dmc.name() : __has_dmc
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'oversight_info_struct', oversight_info_struct)


# Complex type protocol_outcome_struct with content type ELEMENT_ONLY
class protocol_outcome_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type protocol_outcome_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'protocol_outcome_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 161, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measure'), 'measure', '__AbsentNamespace0_protocol_outcome_struct_measure', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 163, 6), )

    
    measure = property(__measure.value, __measure.set, None, None)

    
    # Element time_frame uses Python identifier time_frame
    __time_frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'time_frame'), 'time_frame', '__AbsentNamespace0_protocol_outcome_struct_time_frame', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 164, 6), )

    
    time_frame = property(__time_frame.value, __time_frame.set, None, None)

    
    # Element safety_issue uses Python identifier safety_issue
    __safety_issue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'safety_issue'), 'safety_issue', '__AbsentNamespace0_protocol_outcome_struct_safety_issue', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 165, 6), )

    
    safety_issue = property(__safety_issue.value, __safety_issue.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_protocol_outcome_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 166, 6), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __measure.name() : __measure,
        __time_frame.name() : __time_frame,
        __safety_issue.name() : __safety_issue,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'protocol_outcome_struct', protocol_outcome_struct)


# Complex type enrollment_struct with content type MIXED
class enrollment_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type enrollment_struct with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'enrollment_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 172, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_enrollment_struct_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 173, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 173, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'enrollment_struct', enrollment_struct)


# Complex type arm_group_struct with content type ELEMENT_ONLY
class arm_group_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type arm_group_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arm_group_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 178, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element arm_group_label uses Python identifier arm_group_label
    __arm_group_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'arm_group_label'), 'arm_group_label', '__AbsentNamespace0_arm_group_struct_arm_group_label', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 180, 6), )

    
    arm_group_label = property(__arm_group_label.value, __arm_group_label.set, None, None)

    
    # Element arm_group_type uses Python identifier arm_group_type
    __arm_group_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'arm_group_type'), 'arm_group_type', '__AbsentNamespace0_arm_group_struct_arm_group_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 181, 6), )

    
    arm_group_type = property(__arm_group_type.value, __arm_group_type.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_arm_group_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 182, 6), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __arm_group_label.name() : __arm_group_label,
        __arm_group_type.name() : __arm_group_type,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'arm_group_struct', arm_group_struct)


# Complex type intervention_struct with content type ELEMENT_ONLY
class intervention_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type intervention_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'intervention_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 188, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element intervention_type uses Python identifier intervention_type
    __intervention_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'intervention_type'), 'intervention_type', '__AbsentNamespace0_intervention_struct_intervention_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 190, 6), )

    
    intervention_type = property(__intervention_type.value, __intervention_type.set, None, None)

    
    # Element intervention_name uses Python identifier intervention_name
    __intervention_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'intervention_name'), 'intervention_name', '__AbsentNamespace0_intervention_struct_intervention_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 191, 6), )

    
    intervention_name = property(__intervention_name.value, __intervention_name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_intervention_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 192, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element arm_group_label uses Python identifier arm_group_label
    __arm_group_label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'arm_group_label'), 'arm_group_label', '__AbsentNamespace0_intervention_struct_arm_group_label', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 193, 6), )

    
    arm_group_label = property(__arm_group_label.value, __arm_group_label.set, None, None)

    
    # Element other_name uses Python identifier other_name
    __other_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'other_name'), 'other_name', '__AbsentNamespace0_intervention_struct_other_name', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 194, 6), )

    
    other_name = property(__other_name.value, __other_name.set, None, None)

    _ElementMap.update({
        __intervention_type.name() : __intervention_type,
        __intervention_name.name() : __intervention_name,
        __description.name() : __description,
        __arm_group_label.name() : __arm_group_label,
        __other_name.name() : __other_name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'intervention_struct', intervention_struct)


# Complex type textblock_struct with content type ELEMENT_ONLY
class textblock_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type textblock_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'textblock_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element textblock uses Python identifier textblock
    __textblock = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'textblock'), 'textblock', '__AbsentNamespace0_textblock_struct_textblock', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 202, 6), )

    
    textblock = property(__textblock.value, __textblock.set, None, None)

    _ElementMap.update({
        __textblock.name() : __textblock
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'textblock_struct', textblock_struct)


# Complex type eligibility_struct with content type ELEMENT_ONLY
class eligibility_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type eligibility_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'eligibility_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 208, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element study_pop uses Python identifier study_pop
    __study_pop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'study_pop'), 'study_pop', '__AbsentNamespace0_eligibility_struct_study_pop', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 210, 6), )

    
    study_pop = property(__study_pop.value, __study_pop.set, None, None)

    
    # Element sampling_method uses Python identifier sampling_method
    __sampling_method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sampling_method'), 'sampling_method', '__AbsentNamespace0_eligibility_struct_sampling_method', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 211, 6), )

    
    sampling_method = property(__sampling_method.value, __sampling_method.set, None, None)

    
    # Element criteria uses Python identifier criteria
    __criteria = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'criteria'), 'criteria', '__AbsentNamespace0_eligibility_struct_criteria', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 212, 6), )

    
    criteria = property(__criteria.value, __criteria.set, None, None)

    
    # Element gender uses Python identifier gender
    __gender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'gender'), 'gender', '__AbsentNamespace0_eligibility_struct_gender', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 213, 6), )

    
    gender = property(__gender.value, __gender.set, None, None)

    
    # Element minimum_age uses Python identifier minimum_age
    __minimum_age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'minimum_age'), 'minimum_age', '__AbsentNamespace0_eligibility_struct_minimum_age', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 214, 6), )

    
    minimum_age = property(__minimum_age.value, __minimum_age.set, None, None)

    
    # Element maximum_age uses Python identifier maximum_age
    __maximum_age = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'maximum_age'), 'maximum_age', '__AbsentNamespace0_eligibility_struct_maximum_age', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 215, 6), )

    
    maximum_age = property(__maximum_age.value, __maximum_age.set, None, None)

    
    # Element healthy_volunteers uses Python identifier healthy_volunteers
    __healthy_volunteers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'healthy_volunteers'), 'healthy_volunteers', '__AbsentNamespace0_eligibility_struct_healthy_volunteers', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 216, 6), )

    
    healthy_volunteers = property(__healthy_volunteers.value, __healthy_volunteers.set, None, None)

    _ElementMap.update({
        __study_pop.name() : __study_pop,
        __sampling_method.name() : __sampling_method,
        __criteria.name() : __criteria,
        __gender.name() : __gender,
        __minimum_age.name() : __minimum_age,
        __maximum_age.name() : __maximum_age,
        __healthy_volunteers.name() : __healthy_volunteers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'eligibility_struct', eligibility_struct)


# Complex type contact_struct with content type ELEMENT_ONLY
class contact_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type contact_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contact_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 222, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element first_name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'first_name'), 'first_name', '__AbsentNamespace0_contact_struct_first_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 224, 6), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element middle_name uses Python identifier middle_name
    __middle_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'middle_name'), 'middle_name', '__AbsentNamespace0_contact_struct_middle_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 225, 6), )

    
    middle_name = property(__middle_name.value, __middle_name.set, None, None)

    
    # Element last_name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last_name'), 'last_name', '__AbsentNamespace0_contact_struct_last_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 226, 6), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element degrees uses Python identifier degrees
    __degrees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'degrees'), 'degrees', '__AbsentNamespace0_contact_struct_degrees', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 227, 6), )

    
    degrees = property(__degrees.value, __degrees.set, None, None)

    
    # Element phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'phone'), 'phone', '__AbsentNamespace0_contact_struct_phone', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 228, 6), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element phone_ext uses Python identifier phone_ext
    __phone_ext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'phone_ext'), 'phone_ext', '__AbsentNamespace0_contact_struct_phone_ext', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 229, 6), )

    
    phone_ext = property(__phone_ext.value, __phone_ext.set, None, None)

    
    # Element email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'email'), 'email', '__AbsentNamespace0_contact_struct_email', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 230, 6), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __first_name.name() : __first_name,
        __middle_name.name() : __middle_name,
        __last_name.name() : __last_name,
        __degrees.name() : __degrees,
        __phone.name() : __phone,
        __phone_ext.name() : __phone_ext,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'contact_struct', contact_struct)


# Complex type investigator_struct with content type ELEMENT_ONLY
class investigator_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type investigator_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'investigator_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 236, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element first_name uses Python identifier first_name
    __first_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'first_name'), 'first_name', '__AbsentNamespace0_investigator_struct_first_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 238, 6), )

    
    first_name = property(__first_name.value, __first_name.set, None, None)

    
    # Element middle_name uses Python identifier middle_name
    __middle_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'middle_name'), 'middle_name', '__AbsentNamespace0_investigator_struct_middle_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 239, 6), )

    
    middle_name = property(__middle_name.value, __middle_name.set, None, None)

    
    # Element last_name uses Python identifier last_name
    __last_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'last_name'), 'last_name', '__AbsentNamespace0_investigator_struct_last_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 240, 6), )

    
    last_name = property(__last_name.value, __last_name.set, None, None)

    
    # Element degrees uses Python identifier degrees
    __degrees = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'degrees'), 'degrees', '__AbsentNamespace0_investigator_struct_degrees', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 241, 6), )

    
    degrees = property(__degrees.value, __degrees.set, None, None)

    
    # Element role uses Python identifier role
    __role = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'role'), 'role', '__AbsentNamespace0_investigator_struct_role', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 242, 6), )

    
    role = property(__role.value, __role.set, None, None)

    
    # Element affiliation uses Python identifier affiliation
    __affiliation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'affiliation'), 'affiliation', '__AbsentNamespace0_investigator_struct_affiliation', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 243, 6), )

    
    affiliation = property(__affiliation.value, __affiliation.set, None, None)

    _ElementMap.update({
        __first_name.name() : __first_name,
        __middle_name.name() : __middle_name,
        __last_name.name() : __last_name,
        __degrees.name() : __degrees,
        __role.name() : __role,
        __affiliation.name() : __affiliation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'investigator_struct', investigator_struct)


# Complex type address_struct with content type ELEMENT_ONLY
class address_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type address_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'address_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 249, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'city'), 'city', '__AbsentNamespace0_address_struct_city', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 251, 6), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element state uses Python identifier state
    __state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'state'), 'state', '__AbsentNamespace0_address_struct_state', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 252, 6), )

    
    state = property(__state.value, __state.set, None, None)

    
    # Element zip uses Python identifier zip
    __zip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'zip'), 'zip', '__AbsentNamespace0_address_struct_zip', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 253, 6), )

    
    zip = property(__zip.value, __zip.set, None, None)

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__AbsentNamespace0_address_struct_country', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 254, 6), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __city.name() : __city,
        __state.name() : __state,
        __zip.name() : __zip,
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'address_struct', address_struct)


# Complex type facility_struct with content type ELEMENT_ONLY
class facility_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type facility_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'facility_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 260, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_facility_struct_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 262, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'address'), 'address', '__AbsentNamespace0_facility_struct_address', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 263, 6), )

    
    address = property(__address.value, __address.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __address.name() : __address
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'facility_struct', facility_struct)


# Complex type location_struct with content type ELEMENT_ONLY
class location_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type location_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'location_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 269, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element facility uses Python identifier facility
    __facility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'facility'), 'facility', '__AbsentNamespace0_location_struct_facility', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 271, 6), )

    
    facility = property(__facility.value, __facility.set, None, None)

    
    # Element status uses Python identifier status
    __status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__AbsentNamespace0_location_struct_status', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 272, 6), )

    
    status = property(__status.value, __status.set, None, None)

    
    # Element contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'contact'), 'contact', '__AbsentNamespace0_location_struct_contact', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 273, 6), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element contact_backup uses Python identifier contact_backup
    __contact_backup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'contact_backup'), 'contact_backup', '__AbsentNamespace0_location_struct_contact_backup', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 274, 6), )

    
    contact_backup = property(__contact_backup.value, __contact_backup.set, None, None)

    
    # Element investigator uses Python identifier investigator
    __investigator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'investigator'), 'investigator', '__AbsentNamespace0_location_struct_investigator', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 275, 6), )

    
    investigator = property(__investigator.value, __investigator.set, None, None)

    _ElementMap.update({
        __facility.name() : __facility,
        __status.name() : __status,
        __contact.name() : __contact,
        __contact_backup.name() : __contact_backup,
        __investigator.name() : __investigator
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'location_struct', location_struct)


# Complex type countries_struct with content type ELEMENT_ONLY
class countries_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type countries_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'countries_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 281, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__AbsentNamespace0_countries_struct_country', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 283, 6), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'countries_struct', countries_struct)


# Complex type link_struct with content type ELEMENT_ONLY
class link_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type link_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'link_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 289, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element url uses Python identifier url
    __url = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'url'), 'url', '__AbsentNamespace0_link_struct_url', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 291, 6), )

    
    url = property(__url.value, __url.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_link_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 292, 6), )

    
    description = property(__description.value, __description.set, None, None)

    _ElementMap.update({
        __url.name() : __url,
        __description.name() : __description
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'link_struct', link_struct)


# Complex type reference_struct with content type ELEMENT_ONLY
class reference_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type reference_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reference_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 298, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'citation'), 'citation', '__AbsentNamespace0_reference_struct_citation', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 300, 6), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element PMID uses Python identifier PMID
    __PMID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'PMID'), 'PMID', '__AbsentNamespace0_reference_struct_PMID', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 301, 6), )

    
    PMID = property(__PMID.value, __PMID.set, None, None)

    _ElementMap.update({
        __citation.name() : __citation,
        __PMID.name() : __PMID
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'reference_struct', reference_struct)


# Complex type responsible_party_struct with content type ELEMENT_ONLY
class responsible_party_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type responsible_party_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'responsible_party_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 307, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name_title uses Python identifier name_title
    __name_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name_title'), 'name_title', '__AbsentNamespace0_responsible_party_struct_name_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 309, 6), )

    
    name_title = property(__name_title.value, __name_title.set, None, None)

    
    # Element organization uses Python identifier organization
    __organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'organization'), 'organization', '__AbsentNamespace0_responsible_party_struct_organization', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 310, 6), )

    
    organization = property(__organization.value, __organization.set, None, None)

    
    # Element responsible_party_type uses Python identifier responsible_party_type
    __responsible_party_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'responsible_party_type'), 'responsible_party_type', '__AbsentNamespace0_responsible_party_struct_responsible_party_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 311, 6), )

    
    responsible_party_type = property(__responsible_party_type.value, __responsible_party_type.set, None, None)

    
    # Element investigator_affiliation uses Python identifier investigator_affiliation
    __investigator_affiliation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'investigator_affiliation'), 'investigator_affiliation', '__AbsentNamespace0_responsible_party_struct_investigator_affiliation', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 312, 6), )

    
    investigator_affiliation = property(__investigator_affiliation.value, __investigator_affiliation.set, None, None)

    
    # Element investigator_full_name uses Python identifier investigator_full_name
    __investigator_full_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'investigator_full_name'), 'investigator_full_name', '__AbsentNamespace0_responsible_party_struct_investigator_full_name', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 313, 6), )

    
    investigator_full_name = property(__investigator_full_name.value, __investigator_full_name.set, None, None)

    
    # Element investigator_title uses Python identifier investigator_title
    __investigator_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'investigator_title'), 'investigator_title', '__AbsentNamespace0_responsible_party_struct_investigator_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 314, 6), )

    
    investigator_title = property(__investigator_title.value, __investigator_title.set, None, None)

    _ElementMap.update({
        __name_title.name() : __name_title,
        __organization.name() : __organization,
        __responsible_party_type.name() : __responsible_party_type,
        __investigator_affiliation.name() : __investigator_affiliation,
        __investigator_full_name.name() : __investigator_full_name,
        __investigator_title.name() : __investigator_title
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'responsible_party_struct', responsible_party_struct)


# Complex type browse_struct with content type ELEMENT_ONLY
class browse_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type browse_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'browse_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 320, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mesh_term uses Python identifier mesh_term
    __mesh_term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'mesh_term'), 'mesh_term', '__AbsentNamespace0_browse_struct_mesh_term', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 322, 6), )

    
    mesh_term = property(__mesh_term.value, __mesh_term.set, None, None)

    _ElementMap.update({
        __mesh_term.name() : __mesh_term
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'browse_struct', browse_struct)


# Complex type group_struct with content type ELEMENT_ONLY
class group_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type group_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'group_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 328, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_group_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 330, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_group_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 331, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute group_id uses Python identifier group_id
    __group_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group_id'), 'group_id', '__AbsentNamespace0_group_struct_group_id', pyxb.binding.datatypes.string, required=True)
    __group_id._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 333, 4)
    __group_id._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 333, 4)
    
    group_id = property(__group_id.value, __group_id.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description
    })
    _AttributeMap.update({
        __group_id.name() : __group_id
    })
Namespace.addCategoryObject('typeBinding', u'group_struct', group_struct)


# Complex type participants_struct with content type SIMPLE
class participants_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type participants_struct with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'participants_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 338, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute group_id uses Python identifier group_id
    __group_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group_id'), 'group_id', '__AbsentNamespace0_participants_struct_group_id', pyxb.binding.datatypes.string, required=True)
    __group_id._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 341, 8)
    __group_id._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 341, 8)
    
    group_id = property(__group_id.value, __group_id.set, None, None)

    
    # Attribute count uses Python identifier count
    __count = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'count'), 'count', '__AbsentNamespace0_participants_struct_count', pyxb.binding.datatypes.string)
    __count._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 342, 8)
    __count._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 342, 8)
    
    count = property(__count.value, __count.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __group_id.name() : __group_id,
        __count.name() : __count
    })
Namespace.addCategoryObject('typeBinding', u'participants_struct', participants_struct)


# Complex type milestone_struct with content type ELEMENT_ONLY
class milestone_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type milestone_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'milestone_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 349, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_milestone_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 351, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element participants_list uses Python identifier participants_list
    __participants_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'participants_list'), 'participants_list', '__AbsentNamespace0_milestone_struct_participants_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 352, 6), )

    
    participants_list = property(__participants_list.value, __participants_list.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __participants_list.name() : __participants_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'milestone_struct', milestone_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 353, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element participants uses Python identifier participants
    __participants = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'participants'), 'participants', '__AbsentNamespace0_CTD_ANON_participants', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 355, 12), )

    
    participants = property(__participants.value, __participants.set, None, None)

    _ElementMap.update({
        __participants.name() : __participants
    })
    _AttributeMap.update({
        
    })



# Complex type period_struct with content type ELEMENT_ONLY
class period_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type period_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'period_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 364, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_period_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 366, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element milestone_list uses Python identifier milestone_list
    __milestone_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'milestone_list'), 'milestone_list', '__AbsentNamespace0_period_struct_milestone_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 367, 6), )

    
    milestone_list = property(__milestone_list.value, __milestone_list.set, None, None)

    
    # Element drop_withdraw_reason_list uses Python identifier drop_withdraw_reason_list
    __drop_withdraw_reason_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason_list'), 'drop_withdraw_reason_list', '__AbsentNamespace0_period_struct_drop_withdraw_reason_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 374, 6), )

    
    drop_withdraw_reason_list = property(__drop_withdraw_reason_list.value, __drop_withdraw_reason_list.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __milestone_list.name() : __milestone_list,
        __drop_withdraw_reason_list.name() : __drop_withdraw_reason_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'period_struct', period_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 368, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element milestone uses Python identifier milestone
    __milestone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'milestone'), 'milestone', '__AbsentNamespace0_CTD_ANON__milestone', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 370, 12), )

    
    milestone = property(__milestone.value, __milestone.set, None, None)

    _ElementMap.update({
        __milestone.name() : __milestone
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 375, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element drop_withdraw_reason uses Python identifier drop_withdraw_reason
    __drop_withdraw_reason = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason'), 'drop_withdraw_reason', '__AbsentNamespace0_CTD_ANON_2_drop_withdraw_reason', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 377, 12), )

    
    drop_withdraw_reason = property(__drop_withdraw_reason.value, __drop_withdraw_reason.set, None, None)

    _ElementMap.update({
        __drop_withdraw_reason.name() : __drop_withdraw_reason
    })
    _AttributeMap.update({
        
    })



# Complex type participant_flow_struct with content type ELEMENT_ONLY
class participant_flow_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type participant_flow_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'participant_flow_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 386, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element recruitment_details uses Python identifier recruitment_details
    __recruitment_details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'recruitment_details'), 'recruitment_details', '__AbsentNamespace0_participant_flow_struct_recruitment_details', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 388, 6), )

    
    recruitment_details = property(__recruitment_details.value, __recruitment_details.set, None, None)

    
    # Element pre_assignment_details uses Python identifier pre_assignment_details
    __pre_assignment_details = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pre_assignment_details'), 'pre_assignment_details', '__AbsentNamespace0_participant_flow_struct_pre_assignment_details', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 389, 6), )

    
    pre_assignment_details = property(__pre_assignment_details.value, __pre_assignment_details.set, None, None)

    
    # Element group_list uses Python identifier group_list
    __group_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_list'), 'group_list', '__AbsentNamespace0_participant_flow_struct_group_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 390, 6), )

    
    group_list = property(__group_list.value, __group_list.set, None, None)

    
    # Element period_list uses Python identifier period_list
    __period_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'period_list'), 'period_list', '__AbsentNamespace0_participant_flow_struct_period_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 397, 6), )

    
    period_list = property(__period_list.value, __period_list.set, None, None)

    _ElementMap.update({
        __recruitment_details.name() : __recruitment_details,
        __pre_assignment_details.name() : __pre_assignment_details,
        __group_list.name() : __group_list,
        __period_list.name() : __period_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'participant_flow_struct', participant_flow_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 391, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__AbsentNamespace0_CTD_ANON_3_group', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 393, 12), )

    
    group = property(__group.value, __group.set, None, None)

    _ElementMap.update({
        __group.name() : __group
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
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 398, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element period uses Python identifier period
    __period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'period'), 'period', '__AbsentNamespace0_CTD_ANON_4_period', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 400, 12), )

    
    period = property(__period.value, __period.set, None, None)

    _ElementMap.update({
        __period.name() : __period
    })
    _AttributeMap.update({
        
    })



# Complex type measurement_struct with content type SIMPLE
class measurement_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type measurement_struct with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measurement_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 409, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute group_id uses Python identifier group_id
    __group_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group_id'), 'group_id', '__AbsentNamespace0_measurement_struct_group_id', pyxb.binding.datatypes.string, required=True)
    __group_id._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 412, 8)
    __group_id._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 412, 8)
    
    group_id = property(__group_id.value, __group_id.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__AbsentNamespace0_measurement_struct_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 413, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 413, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute spread uses Python identifier spread
    __spread = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spread'), 'spread', '__AbsentNamespace0_measurement_struct_spread', pyxb.binding.datatypes.string)
    __spread._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 414, 8)
    __spread._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 414, 8)
    
    spread = property(__spread.value, __spread.set, None, None)

    
    # Attribute lower_limit uses Python identifier lower_limit
    __lower_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lower_limit'), 'lower_limit', '__AbsentNamespace0_measurement_struct_lower_limit', pyxb.binding.datatypes.string)
    __lower_limit._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 415, 8)
    __lower_limit._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 415, 8)
    
    lower_limit = property(__lower_limit.value, __lower_limit.set, None, None)

    
    # Attribute upper_limit uses Python identifier upper_limit
    __upper_limit = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'upper_limit'), 'upper_limit', '__AbsentNamespace0_measurement_struct_upper_limit', pyxb.binding.datatypes.string)
    __upper_limit._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 416, 8)
    __upper_limit._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 416, 8)
    
    upper_limit = property(__upper_limit.value, __upper_limit.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __group_id.name() : __group_id,
        __value.name() : __value,
        __spread.name() : __spread,
        __lower_limit.name() : __lower_limit,
        __upper_limit.name() : __upper_limit
    })
Namespace.addCategoryObject('typeBinding', u'measurement_struct', measurement_struct)


# Complex type measure_category_struct with content type ELEMENT_ONLY
class measure_category_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type measure_category_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measure_category_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 423, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sub_title uses Python identifier sub_title
    __sub_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sub_title'), 'sub_title', '__AbsentNamespace0_measure_category_struct_sub_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 425, 6), )

    
    sub_title = property(__sub_title.value, __sub_title.set, None, None)

    
    # Element measurement_list uses Python identifier measurement_list
    __measurement_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measurement_list'), 'measurement_list', '__AbsentNamespace0_measure_category_struct_measurement_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 426, 6), )

    
    measurement_list = property(__measurement_list.value, __measurement_list.set, None, None)

    _ElementMap.update({
        __sub_title.name() : __sub_title,
        __measurement_list.name() : __measurement_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'measure_category_struct', measure_category_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 427, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measurement uses Python identifier measurement
    __measurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measurement'), 'measurement', '__AbsentNamespace0_CTD_ANON_5_measurement', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 429, 12), )

    
    measurement = property(__measurement.value, __measurement.set, None, None)

    _ElementMap.update({
        __measurement.name() : __measurement
    })
    _AttributeMap.update({
        
    })



# Complex type measure_struct with content type ELEMENT_ONLY
class measure_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type measure_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'measure_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 438, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_measure_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 440, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_measure_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 441, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element units uses Python identifier units
    __units = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__AbsentNamespace0_measure_struct_units', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 442, 6), )

    
    units = property(__units.value, __units.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'param'), 'param', '__AbsentNamespace0_measure_struct_param', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 443, 6), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Element dispersion uses Python identifier dispersion
    __dispersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dispersion'), 'dispersion', '__AbsentNamespace0_measure_struct_dispersion', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 444, 6), )

    
    dispersion = property(__dispersion.value, __dispersion.set, None, None)

    
    # Element category_list uses Python identifier category_list
    __category_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'category_list'), 'category_list', '__AbsentNamespace0_measure_struct_category_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 445, 6), )

    
    category_list = property(__category_list.value, __category_list.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __description.name() : __description,
        __units.name() : __units,
        __param.name() : __param,
        __dispersion.name() : __dispersion,
        __category_list.name() : __category_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'measure_struct', measure_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 446, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__AbsentNamespace0_CTD_ANON_6_category', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 448, 12), )

    
    category = property(__category.value, __category.set, None, None)

    _ElementMap.update({
        __category.name() : __category
    })
    _AttributeMap.update({
        
    })



# Complex type baseline_struct with content type ELEMENT_ONLY
class baseline_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type baseline_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseline_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 457, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element population uses Python identifier population
    __population = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'population'), 'population', '__AbsentNamespace0_baseline_struct_population', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 459, 6), )

    
    population = property(__population.value, __population.set, None, None)

    
    # Element group_list uses Python identifier group_list
    __group_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_list'), 'group_list', '__AbsentNamespace0_baseline_struct_group_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 460, 6), )

    
    group_list = property(__group_list.value, __group_list.set, None, None)

    
    # Element measure_list uses Python identifier measure_list
    __measure_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measure_list'), 'measure_list', '__AbsentNamespace0_baseline_struct_measure_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 467, 6), )

    
    measure_list = property(__measure_list.value, __measure_list.set, None, None)

    _ElementMap.update({
        __population.name() : __population,
        __group_list.name() : __group_list,
        __measure_list.name() : __measure_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'baseline_struct', baseline_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 461, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__AbsentNamespace0_CTD_ANON_7_group', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 463, 12), )

    
    group = property(__group.value, __group.set, None, None)

    _ElementMap.update({
        __group.name() : __group
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
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 468, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measure'), 'measure', '__AbsentNamespace0_CTD_ANON_8_measure', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 470, 12), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })



# Complex type analysis_struct with content type ELEMENT_ONLY
class analysis_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type analysis_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'analysis_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 479, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group_id_list uses Python identifier group_id_list
    __group_id_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_id_list'), 'group_id_list', '__AbsentNamespace0_analysis_struct_group_id_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 481, 6), )

    
    group_id_list = property(__group_id_list.value, __group_id_list.set, None, None)

    
    # Element groups_desc uses Python identifier groups_desc
    __groups_desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'groups_desc'), 'groups_desc', '__AbsentNamespace0_analysis_struct_groups_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 488, 6), )

    
    groups_desc = property(__groups_desc.value, __groups_desc.set, None, None)

    
    # Element non_inferiority uses Python identifier non_inferiority
    __non_inferiority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'non_inferiority'), 'non_inferiority', '__AbsentNamespace0_analysis_struct_non_inferiority', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 489, 6), )

    
    non_inferiority = property(__non_inferiority.value, __non_inferiority.set, None, None)

    
    # Element non_inferiority_desc uses Python identifier non_inferiority_desc
    __non_inferiority_desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'non_inferiority_desc'), 'non_inferiority_desc', '__AbsentNamespace0_analysis_struct_non_inferiority_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 490, 6), )

    
    non_inferiority_desc = property(__non_inferiority_desc.value, __non_inferiority_desc.set, None, None)

    
    # Element p_value uses Python identifier p_value
    __p_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'p_value'), 'p_value', '__AbsentNamespace0_analysis_struct_p_value', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 491, 6), )

    
    p_value = property(__p_value.value, __p_value.set, None, None)

    
    # Element p_value_desc uses Python identifier p_value_desc
    __p_value_desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'p_value_desc'), 'p_value_desc', '__AbsentNamespace0_analysis_struct_p_value_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 492, 6), )

    
    p_value_desc = property(__p_value_desc.value, __p_value_desc.set, None, None)

    
    # Element method uses Python identifier method
    __method = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'method'), 'method', '__AbsentNamespace0_analysis_struct_method', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 493, 6), )

    
    method = property(__method.value, __method.set, None, None)

    
    # Element method_desc uses Python identifier method_desc
    __method_desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'method_desc'), 'method_desc', '__AbsentNamespace0_analysis_struct_method_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 494, 6), )

    
    method_desc = property(__method_desc.value, __method_desc.set, None, None)

    
    # Element param_type uses Python identifier param_type
    __param_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'param_type'), 'param_type', '__AbsentNamespace0_analysis_struct_param_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 495, 6), )

    
    param_type = property(__param_type.value, __param_type.set, None, None)

    
    # Element param_value uses Python identifier param_value
    __param_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'param_value'), 'param_value', '__AbsentNamespace0_analysis_struct_param_value', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 496, 6), )

    
    param_value = property(__param_value.value, __param_value.set, None, None)

    
    # Element dispersion_type uses Python identifier dispersion_type
    __dispersion_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dispersion_type'), 'dispersion_type', '__AbsentNamespace0_analysis_struct_dispersion_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 497, 6), )

    
    dispersion_type = property(__dispersion_type.value, __dispersion_type.set, None, None)

    
    # Element dispersion_value uses Python identifier dispersion_value
    __dispersion_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dispersion_value'), 'dispersion_value', '__AbsentNamespace0_analysis_struct_dispersion_value', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 498, 6), )

    
    dispersion_value = property(__dispersion_value.value, __dispersion_value.set, None, None)

    
    # Element ci_percent uses Python identifier ci_percent
    __ci_percent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ci_percent'), 'ci_percent', '__AbsentNamespace0_analysis_struct_ci_percent', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 499, 6), )

    
    ci_percent = property(__ci_percent.value, __ci_percent.set, None, None)

    
    # Element ci_n_sides uses Python identifier ci_n_sides
    __ci_n_sides = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ci_n_sides'), 'ci_n_sides', '__AbsentNamespace0_analysis_struct_ci_n_sides', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 500, 6), )

    
    ci_n_sides = property(__ci_n_sides.value, __ci_n_sides.set, None, None)

    
    # Element ci_lower_limit uses Python identifier ci_lower_limit
    __ci_lower_limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ci_lower_limit'), 'ci_lower_limit', '__AbsentNamespace0_analysis_struct_ci_lower_limit', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 501, 6), )

    
    ci_lower_limit = property(__ci_lower_limit.value, __ci_lower_limit.set, None, None)

    
    # Element ci_upper_limit uses Python identifier ci_upper_limit
    __ci_upper_limit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ci_upper_limit'), 'ci_upper_limit', '__AbsentNamespace0_analysis_struct_ci_upper_limit', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 502, 6), )

    
    ci_upper_limit = property(__ci_upper_limit.value, __ci_upper_limit.set, None, None)

    
    # Element ci_upper_limit_na_comment uses Python identifier ci_upper_limit_na_comment
    __ci_upper_limit_na_comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'ci_upper_limit_na_comment'), 'ci_upper_limit_na_comment', '__AbsentNamespace0_analysis_struct_ci_upper_limit_na_comment', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 503, 6), )

    
    ci_upper_limit_na_comment = property(__ci_upper_limit_na_comment.value, __ci_upper_limit_na_comment.set, None, None)

    
    # Element estimate_desc uses Python identifier estimate_desc
    __estimate_desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'estimate_desc'), 'estimate_desc', '__AbsentNamespace0_analysis_struct_estimate_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 504, 6), )

    
    estimate_desc = property(__estimate_desc.value, __estimate_desc.set, None, None)

    _ElementMap.update({
        __group_id_list.name() : __group_id_list,
        __groups_desc.name() : __groups_desc,
        __non_inferiority.name() : __non_inferiority,
        __non_inferiority_desc.name() : __non_inferiority_desc,
        __p_value.name() : __p_value,
        __p_value_desc.name() : __p_value_desc,
        __method.name() : __method,
        __method_desc.name() : __method_desc,
        __param_type.name() : __param_type,
        __param_value.name() : __param_value,
        __dispersion_type.name() : __dispersion_type,
        __dispersion_value.name() : __dispersion_value,
        __ci_percent.name() : __ci_percent,
        __ci_n_sides.name() : __ci_n_sides,
        __ci_lower_limit.name() : __ci_lower_limit,
        __ci_upper_limit.name() : __ci_upper_limit,
        __ci_upper_limit_na_comment.name() : __ci_upper_limit_na_comment,
        __estimate_desc.name() : __estimate_desc
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'analysis_struct', analysis_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 482, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group_id uses Python identifier group_id
    __group_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_id'), 'group_id', '__AbsentNamespace0_CTD_ANON_9_group_id', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 484, 12), )

    
    group_id = property(__group_id.value, __group_id.set, None, None)

    _ElementMap.update({
        __group_id.name() : __group_id
    })
    _AttributeMap.update({
        
    })



# Complex type results_outcome_struct with content type ELEMENT_ONLY
class results_outcome_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type results_outcome_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'results_outcome_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 510, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_results_outcome_struct_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 512, 6), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_results_outcome_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 513, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_results_outcome_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 514, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element time_frame uses Python identifier time_frame
    __time_frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'time_frame'), 'time_frame', '__AbsentNamespace0_results_outcome_struct_time_frame', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 515, 6), )

    
    time_frame = property(__time_frame.value, __time_frame.set, None, None)

    
    # Element safety_issue uses Python identifier safety_issue
    __safety_issue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'safety_issue'), 'safety_issue', '__AbsentNamespace0_results_outcome_struct_safety_issue', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 516, 6), )

    
    safety_issue = property(__safety_issue.value, __safety_issue.set, None, None)

    
    # Element posting_date uses Python identifier posting_date
    __posting_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'posting_date'), 'posting_date', '__AbsentNamespace0_results_outcome_struct_posting_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 517, 6), )

    
    posting_date = property(__posting_date.value, __posting_date.set, None, None)

    
    # Element population uses Python identifier population
    __population = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'population'), 'population', '__AbsentNamespace0_results_outcome_struct_population', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 518, 6), )

    
    population = property(__population.value, __population.set, None, None)

    
    # Element group_list uses Python identifier group_list
    __group_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_list'), 'group_list', '__AbsentNamespace0_results_outcome_struct_group_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 519, 6), )

    
    group_list = property(__group_list.value, __group_list.set, None, None)

    
    # Element measure_list uses Python identifier measure_list
    __measure_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measure_list'), 'measure_list', '__AbsentNamespace0_results_outcome_struct_measure_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 526, 6), )

    
    measure_list = property(__measure_list.value, __measure_list.set, None, None)

    
    # Element analysis_list uses Python identifier analysis_list
    __analysis_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'analysis_list'), 'analysis_list', '__AbsentNamespace0_results_outcome_struct_analysis_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 533, 6), )

    
    analysis_list = property(__analysis_list.value, __analysis_list.set, None, None)

    _ElementMap.update({
        __type.name() : __type,
        __title.name() : __title,
        __description.name() : __description,
        __time_frame.name() : __time_frame,
        __safety_issue.name() : __safety_issue,
        __posting_date.name() : __posting_date,
        __population.name() : __population,
        __group_list.name() : __group_list,
        __measure_list.name() : __measure_list,
        __analysis_list.name() : __analysis_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'results_outcome_struct', results_outcome_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 520, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__AbsentNamespace0_CTD_ANON_10_group', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 522, 12), )

    
    group = property(__group.value, __group.set, None, None)

    _ElementMap.update({
        __group.name() : __group
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 527, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element measure uses Python identifier measure
    __measure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'measure'), 'measure', '__AbsentNamespace0_CTD_ANON_11_measure', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 529, 12), )

    
    measure = property(__measure.value, __measure.set, None, None)

    _ElementMap.update({
        __measure.name() : __measure
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 534, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element analysis uses Python identifier analysis
    __analysis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'analysis'), 'analysis', '__AbsentNamespace0_CTD_ANON_12_analysis', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 536, 12), )

    
    analysis = property(__analysis.value, __analysis.set, None, None)

    _ElementMap.update({
        __analysis.name() : __analysis
    })
    _AttributeMap.update({
        
    })



# Complex type vocab_term_struct with content type SIMPLE
class vocab_term_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vocab_term_struct with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vocab_term_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 545, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute vocab uses Python identifier vocab
    __vocab = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vocab'), 'vocab', '__AbsentNamespace0_vocab_term_struct_vocab', pyxb.binding.datatypes.string)
    __vocab._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 548, 8)
    __vocab._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 548, 8)
    
    vocab = property(__vocab.value, __vocab.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vocab.name() : __vocab
    })
Namespace.addCategoryObject('typeBinding', u'vocab_term_struct', vocab_term_struct)


# Complex type event_counts_struct with content type SIMPLE
class event_counts_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type event_counts_struct with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'event_counts_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 555, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute group_id uses Python identifier group_id
    __group_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'group_id'), 'group_id', '__AbsentNamespace0_event_counts_struct_group_id', pyxb.binding.datatypes.string)
    __group_id._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 558, 8)
    __group_id._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 558, 8)
    
    group_id = property(__group_id.value, __group_id.set, None, None)

    
    # Attribute subjects_affected uses Python identifier subjects_affected
    __subjects_affected = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'subjects_affected'), 'subjects_affected', '__AbsentNamespace0_event_counts_struct_subjects_affected', pyxb.binding.datatypes.string)
    __subjects_affected._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 559, 8)
    __subjects_affected._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 559, 8)
    
    subjects_affected = property(__subjects_affected.value, __subjects_affected.set, None, None)

    
    # Attribute subjects_at_risk uses Python identifier subjects_at_risk
    __subjects_at_risk = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'subjects_at_risk'), 'subjects_at_risk', '__AbsentNamespace0_event_counts_struct_subjects_at_risk', pyxb.binding.datatypes.string)
    __subjects_at_risk._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 560, 8)
    __subjects_at_risk._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 560, 8)
    
    subjects_at_risk = property(__subjects_at_risk.value, __subjects_at_risk.set, None, None)

    
    # Attribute events uses Python identifier events
    __events = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'events'), 'events', '__AbsentNamespace0_event_counts_struct_events', pyxb.binding.datatypes.string)
    __events._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 561, 8)
    __events._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 561, 8)
    
    events = property(__events.value, __events.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __group_id.name() : __group_id,
        __subjects_affected.name() : __subjects_affected,
        __subjects_at_risk.name() : __subjects_at_risk,
        __events.name() : __events
    })
Namespace.addCategoryObject('typeBinding', u'event_counts_struct', event_counts_struct)


# Complex type event_struct with content type ELEMENT_ONLY
class event_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type event_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'event_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 568, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sub_title uses Python identifier sub_title
    __sub_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sub_title'), 'sub_title', '__AbsentNamespace0_event_struct_sub_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 570, 6), )

    
    sub_title = property(__sub_title.value, __sub_title.set, None, None)

    
    # Element assessment uses Python identifier assessment
    __assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'assessment'), 'assessment', '__AbsentNamespace0_event_struct_assessment', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 571, 6), )

    
    assessment = property(__assessment.value, __assessment.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_event_struct_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 572, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element counts uses Python identifier counts
    __counts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'counts'), 'counts', '__AbsentNamespace0_event_struct_counts', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 573, 6), )

    
    counts = property(__counts.value, __counts.set, None, None)

    _ElementMap.update({
        __sub_title.name() : __sub_title,
        __assessment.name() : __assessment,
        __description.name() : __description,
        __counts.name() : __counts
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'event_struct', event_struct)


# Complex type event_category_struct with content type ELEMENT_ONLY
class event_category_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type event_category_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'event_category_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 579, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'title'), 'title', '__AbsentNamespace0_event_category_struct_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 581, 6), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element event_list uses Python identifier event_list
    __event_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'event_list'), 'event_list', '__AbsentNamespace0_event_category_struct_event_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 582, 6), )

    
    event_list = property(__event_list.value, __event_list.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __event_list.name() : __event_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'event_category_struct', event_category_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 583, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'event'), 'event', '__AbsentNamespace0_CTD_ANON_13_event', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 585, 12), )

    
    event = property(__event.value, __event.set, None, None)

    _ElementMap.update({
        __event.name() : __event
    })
    _AttributeMap.update({
        
    })



# Complex type events_struct with content type ELEMENT_ONLY
class events_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type events_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'events_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 594, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element frequency_threshold uses Python identifier frequency_threshold
    __frequency_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'frequency_threshold'), 'frequency_threshold', '__AbsentNamespace0_events_struct_frequency_threshold', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 596, 6), )

    
    frequency_threshold = property(__frequency_threshold.value, __frequency_threshold.set, None, None)

    
    # Element default_vocab uses Python identifier default_vocab
    __default_vocab = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'default_vocab'), 'default_vocab', '__AbsentNamespace0_events_struct_default_vocab', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 597, 6), )

    
    default_vocab = property(__default_vocab.value, __default_vocab.set, None, None)

    
    # Element default_assessment uses Python identifier default_assessment
    __default_assessment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'default_assessment'), 'default_assessment', '__AbsentNamespace0_events_struct_default_assessment', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 598, 6), )

    
    default_assessment = property(__default_assessment.value, __default_assessment.set, None, None)

    
    # Element category_list uses Python identifier category_list
    __category_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'category_list'), 'category_list', '__AbsentNamespace0_events_struct_category_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 599, 6), )

    
    category_list = property(__category_list.value, __category_list.set, None, None)

    _ElementMap.update({
        __frequency_threshold.name() : __frequency_threshold,
        __default_vocab.name() : __default_vocab,
        __default_assessment.name() : __default_assessment,
        __category_list.name() : __category_list
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'events_struct', events_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 600, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element category uses Python identifier category
    __category = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'category'), 'category', '__AbsentNamespace0_CTD_ANON_14_category', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 602, 12), )

    
    category = property(__category.value, __category.set, None, None)

    _ElementMap.update({
        __category.name() : __category
    })
    _AttributeMap.update({
        
    })



# Complex type reported_events_struct with content type ELEMENT_ONLY
class reported_events_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type reported_events_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'reported_events_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 611, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element time_frame uses Python identifier time_frame
    __time_frame = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'time_frame'), 'time_frame', '__AbsentNamespace0_reported_events_struct_time_frame', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 613, 6), )

    
    time_frame = property(__time_frame.value, __time_frame.set, None, None)

    
    # Element desc uses Python identifier desc
    __desc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'desc'), 'desc', '__AbsentNamespace0_reported_events_struct_desc', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 614, 6), )

    
    desc = property(__desc.value, __desc.set, None, None)

    
    # Element group_list uses Python identifier group_list
    __group_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group_list'), 'group_list', '__AbsentNamespace0_reported_events_struct_group_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 615, 6), )

    
    group_list = property(__group_list.value, __group_list.set, None, None)

    
    # Element serious_events uses Python identifier serious_events
    __serious_events = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'serious_events'), 'serious_events', '__AbsentNamespace0_reported_events_struct_serious_events', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 622, 6), )

    
    serious_events = property(__serious_events.value, __serious_events.set, None, None)

    
    # Element other_events uses Python identifier other_events
    __other_events = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'other_events'), 'other_events', '__AbsentNamespace0_reported_events_struct_other_events', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 623, 6), )

    
    other_events = property(__other_events.value, __other_events.set, None, None)

    _ElementMap.update({
        __time_frame.name() : __time_frame,
        __desc.name() : __desc,
        __group_list.name() : __group_list,
        __serious_events.name() : __serious_events,
        __other_events.name() : __other_events
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'reported_events_struct', reported_events_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 616, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'group'), 'group', '__AbsentNamespace0_CTD_ANON_15_group', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 618, 12), )

    
    group = property(__group.value, __group.set, None, None)

    _ElementMap.update({
        __group.name() : __group
    })
    _AttributeMap.update({
        
    })



# Complex type certain_agreements_struct with content type ELEMENT_ONLY
class certain_agreements_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type certain_agreements_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'certain_agreements_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 629, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pi_employee uses Python identifier pi_employee
    __pi_employee = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'pi_employee'), 'pi_employee', '__AbsentNamespace0_certain_agreements_struct_pi_employee', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 631, 6), )

    
    pi_employee = property(__pi_employee.value, __pi_employee.set, None, None)

    
    # Element restrictive_agreement uses Python identifier restrictive_agreement
    __restrictive_agreement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'restrictive_agreement'), 'restrictive_agreement', '__AbsentNamespace0_certain_agreements_struct_restrictive_agreement', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 632, 6), )

    
    restrictive_agreement = property(__restrictive_agreement.value, __restrictive_agreement.set, None, None)

    _ElementMap.update({
        __pi_employee.name() : __pi_employee,
        __restrictive_agreement.name() : __restrictive_agreement
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'certain_agreements_struct', certain_agreements_struct)


# Complex type point_of_contact_struct with content type ELEMENT_ONLY
class point_of_contact_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type point_of_contact_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'point_of_contact_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 638, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name_or_title uses Python identifier name_or_title
    __name_or_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name_or_title'), 'name_or_title', '__AbsentNamespace0_point_of_contact_struct_name_or_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 640, 6), )

    
    name_or_title = property(__name_or_title.value, __name_or_title.set, None, None)

    
    # Element organization uses Python identifier organization
    __organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'organization'), 'organization', '__AbsentNamespace0_point_of_contact_struct_organization', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 641, 6), )

    
    organization = property(__organization.value, __organization.set, None, None)

    
    # Element phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'phone'), 'phone', '__AbsentNamespace0_point_of_contact_struct_phone', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 642, 6), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'email'), 'email', '__AbsentNamespace0_point_of_contact_struct_email', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 643, 6), )

    
    email = property(__email.value, __email.set, None, None)

    _ElementMap.update({
        __name_or_title.name() : __name_or_title,
        __organization.name() : __organization,
        __phone.name() : __phone,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'point_of_contact_struct', point_of_contact_struct)


# Complex type clinical_results_struct with content type ELEMENT_ONLY
class clinical_results_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type clinical_results_struct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'clinical_results_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 649, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element participant_flow uses Python identifier participant_flow
    __participant_flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'participant_flow'), 'participant_flow', '__AbsentNamespace0_clinical_results_struct_participant_flow', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 651, 6), )

    
    participant_flow = property(__participant_flow.value, __participant_flow.set, None, None)

    
    # Element baseline uses Python identifier baseline
    __baseline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'baseline'), 'baseline', '__AbsentNamespace0_clinical_results_struct_baseline', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 652, 6), )

    
    baseline = property(__baseline.value, __baseline.set, None, None)

    
    # Element outcome_list uses Python identifier outcome_list
    __outcome_list = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'outcome_list'), 'outcome_list', '__AbsentNamespace0_clinical_results_struct_outcome_list', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 653, 6), )

    
    outcome_list = property(__outcome_list.value, __outcome_list.set, None, None)

    
    # Element reported_events uses Python identifier reported_events
    __reported_events = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reported_events'), 'reported_events', '__AbsentNamespace0_clinical_results_struct_reported_events', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 660, 6), )

    
    reported_events = property(__reported_events.value, __reported_events.set, None, None)

    
    # Element certain_agreements uses Python identifier certain_agreements
    __certain_agreements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'certain_agreements'), 'certain_agreements', '__AbsentNamespace0_clinical_results_struct_certain_agreements', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 661, 6), )

    
    certain_agreements = property(__certain_agreements.value, __certain_agreements.set, None, None)

    
    # Element limitations_and_caveats uses Python identifier limitations_and_caveats
    __limitations_and_caveats = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'limitations_and_caveats'), 'limitations_and_caveats', '__AbsentNamespace0_clinical_results_struct_limitations_and_caveats', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 662, 6), )

    
    limitations_and_caveats = property(__limitations_and_caveats.value, __limitations_and_caveats.set, None, None)

    
    # Element point_of_contact uses Python identifier point_of_contact
    __point_of_contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'point_of_contact'), 'point_of_contact', '__AbsentNamespace0_clinical_results_struct_point_of_contact', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 663, 6), )

    
    point_of_contact = property(__point_of_contact.value, __point_of_contact.set, None, None)

    _ElementMap.update({
        __participant_flow.name() : __participant_flow,
        __baseline.name() : __baseline,
        __outcome_list.name() : __outcome_list,
        __reported_events.name() : __reported_events,
        __certain_agreements.name() : __certain_agreements,
        __limitations_and_caveats.name() : __limitations_and_caveats,
        __point_of_contact.name() : __point_of_contact
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'clinical_results_struct', clinical_results_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 654, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element outcome uses Python identifier outcome
    __outcome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'outcome'), 'outcome', '__AbsentNamespace0_CTD_ANON_16_outcome', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 656, 12), )

    
    outcome = property(__outcome.value, __outcome.set, None, None)

    _ElementMap.update({
        __outcome.name() : __outcome
    })
    _AttributeMap.update({
        
    })



# Complex type date_struct with content type MIXED
class date_struct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type date_struct with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'date_struct')
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 669, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_date_struct_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 670, 4)
    __type._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 670, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'date_struct', date_struct)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 676, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element required_header uses Python identifier required_header
    __required_header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'required_header'), 'required_header', '__AbsentNamespace0_CTD_ANON_17_required_header', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 678, 8), )

    
    required_header = property(__required_header.value, __required_header.set, None, None)

    
    # Element id_info uses Python identifier id_info
    __id_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'id_info'), 'id_info', '__AbsentNamespace0_CTD_ANON_17_id_info', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 679, 8), )

    
    id_info = property(__id_info.value, __id_info.set, None, None)

    
    # Element brief_title uses Python identifier brief_title
    __brief_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'brief_title'), 'brief_title', '__AbsentNamespace0_CTD_ANON_17_brief_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 680, 8), )

    
    brief_title = property(__brief_title.value, __brief_title.set, None, None)

    
    # Element acronym uses Python identifier acronym
    __acronym = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'acronym'), 'acronym', '__AbsentNamespace0_CTD_ANON_17_acronym', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 681, 8), )

    
    acronym = property(__acronym.value, __acronym.set, None, None)

    
    # Element official_title uses Python identifier official_title
    __official_title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'official_title'), 'official_title', '__AbsentNamespace0_CTD_ANON_17_official_title', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 682, 8), )

    
    official_title = property(__official_title.value, __official_title.set, None, None)

    
    # Element sponsors uses Python identifier sponsors
    __sponsors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sponsors'), 'sponsors', '__AbsentNamespace0_CTD_ANON_17_sponsors', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 683, 8), )

    
    sponsors = property(__sponsors.value, __sponsors.set, None, None)

    
    # Element source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'source'), 'source', '__AbsentNamespace0_CTD_ANON_17_source', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 684, 8), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element oversight_info uses Python identifier oversight_info
    __oversight_info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'oversight_info'), 'oversight_info', '__AbsentNamespace0_CTD_ANON_17_oversight_info', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 685, 8), )

    
    oversight_info = property(__oversight_info.value, __oversight_info.set, None, None)

    
    # Element brief_summary uses Python identifier brief_summary
    __brief_summary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'brief_summary'), 'brief_summary', '__AbsentNamespace0_CTD_ANON_17_brief_summary', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 686, 8), )

    
    brief_summary = property(__brief_summary.value, __brief_summary.set, None, None)

    
    # Element detailed_description uses Python identifier detailed_description
    __detailed_description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'detailed_description'), 'detailed_description', '__AbsentNamespace0_CTD_ANON_17_detailed_description', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 687, 8), )

    
    detailed_description = property(__detailed_description.value, __detailed_description.set, None, None)

    
    # Element overall_status uses Python identifier overall_status
    __overall_status = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'overall_status'), 'overall_status', '__AbsentNamespace0_CTD_ANON_17_overall_status', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 688, 8), )

    
    overall_status = property(__overall_status.value, __overall_status.set, None, None)

    
    # Element why_stopped uses Python identifier why_stopped
    __why_stopped = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'why_stopped'), 'why_stopped', '__AbsentNamespace0_CTD_ANON_17_why_stopped', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 689, 8), )

    
    why_stopped = property(__why_stopped.value, __why_stopped.set, None, None)

    
    # Element start_date uses Python identifier start_date
    __start_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'start_date'), 'start_date', '__AbsentNamespace0_CTD_ANON_17_start_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 690, 8), )

    
    start_date = property(__start_date.value, __start_date.set, None, None)

    
    # Element end_date uses Python identifier end_date
    __end_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'end_date'), 'end_date', '__AbsentNamespace0_CTD_ANON_17_end_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 691, 8), )

    
    end_date = property(__end_date.value, __end_date.set, None, None)

    
    # Element completion_date uses Python identifier completion_date
    __completion_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'completion_date'), 'completion_date', '__AbsentNamespace0_CTD_ANON_17_completion_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 692, 8), )

    
    completion_date = property(__completion_date.value, __completion_date.set, None, None)

    
    # Element primary_completion_date uses Python identifier primary_completion_date
    __primary_completion_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'primary_completion_date'), 'primary_completion_date', '__AbsentNamespace0_CTD_ANON_17_primary_completion_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 693, 8), )

    
    primary_completion_date = property(__primary_completion_date.value, __primary_completion_date.set, None, None)

    
    # Element phase uses Python identifier phase
    __phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'phase'), 'phase', '__AbsentNamespace0_CTD_ANON_17_phase', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 694, 8), )

    
    phase = property(__phase.value, __phase.set, None, None)

    
    # Element study_type uses Python identifier study_type
    __study_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'study_type'), 'study_type', '__AbsentNamespace0_CTD_ANON_17_study_type', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 695, 8), )

    
    study_type = property(__study_type.value, __study_type.set, None, None)

    
    # Element study_design uses Python identifier study_design
    __study_design = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'study_design'), 'study_design', '__AbsentNamespace0_CTD_ANON_17_study_design', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 696, 8), )

    
    study_design = property(__study_design.value, __study_design.set, None, None)

    
    # Element target_duration uses Python identifier target_duration
    __target_duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'target_duration'), 'target_duration', '__AbsentNamespace0_CTD_ANON_17_target_duration', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 697, 8), )

    
    target_duration = property(__target_duration.value, __target_duration.set, None, None)

    
    # Element primary_outcome uses Python identifier primary_outcome
    __primary_outcome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'primary_outcome'), 'primary_outcome', '__AbsentNamespace0_CTD_ANON_17_primary_outcome', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 698, 8), )

    
    primary_outcome = property(__primary_outcome.value, __primary_outcome.set, None, None)

    
    # Element secondary_outcome uses Python identifier secondary_outcome
    __secondary_outcome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'secondary_outcome'), 'secondary_outcome', '__AbsentNamespace0_CTD_ANON_17_secondary_outcome', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 699, 8), )

    
    secondary_outcome = property(__secondary_outcome.value, __secondary_outcome.set, None, None)

    
    # Element other_outcome uses Python identifier other_outcome
    __other_outcome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'other_outcome'), 'other_outcome', '__AbsentNamespace0_CTD_ANON_17_other_outcome', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 700, 8), )

    
    other_outcome = property(__other_outcome.value, __other_outcome.set, None, None)

    
    # Element number_of_arms uses Python identifier number_of_arms
    __number_of_arms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'number_of_arms'), 'number_of_arms', '__AbsentNamespace0_CTD_ANON_17_number_of_arms', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 701, 8), )

    
    number_of_arms = property(__number_of_arms.value, __number_of_arms.set, None, None)

    
    # Element number_of_groups uses Python identifier number_of_groups
    __number_of_groups = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'number_of_groups'), 'number_of_groups', '__AbsentNamespace0_CTD_ANON_17_number_of_groups', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 702, 8), )

    
    number_of_groups = property(__number_of_groups.value, __number_of_groups.set, None, None)

    
    # Element enrollment uses Python identifier enrollment
    __enrollment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'enrollment'), 'enrollment', '__AbsentNamespace0_CTD_ANON_17_enrollment', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 703, 8), )

    
    enrollment = property(__enrollment.value, __enrollment.set, None, None)

    
    # Element condition uses Python identifier condition
    __condition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'condition'), 'condition', '__AbsentNamespace0_CTD_ANON_17_condition', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 704, 8), )

    
    condition = property(__condition.value, __condition.set, None, None)

    
    # Element arm_group uses Python identifier arm_group
    __arm_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'arm_group'), 'arm_group', '__AbsentNamespace0_CTD_ANON_17_arm_group', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 705, 8), )

    
    arm_group = property(__arm_group.value, __arm_group.set, None, None)

    
    # Element intervention uses Python identifier intervention
    __intervention = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'intervention'), 'intervention', '__AbsentNamespace0_CTD_ANON_17_intervention', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 706, 8), )

    
    intervention = property(__intervention.value, __intervention.set, None, None)

    
    # Element biospec_retention uses Python identifier biospec_retention
    __biospec_retention = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'biospec_retention'), 'biospec_retention', '__AbsentNamespace0_CTD_ANON_17_biospec_retention', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 707, 8), )

    
    biospec_retention = property(__biospec_retention.value, __biospec_retention.set, None, None)

    
    # Element biospec_descr uses Python identifier biospec_descr
    __biospec_descr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'biospec_descr'), 'biospec_descr', '__AbsentNamespace0_CTD_ANON_17_biospec_descr', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 708, 8), )

    
    biospec_descr = property(__biospec_descr.value, __biospec_descr.set, None, None)

    
    # Element eligibility uses Python identifier eligibility
    __eligibility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'eligibility'), 'eligibility', '__AbsentNamespace0_CTD_ANON_17_eligibility', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 709, 8), )

    
    eligibility = property(__eligibility.value, __eligibility.set, None, None)

    
    # Element overall_official uses Python identifier overall_official
    __overall_official = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'overall_official'), 'overall_official', '__AbsentNamespace0_CTD_ANON_17_overall_official', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 710, 8), )

    
    overall_official = property(__overall_official.value, __overall_official.set, None, None)

    
    # Element overall_contact uses Python identifier overall_contact
    __overall_contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'overall_contact'), 'overall_contact', '__AbsentNamespace0_CTD_ANON_17_overall_contact', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 711, 8), )

    
    overall_contact = property(__overall_contact.value, __overall_contact.set, None, None)

    
    # Element overall_contact_backup uses Python identifier overall_contact_backup
    __overall_contact_backup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'overall_contact_backup'), 'overall_contact_backup', '__AbsentNamespace0_CTD_ANON_17_overall_contact_backup', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 712, 8), )

    
    overall_contact_backup = property(__overall_contact_backup.value, __overall_contact_backup.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__AbsentNamespace0_CTD_ANON_17_location', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 713, 8), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element location_countries uses Python identifier location_countries
    __location_countries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location_countries'), 'location_countries', '__AbsentNamespace0_CTD_ANON_17_location_countries', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 714, 8), )

    
    location_countries = property(__location_countries.value, __location_countries.set, None, None)

    
    # Element removed_countries uses Python identifier removed_countries
    __removed_countries = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'removed_countries'), 'removed_countries', '__AbsentNamespace0_CTD_ANON_17_removed_countries', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 715, 8), )

    
    removed_countries = property(__removed_countries.value, __removed_countries.set, None, None)

    
    # Element link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'link'), 'link', '__AbsentNamespace0_CTD_ANON_17_link', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 716, 8), )

    
    link = property(__link.value, __link.set, None, None)

    
    # Element reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'reference'), 'reference', '__AbsentNamespace0_CTD_ANON_17_reference', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 717, 8), )

    
    reference = property(__reference.value, __reference.set, None, None)

    
    # Element results_reference uses Python identifier results_reference
    __results_reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'results_reference'), 'results_reference', '__AbsentNamespace0_CTD_ANON_17_results_reference', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 718, 8), )

    
    results_reference = property(__results_reference.value, __results_reference.set, None, None)

    
    # Element verification_date uses Python identifier verification_date
    __verification_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'verification_date'), 'verification_date', '__AbsentNamespace0_CTD_ANON_17_verification_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 719, 8), )

    
    verification_date = property(__verification_date.value, __verification_date.set, None, None)

    
    # Element lastchanged_date uses Python identifier lastchanged_date
    __lastchanged_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'lastchanged_date'), 'lastchanged_date', '__AbsentNamespace0_CTD_ANON_17_lastchanged_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 720, 8), )

    
    lastchanged_date = property(__lastchanged_date.value, __lastchanged_date.set, None, None)

    
    # Element firstreceived_date uses Python identifier firstreceived_date
    __firstreceived_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'firstreceived_date'), 'firstreceived_date', '__AbsentNamespace0_CTD_ANON_17_firstreceived_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 721, 8), )

    
    firstreceived_date = property(__firstreceived_date.value, __firstreceived_date.set, None, None)

    
    # Element firstreceived_results_date uses Python identifier firstreceived_results_date
    __firstreceived_results_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'firstreceived_results_date'), 'firstreceived_results_date', '__AbsentNamespace0_CTD_ANON_17_firstreceived_results_date', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 722, 8), )

    
    firstreceived_results_date = property(__firstreceived_results_date.value, __firstreceived_results_date.set, None, None)

    
    # Element responsible_party uses Python identifier responsible_party
    __responsible_party = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'responsible_party'), 'responsible_party', '__AbsentNamespace0_CTD_ANON_17_responsible_party', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 723, 8), )

    
    responsible_party = property(__responsible_party.value, __responsible_party.set, None, None)

    
    # Element keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'keyword'), 'keyword', '__AbsentNamespace0_CTD_ANON_17_keyword', True, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 724, 8), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element is_fda_regulated uses Python identifier is_fda_regulated
    __is_fda_regulated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is_fda_regulated'), 'is_fda_regulated', '__AbsentNamespace0_CTD_ANON_17_is_fda_regulated', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 725, 8), )

    
    is_fda_regulated = property(__is_fda_regulated.value, __is_fda_regulated.set, None, None)

    
    # Element is_section_801 uses Python identifier is_section_801
    __is_section_801 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'is_section_801'), 'is_section_801', '__AbsentNamespace0_CTD_ANON_17_is_section_801', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 726, 8), )

    
    is_section_801 = property(__is_section_801.value, __is_section_801.set, None, None)

    
    # Element has_expanded_access uses Python identifier has_expanded_access
    __has_expanded_access = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'has_expanded_access'), 'has_expanded_access', '__AbsentNamespace0_CTD_ANON_17_has_expanded_access', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 727, 8), )

    
    has_expanded_access = property(__has_expanded_access.value, __has_expanded_access.set, None, None)

    
    # Element condition_browse uses Python identifier condition_browse
    __condition_browse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'condition_browse'), 'condition_browse', '__AbsentNamespace0_CTD_ANON_17_condition_browse', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 728, 8), )

    
    condition_browse = property(__condition_browse.value, __condition_browse.set, None, None)

    
    # Element intervention_browse uses Python identifier intervention_browse
    __intervention_browse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'intervention_browse'), 'intervention_browse', '__AbsentNamespace0_CTD_ANON_17_intervention_browse', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 729, 8), )

    
    intervention_browse = property(__intervention_browse.value, __intervention_browse.set, None, None)

    
    # Element clinical_results uses Python identifier clinical_results
    __clinical_results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'clinical_results'), 'clinical_results', '__AbsentNamespace0_CTD_ANON_17_clinical_results', False, pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 730, 8), )

    
    clinical_results = property(__clinical_results.value, __clinical_results.set, None, None)

    
    # Attribute rank uses Python identifier rank
    __rank = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'rank'), 'rank', '__AbsentNamespace0_CTD_ANON_17_rank', pyxb.binding.datatypes.string)
    __rank._DeclarationLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 732, 6)
    __rank._UseLocation = pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 732, 6)
    
    rank = property(__rank.value, __rank.set, None, None)

    _ElementMap.update({
        __required_header.name() : __required_header,
        __id_info.name() : __id_info,
        __brief_title.name() : __brief_title,
        __acronym.name() : __acronym,
        __official_title.name() : __official_title,
        __sponsors.name() : __sponsors,
        __source.name() : __source,
        __oversight_info.name() : __oversight_info,
        __brief_summary.name() : __brief_summary,
        __detailed_description.name() : __detailed_description,
        __overall_status.name() : __overall_status,
        __why_stopped.name() : __why_stopped,
        __start_date.name() : __start_date,
        __end_date.name() : __end_date,
        __completion_date.name() : __completion_date,
        __primary_completion_date.name() : __primary_completion_date,
        __phase.name() : __phase,
        __study_type.name() : __study_type,
        __study_design.name() : __study_design,
        __target_duration.name() : __target_duration,
        __primary_outcome.name() : __primary_outcome,
        __secondary_outcome.name() : __secondary_outcome,
        __other_outcome.name() : __other_outcome,
        __number_of_arms.name() : __number_of_arms,
        __number_of_groups.name() : __number_of_groups,
        __enrollment.name() : __enrollment,
        __condition.name() : __condition,
        __arm_group.name() : __arm_group,
        __intervention.name() : __intervention,
        __biospec_retention.name() : __biospec_retention,
        __biospec_descr.name() : __biospec_descr,
        __eligibility.name() : __eligibility,
        __overall_official.name() : __overall_official,
        __overall_contact.name() : __overall_contact,
        __overall_contact_backup.name() : __overall_contact_backup,
        __location.name() : __location,
        __location_countries.name() : __location_countries,
        __removed_countries.name() : __removed_countries,
        __link.name() : __link,
        __reference.name() : __reference,
        __results_reference.name() : __results_reference,
        __verification_date.name() : __verification_date,
        __lastchanged_date.name() : __lastchanged_date,
        __firstreceived_date.name() : __firstreceived_date,
        __firstreceived_results_date.name() : __firstreceived_results_date,
        __responsible_party.name() : __responsible_party,
        __keyword.name() : __keyword,
        __is_fda_regulated.name() : __is_fda_regulated,
        __is_section_801.name() : __is_section_801,
        __has_expanded_access.name() : __has_expanded_access,
        __condition_browse.name() : __condition_browse,
        __intervention_browse.name() : __intervention_browse,
        __clinical_results.name() : __clinical_results
    })
    _AttributeMap.update({
        __rank.name() : __rank
    })



clinical_study = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clinical_study'), CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 675, 2))
Namespace.addCategoryObject('elementBinding', clinical_study.name().localName(), clinical_study)



required_header_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'download_date'), pyxb.binding.datatypes.string, scope=required_header_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 115, 6)))

required_header_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link_text'), pyxb.binding.datatypes.string, scope=required_header_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 116, 6)))

required_header_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'url'), pyxb.binding.datatypes.string, scope=required_header_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 117, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(required_header_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'download_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(required_header_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'link_text')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 116, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(required_header_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'url')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 117, 6))
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
required_header_struct._Automaton = _BuildAutomaton()




id_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'org_study_id'), pyxb.binding.datatypes.string, scope=id_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 125, 6)))

id_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'secondary_id'), pyxb.binding.datatypes.string, scope=id_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 126, 6)))

id_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'nct_id'), pyxb.binding.datatypes.string, scope=id_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 127, 6)))

id_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'nct_alias'), pyxb.binding.datatypes.string, scope=id_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 128, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 126, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 128, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(id_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'org_study_id')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(id_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'secondary_id')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 126, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(id_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'nct_id')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 127, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(id_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'nct_alias')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 128, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
id_info_struct._Automaton = _BuildAutomaton_()




sponsor_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'agency'), pyxb.binding.datatypes.string, scope=sponsor_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 136, 6)))

sponsor_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'agency_class'), pyxb.binding.datatypes.string, scope=sponsor_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 137, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(sponsor_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'agency')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 136, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sponsor_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'agency_class')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 137, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
sponsor_struct._Automaton = _BuildAutomaton_2()




sponsors_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'lead_sponsor'), sponsor_struct, scope=sponsors_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 145, 6)))

sponsors_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'collaborator'), sponsor_struct, scope=sponsors_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 146, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 146, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sponsors_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'lead_sponsor')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 145, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sponsors_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'collaborator')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 146, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
sponsors_struct._Automaton = _BuildAutomaton_3()




oversight_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'authority'), pyxb.binding.datatypes.string, scope=oversight_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 154, 6)))

oversight_info_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'has_dmc'), pyxb.binding.datatypes.string, scope=oversight_info_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 155, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 154, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 155, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(oversight_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'authority')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 154, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(oversight_info_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'has_dmc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 155, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
oversight_info_struct._Automaton = _BuildAutomaton_4()




protocol_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measure'), pyxb.binding.datatypes.string, scope=protocol_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 163, 6)))

protocol_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'time_frame'), pyxb.binding.datatypes.string, scope=protocol_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 164, 6)))

protocol_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'safety_issue'), pyxb.binding.datatypes.string, scope=protocol_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 165, 6)))

protocol_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=protocol_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 166, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 164, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 165, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 166, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(protocol_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'measure')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 163, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(protocol_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'time_frame')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 164, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(protocol_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'safety_issue')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 165, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(protocol_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 166, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
protocol_outcome_struct._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
enrollment_struct._Automaton = _BuildAutomaton_6()




arm_group_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'arm_group_label'), pyxb.binding.datatypes.string, scope=arm_group_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 180, 6)))

arm_group_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'arm_group_type'), pyxb.binding.datatypes.string, scope=arm_group_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 181, 6)))

arm_group_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=arm_group_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 182, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 181, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 182, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(arm_group_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'arm_group_label')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 180, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(arm_group_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'arm_group_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 181, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(arm_group_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 182, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
arm_group_struct._Automaton = _BuildAutomaton_7()




intervention_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'intervention_type'), pyxb.binding.datatypes.string, scope=intervention_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 190, 6)))

intervention_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'intervention_name'), pyxb.binding.datatypes.string, scope=intervention_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 191, 6)))

intervention_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=intervention_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 192, 6)))

intervention_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'arm_group_label'), pyxb.binding.datatypes.string, scope=intervention_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 193, 6)))

intervention_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'other_name'), pyxb.binding.datatypes.string, scope=intervention_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 194, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 192, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 193, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 194, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(intervention_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'intervention_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 190, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(intervention_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'intervention_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 191, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(intervention_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 192, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(intervention_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'arm_group_label')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 193, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(intervention_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'other_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 194, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
intervention_struct._Automaton = _BuildAutomaton_8()




textblock_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'textblock'), pyxb.binding.datatypes.string, scope=textblock_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 202, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(textblock_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'textblock')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 202, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
textblock_struct._Automaton = _BuildAutomaton_9()




eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'study_pop'), textblock_struct, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 210, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sampling_method'), pyxb.binding.datatypes.string, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 211, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'criteria'), textblock_struct, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 212, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'gender'), pyxb.binding.datatypes.string, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 213, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'minimum_age'), pyxb.binding.datatypes.string, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 214, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'maximum_age'), pyxb.binding.datatypes.string, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 215, 6)))

eligibility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'healthy_volunteers'), pyxb.binding.datatypes.string, scope=eligibility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 216, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 210, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 211, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 212, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 216, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'study_pop')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 210, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'sampling_method')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 211, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'criteria')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 212, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'gender')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 213, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'minimum_age')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 214, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'maximum_age')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 215, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(eligibility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'healthy_volunteers')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 216, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
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
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
eligibility_struct._Automaton = _BuildAutomaton_10()




contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'first_name'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 224, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'middle_name'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 225, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last_name'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 226, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'degrees'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 227, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'phone'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 228, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'phone_ext'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 229, 6)))

contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'email'), pyxb.binding.datatypes.string, scope=contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 230, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 224, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 225, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 226, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 227, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 228, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 229, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 230, 6))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'first_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 224, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'middle_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 225, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'last_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 226, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'degrees')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 227, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'phone')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 228, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'phone_ext')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 229, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'email')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 230, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
contact_struct._Automaton = _BuildAutomaton_11()




investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'first_name'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 238, 6)))

investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'middle_name'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 239, 6)))

investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'last_name'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 240, 6)))

investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'degrees'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 241, 6)))

investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'role'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 242, 6)))

investigator_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'affiliation'), pyxb.binding.datatypes.string, scope=investigator_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 243, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 238, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 239, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 241, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 242, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 243, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'first_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 238, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'middle_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 239, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'last_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 240, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'degrees')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 241, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'role')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 242, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(investigator_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'affiliation')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 243, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
investigator_struct._Automaton = _BuildAutomaton_12()




address_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'city'), pyxb.binding.datatypes.string, scope=address_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 251, 6)))

address_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'state'), pyxb.binding.datatypes.string, scope=address_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 252, 6)))

address_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'zip'), pyxb.binding.datatypes.string, scope=address_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 253, 6)))

address_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'country'), pyxb.binding.datatypes.string, scope=address_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 254, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 252, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 253, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'city')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 251, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'state')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 252, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(address_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'zip')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 253, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(address_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'country')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 254, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
address_struct._Automaton = _BuildAutomaton_13()




facility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=facility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 262, 6)))

facility_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'address'), address_struct, scope=facility_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 263, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 262, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 263, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(facility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 262, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(facility_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'address')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 263, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
facility_struct._Automaton = _BuildAutomaton_14()




location_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'facility'), facility_struct, scope=location_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 271, 6)))

location_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'status'), pyxb.binding.datatypes.string, scope=location_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 272, 6)))

location_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'contact'), contact_struct, scope=location_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 273, 6)))

location_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'contact_backup'), contact_struct, scope=location_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 274, 6)))

location_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'investigator'), investigator_struct, scope=location_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 275, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 271, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 272, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 273, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 274, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 275, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(location_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'facility')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 271, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(location_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'status')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 272, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(location_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'contact')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 273, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(location_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'contact_backup')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 274, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(location_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'investigator')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 275, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
location_struct._Automaton = _BuildAutomaton_15()




countries_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'country'), pyxb.binding.datatypes.string, scope=countries_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 283, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 283, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(countries_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'country')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 283, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
countries_struct._Automaton = _BuildAutomaton_16()




link_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'url'), pyxb.binding.datatypes.string, scope=link_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 291, 6)))

link_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=link_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 292, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 292, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(link_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'url')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 291, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(link_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 292, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
link_struct._Automaton = _BuildAutomaton_17()




reference_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'citation'), pyxb.binding.datatypes.string, scope=reference_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 300, 6)))

reference_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'PMID'), pyxb.binding.datatypes.string, scope=reference_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 301, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 300, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 301, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reference_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'citation')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 300, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(reference_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'PMID')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 301, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
reference_struct._Automaton = _BuildAutomaton_18()




responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name_title'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 309, 6)))

responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'organization'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 310, 6)))

responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'responsible_party_type'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 311, 6)))

responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'investigator_affiliation'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 312, 6)))

responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'investigator_full_name'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 313, 6)))

responsible_party_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'investigator_title'), pyxb.binding.datatypes.string, scope=responsible_party_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 314, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 309, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 310, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 311, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 312, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 313, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 314, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'name_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 309, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'organization')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 310, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'responsible_party_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 311, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'investigator_affiliation')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 312, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'investigator_full_name')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 313, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(responsible_party_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'investigator_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 314, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
responsible_party_struct._Automaton = _BuildAutomaton_19()




browse_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'mesh_term'), pyxb.binding.datatypes.string, scope=browse_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 322, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 322, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(browse_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'mesh_term')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 322, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
browse_struct._Automaton = _BuildAutomaton_20()




group_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=group_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 330, 6)))

group_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=group_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 331, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 331, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(group_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 330, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(group_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 331, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
group_struct._Automaton = _BuildAutomaton_21()




milestone_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=milestone_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 351, 6)))

milestone_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'participants_list'), CTD_ANON, scope=milestone_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 352, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(milestone_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 351, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(milestone_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'participants_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 352, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
milestone_struct._Automaton = _BuildAutomaton_22()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'participants'), participants_struct, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 355, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'participants')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 355, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_23()




period_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=period_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 366, 6)))

period_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'milestone_list'), CTD_ANON_, scope=period_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 367, 6)))

period_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason_list'), CTD_ANON_2, scope=period_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 374, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 374, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(period_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 366, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(period_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'milestone_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 367, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(period_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 374, 6))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
period_struct._Automaton = _BuildAutomaton_24()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'milestone'), milestone_struct, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 370, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'milestone')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 370, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_25()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason'), milestone_struct, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 377, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 377, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(None, u'drop_withdraw_reason')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 377, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_26()




participant_flow_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'recruitment_details'), pyxb.binding.datatypes.string, scope=participant_flow_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 388, 6)))

participant_flow_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pre_assignment_details'), pyxb.binding.datatypes.string, scope=participant_flow_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 389, 6)))

participant_flow_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_list'), CTD_ANON_3, scope=participant_flow_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 390, 6)))

participant_flow_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'period_list'), CTD_ANON_4, scope=participant_flow_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 397, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 388, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 389, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(participant_flow_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'recruitment_details')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 388, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(participant_flow_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'pre_assignment_details')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 389, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(participant_flow_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'group_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 390, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(participant_flow_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'period_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 397, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
participant_flow_struct._Automaton = _BuildAutomaton_27()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group'), group_struct, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 393, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(None, u'group')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 393, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_28()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'period'), period_struct, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 400, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(None, u'period')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 400, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_29()




measure_category_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sub_title'), pyxb.binding.datatypes.string, scope=measure_category_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 425, 6)))

measure_category_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measurement_list'), CTD_ANON_5, scope=measure_category_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 426, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 425, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_category_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'sub_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 425, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(measure_category_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'measurement_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 426, 6))
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
measure_category_struct._Automaton = _BuildAutomaton_30()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measurement'), measurement_struct, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 429, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(None, u'measurement')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 429, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_31()




measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 440, 6)))

measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 441, 6)))

measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'units'), pyxb.binding.datatypes.string, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 442, 6)))

measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'param'), pyxb.binding.datatypes.string, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 443, 6)))

measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dispersion'), pyxb.binding.datatypes.string, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 444, 6)))

measure_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'category_list'), CTD_ANON_6, scope=measure_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 445, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 441, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 442, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 443, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 444, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 440, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 441, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'units')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 442, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'param')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 443, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'dispersion')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 444, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(measure_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'category_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 445, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
measure_struct._Automaton = _BuildAutomaton_32()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'category'), measure_category_struct, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 448, 12)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(None, u'category')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 448, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_33()




baseline_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'population'), pyxb.binding.datatypes.string, scope=baseline_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 459, 6)))

baseline_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_list'), CTD_ANON_7, scope=baseline_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 460, 6)))

baseline_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measure_list'), CTD_ANON_8, scope=baseline_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 467, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 459, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseline_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'population')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 459, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(baseline_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'group_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 460, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(baseline_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'measure_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 467, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
baseline_struct._Automaton = _BuildAutomaton_34()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group'), group_struct, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 463, 12)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(None, u'group')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 463, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_35()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measure'), measure_struct, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 470, 12)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(None, u'measure')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 470, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_36()




analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_id_list'), CTD_ANON_9, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 481, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'groups_desc'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 488, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'non_inferiority'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 489, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'non_inferiority_desc'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 490, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'p_value'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 491, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'p_value_desc'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 492, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'method'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 493, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'method_desc'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 494, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'param_type'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 495, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'param_value'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 496, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dispersion_type'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 497, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dispersion_value'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 498, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ci_percent'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 499, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ci_n_sides'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 500, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ci_lower_limit'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 501, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ci_upper_limit'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 502, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'ci_upper_limit_na_comment'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 503, 6)))

analysis_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'estimate_desc'), pyxb.binding.datatypes.string, scope=analysis_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 504, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 488, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 489, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 490, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 491, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 492, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 493, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 494, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 495, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 496, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 497, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 498, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 499, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 500, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 501, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 502, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 503, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 504, 6))
    counters.add(cc_16)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'group_id_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 481, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'groups_desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 488, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'non_inferiority')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 489, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'non_inferiority_desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 490, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'p_value')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 491, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'p_value_desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 492, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'method')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 493, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'method_desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 494, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'param_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 495, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'param_value')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 496, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'dispersion_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 497, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'dispersion_value')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 498, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'ci_percent')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 499, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'ci_n_sides')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 500, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'ci_lower_limit')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 501, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'ci_upper_limit')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 502, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'ci_upper_limit_na_comment')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 503, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(analysis_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'estimate_desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 504, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
analysis_struct._Automaton = _BuildAutomaton_37()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_id'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 484, 12)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(None, u'group_id')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 484, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_38()




results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'type'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 512, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 513, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 514, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'time_frame'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 515, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'safety_issue'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 516, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'posting_date'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 517, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'population'), pyxb.binding.datatypes.string, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 518, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_list'), CTD_ANON_10, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 519, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measure_list'), CTD_ANON_11, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 526, 6)))

results_outcome_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'analysis_list'), CTD_ANON_12, scope=results_outcome_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 533, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 514, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 516, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 517, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 518, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 519, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 526, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 533, 6))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 512, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 513, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 514, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'time_frame')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 515, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'safety_issue')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 516, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'posting_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 517, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'population')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 518, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'group_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 519, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'measure_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 526, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(results_outcome_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'analysis_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 533, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
results_outcome_struct._Automaton = _BuildAutomaton_39()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group'), group_struct, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 522, 12)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(None, u'group')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 522, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_40()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'measure'), measure_struct, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 529, 12)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(None, u'measure')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 529, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_41()




CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'analysis'), analysis_struct, scope=CTD_ANON_12, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 536, 12)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(None, u'analysis')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 536, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_42()




event_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sub_title'), vocab_term_struct, scope=event_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 570, 6)))

event_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'assessment'), pyxb.binding.datatypes.string, scope=event_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 571, 6)))

event_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=event_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 572, 6)))

event_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'counts'), event_counts_struct, scope=event_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 573, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 571, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 572, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(event_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'sub_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 570, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(event_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'assessment')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 571, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(event_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 572, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(event_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'counts')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 573, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
event_struct._Automaton = _BuildAutomaton_43()




event_category_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'title'), pyxb.binding.datatypes.string, scope=event_category_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 581, 6)))

event_category_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'event_list'), CTD_ANON_13, scope=event_category_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 582, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(event_category_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 581, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(event_category_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'event_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 582, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
event_category_struct._Automaton = _BuildAutomaton_44()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'event'), event_struct, scope=CTD_ANON_13, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 585, 12)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(None, u'event')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 585, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_45()




events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'frequency_threshold'), pyxb.binding.datatypes.string, scope=events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 596, 6)))

events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'default_vocab'), pyxb.binding.datatypes.string, scope=events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 597, 6)))

events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'default_assessment'), pyxb.binding.datatypes.string, scope=events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 598, 6)))

events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'category_list'), CTD_ANON_14, scope=events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 599, 6)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 596, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 597, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 598, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'frequency_threshold')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 596, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'default_vocab')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 597, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'default_assessment')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 598, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'category_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 599, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
events_struct._Automaton = _BuildAutomaton_46()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'category'), event_category_struct, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 602, 12)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(None, u'category')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 602, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_47()




reported_events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'time_frame'), pyxb.binding.datatypes.string, scope=reported_events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 613, 6)))

reported_events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'desc'), pyxb.binding.datatypes.string, scope=reported_events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 614, 6)))

reported_events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group_list'), CTD_ANON_15, scope=reported_events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 615, 6)))

reported_events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'serious_events'), events_struct, scope=reported_events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 622, 6)))

reported_events_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'other_events'), events_struct, scope=reported_events_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 623, 6)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 613, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 614, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 622, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 623, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(reported_events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'time_frame')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 613, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(reported_events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'desc')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 614, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(reported_events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'group_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 615, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(reported_events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'serious_events')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 622, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(reported_events_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'other_events')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 623, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
reported_events_struct._Automaton = _BuildAutomaton_48()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'group'), group_struct, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 618, 12)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(None, u'group')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 618, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_49()




certain_agreements_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'pi_employee'), pyxb.binding.datatypes.string, scope=certain_agreements_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 631, 6)))

certain_agreements_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'restrictive_agreement'), pyxb.binding.datatypes.string, scope=certain_agreements_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 632, 6)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 631, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 632, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(certain_agreements_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'pi_employee')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 631, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(certain_agreements_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'restrictive_agreement')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 632, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
certain_agreements_struct._Automaton = _BuildAutomaton_50()




point_of_contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name_or_title'), pyxb.binding.datatypes.string, scope=point_of_contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 640, 6)))

point_of_contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'organization'), pyxb.binding.datatypes.string, scope=point_of_contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 641, 6)))

point_of_contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'phone'), pyxb.binding.datatypes.string, scope=point_of_contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 642, 6)))

point_of_contact_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'email'), pyxb.binding.datatypes.string, scope=point_of_contact_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 643, 6)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 642, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 643, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(point_of_contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'name_or_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 640, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(point_of_contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'organization')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 641, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(point_of_contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'phone')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 642, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(point_of_contact_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'email')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 643, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
point_of_contact_struct._Automaton = _BuildAutomaton_51()




clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'participant_flow'), participant_flow_struct, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 651, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'baseline'), baseline_struct, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 652, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'outcome_list'), CTD_ANON_16, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 653, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reported_events'), reported_events_struct, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 660, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'certain_agreements'), certain_agreements_struct, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 661, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'limitations_and_caveats'), pyxb.binding.datatypes.string, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 662, 6)))

clinical_results_struct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'point_of_contact'), point_of_contact_struct, scope=clinical_results_struct, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 663, 6)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 660, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 661, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 662, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 663, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'participant_flow')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 651, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'baseline')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 652, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'outcome_list')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 653, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'reported_events')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 660, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'certain_agreements')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 661, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'limitations_and_caveats')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 662, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(clinical_results_struct._UseForTag(pyxb.namespace.ExpandedName(None, u'point_of_contact')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 663, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
clinical_results_struct._Automaton = _BuildAutomaton_52()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'outcome'), results_outcome_struct, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 656, 12)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(None, u'outcome')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 656, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_53()




def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
date_struct._Automaton = _BuildAutomaton_54()




CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'required_header'), required_header_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 678, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'id_info'), id_info_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 679, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'brief_title'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 680, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'acronym'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 681, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'official_title'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 682, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sponsors'), sponsors_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 683, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'source'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 684, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'oversight_info'), oversight_info_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 685, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'brief_summary'), textblock_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 686, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'detailed_description'), textblock_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 687, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'overall_status'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 688, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'why_stopped'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 689, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'start_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 690, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'end_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 691, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'completion_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 692, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'primary_completion_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 693, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'phase'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 694, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'study_type'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 695, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'study_design'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 696, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'target_duration'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 697, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'primary_outcome'), protocol_outcome_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 698, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'secondary_outcome'), protocol_outcome_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 699, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'other_outcome'), protocol_outcome_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 700, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'number_of_arms'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 701, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'number_of_groups'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 702, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'enrollment'), enrollment_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 703, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'condition'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 704, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'arm_group'), arm_group_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 705, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'intervention'), intervention_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 706, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'biospec_retention'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 707, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'biospec_descr'), textblock_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 708, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'eligibility'), eligibility_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 709, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'overall_official'), investigator_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 710, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'overall_contact'), contact_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 711, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'overall_contact_backup'), contact_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 712, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), location_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 713, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location_countries'), countries_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 714, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'removed_countries'), countries_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 715, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'link'), link_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 716, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'reference'), reference_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 717, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'results_reference'), reference_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 718, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'verification_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 719, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'lastchanged_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 720, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'firstreceived_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 721, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'firstreceived_results_date'), date_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 722, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'responsible_party'), responsible_party_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 723, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'keyword'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 724, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is_fda_regulated'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 725, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'is_section_801'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 726, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'has_expanded_access'), pyxb.binding.datatypes.string, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 727, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'condition_browse'), browse_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 728, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'intervention_browse'), browse_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 729, 8)))

CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'clinical_results'), clinical_results_struct, scope=CTD_ANON_17, location=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 730, 8)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 681, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 682, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 685, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 686, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 687, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 689, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 690, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 691, 8))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 692, 8))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 693, 8))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 698, 8))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 699, 8))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 700, 8))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 701, 8))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 702, 8))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 703, 8))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 704, 8))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 705, 8))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 706, 8))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 707, 8))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 708, 8))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 709, 8))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 710, 8))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 711, 8))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 712, 8))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 713, 8))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 714, 8))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 715, 8))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 716, 8))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 717, 8))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 718, 8))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 719, 8))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 720, 8))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 722, 8))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 723, 8))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 724, 8))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 725, 8))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 726, 8))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 727, 8))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 728, 8))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 729, 8))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 730, 8))
    counters.add(cc_41)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'required_header')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 678, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'id_info')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 679, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'brief_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 680, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'acronym')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 681, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'official_title')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 682, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'sponsors')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 683, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'source')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 684, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'oversight_info')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 685, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'brief_summary')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 686, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'detailed_description')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 687, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'overall_status')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 688, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'why_stopped')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 689, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'start_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 690, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'end_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 691, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'completion_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 692, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'primary_completion_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 693, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'phase')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 694, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'study_type')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 695, 8))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'study_design')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 696, 8))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'target_duration')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 697, 8))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'primary_outcome')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 698, 8))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'secondary_outcome')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 699, 8))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'other_outcome')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 700, 8))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'number_of_arms')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 701, 8))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'number_of_groups')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 702, 8))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'enrollment')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 703, 8))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'condition')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 704, 8))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'arm_group')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 705, 8))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'intervention')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 706, 8))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'biospec_retention')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 707, 8))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'biospec_descr')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 708, 8))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'eligibility')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 709, 8))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'overall_official')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 710, 8))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'overall_contact')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 711, 8))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'overall_contact_backup')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 712, 8))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 713, 8))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'location_countries')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 714, 8))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'removed_countries')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 715, 8))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'link')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 716, 8))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'reference')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 717, 8))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'results_reference')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 718, 8))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'verification_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 719, 8))
    st_41 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'lastchanged_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 720, 8))
    st_42 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'firstreceived_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 721, 8))
    st_43 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'firstreceived_results_date')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 722, 8))
    st_44 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'responsible_party')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 723, 8))
    st_45 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_45)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'keyword')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 724, 8))
    st_46 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_46)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'is_fda_regulated')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 725, 8))
    st_47 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_47)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'is_section_801')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 726, 8))
    st_48 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_48)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'has_expanded_access')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 727, 8))
    st_49 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_49)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'condition_browse')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 728, 8))
    st_50 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_50)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'intervention_browse')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 729, 8))
    st_51 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_51)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(None, u'clinical_results')), pyxb.utils.utility.Location('http://clinicaltrials.gov/ct2/html/images/info/public.xsd', 730, 8))
    st_52 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_52)
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
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
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
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    transitions.append(fac.Transition(st_41, [
         ]))
    transitions.append(fac.Transition(st_42, [
         ]))
    transitions.append(fac.Transition(st_43, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
         ]))
    transitions.append(fac.Transition(st_45, [
         ]))
    transitions.append(fac.Transition(st_46, [
         ]))
    transitions.append(fac.Transition(st_47, [
         ]))
    transitions.append(fac.Transition(st_48, [
         ]))
    transitions.append(fac.Transition(st_49, [
         ]))
    transitions.append(fac.Transition(st_50, [
         ]))
    transitions.append(fac.Transition(st_51, [
         ]))
    transitions.append(fac.Transition(st_52, [
         ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_44._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_45, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_45._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_46, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_46._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_47, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_47._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_48, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_48._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_49, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_49._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_50, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_50._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_51, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_51._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_52, [
        fac.UpdateInstruction(cc_41, True) ]))
    st_52._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_55()

