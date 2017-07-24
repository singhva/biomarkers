# ./schema/uniprot_org.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:8c04c93a68fd0ee0b2faec7d005fb345adc8757f
# Generated 2014-04-29 11:42:06.366788 by PyXB version 1.2.3
# Namespace http://uniprot.org/uniprot

import io
import sys

import pyxb
import pyxb.binding
import pyxb.binding.datatypes
import pyxb.binding.saxer
import pyxb.utils.domutils
import pyxb.utils.utility


# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d127226b-cfb4-11e3-8508-14109fd9e1c1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://uniprot.org/uniprot', create_if_missing=True)
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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 56, 16)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Swiss_Prot = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'Swiss-Prot', tag=u'Swiss_Prot')
STD_ANON.TrEMBL = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'TrEMBL', tag=u'TrEMBL')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 158, 20)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.primary = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'primary', tag=u'primary')
STD_ANON_.synonym = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'synonym', tag=u'synonym')
STD_ANON_.ordered_locus = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'ordered locus', tag=u'ordered_locus')
STD_ANON_.ORF = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'ORF', tag=u'ORF')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 211, 20)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.common = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'common', tag=u'common')
STD_ANON_2.full = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'full', tag=u'full')
STD_ANON_2.scientific = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'scientific', tag=u'scientific')
STD_ANON_2.synonym = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'synonym', tag=u'synonym')
STD_ANON_2.abbreviation = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'abbreviation', tag=u'abbreviation')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 236, 12)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.apicoplast = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'apicoplast', tag=u'apicoplast')
STD_ANON_3.chloroplast = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'chloroplast', tag=u'chloroplast')
STD_ANON_3.organellar_chromatophore = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'organellar chromatophore', tag=u'organellar_chromatophore')
STD_ANON_3.cyanelle = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'cyanelle', tag=u'cyanelle')
STD_ANON_3.hydrogenosome = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'hydrogenosome', tag=u'hydrogenosome')
STD_ANON_3.mitochondrion = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'mitochondrion', tag=u'mitochondrion')
STD_ANON_3.non_photosynthetic_plastid = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'non-photosynthetic plastid', tag=u'non_photosynthetic_plastid')
STD_ANON_3.nucleomorph = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'nucleomorph', tag=u'nucleomorph')
STD_ANON_3.plasmid = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'plasmid', tag=u'plasmid')
STD_ANON_3.plastid = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value=u'plastid', tag=u'plastid')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 260, 20)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.known = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'known', tag=u'known')
STD_ANON_4.unknown = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 329, 12)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.book = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'book', tag=u'book')
STD_ANON_5.journal_article = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'journal article', tag=u'journal_article')
STD_ANON_5.online_journal_article = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'online journal article', tag=u'online_journal_article')
STD_ANON_5.patent = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'patent', tag=u'patent')
STD_ANON_5.submission = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'submission', tag=u'submission')
STD_ANON_5.thesis = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'thesis', tag=u'thesis')
STD_ANON_5.unpublished_observations = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value=u'unpublished observations', tag=u'unpublished_observations')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_6 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 342, 12)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.date, pyxb.binding.datatypes.gYearMonth, pyxb.binding.datatypes.gYear, )
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6)
STD_ANON_6._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration,
   STD_ANON_6._CF_pattern)

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 502, 40)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.EMBL_CDS = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'EMBL-CDS', tag=u'EMBL_CDS')
STD_ANON_7.EMBL = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value=u'EMBL', tag=u'EMBL')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 515, 28)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.frameshift = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'frameshift', tag=u'frameshift')
STD_ANON_8.erroneous_initiation = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'erroneous initiation', tag=u'erroneous_initiation')
STD_ANON_8.erroneous_termination = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'erroneous termination', tag=u'erroneous_termination')
STD_ANON_8.erroneous_gene_model_prediction = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'erroneous gene model prediction', tag=u'erroneous_gene_model_prediction')
STD_ANON_8.erroneous_translation = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'erroneous translation', tag=u'erroneous_translation')
STD_ANON_8.miscellaneous_discrepancy = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value=u'miscellaneous discrepancy', tag=u'miscellaneous_discrepancy')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 598, 12)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.allergen = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'allergen', tag=u'allergen')
STD_ANON_9.alternative_products = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'alternative products', tag=u'alternative_products')
STD_ANON_9.biotechnology = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'biotechnology', tag=u'biotechnology')
STD_ANON_9.biophysicochemical_properties = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'biophysicochemical properties', tag=u'biophysicochemical_properties')
STD_ANON_9.catalytic_activity = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'catalytic activity', tag=u'catalytic_activity')
STD_ANON_9.caution = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'caution', tag=u'caution')
STD_ANON_9.cofactor = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'cofactor', tag=u'cofactor')
STD_ANON_9.developmental_stage = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'developmental stage', tag=u'developmental_stage')
STD_ANON_9.disease = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'disease', tag=u'disease')
STD_ANON_9.domain = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'domain', tag=u'domain')
STD_ANON_9.disruption_phenotype = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'disruption phenotype', tag=u'disruption_phenotype')
STD_ANON_9.enzyme_regulation = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'enzyme regulation', tag=u'enzyme_regulation')
STD_ANON_9.function = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'function', tag=u'function')
STD_ANON_9.induction = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'induction', tag=u'induction')
STD_ANON_9.miscellaneous = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'miscellaneous', tag=u'miscellaneous')
STD_ANON_9.pathway = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'pathway', tag=u'pathway')
STD_ANON_9.pharmaceutical = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'pharmaceutical', tag=u'pharmaceutical')
STD_ANON_9.polymorphism = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'polymorphism', tag=u'polymorphism')
STD_ANON_9.PTM = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'PTM', tag=u'PTM')
STD_ANON_9.RNA_editing = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'RNA editing', tag=u'RNA_editing')
STD_ANON_9.similarity = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'similarity', tag=u'similarity')
STD_ANON_9.subcellular_location = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'subcellular location', tag=u'subcellular_location')
STD_ANON_9.sequence_caution = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'sequence caution', tag=u'sequence_caution')
STD_ANON_9.subunit = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'subunit', tag=u'subunit')
STD_ANON_9.tissue_specificity = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'tissue specificity', tag=u'tissue_specificity')
STD_ANON_9.toxic_dose = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'toxic dose', tag=u'toxic_dose')
STD_ANON_9.online_information = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'online information', tag=u'online_information')
STD_ANON_9.mass_spectrometry = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'mass spectrometry', tag=u'mass_spectrometry')
STD_ANON_9.interaction = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value=u'interaction', tag=u'interaction')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 708, 12)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.alternative_splicing = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'alternative splicing', tag=u'alternative_splicing')
STD_ANON_10.alternative_initiation = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'alternative initiation', tag=u'alternative_initiation')
STD_ANON_10.alternative_promoter = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'alternative promoter', tag=u'alternative_promoter')
STD_ANON_10.ribosomal_frameshifting = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value=u'ribosomal frameshifting', tag=u'ribosomal_frameshifting')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 737, 24)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.not_described = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'not described', tag=u'not_described')
STD_ANON_11.described = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'described', tag=u'described')
STD_ANON_11.displayed = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'displayed', tag=u'displayed')
STD_ANON_11.external = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value=u'external', tag=u'external')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 811, 12)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.evidence_at_protein_level = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'evidence at protein level', tag=u'evidence_at_protein_level')
STD_ANON_12.evidence_at_transcript_level = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'evidence at transcript level', tag=u'evidence_at_transcript_level')
STD_ANON_12.inferred_from_homology = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'inferred from homology', tag=u'inferred_from_homology')
STD_ANON_12.predicted = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'predicted', tag=u'predicted')
STD_ANON_12.uncertain = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value=u'uncertain', tag=u'uncertain')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 863, 12)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.active_site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'active site', tag=u'active_site')
STD_ANON_13.binding_site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'binding site', tag=u'binding_site')
STD_ANON_13.calcium_binding_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'calcium-binding region', tag=u'calcium_binding_region')
STD_ANON_13.chain = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'chain', tag=u'chain')
STD_ANON_13.coiled_coil_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'coiled-coil region', tag=u'coiled_coil_region')
STD_ANON_13.compositionally_biased_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'compositionally biased region', tag=u'compositionally_biased_region')
STD_ANON_13.cross_link = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'cross-link', tag=u'cross_link')
STD_ANON_13.disulfide_bond = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'disulfide bond', tag=u'disulfide_bond')
STD_ANON_13.DNA_binding_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'DNA-binding region', tag=u'DNA_binding_region')
STD_ANON_13.domain = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'domain', tag=u'domain')
STD_ANON_13.glycosylation_site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'glycosylation site', tag=u'glycosylation_site')
STD_ANON_13.helix = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'helix', tag=u'helix')
STD_ANON_13.initiator_methionine = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'initiator methionine', tag=u'initiator_methionine')
STD_ANON_13.lipid_moiety_binding_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'lipid moiety-binding region', tag=u'lipid_moiety_binding_region')
STD_ANON_13.metal_ion_binding_site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'metal ion-binding site', tag=u'metal_ion_binding_site')
STD_ANON_13.modified_residue = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'modified residue', tag=u'modified_residue')
STD_ANON_13.mutagenesis_site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'mutagenesis site', tag=u'mutagenesis_site')
STD_ANON_13.non_consecutive_residues = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'non-consecutive residues', tag=u'non_consecutive_residues')
STD_ANON_13.non_terminal_residue = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'non-terminal residue', tag=u'non_terminal_residue')
STD_ANON_13.nucleotide_phosphate_binding_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'nucleotide phosphate-binding region', tag=u'nucleotide_phosphate_binding_region')
STD_ANON_13.peptide = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'peptide', tag=u'peptide')
STD_ANON_13.propeptide = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'propeptide', tag=u'propeptide')
STD_ANON_13.region_of_interest = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'region of interest', tag=u'region_of_interest')
STD_ANON_13.repeat = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'repeat', tag=u'repeat')
STD_ANON_13.non_standard_amino_acid = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'non-standard amino acid', tag=u'non_standard_amino_acid')
STD_ANON_13.sequence_conflict = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'sequence conflict', tag=u'sequence_conflict')
STD_ANON_13.sequence_variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'sequence variant', tag=u'sequence_variant')
STD_ANON_13.short_sequence_motif = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'short sequence motif', tag=u'short_sequence_motif')
STD_ANON_13.signal_peptide = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'signal peptide', tag=u'signal_peptide')
STD_ANON_13.site = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'site', tag=u'site')
STD_ANON_13.splice_variant = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'splice variant', tag=u'splice_variant')
STD_ANON_13.strand = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'strand', tag=u'strand')
STD_ANON_13.topological_domain = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'topological domain', tag=u'topological_domain')
STD_ANON_13.transit_peptide = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'transit peptide', tag=u'transit_peptide')
STD_ANON_13.transmembrane_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'transmembrane region', tag=u'transmembrane_region')
STD_ANON_13.turn = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'turn', tag=u'turn')
STD_ANON_13.unsure_residue = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'unsure residue', tag=u'unsure_residue')
STD_ANON_13.zinc_finger_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'zinc finger region', tag=u'zinc_finger_region')
STD_ANON_13.intramembrane_region = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value=u'intramembrane region', tag=u'intramembrane_region')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 908, 12)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.by_similarity = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'by similarity', tag=u'by_similarity')
STD_ANON_14.probable = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'probable', tag=u'probable')
STD_ANON_14.potential = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value=u'potential', tag=u'potential')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 939, 12)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.certain = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'certain', tag=u'certain')
STD_ANON_15.uncertain = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'uncertain', tag=u'uncertain')
STD_ANON_15.less_than = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'less than', tag=u'less_than')
STD_ANON_15.greater_than = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'greater than', tag=u'greater_than')
STD_ANON_15.unknown = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value=u'unknown', tag=u'unknown')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 964, 20)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.single = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'single', tag=u'single')
STD_ANON_16.multiple = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value=u'multiple', tag=u'multiple')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1034, 20)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.by_similarity = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'by similarity', tag=u'by_similarity')
STD_ANON_17.probable = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'probable', tag=u'probable')
STD_ANON_17.potential = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value=u'potential', tag=u'potential')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)

