from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Element:
    uri: str
    label: Optional[str] = None
    comment: Optional[str] = None
    description: Optional[str] = None
    is_defined_by: Optional[str] = None
    type_label: Optional[str] = None
    url: Optional[str] = None # Calculated link (internal anchor or external URI)
    anchor: Optional[str] = None # Short id used as the HTML anchor of this term
    figure: Optional[str] = None # Relative path of the Graffoo diagram for this term, when one exists
    chapter: Optional[dict] = None # {'n', 'title', 'slug'} of the narrative chapter that discusses this term
    other_labels: List[str] = field(default_factory=list) # Alternative translations/labels
    examples: List[str] = field(default_factory=list) # skos:example — usage snippets, rendered verbatim
    scope_notes: List[str] = field(default_factory=list) # skos:scopeNote / skos:note — how and when to use the term
    skos_properties: list[tuple[str, str]] = field(default_factory=list) # remaining SKOS annotations (external alignment)

@dataclass
class Restriction:
    on_property: Element
    type: str
    amount: str = None # for cardinality
    values: list[Element] = field(default_factory=list) # target classes/things
    literal_value: str = None # for when target is a literal or datatype

@dataclass
class Class(Element):
    super_classes: list[Element] = field(default_factory=list)
    sub_classes: list[Element] = field(default_factory=list)
    in_domain_of: list[Element] = field(default_factory=list)
    in_range_of: list[Element] = field(default_factory=list)
    members: list[Element] = field(default_factory=list)
    disjoint_with: list[Element] = field(default_factory=list)
    restrictions: list[Restriction] = field(default_factory=list)

@dataclass
class Property(Element):
    super_properties: list[Element] = field(default_factory=list)
    sub_properties: list[Element] = field(default_factory=list)
    domains: list[Element] = field(default_factory=list)
    ranges: list[Element] = field(default_factory=list)
    inverse: list[Element] = field(default_factory=list)
    disjoint_with: list[Element] = field(default_factory=list)

@dataclass
class Individual(Element):
    types: List[Class] = field(default_factory=list)
    same_as: list[str] = field(default_factory=list)
    assertions: list[tuple[str, str, str, str | None]] = field(default_factory=list) # prop_label, prop_uri, val_label, val_uri

@dataclass
class OntologyMetadata:
    uri: str
    title: Optional[str] = None
    date: Optional[str] = None
    version: Optional[str] = None
    creators: List[str] = field(default_factory=list)
    contributors: List[str] = field(default_factory=list)
    publishers: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    license: Optional[str] = None
    abstract: Optional[str] = None
    description: Optional[str] = None