# List simple type: {http://uniprot.org/uniprot}intListType
# superclasses pyxb.binding.datatypes.anySimpleType
class intListType (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.int."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'intListType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1046, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.int
intListType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'intListType', intListType)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Describes a collection of UniProtKB entries."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 23, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'entry'), 'entry', '__httpuniprot_orguniprot_CTD_ANON_httpuniprot_orguniprotentry', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 33, 4), )

    
    entry = property(__entry.value, __entry.set, None, u'Describes a UniProtKB entry.')

    
    # Element {http://uniprot.org/uniprot}copyright uses Python identifier copyright
    __copyright = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'copyright'), 'copyright', '__httpuniprot_orguniprot_CTD_ANON_httpuniprot_orguniprotcopyright', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 70, 4), )

    
    copyright = property(__copyright.value, __copyright.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry,
        __copyright.name() : __copyright
    })
    _AttributeMap.update({
        
    })



# Complex type {http://uniprot.org/uniprot}proteinType with content type ELEMENT_ONLY
class proteinType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the names for the protein and parts thereof.
            Equivalent to the flat file DE-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'proteinType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 73, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}domain uses Python identifier domain
    __domain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'domain'), 'domain', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotdomain', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 80, 12), )

    
    domain = property(__domain.value, __domain.set, None, u'Describes names of "domains".\n                    Equivalent to the flat file DE-line Includes: section.')

    
    # Element {http://uniprot.org/uniprot}component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'component'), 'component', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotcomponent', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 89, 12), )

    
    component = property(__component.value, __component.set, None, u'Describes names of processed products.\n                    Equivalent to the flat file DE-line Contains: section.')

    
    # Element {http://uniprot.org/uniprot}recommendedName uses Python identifier recommendedName
    __recommendedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), 'recommendedName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotrecommendedName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12), )

    
    recommendedName = property(__recommendedName.value, __recommendedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}alternativeName uses Python identifier alternativeName
    __alternativeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), 'alternativeName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotalternativeName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12), )

    
    alternativeName = property(__alternativeName.value, __alternativeName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}submittedName uses Python identifier submittedName
    __submittedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), 'submittedName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotsubmittedName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12), )

    
    submittedName = property(__submittedName.value, __submittedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}allergenName uses Python identifier allergenName
    __allergenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), 'allergenName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotallergenName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12), )

    
    allergenName = property(__allergenName.value, __allergenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}biotechName uses Python identifier biotechName
    __biotechName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), 'biotechName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotbiotechName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12), )

    
    biotechName = property(__biotechName.value, __biotechName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}cdAntigenName uses Python identifier cdAntigenName
    __cdAntigenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), 'cdAntigenName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotcdAntigenName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12), )

    
    cdAntigenName = property(__cdAntigenName.value, __cdAntigenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}innName uses Python identifier innName
    __innName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'innName'), 'innName', '__httpuniprot_orguniprot_proteinType_httpuniprot_orguniprotinnName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12), )

    
    innName = property(__innName.value, __innName.set, None, None)

    _ElementMap.update({
        __domain.name() : __domain,
        __component.name() : __component,
        __recommendedName.name() : __recommendedName,
        __alternativeName.name() : __alternativeName,
        __submittedName.name() : __submittedName,
        __allergenName.name() : __allergenName,
        __biotechName.name() : __biotechName,
        __cdAntigenName.name() : __cdAntigenName,
        __innName.name() : __innName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'proteinType', proteinType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Describes names of "domains".
                    Equivalent to the flat file DE-line Includes: section."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 85, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}recommendedName uses Python identifier recommendedName
    __recommendedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), 'recommendedName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotrecommendedName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12), )

    
    recommendedName = property(__recommendedName.value, __recommendedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}alternativeName uses Python identifier alternativeName
    __alternativeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), 'alternativeName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotalternativeName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12), )

    
    alternativeName = property(__alternativeName.value, __alternativeName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}submittedName uses Python identifier submittedName
    __submittedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), 'submittedName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotsubmittedName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12), )

    
    submittedName = property(__submittedName.value, __submittedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}allergenName uses Python identifier allergenName
    __allergenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), 'allergenName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotallergenName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12), )

    
    allergenName = property(__allergenName.value, __allergenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}biotechName uses Python identifier biotechName
    __biotechName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), 'biotechName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotbiotechName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12), )

    
    biotechName = property(__biotechName.value, __biotechName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}cdAntigenName uses Python identifier cdAntigenName
    __cdAntigenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), 'cdAntigenName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotcdAntigenName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12), )

    
    cdAntigenName = property(__cdAntigenName.value, __cdAntigenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}innName uses Python identifier innName
    __innName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'innName'), 'innName', '__httpuniprot_orguniprot_CTD_ANON__httpuniprot_orguniprotinnName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12), )

    
    innName = property(__innName.value, __innName.set, None, None)

    _ElementMap.update({
        __recommendedName.name() : __recommendedName,
        __alternativeName.name() : __alternativeName,
        __submittedName.name() : __submittedName,
        __allergenName.name() : __allergenName,
        __biotechName.name() : __biotechName,
        __cdAntigenName.name() : __cdAntigenName,
        __innName.name() : __innName
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Describes names of processed products.
                    Equivalent to the flat file DE-line Contains: section."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 94, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}recommendedName uses Python identifier recommendedName
    __recommendedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), 'recommendedName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotrecommendedName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12), )

    
    recommendedName = property(__recommendedName.value, __recommendedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}alternativeName uses Python identifier alternativeName
    __alternativeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), 'alternativeName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotalternativeName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12), )

    
    alternativeName = property(__alternativeName.value, __alternativeName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}submittedName uses Python identifier submittedName
    __submittedName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), 'submittedName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotsubmittedName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12), )

    
    submittedName = property(__submittedName.value, __submittedName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}allergenName uses Python identifier allergenName
    __allergenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), 'allergenName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotallergenName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12), )

    
    allergenName = property(__allergenName.value, __allergenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}biotechName uses Python identifier biotechName
    __biotechName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), 'biotechName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotbiotechName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12), )

    
    biotechName = property(__biotechName.value, __biotechName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}cdAntigenName uses Python identifier cdAntigenName
    __cdAntigenName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), 'cdAntigenName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotcdAntigenName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12), )

    
    cdAntigenName = property(__cdAntigenName.value, __cdAntigenName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}innName uses Python identifier innName
    __innName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'innName'), 'innName', '__httpuniprot_orguniprot_CTD_ANON_2_httpuniprot_orguniprotinnName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12), )

    
    innName = property(__innName.value, __innName.set, None, None)

    _ElementMap.update({
        __recommendedName.name() : __recommendedName,
        __alternativeName.name() : __alternativeName,
        __submittedName.name() : __submittedName,
        __allergenName.name() : __allergenName,
        __biotechName.name() : __biotechName,
        __cdAntigenName.name() : __cdAntigenName,
        __innName.name() : __innName
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 103, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}fullName uses Python identifier fullName
    __fullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fullName'), 'fullName', '__httpuniprot_orguniprot_CTD_ANON_3_httpuniprot_orguniprotfullName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 105, 24), )

    
    fullName = property(__fullName.value, __fullName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}shortName uses Python identifier shortName
    __shortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shortName'), 'shortName', '__httpuniprot_orguniprot_CTD_ANON_3_httpuniprot_orguniprotshortName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 106, 24), )

    
    shortName = property(__shortName.value, __shortName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}ecNumber uses Python identifier ecNumber
    __ecNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), 'ecNumber', '__httpuniprot_orguniprot_CTD_ANON_3_httpuniprot_orguniprotecNumber', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 107, 24), )

    
    ecNumber = property(__ecNumber.value, __ecNumber.set, None, None)

    _ElementMap.update({
        __fullName.name() : __fullName,
        __shortName.name() : __shortName,
        __ecNumber.name() : __ecNumber
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 113, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}fullName uses Python identifier fullName
    __fullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fullName'), 'fullName', '__httpuniprot_orguniprot_CTD_ANON_4_httpuniprot_orguniprotfullName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 115, 24), )

    
    fullName = property(__fullName.value, __fullName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}shortName uses Python identifier shortName
    __shortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'shortName'), 'shortName', '__httpuniprot_orguniprot_CTD_ANON_4_httpuniprot_orguniprotshortName', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 116, 24), )

    
    shortName = property(__shortName.value, __shortName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}ecNumber uses Python identifier ecNumber
    __ecNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), 'ecNumber', '__httpuniprot_orguniprot_CTD_ANON_4_httpuniprot_orguniprotecNumber', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 117, 24), )

    
    ecNumber = property(__ecNumber.value, __ecNumber.set, None, None)

    _ElementMap.update({
        __fullName.name() : __fullName,
        __shortName.name() : __shortName,
        __ecNumber.name() : __ecNumber
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 123, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}fullName uses Python identifier fullName
    __fullName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fullName'), 'fullName', '__httpuniprot_orguniprot_CTD_ANON_5_httpuniprot_orguniprotfullName', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 125, 24), )

    
    fullName = property(__fullName.value, __fullName.set, None, None)

    
    # Element {http://uniprot.org/uniprot}ecNumber uses Python identifier ecNumber
    __ecNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), 'ecNumber', '__httpuniprot_orguniprot_CTD_ANON_5_httpuniprot_orguniprotecNumber', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 126, 24), )

    
    ecNumber = property(__ecNumber.value, __ecNumber.set, None, None)

    _ElementMap.update({
        __fullName.name() : __fullName,
        __ecNumber.name() : __ecNumber
    })
    _AttributeMap.update({
        
    })



# Complex type {http://uniprot.org/uniprot}geneType with content type ELEMENT_ONLY
class geneType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a gene.
            Equivalent to the flat file GN-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'geneType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 140, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_geneType_httpuniprot_orguniprotname', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 146, 12), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'geneType', geneType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Describes the lineage of the source organism.
                    Equivalent to the flat file OC-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 195, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}taxon uses Python identifier taxon
    __taxon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'taxon'), 'taxon', '__httpuniprot_orguniprot_CTD_ANON_6_httpuniprot_orguniprottaxon', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 197, 24), )

    
    taxon = property(__taxon.value, __taxon.set, None, None)

    _ElementMap.update({
        __taxon.name() : __taxon
    })
    _AttributeMap.update({
        
    })



# Complex type {http://uniprot.org/uniprot}consortiumType with content type EMPTY
class consortiumType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the authors of a citation when these are represented by a consortium.
            Equivalent to the flat file RG-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'consortiumType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 397, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpuniprot_orguniprot_consortiumType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 402, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 402, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'consortiumType', consortiumType)


# Complex type {http://uniprot.org/uniprot}personType with content type EMPTY
class personType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}personType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 404, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpuniprot_orguniprot_personType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 405, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 405, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'personType', personType)


# Complex type {http://uniprot.org/uniprot}nameListType with content type ELEMENT_ONLY
class nameListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}nameListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameListType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 407, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}consortium uses Python identifier consortium
    __consortium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'consortium'), 'consortium', '__httpuniprot_orguniprot_nameListType_httpuniprot_orguniprotconsortium', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 409, 12), )

    
    consortium = property(__consortium.value, __consortium.set, None, None)

    
    # Element {http://uniprot.org/uniprot}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'person'), 'person', '__httpuniprot_orguniprot_nameListType_httpuniprot_orguniprotperson', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 410, 12), )

    
    person = property(__person.value, __person.set, None, None)

    _ElementMap.update({
        __consortium.name() : __consortium,
        __person.name() : __person
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'nameListType', nameListType)


# Complex type {http://uniprot.org/uniprot}sourceDataType with content type ELEMENT_ONLY
class sourceDataType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the source of the sequence according to the citation.
            Equivalent to the flat file RC-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceDataType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 430, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}strain uses Python identifier strain
    __strain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'strain'), 'strain', '__httpuniprot_orguniprot_sourceDataType_httpuniprot_orguniprotstrain', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 436, 12), )

    
    strain = property(__strain.value, __strain.set, None, None)

    
    # Element {http://uniprot.org/uniprot}plasmid uses Python identifier plasmid
    __plasmid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'plasmid'), 'plasmid', '__httpuniprot_orguniprot_sourceDataType_httpuniprot_orguniprotplasmid', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 445, 12), )

    
    plasmid = property(__plasmid.value, __plasmid.set, None, None)

    
    # Element {http://uniprot.org/uniprot}transposon uses Python identifier transposon
    __transposon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'transposon'), 'transposon', '__httpuniprot_orguniprot_sourceDataType_httpuniprot_orguniprottransposon', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 454, 12), )

    
    transposon = property(__transposon.value, __transposon.set, None, None)

    
    # Element {http://uniprot.org/uniprot}tissue uses Python identifier tissue
    __tissue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tissue'), 'tissue', '__httpuniprot_orguniprot_sourceDataType_httpuniprot_orguniprottissue', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 463, 12), )

    
    tissue = property(__tissue.value, __tissue.set, None, None)

    _ElementMap.update({
        __strain.name() : __strain,
        __plasmid.name() : __plasmid,
        __transposon.name() : __transposon,
        __tissue.name() : __tissue
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'sourceDataType', sourceDataType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Used in 'online information' annotations."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 539, 24)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpuniprot_orguniprot_CTD_ANON_7_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 540, 28)
    __uri._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 540, 28)
    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Used in 'disease' annotations."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 566, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_CTD_ANON_8_httpuniprot_orguniprotname', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 568, 28), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://uniprot.org/uniprot}acronym uses Python identifier acronym
    __acronym = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'acronym'), 'acronym', '__httpuniprot_orguniprot_CTD_ANON_8_httpuniprot_orguniprotacronym', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 569, 28), )

    
    acronym = property(__acronym.value, __acronym.set, None, None)

    
    # Element {http://uniprot.org/uniprot}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpuniprot_orguniprot_CTD_ANON_8_httpuniprot_orguniprotdescription', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 570, 28), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_CTD_ANON_8_httpuniprot_orguniprotdbReference', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 571, 28), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_CTD_ANON_8_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 573, 24)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 573, 24)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __acronym.name() : __acronym,
        __description.name() : __description,
        __dbReference.name() : __dbReference
    })
    _AttributeMap.update({
        __id.name() : __id
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 670, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'max'), 'max', '__httpuniprot_orguniprot_CTD_ANON_9_httpuniprot_orguniprotmax', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 672, 24), )

    
    max = property(__max.value, __max.set, None, None)

    
    # Element {http://uniprot.org/uniprot}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'text'), 'text', '__httpuniprot_orguniprot_CTD_ANON_9_httpuniprot_orguniprottext', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 673, 24), )

    
    text = property(__text.value, __text.set, None, None)

    _ElementMap.update({
        __max.name() : __max,
        __text.name() : __text
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
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 678, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}KM uses Python identifier KM
    __KM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'KM'), 'KM', '__httpuniprot_orguniprot_CTD_ANON_10_httpuniprot_orguniprotKM', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 680, 24), )

    
    KM = property(__KM.value, __KM.set, None, None)

    
    # Element {http://uniprot.org/uniprot}Vmax uses Python identifier Vmax
    __Vmax = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Vmax'), 'Vmax', '__httpuniprot_orguniprot_CTD_ANON_10_httpuniprot_orguniprotVmax', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 681, 24), )

    
    Vmax = property(__Vmax.value, __Vmax.set, None, None)

    
    # Element {http://uniprot.org/uniprot}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'text'), 'text', '__httpuniprot_orguniprot_CTD_ANON_10_httpuniprot_orguniprottext', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 682, 24), )

    
    text = property(__text.value, __text.set, None, None)

    _ElementMap.update({
        __KM.name() : __KM,
        __Vmax.name() : __Vmax,
        __text.name() : __text
    })
    _AttributeMap.update({
        
    })



# Complex type {http://uniprot.org/uniprot}subcellularLocationType with content type ELEMENT_ONLY
class subcellularLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the subcellular location and optionally the topology and orientation of a molecule."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'subcellularLocationType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 692, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'location'), 'location', '__httpuniprot_orguniprot_subcellularLocationType_httpuniprot_orguniprotlocation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 697, 12), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element {http://uniprot.org/uniprot}topology uses Python identifier topology
    __topology = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'topology'), 'topology', '__httpuniprot_orguniprot_subcellularLocationType_httpuniprot_orguniprottopology', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 698, 12), )

    
    topology = property(__topology.value, __topology.set, None, None)

    
    # Element {http://uniprot.org/uniprot}orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'orientation'), 'orientation', '__httpuniprot_orguniprot_subcellularLocationType_httpuniprot_orguniprotorientation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 699, 12), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __topology.name() : __topology,
        __orientation.name() : __orientation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'subcellularLocationType', subcellularLocationType)


# Complex type {http://uniprot.org/uniprot}isoformType with content type ELEMENT_ONLY
class isoformType (pyxb.binding.basis.complexTypeDefinition):
    """Describes isoforms in 'alternative products' annotations."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'isoformType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 719, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpuniprot_orguniprot_isoformType_httpuniprot_orguniprotid', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 724, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_isoformType_httpuniprot_orguniprotname', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 725, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://uniprot.org/uniprot}sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sequence'), 'sequence', '__httpuniprot_orguniprot_isoformType_httpuniprot_orguniprotsequence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 734, 12), )

    
    sequence = property(__sequence.value, __sequence.set, None, None)

    
    # Element {http://uniprot.org/uniprot}note uses Python identifier note
    __note = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'note'), 'note', '__httpuniprot_orguniprot_isoformType_httpuniprot_orguniprotnote', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 749, 12), )

    
    note = property(__note.value, __note.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __name.name() : __name,
        __sequence.name() : __sequence,
        __note.name() : __note
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'isoformType', isoformType)


# Complex type {http://uniprot.org/uniprot}interactantType with content type ELEMENT_ONLY
class interactantType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}interactantType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'interactantType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 767, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'id'), 'id', '__httpuniprot_orguniprot_interactantType_httpuniprot_orguniprotid', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 763, 12), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://uniprot.org/uniprot}label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'label'), 'label', '__httpuniprot_orguniprot_interactantType_httpuniprot_orguniprotlabel', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 764, 12), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute intactId uses Python identifier intactId
    __intactId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'intactId'), 'intactId', '__httpuniprot_orguniprot_interactantType_intactId', pyxb.binding.datatypes.string, required=True)
    __intactId._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 769, 8)
    __intactId._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 769, 8)
    
    intactId = property(__intactId.value, __intactId.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __label.name() : __label
    })
    _AttributeMap.update({
        __intactId.name() : __intactId
    })
Namespace.addCategoryObject('typeBinding', u'interactantType', interactantType)


# Complex type {http://uniprot.org/uniprot}propertyType with content type EMPTY
class propertyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}propertyType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'propertyType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 798, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_propertyType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 799, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 799, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'value'), 'value_', '__httpuniprot_orguniprot_propertyType_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 800, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 800, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', u'propertyType', propertyType)


# Complex type {http://uniprot.org/uniprot}locationType with content type ELEMENT_ONLY
class locationType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a sequence location as either a range with a begin and end or as a position. The 'sequence' attribute is only used when the location is not on the canonical sequence displayed in the current entry."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'locationType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 922, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'begin'), 'begin', '__httpuniprot_orguniprot_locationType_httpuniprot_orguniprotbegin', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 928, 16), )

    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Element {http://uniprot.org/uniprot}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'end'), 'end', '__httpuniprot_orguniprot_locationType_httpuniprot_orguniprotend', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 929, 16), )

    
    end = property(__end.value, __end.set, None, None)

    
    # Element {http://uniprot.org/uniprot}position uses Python identifier position
    __position = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'position'), 'position', '__httpuniprot_orguniprot_locationType_httpuniprot_orguniprotposition', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 931, 12), )

    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sequence'), 'sequence', '__httpuniprot_orguniprot_locationType_sequence', pyxb.binding.datatypes.string)
    __sequence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 933, 8)
    __sequence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 933, 8)
    
    sequence = property(__sequence.value, __sequence.set, None, None)

    _ElementMap.update({
        __begin.name() : __begin,
        __end.name() : __end,
        __position.name() : __position
    })
    _AttributeMap.update({
        __sequence.name() : __sequence
    })
Namespace.addCategoryObject('typeBinding', u'locationType', locationType)


# Complex type {http://uniprot.org/uniprot}moleculeType with content type SIMPLE
class moleculeType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a molecule by name or unique identifier."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'moleculeType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 977, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_moleculeType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 983, 16)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 983, 16)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'moleculeType', moleculeType)


# Complex type {http://uniprot.org/uniprot}evidenceType with content type ELEMENT_ONLY
class evidenceType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the evidence for an annotation.
            No flat file equivalent."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'evidenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 990, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpuniprot_orguniprot_evidenceType_httpuniprot_orguniprotsource', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 996, 12), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Element {http://uniprot.org/uniprot}importedFrom uses Python identifier importedFrom
    __importedFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'importedFrom'), 'importedFrom', '__httpuniprot_orguniprot_evidenceType_httpuniprot_orguniprotimportedFrom', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 997, 12), )

    
    importedFrom = property(__importedFrom.value, __importedFrom.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_evidenceType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 999, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 999, 8)
    
    type = property(__type.value, __type.set, None, u'Describes the type of an evidence using the Evidence Code Ontology (http://www.obofoundry.org/cgi-bin/detail.cgi?id=evidence_code).')

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__httpuniprot_orguniprot_evidenceType_key', pyxb.binding.datatypes.integer, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1004, 8)
    __key._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1004, 8)
    
    key = property(__key.value, __key.set, None, u"A unique key to link annotations (via 'evidence' attributes) to evidences.")

    _ElementMap.update({
        __source.name() : __source,
        __importedFrom.name() : __importedFrom
    })
    _AttributeMap.update({
        __type.name() : __type,
        __key.name() : __key
    })
Namespace.addCategoryObject('typeBinding', u'evidenceType', evidenceType)


# Complex type {http://uniprot.org/uniprot}sourceType with content type ELEMENT_ONLY
class sourceType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the source of the data using a database cross-reference (or a 'ref' attribute when the source cannot be found in a public data source, such as PubMed, and is cited only within the UniProtKB entry)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sourceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1010, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_sourceType_httpuniprot_orguniprotdbReference', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1015, 12), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpuniprot_orguniprot_sourceType_ref', pyxb.binding.datatypes.integer)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1017, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1017, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        __dbReference.name() : __dbReference
    })
    _AttributeMap.update({
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', u'sourceType', sourceType)


# Complex type {http://uniprot.org/uniprot}importedFromType with content type ELEMENT_ONLY
class importedFromType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the source of the evidence, when it is not assigned by UniProt, but imported from an external database."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'importedFromType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1019, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_importedFromType_httpuniprot_orguniprotdbReference', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1024, 12), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, None)

    _ElementMap.update({
        __dbReference.name() : __dbReference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'importedFromType', importedFromType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Describes a UniProtKB entry."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 37, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}accession uses Python identifier accession
    __accession = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'accession'), 'accession', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotaccession', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 39, 16), )

    
    accession = property(__accession.value, __accession.set, None, None)

    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotname', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 40, 16), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://uniprot.org/uniprot}protein uses Python identifier protein
    __protein = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'protein'), 'protein', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotprotein', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 41, 16), )

    
    protein = property(__protein.value, __protein.set, None, None)

    
    # Element {http://uniprot.org/uniprot}gene uses Python identifier gene
    __gene = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'gene'), 'gene', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotgene', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 42, 16), )

    
    gene = property(__gene.value, __gene.set, None, None)

    
    # Element {http://uniprot.org/uniprot}organism uses Python identifier organism
    __organism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organism'), 'organism', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotorganism', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 43, 16), )

    
    organism = property(__organism.value, __organism.set, None, None)

    
    # Element {http://uniprot.org/uniprot}organismHost uses Python identifier organismHost
    __organismHost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organismHost'), 'organismHost', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotorganismHost', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 44, 16), )

    
    organismHost = property(__organismHost.value, __organismHost.set, None, None)

    
    # Element {http://uniprot.org/uniprot}geneLocation uses Python identifier geneLocation
    __geneLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'geneLocation'), 'geneLocation', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotgeneLocation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 45, 16), )

    
    geneLocation = property(__geneLocation.value, __geneLocation.set, None, None)

    
    # Element {http://uniprot.org/uniprot}reference uses Python identifier reference
    __reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reference'), 'reference', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotreference', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 46, 16), )

    
    reference = property(__reference.value, __reference.set, None, None)

    
    # Element {http://uniprot.org/uniprot}comment uses Python identifier comment
    __comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'comment'), 'comment', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotcomment', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 47, 16), )

    
    comment = property(__comment.value, __comment.set, None, None)

    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotdbReference', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 48, 16), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, None)

    
    # Element {http://uniprot.org/uniprot}proteinExistence uses Python identifier proteinExistence
    __proteinExistence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'proteinExistence'), 'proteinExistence', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotproteinExistence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 49, 16), )

    
    proteinExistence = property(__proteinExistence.value, __proteinExistence.set, None, None)

    
    # Element {http://uniprot.org/uniprot}keyword uses Python identifier keyword
    __keyword = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'keyword'), 'keyword', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotkeyword', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 50, 16), )

    
    keyword = property(__keyword.value, __keyword.set, None, None)

    
    # Element {http://uniprot.org/uniprot}feature uses Python identifier feature
    __feature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'feature'), 'feature', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotfeature', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 51, 16), )

    
    feature = property(__feature.value, __feature.set, None, None)

    
    # Element {http://uniprot.org/uniprot}evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotevidence', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 52, 16), )

    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Element {http://uniprot.org/uniprot}sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sequence'), 'sequence', '__httpuniprot_orguniprot_CTD_ANON_11_httpuniprot_orguniprotsequence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 53, 16), )

    
    sequence = property(__sequence.value, __sequence.set, None, None)

    
    # Attribute dataset uses Python identifier dataset
    __dataset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'dataset'), 'dataset', '__httpuniprot_orguniprot_CTD_ANON_11_dataset', STD_ANON, required=True)
    __dataset._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 55, 12)
    __dataset._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 55, 12)
    
    dataset = property(__dataset.value, __dataset.set, None, None)

    
    # Attribute created uses Python identifier created
    __created = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'created'), 'created', '__httpuniprot_orguniprot_CTD_ANON_11_created', pyxb.binding.datatypes.date, required=True)
    __created._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 63, 12)
    __created._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 63, 12)
    
    created = property(__created.value, __created.set, None, None)

    
    # Attribute modified uses Python identifier modified
    __modified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'modified'), 'modified', '__httpuniprot_orguniprot_CTD_ANON_11_modified', pyxb.binding.datatypes.date, required=True)
    __modified._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 64, 12)
    __modified._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 64, 12)
    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpuniprot_orguniprot_CTD_ANON_11_version', pyxb.binding.datatypes.int, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 65, 12)
    __version._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 65, 12)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __accession.name() : __accession,
        __name.name() : __name,
        __protein.name() : __protein,
        __gene.name() : __gene,
        __organism.name() : __organism,
        __organismHost.name() : __organismHost,
        __geneLocation.name() : __geneLocation,
        __reference.name() : __reference,
        __comment.name() : __comment,
        __dbReference.name() : __dbReference,
        __proteinExistence.name() : __proteinExistence,
        __keyword.name() : __keyword,
        __feature.name() : __feature,
        __evidence.name() : __evidence,
        __sequence.name() : __sequence
    })
    _AttributeMap.update({
        __dataset.name() : __dataset,
        __created.name() : __created,
        __modified.name() : __modified,
        __version.name() : __version
    })



# Complex type {http://uniprot.org/uniprot}geneNameType with content type SIMPLE
class geneNameType (pyxb.binding.basis.complexTypeDefinition):
    """Describes different types of gene designations.
            Equivalent to the flat file GN-line."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'geneNameType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_geneNameType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 156, 16)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 156, 16)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_geneNameType_type', STD_ANON_, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 157, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 157, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'geneNameType', geneNameType)


# Complex type {http://uniprot.org/uniprot}organismType with content type ELEMENT_ONLY
class organismType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the source organism."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'organismType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 173, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_organismType_httpuniprot_orguniprotname', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 178, 12), )

    
    name = property(__name.value, __name.set, None, u'Describes the names of the source organism.\n                    Equivalent to the flat file OS-line.')

    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_organismType_httpuniprot_orguniprotdbReference', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 184, 12), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, u'Describes a cross-reference to the NCBI taxonomy database.\n                    Equivalent to the flat file OX-line.')

    
    # Element {http://uniprot.org/uniprot}lineage uses Python identifier lineage
    __lineage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lineage'), 'lineage', '__httpuniprot_orguniprot_organismType_httpuniprot_orguniprotlineage', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 190, 12), )

    
    lineage = property(__lineage.value, __lineage.set, None, u'Describes the lineage of the source organism.\n                    Equivalent to the flat file OC-line.')

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_organismType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 202, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 202, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __dbReference.name() : __dbReference,
        __lineage.name() : __lineage
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })
Namespace.addCategoryObject('typeBinding', u'organismType', organismType)


# Complex type {http://uniprot.org/uniprot}organismNameType with content type SIMPLE
class organismNameType (pyxb.binding.basis.complexTypeDefinition):
    """Describes different types of source organism names."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'organismNameType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 204, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_organismNameType_type', STD_ANON_2, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 210, 16)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 210, 16)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'organismNameType', organismNameType)


# Complex type {http://uniprot.org/uniprot}geneLocationType with content type ELEMENT_ONLY
class geneLocationType (pyxb.binding.basis.complexTypeDefinition):
    """Describes non-nuclear gene locations (organelles and plasmids).
            Equivalent to the flat file OG-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'geneLocationType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 227, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpuniprot_orguniprot_geneLocationType_httpuniprot_orguniprotname', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 233, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_geneLocationType_type', STD_ANON_3, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 235, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 235, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_geneLocationType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 251, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 251, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        __name.name() : __name
    })
    _AttributeMap.update({
        __type.name() : __type,
        __evidence.name() : __evidence
    })
Namespace.addCategoryObject('typeBinding', u'geneLocationType', geneLocationType)


# Complex type {http://uniprot.org/uniprot}statusType with content type SIMPLE
class statusType (pyxb.binding.basis.complexTypeDefinition):
    """Indicates whether the name of a plasmid is known or unknown."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'statusType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 253, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpuniprot_orguniprot_statusType_status', STD_ANON_4, unicode_default=u'known')
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 259, 16)
    __status._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 259, 16)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __status.name() : __status
    })
Namespace.addCategoryObject('typeBinding', u'statusType', statusType)


# Complex type {http://uniprot.org/uniprot}referenceType with content type ELEMENT_ONLY
class referenceType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a citation and a summary of its content.
            Equivalent to the flat file RN-, RP-, RC-, RX-, RG-, RA-, RT- and RL-lines."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'referenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 273, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'citation'), 'citation', '__httpuniprot_orguniprot_referenceType_httpuniprot_orguniprotcitation', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 279, 12), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element {http://uniprot.org/uniprot}scope uses Python identifier scope
    __scope = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'scope'), 'scope', '__httpuniprot_orguniprot_referenceType_httpuniprot_orguniprotscope', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 421, 12), )

    
    scope = property(__scope.value, __scope.set, None, u'Describes the scope of a citation.\n                    Equivalent to the flat file RP-line.')

    
    # Element {http://uniprot.org/uniprot}source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'source'), 'source', '__httpuniprot_orguniprot_referenceType_httpuniprot_orguniprotsource', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 427, 12), )

    
    source = property(__source.value, __source.set, None, None)

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_referenceType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 282, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 282, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'key'), 'key', '__httpuniprot_orguniprot_referenceType_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 283, 8)
    __key._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 283, 8)
    
    key = property(__key.value, __key.set, None, None)

    _ElementMap.update({
        __citation.name() : __citation,
        __scope.name() : __scope,
        __source.name() : __source
    })
    _AttributeMap.update({
        __evidence.name() : __evidence,
        __key.name() : __key
    })
Namespace.addCategoryObject('typeBinding', u'referenceType', referenceType)


# Complex type {http://uniprot.org/uniprot}citationType with content type ELEMENT_ONLY
class citationType (pyxb.binding.basis.complexTypeDefinition):
    """Describes different types of citations.
            Equivalent to the flat file RX-, RG-, RA-, RT- and RL-lines."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'citationType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 288, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpuniprot_orguniprot_citationType_httpuniprot_orguniprottitle', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 294, 12), )

    
    title = property(__title.value, __title.set, None, u'Describes the title of a citation.\n                    Equivalent to the flat file RT-line.')

    
    # Element {http://uniprot.org/uniprot}editorList uses Python identifier editorList
    __editorList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'editorList'), 'editorList', '__httpuniprot_orguniprot_citationType_httpuniprot_orguniproteditorList', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 300, 12), )

    
    editorList = property(__editorList.value, __editorList.set, None, u'Describes the editors of a book (only used for books).\n                    Equivalent to part of the flat file RL-line of books.')

    
    # Element {http://uniprot.org/uniprot}authorList uses Python identifier authorList
    __authorList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authorList'), 'authorList', '__httpuniprot_orguniprot_citationType_httpuniprot_orguniprotauthorList', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 306, 12), )

    
    authorList = property(__authorList.value, __authorList.set, None, u'Describes the authors of a citation.\n                    Equivalent to the flat file RA-line.')

    
    # Element {http://uniprot.org/uniprot}locator uses Python identifier locator
    __locator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'locator'), 'locator', '__httpuniprot_orguniprot_citationType_httpuniprot_orguniprotlocator', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 312, 12), )

    
    locator = property(__locator.value, __locator.set, None, u'Describes the location (URL) of an online journal article.\n                    No flat file equivalent.')

    
    # Element {http://uniprot.org/uniprot}dbReference uses Python identifier dbReference
    __dbReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), 'dbReference', '__httpuniprot_orguniprot_citationType_httpuniprot_orguniprotdbReference', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 318, 12), )

    
    dbReference = property(__dbReference.value, __dbReference.set, None, u'Describes cross-references to bibliography databases (MEDLINE, PubMed, AGRICOLA) or other online resources (DOI).\n                    Equivalent to the flat file RX-line.')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_citationType_type', STD_ANON_5, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 325, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 325, 8)
    
    type = property(__type.value, __type.set, None, u'Describes the type of a citation.')

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'date'), 'date', '__httpuniprot_orguniprot_citationType_date', STD_ANON_6)
    __date._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 341, 8)
    __date._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 341, 8)
    
    date = property(__date.value, __date.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpuniprot_orguniprot_citationType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 346, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 346, 8)
    
    name = property(__name.value, __name.set, None, u'Describes the name of an (online) journal or book.')

    
    # Attribute volume uses Python identifier volume
    __volume = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'volume'), 'volume', '__httpuniprot_orguniprot_citationType_volume', pyxb.binding.datatypes.string)
    __volume._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 351, 8)
    __volume._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 351, 8)
    
    volume = property(__volume.value, __volume.set, None, u'Describes the volume of a journal or book.')

    
    # Attribute first uses Python identifier first
    __first = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'first'), 'first', '__httpuniprot_orguniprot_citationType_first', pyxb.binding.datatypes.string)
    __first._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 356, 8)
    __first._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 356, 8)
    
    first = property(__first.value, __first.set, None, u'Describes the first page of an article.')

    
    # Attribute last uses Python identifier last
    __last = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'last'), 'last', '__httpuniprot_orguniprot_citationType_last', pyxb.binding.datatypes.string)
    __last._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 361, 8)
    __last._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 361, 8)
    
    last = property(__last.value, __last.set, None, u'Describes the last page of an article.')

    
    # Attribute publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'publisher'), 'publisher', '__httpuniprot_orguniprot_citationType_publisher', pyxb.binding.datatypes.string)
    __publisher._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 366, 8)
    __publisher._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 366, 8)
    
    publisher = property(__publisher.value, __publisher.set, None, u'Describes the publisher of a book.')

    
    # Attribute city uses Python identifier city
    __city = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'city'), 'city', '__httpuniprot_orguniprot_citationType_city', pyxb.binding.datatypes.string)
    __city._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 371, 8)
    __city._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 371, 8)
    
    city = property(__city.value, __city.set, None, u'Describes the city where a book was published.')

    
    # Attribute db uses Python identifier db
    __db = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'db'), 'db', '__httpuniprot_orguniprot_citationType_db', pyxb.binding.datatypes.string)
    __db._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 376, 8)
    __db._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 376, 8)
    
    db = property(__db.value, __db.set, None, u'Describes the database name of submissions.')

    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'number'), 'number', '__httpuniprot_orguniprot_citationType_number', pyxb.binding.datatypes.string)
    __number._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 381, 8)
    __number._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 381, 8)
    
    number = property(__number.value, __number.set, None, u'Describes a patent number.')

    
    # Attribute institute uses Python identifier institute
    __institute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'institute'), 'institute', '__httpuniprot_orguniprot_citationType_institute', pyxb.binding.datatypes.string)
    __institute._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 386, 8)
    __institute._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 386, 8)
    
    institute = property(__institute.value, __institute.set, None, u'Describes the institute where a thesis was made.')

    
    # Attribute country uses Python identifier country
    __country = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__httpuniprot_orguniprot_citationType_country', pyxb.binding.datatypes.string)
    __country._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 391, 8)
    __country._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 391, 8)
    
    country = property(__country.value, __country.set, None, u'Describes the country where a thesis was made.')

    _ElementMap.update({
        __title.name() : __title,
        __editorList.name() : __editorList,
        __authorList.name() : __authorList,
        __locator.name() : __locator,
        __dbReference.name() : __dbReference
    })
    _AttributeMap.update({
        __type.name() : __type,
        __date.name() : __date,
        __name.name() : __name,
        __volume.name() : __volume,
        __first.name() : __first,
        __last.name() : __last,
        __publisher.name() : __publisher,
        __city.name() : __city,
        __db.name() : __db,
        __number.name() : __number,
        __institute.name() : __institute,
        __country.name() : __country
    })
Namespace.addCategoryObject('typeBinding', u'citationType', citationType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 437, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_12_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 440, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 440, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 446, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_13_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 449, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 449, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 455, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_14_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 458, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 458, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 464, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_15_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 467, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 467, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type {http://uniprot.org/uniprot}commentType with content type ELEMENT_ONLY
class commentType (pyxb.binding.basis.complexTypeDefinition):
    """Describes different types of general annotations.
            Equivalent to the flat file CC-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'commentType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 477, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}molecule uses Python identifier molecule
    __molecule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'molecule'), 'molecule', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotmolecule', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 489, 20), )

    
    molecule = property(__molecule.value, __molecule.set, None, None)

    
    # Element {http://uniprot.org/uniprot}subcellularLocation uses Python identifier subcellularLocation
    __subcellularLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'subcellularLocation'), 'subcellularLocation', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotsubcellularLocation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 490, 20), )

    
    subcellularLocation = property(__subcellularLocation.value, __subcellularLocation.set, None, None)

    
    # Element {http://uniprot.org/uniprot}conflict uses Python identifier conflict
    __conflict = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'conflict'), 'conflict', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotconflict', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 493, 16), )

    
    conflict = property(__conflict.value, __conflict.set, None, u"Used in 'sequence caution' annotations.")

    
    # Element {http://uniprot.org/uniprot}link uses Python identifier link
    __link = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'link'), 'link', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotlink', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 535, 20), )

    
    link = property(__link.value, __link.set, None, u"Used in 'online information' annotations.")

    
    # Element {http://uniprot.org/uniprot}event uses Python identifier event
    __event = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'event'), 'event', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotevent', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 549, 20), )

    
    event = property(__event.value, __event.set, None, None)

    
    # Element {http://uniprot.org/uniprot}isoform uses Python identifier isoform
    __isoform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'isoform'), 'isoform', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotisoform', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 550, 20), )

    
    isoform = property(__isoform.value, __isoform.set, None, None)

    
    # Element {http://uniprot.org/uniprot}interactant uses Python identifier interactant
    __interactant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'interactant'), 'interactant', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotinteractant', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 557, 20), )

    
    interactant = property(__interactant.value, __interactant.set, None, None)

    
    # Element {http://uniprot.org/uniprot}organismsDiffer uses Python identifier organismsDiffer
    __organismsDiffer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organismsDiffer'), 'organismsDiffer', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotorganismsDiffer', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 558, 20), )

    
    organismsDiffer = property(__organismsDiffer.value, __organismsDiffer.set, None, None)

    
    # Element {http://uniprot.org/uniprot}experiments uses Python identifier experiments
    __experiments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'experiments'), 'experiments', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotexperiments', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 559, 20), )

    
    experiments = property(__experiments.value, __experiments.set, None, None)

    
    # Element {http://uniprot.org/uniprot}disease uses Python identifier disease
    __disease = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'disease'), 'disease', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotdisease', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 562, 16), )

    
    disease = property(__disease.value, __disease.set, None, u"Used in 'disease' annotations.")

    
    # Element {http://uniprot.org/uniprot}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'location'), 'location', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotlocation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 579, 12), )

    
    location = property(__location.value, __location.set, None, u"Used in 'mass spectrometry' and 'sequence caution' annotations.")

    
    # Element {http://uniprot.org/uniprot}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'text'), 'text', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprottext', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 585, 12), )

    
    text = property(__text.value, __text.set, None, u'Used to store non-structured types of annotations, as well as optional free-text notes of structured types of annotations.')

    
    # Element {http://uniprot.org/uniprot}absorption uses Python identifier absorption
    __absorption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'absorption'), 'absorption', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotabsorption', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 669, 12), )

    
    absorption = property(__absorption.value, __absorption.set, None, None)

    
    # Element {http://uniprot.org/uniprot}kinetics uses Python identifier kinetics
    __kinetics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'kinetics'), 'kinetics', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotkinetics', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 677, 12), )

    
    kinetics = property(__kinetics.value, __kinetics.set, None, None)

    
    # Element {http://uniprot.org/uniprot}phDependence uses Python identifier phDependence
    __phDependence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phDependence'), 'phDependence', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotphDependence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 686, 12), )

    
    phDependence = property(__phDependence.value, __phDependence.set, None, None)

    
    # Element {http://uniprot.org/uniprot}redoxPotential uses Python identifier redoxPotential
    __redoxPotential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'redoxPotential'), 'redoxPotential', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprotredoxPotential', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 687, 12), )

    
    redoxPotential = property(__redoxPotential.value, __redoxPotential.set, None, None)

    
    # Element {http://uniprot.org/uniprot}temperatureDependence uses Python identifier temperatureDependence
    __temperatureDependence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'temperatureDependence'), 'temperatureDependence', '__httpuniprot_orguniprot_commentType_httpuniprot_orguniprottemperatureDependence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 688, 12), )

    
    temperatureDependence = property(__temperatureDependence.value, __temperatureDependence.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_commentType_type', STD_ANON_9, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 593, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 593, 8)
    
    type = property(__type.value, __type.set, None, u'Describes the type of a general annotation.\n                Equivalent to the flat file CC comment topics (except for "DATABASE" which is translated to "online information").')

    
    # Attribute locationType uses Python identifier locationType
    __locationType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locationType'), 'locationType', '__httpuniprot_orguniprot_commentType_locationType', pyxb.binding.datatypes.string)
    __locationType._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 633, 8)
    __locationType._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 633, 8)
    
    locationType = property(__locationType.value, __locationType.set, None, u'Describes the type of sequence location in \'RNA editing\' annotations. Common values are "Not_applicable" and "Undetermined".')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpuniprot_orguniprot_commentType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 639, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 639, 8)
    
    name = property(__name.value, __name.set, None, u"Describes an optional name for an 'online information'.")

    
    # Attribute mass uses Python identifier mass
    __mass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mass'), 'mass', '__httpuniprot_orguniprot_commentType_mass', pyxb.binding.datatypes.float)
    __mass._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 645, 8)
    __mass._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 645, 8)
    
    mass = property(__mass.value, __mass.set, None, u"Describes the molecular mass in 'mass spectrometry' annotations.")

    
    # Attribute error uses Python identifier error
    __error = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'error'), 'error', '__httpuniprot_orguniprot_commentType_error', pyxb.binding.datatypes.string)
    __error._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 650, 8)
    __error._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 650, 8)
    
    error = property(__error.value, __error.set, None, u"Describes the error of the mass measurement in 'mass spectrometry' annotations.")

    
    # Attribute method uses Python identifier method
    __method = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'method'), 'method', '__httpuniprot_orguniprot_commentType_method', pyxb.binding.datatypes.string)
    __method._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 655, 8)
    __method._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 655, 8)
    
    method = property(__method.value, __method.set, None, u"Describes the experimental method in 'mass spectrometry' annotations.")

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_commentType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 661, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 661, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        __molecule.name() : __molecule,
        __subcellularLocation.name() : __subcellularLocation,
        __conflict.name() : __conflict,
        __link.name() : __link,
        __event.name() : __event,
        __isoform.name() : __isoform,
        __interactant.name() : __interactant,
        __organismsDiffer.name() : __organismsDiffer,
        __experiments.name() : __experiments,
        __disease.name() : __disease,
        __location.name() : __location,
        __text.name() : __text,
        __absorption.name() : __absorption,
        __kinetics.name() : __kinetics,
        __phDependence.name() : __phDependence,
        __redoxPotential.name() : __redoxPotential,
        __temperatureDependence.name() : __temperatureDependence
    })
    _AttributeMap.update({
        __type.name() : __type,
        __locationType.name() : __locationType,
        __name.name() : __name,
        __mass.name() : __mass,
        __error.name() : __error,
        __method.name() : __method,
        __evidence.name() : __evidence
    })
Namespace.addCategoryObject('typeBinding', u'commentType', commentType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Used in 'sequence caution' annotations."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 497, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}sequence uses Python identifier sequence
    __sequence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sequence'), 'sequence', '__httpuniprot_orguniprot_CTD_ANON_16_httpuniprot_orguniprotsequence', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 499, 28), )

    
    sequence = property(__sequence.value, __sequence.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_CTD_ANON_16_type', STD_ANON_8, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 514, 24)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 514, 24)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpuniprot_orguniprot_CTD_ANON_16_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 526, 24)
    __ref._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 526, 24)
    
    ref = property(__ref.value, __ref.set, None, u"Refers to the 'key' attribute of a 'reference' element.")

    _ElementMap.update({
        __sequence.name() : __sequence
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ref.name() : __ref
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 500, 32)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute resource uses Python identifier resource
    __resource = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'resource'), 'resource', '__httpuniprot_orguniprot_CTD_ANON_17_resource', STD_ANON_7, required=True)
    __resource._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 501, 36)
    __resource._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 501, 36)
    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_CTD_ANON_17_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 509, 36)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 509, 36)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpuniprot_orguniprot_CTD_ANON_17_version', pyxb.binding.datatypes.int)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 510, 36)
    __version._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 510, 36)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __resource.name() : __resource,
        __id.name() : __id,
        __version.name() : __version
    })



# Complex type {http://uniprot.org/uniprot}eventType with content type EMPTY
class eventType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the type of events that cause alternative products."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'eventType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 703, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_eventType_type', STD_ANON_10, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 707, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 707, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'eventType', eventType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 726, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_18_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 729, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 729, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 735, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_CTD_ANON_19_type', STD_ANON_11, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 736, 20)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 736, 20)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpuniprot_orguniprot_CTD_ANON_19_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 746, 20)
    __ref._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 746, 20)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type,
        __ref.name() : __ref
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 750, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_CTD_ANON_20_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 753, 28)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 753, 28)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence
    })



# Complex type {http://uniprot.org/uniprot}dbReferenceType with content type ELEMENT_ONLY
class dbReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Describes a database cross-reference.
            Equivalent to the flat file DR-line.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dbReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 774, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}molecule uses Python identifier molecule
    __molecule = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'molecule'), 'molecule', '__httpuniprot_orguniprot_dbReferenceType_httpuniprot_orguniprotmolecule', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 781, 12), )

    
    molecule = property(__molecule.value, __molecule.set, None, None)

    
    # Element {http://uniprot.org/uniprot}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'property'), 'property_', '__httpuniprot_orguniprot_dbReferenceType_httpuniprot_orguniprotproperty', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 782, 12), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_dbReferenceType_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 784, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 784, 8)
    
    type = property(__type.value, __type.set, None, u'Describes the name of the database.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_dbReferenceType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 789, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 789, 8)
    
    id = property(__id.value, __id.set, None, u'Describes a unique database identifier.')

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_dbReferenceType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 794, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 794, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        __molecule.name() : __molecule,
        __property.name() : __property
    })
    _AttributeMap.update({
        __type.name() : __type,
        __id.name() : __id,
        __evidence.name() : __evidence
    })
Namespace.addCategoryObject('typeBinding', u'dbReferenceType', dbReferenceType)


# Complex type {http://uniprot.org/uniprot}proteinExistenceType with content type EMPTY
class proteinExistenceType (pyxb.binding.basis.complexTypeDefinition):
    """Describes the evidence for the protein's existence.
            Equivalent to the flat file PE-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'proteinExistenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 805, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_proteinExistenceType_type', STD_ANON_12, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 810, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 810, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'proteinExistenceType', proteinExistenceType)


# Complex type {http://uniprot.org/uniprot}keywordType with content type SIMPLE
class keywordType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}keywordType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'keywordType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 825, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_keywordType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 828, 16)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 828, 16)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_keywordType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 829, 16)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 829, 16)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence,
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'keywordType', keywordType)


# Complex type {http://uniprot.org/uniprot}featureType with content type ELEMENT_ONLY
class featureType (pyxb.binding.basis.complexTypeDefinition):
    """Describes different types of sequence annotations.
            Equivalent to the flat file FT-line."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'featureType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 836, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://uniprot.org/uniprot}original uses Python identifier original
    __original = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'original'), 'original', '__httpuniprot_orguniprot_featureType_httpuniprot_orguniprotoriginal', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 842, 12), )

    
    original = property(__original.value, __original.set, None, u'Describes the original sequence in annotations that describe natural or artifical sequence variations.')

    
    # Element {http://uniprot.org/uniprot}variation uses Python identifier variation
    __variation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'variation'), 'variation', '__httpuniprot_orguniprot_featureType_httpuniprot_orguniprotvariation', True, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 847, 12), )

    
    variation = property(__variation.value, __variation.set, None, u'Describes the variant sequence in annotations that describe natural or artifical sequence variations.')

    
    # Element {http://uniprot.org/uniprot}location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'location'), 'location', '__httpuniprot_orguniprot_featureType_httpuniprot_orguniprotlocation', False, pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 852, 12), )

    
    location = property(__location.value, __location.set, None, u'Describes the sequence coordinates of the annotation.')

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpuniprot_orguniprot_featureType_type', STD_ANON_13, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 858, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 858, 8)
    
    type = property(__type.value, __type.set, None, u'Describes the type of a sequence annotation.\n                Equivalent to the flat file FT feature keys, but using full terms instead of acronyms.')

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpuniprot_orguniprot_featureType_status', STD_ANON_14)
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 907, 8)
    __status._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 907, 8)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__httpuniprot_orguniprot_featureType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 916, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 916, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__httpuniprot_orguniprot_featureType_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 917, 8)
    __description._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 917, 8)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_featureType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 918, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 918, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Attribute ref uses Python identifier ref
    __ref = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ref'), 'ref', '__httpuniprot_orguniprot_featureType_ref', pyxb.binding.datatypes.string)
    __ref._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 919, 8)
    __ref._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 919, 8)
    
    ref = property(__ref.value, __ref.set, None, None)

    _ElementMap.update({
        __original.name() : __original,
        __variation.name() : __variation,
        __location.name() : __location
    })
    _AttributeMap.update({
        __type.name() : __type,
        __status.name() : __status,
        __id.name() : __id,
        __description.name() : __description,
        __evidence.name() : __evidence,
        __ref.name() : __ref
    })
Namespace.addCategoryObject('typeBinding', u'featureType', featureType)


# Complex type {http://uniprot.org/uniprot}positionType with content type EMPTY
class positionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}positionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'positionType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 936, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'position'), 'position', '__httpuniprot_orguniprot_positionType_position', pyxb.binding.datatypes.unsignedLong)
    __position._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 937, 8)
    __position._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 937, 8)
    
    position = property(__position.value, __position.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpuniprot_orguniprot_positionType_status', STD_ANON_15, unicode_default=u'certain')
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 938, 8)
    __status._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 938, 8)
    
    status = property(__status.value, __status.set, None, None)

    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_positionType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 949, 8)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 949, 8)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __position.name() : __position,
        __status.name() : __status,
        __evidence.name() : __evidence
    })
Namespace.addCategoryObject('typeBinding', u'positionType', positionType)


# Complex type {http://uniprot.org/uniprot}sequenceType with content type SIMPLE
class sequenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}sequenceType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sequenceType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 954, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'length'), 'length', '__httpuniprot_orguniprot_sequenceType_length', pyxb.binding.datatypes.int, required=True)
    __length._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 957, 16)
    __length._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 957, 16)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute mass uses Python identifier mass
    __mass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mass'), 'mass', '__httpuniprot_orguniprot_sequenceType_mass', pyxb.binding.datatypes.int, required=True)
    __mass._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 958, 16)
    __mass._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 958, 16)
    
    mass = property(__mass.value, __mass.set, None, None)

    
    # Attribute checksum uses Python identifier checksum
    __checksum = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'checksum'), 'checksum', '__httpuniprot_orguniprot_sequenceType_checksum', pyxb.binding.datatypes.string, required=True)
    __checksum._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 959, 16)
    __checksum._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 959, 16)
    
    checksum = property(__checksum.value, __checksum.set, None, None)

    
    # Attribute modified uses Python identifier modified
    __modified = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'modified'), 'modified', '__httpuniprot_orguniprot_sequenceType_modified', pyxb.binding.datatypes.date, required=True)
    __modified._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 960, 16)
    __modified._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 960, 16)
    
    modified = property(__modified.value, __modified.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpuniprot_orguniprot_sequenceType_version', pyxb.binding.datatypes.int, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 961, 16)
    __version._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 961, 16)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute precursor uses Python identifier precursor
    __precursor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'precursor'), 'precursor', '__httpuniprot_orguniprot_sequenceType_precursor', pyxb.binding.datatypes.boolean)
    __precursor._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 962, 16)
    __precursor._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 962, 16)
    
    precursor = property(__precursor.value, __precursor.set, None, None)

    
    # Attribute fragment uses Python identifier fragment
    __fragment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fragment'), 'fragment', '__httpuniprot_orguniprot_sequenceType_fragment', STD_ANON_16)
    __fragment._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 963, 16)
    __fragment._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 963, 16)
    
    fragment = property(__fragment.value, __fragment.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __length.name() : __length,
        __mass.name() : __mass,
        __checksum.name() : __checksum,
        __modified.name() : __modified,
        __version.name() : __version,
        __precursor.name() : __precursor,
        __fragment.name() : __fragment
    })
Namespace.addCategoryObject('typeBinding', u'sequenceType', sequenceType)


# Complex type {http://uniprot.org/uniprot}evidencedStringType with content type SIMPLE
class evidencedStringType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://uniprot.org/uniprot}evidencedStringType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'evidencedStringType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1029, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute evidence uses Python identifier evidence
    __evidence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'evidence'), 'evidence', '__httpuniprot_orguniprot_evidencedStringType_evidence', intListType)
    __evidence._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1032, 16)
    __evidence._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1032, 16)
    
    evidence = property(__evidence.value, __evidence.set, None, None)

    
    # Attribute status uses Python identifier status
    __status = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'status'), 'status', '__httpuniprot_orguniprot_evidencedStringType_status', STD_ANON_17)
    __status._DeclarationLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1033, 16)
    __status._UseLocation = pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1033, 16)
    
    status = property(__status.value, __status.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __evidence.name() : __evidence,
        __status.name() : __status
    })
Namespace.addCategoryObject('typeBinding', u'evidencedStringType', evidencedStringType)


copyright = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'copyright'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 70, 4))
Namespace.addCategoryObject('elementBinding', copyright.name().localName(), copyright)

uniprot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'uniprot'), CTD_ANON, documentation=u'Describes a collection of UniProtKB entries.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 19, 4))
Namespace.addCategoryObject('elementBinding', uniprot.name().localName(), uniprot)

entry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), CTD_ANON_11, documentation=u'Describes a UniProtKB entry.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 33, 4))
Namespace.addCategoryObject('elementBinding', entry.name().localName(), entry)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'entry'), CTD_ANON_11, scope=CTD_ANON, documentation=u'Describes a UniProtKB entry.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 33, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'copyright'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 70, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 26, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'entry')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 25, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'copyright')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 26, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'domain'), CTD_ANON_, scope=proteinType, documentation=u'Describes names of "domains".\n                    Equivalent to the flat file DE-line Includes: section.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 80, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'component'), CTD_ANON_2, scope=proteinType, documentation=u'Describes names of processed products.\n                    Equivalent to the flat file DE-line Contains: section.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 89, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), CTD_ANON_3, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), CTD_ANON_4, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), CTD_ANON_5, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), evidencedStringType, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), evidencedStringType, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), evidencedStringType, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12)))

proteinType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'innName'), evidencedStringType, scope=proteinType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 80, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 89, 12))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recommendedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternativeName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'submittedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allergenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biotechName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'innName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'domain')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 80, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(proteinType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'component')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 89, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
proteinType._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), CTD_ANON_3, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), CTD_ANON_4, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), CTD_ANON_5, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), evidencedStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), evidencedStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), evidencedStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'innName'), evidencedStringType, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recommendedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternativeName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'submittedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allergenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biotechName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'innName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
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
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'recommendedName'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'alternativeName'), CTD_ANON_4, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'submittedName'), CTD_ANON_5, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'allergenName'), evidencedStringType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'biotechName'), evidencedStringType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName'), evidencedStringType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'innName'), evidencedStringType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'recommendedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'alternativeName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 112, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'submittedName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 122, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'allergenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 131, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'biotechName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 132, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cdAntigenName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 133, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'innName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 134, 12))
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
CTD_ANON_2._Automaton = _BuildAutomaton_3()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fullName'), evidencedStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 105, 24)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shortName'), evidencedStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 106, 24)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), evidencedStringType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 107, 24)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 106, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 107, 24))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fullName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 105, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shortName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 106, 24))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecNumber')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 107, 24))
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
CTD_ANON_3._Automaton = _BuildAutomaton_4()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fullName'), evidencedStringType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 115, 24)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shortName'), evidencedStringType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 116, 24)))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), evidencedStringType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 117, 24)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 115, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 116, 24))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 117, 24))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fullName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 115, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shortName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 116, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecNumber')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 117, 24))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fullName'), evidencedStringType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 125, 24)))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ecNumber'), evidencedStringType, scope=CTD_ANON_5, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 126, 24)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 126, 24))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fullName')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 125, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ecNumber')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 126, 24))
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
CTD_ANON_5._Automaton = _BuildAutomaton_6()




geneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), geneNameType, scope=geneType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 146, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geneType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 146, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
geneType._Automaton = _BuildAutomaton_7()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'taxon'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 197, 24)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'taxon')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 197, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_8()




nameListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'consortium'), consortiumType, scope=nameListType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 409, 12)))

nameListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'person'), personType, scope=nameListType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 410, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nameListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'consortium')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 409, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(nameListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'person')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 410, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
nameListType._Automaton = _BuildAutomaton_9()




sourceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strain'), CTD_ANON_12, scope=sourceDataType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 436, 12)))

sourceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'plasmid'), CTD_ANON_13, scope=sourceDataType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 445, 12)))

sourceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'transposon'), CTD_ANON_14, scope=sourceDataType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 454, 12)))

sourceDataType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tissue'), CTD_ANON_15, scope=sourceDataType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 463, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sourceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strain')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 436, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sourceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'plasmid')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 445, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sourceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'transposon')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 454, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(sourceDataType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tissue')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 463, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
sourceDataType._Automaton = _BuildAutomaton_10()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 568, 28)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'acronym'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 569, 28)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 570, 28)))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 571, 28)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 568, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'acronym')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 569, 28))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 570, 28))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 571, 28))
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
CTD_ANON_8._Automaton = _BuildAutomaton_11()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'max'), evidencedStringType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 672, 24)))

CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'text'), evidencedStringType, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 673, 24)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 672, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 673, 24))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'max')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 672, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'text')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 673, 24))
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
CTD_ANON_9._Automaton = _BuildAutomaton_12()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KM'), evidencedStringType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 680, 24)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Vmax'), evidencedStringType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 681, 24)))

CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'text'), evidencedStringType, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 682, 24)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 680, 24))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 681, 24))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 682, 24))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KM')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 680, 24))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Vmax')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 681, 24))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'text')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 682, 24))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_13()




subcellularLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'location'), evidencedStringType, scope=subcellularLocationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 697, 12)))

subcellularLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'topology'), evidencedStringType, scope=subcellularLocationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 698, 12)))

subcellularLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orientation'), evidencedStringType, scope=subcellularLocationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 699, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 698, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 699, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(subcellularLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'location')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 697, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subcellularLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'topology')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 698, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subcellularLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orientation')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 699, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
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
subcellularLocationType._Automaton = _BuildAutomaton_14()




isoformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), pyxb.binding.datatypes.string, scope=isoformType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 724, 12)))

isoformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), CTD_ANON_18, scope=isoformType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 725, 12)))

isoformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sequence'), CTD_ANON_19, scope=isoformType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 734, 12)))

isoformType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'note'), CTD_ANON_20, scope=isoformType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 749, 12)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 749, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(isoformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 724, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(isoformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 725, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(isoformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sequence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 734, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(isoformType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'note')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 749, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
isoformType._Automaton = _BuildAutomaton_15()




interactantType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'id'), pyxb.binding.datatypes.string, scope=interactantType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 763, 12)))

interactantType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'label'), pyxb.binding.datatypes.string, scope=interactantType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 764, 12)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 768, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 764, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(interactantType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'id')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 763, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(interactantType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'label')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 764, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
interactantType._Automaton = _BuildAutomaton_16()




locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'begin'), positionType, scope=locationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 928, 16)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'end'), positionType, scope=locationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 929, 16)))

locationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'position'), positionType, scope=locationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 931, 12)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'begin')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 928, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'end')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 929, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(locationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'position')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 931, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
locationType._Automaton = _BuildAutomaton_17()




evidenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), sourceType, scope=evidenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 996, 12)))

evidenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'importedFrom'), importedFromType, scope=evidenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 997, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 996, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 997, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(evidenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 996, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(evidenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'importedFrom')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 997, 12))
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
evidenceType._Automaton = _BuildAutomaton_18()




sourceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=sourceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1015, 12)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1015, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(sourceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1015, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
sourceType._Automaton = _BuildAutomaton_19()




importedFromType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=importedFromType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1024, 12)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(importedFromType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 1024, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
importedFromType._Automaton = _BuildAutomaton_20()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'accession'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 39, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 40, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protein'), proteinType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 41, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gene'), geneType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 42, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organism'), organismType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 43, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organismHost'), organismType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 44, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'geneLocation'), geneLocationType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 45, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reference'), referenceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 46, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'comment'), commentType, nillable=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 47, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 48, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'proteinExistence'), proteinExistenceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 49, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'keyword'), keywordType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 50, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'feature'), featureType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 51, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'evidence'), evidenceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 52, 16)))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sequence'), sequenceType, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 53, 16)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 42, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 44, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 45, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 47, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 48, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 50, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 51, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 52, 16))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'accession')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 39, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 40, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protein')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 41, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gene')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 42, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organism')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 43, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organismHost')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 44, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'geneLocation')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 45, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 46, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'comment')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 47, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 48, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'proteinExistence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 49, 16))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'keyword')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 50, 16))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'feature')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 51, 16))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'evidence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 52, 16))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sequence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 53, 16))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
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
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_21()




organismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), organismNameType, scope=organismType, documentation=u'Describes the names of the source organism.\n                    Equivalent to the flat file OS-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 178, 12)))

organismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=organismType, documentation=u'Describes a cross-reference to the NCBI taxonomy database.\n                    Equivalent to the flat file OX-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 184, 12)))

organismType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineage'), CTD_ANON_6, scope=organismType, documentation=u'Describes the lineage of the source organism.\n                    Equivalent to the flat file OC-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 190, 12)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 190, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(organismType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 178, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(organismType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 184, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(organismType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineage')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 190, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
organismType._Automaton = _BuildAutomaton_22()




geneLocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), statusType, scope=geneLocationType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 233, 12)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 233, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(geneLocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 233, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
geneLocationType._Automaton = _BuildAutomaton_23()




referenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'citation'), citationType, scope=referenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 279, 12)))

referenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scope'), pyxb.binding.datatypes.string, scope=referenceType, documentation=u'Describes the scope of a citation.\n                    Equivalent to the flat file RP-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 421, 12)))

referenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'source'), sourceDataType, scope=referenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 427, 12)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 427, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(referenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'citation')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 279, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(referenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scope')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 421, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(referenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'source')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 427, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
referenceType._Automaton = _BuildAutomaton_24()




citationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), pyxb.binding.datatypes.string, scope=citationType, documentation=u'Describes the title of a citation.\n                    Equivalent to the flat file RT-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 294, 12)))

citationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'editorList'), nameListType, scope=citationType, documentation=u'Describes the editors of a book (only used for books).\n                    Equivalent to part of the flat file RL-line of books.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 300, 12)))

citationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authorList'), nameListType, scope=citationType, documentation=u'Describes the authors of a citation.\n                    Equivalent to the flat file RA-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 306, 12)))

citationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locator'), pyxb.binding.datatypes.string, scope=citationType, documentation=u'Describes the location (URL) of an online journal article.\n                    No flat file equivalent.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 312, 12)))

citationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dbReference'), dbReferenceType, scope=citationType, documentation=u'Describes cross-references to bibliography databases (MEDLINE, PubMed, AGRICOLA) or other online resources (DOI).\n                    Equivalent to the flat file RX-line.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 318, 12)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 294, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 300, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 306, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 312, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 318, 12))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(citationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 294, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(citationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'editorList')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 300, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(citationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authorList')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 306, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(citationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locator')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 312, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(citationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dbReference')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 318, 12))
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
citationType._Automaton = _BuildAutomaton_25()




commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'molecule'), moleculeType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 489, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'subcellularLocation'), subcellularLocationType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 490, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'conflict'), CTD_ANON_16, scope=commentType, documentation=u"Used in 'sequence caution' annotations.", location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 493, 16)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'link'), CTD_ANON_7, scope=commentType, documentation=u"Used in 'online information' annotations.", location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 535, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'event'), eventType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 549, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'isoform'), isoformType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 550, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'interactant'), interactantType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 557, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organismsDiffer'), pyxb.binding.datatypes.boolean, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 558, 20), unicode_default=u'false'))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'experiments'), pyxb.binding.datatypes.int, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 559, 20)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'disease'), CTD_ANON_8, scope=commentType, documentation=u"Used in 'disease' annotations.", location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 562, 16)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'location'), locationType, scope=commentType, documentation=u"Used in 'mass spectrometry' and 'sequence caution' annotations.", location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 579, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'text'), evidencedStringType, scope=commentType, documentation=u'Used to store non-structured types of annotations, as well as optional free-text notes of structured types of annotations.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 585, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absorption'), CTD_ANON_9, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 669, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'kinetics'), CTD_ANON_10, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 677, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phDependence'), evidencedStringType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 686, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'redoxPotential'), evidencedStringType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 687, 12)))

commentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'temperatureDependence'), evidencedStringType, scope=commentType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 688, 12)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 483, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 669, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 677, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 686, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 687, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 688, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 489, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 535, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=1, max=4L, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 549, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 550, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=2L, max=2L, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 557, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 579, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 585, 12))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absorption')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 669, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'kinetics')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 677, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phDependence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 686, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'redoxPotential')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 687, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'temperatureDependence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 688, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'molecule')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 489, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'subcellularLocation')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 490, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'conflict')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 493, 16))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'link')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 535, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'event')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 549, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'isoform')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 550, 20))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'interactant')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 557, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organismsDiffer')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 558, 20))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'experiments')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 559, 20))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'disease')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 562, 16))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'location')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 579, 12))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(commentType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'text')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 585, 12))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_7, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_8, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False),
        fac.UpdateInstruction(cc_9, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
commentType._Automaton = _BuildAutomaton_26()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sequence'), CTD_ANON_17, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 499, 28)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 499, 28))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sequence')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 499, 28))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_27()




dbReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'molecule'), moleculeType, scope=dbReferenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 781, 12)))

dbReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'property'), propertyType, scope=dbReferenceType, location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 782, 12)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 781, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 782, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dbReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'molecule')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 781, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dbReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'property')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 782, 12))
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
dbReferenceType._Automaton = _BuildAutomaton_28()




featureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'original'), pyxb.binding.datatypes.string, scope=featureType, documentation=u'Describes the original sequence in annotations that describe natural or artifical sequence variations.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 842, 12)))

featureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'variation'), pyxb.binding.datatypes.string, scope=featureType, documentation=u'Describes the variant sequence in annotations that describe natural or artifical sequence variations.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 847, 12)))

featureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'location'), locationType, scope=featureType, documentation=u'Describes the sequence coordinates of the annotation.', location=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 852, 12)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 842, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 847, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(featureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'original')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 842, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(featureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'variation')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 847, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(featureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'location')), pyxb.utils.utility.Location('http://www.uniprot.org/docs/uniprot.xsd', 852, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
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
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
featureType._Automaton = _BuildAutomaton_29()

