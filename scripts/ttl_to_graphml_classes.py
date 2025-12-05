#!/usr/bin/env python3
"""
TTL to GraphML conversion script for ontology classes (Graffoo format)
Converts OWL/TTL ontology classes to yEd GraphML format following Graffoo conventions
"""

import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom
from rdflib import Graph, Namespace, RDF, RDFS, OWL
from urllib.parse import urlparse
import argparse


def create_graphml_base():
    """Create base GraphML structure with yEd namespaces"""
    graphml = ET.Element('graphml')
    graphml.set('xmlns', 'http://graphml.graphdrawing.org/xmlns')
    graphml.set('xmlns:java', 'http://www.yworks.com/xml/yfiles-common/1.0/java')
    graphml.set('xmlns:sys', 'http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0')
    graphml.set('xmlns:x', 'http://www.yworks.com/xml/yfiles-common/markup/2.0')
    graphml.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    graphml.set('xmlns:y', 'http://www.yworks.com/xml/graphml')
    graphml.set('xmlns:yed', 'http://www.yworks.com/xml/yed/3')
    graphml.set('xsi:schemaLocation', 'http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd')
    
    # Add comment
    comment = ET.Comment('Created by ttl_to_graphml_classes.py')
    graphml.append(comment)
    
    # Add key definitions
    keys = [
        ('d0', 'graph', 'string', 'Description'),
        ('d1', 'port', None, 'portgraphics'),
        ('d2', 'port', None, 'portgeometry'),
        ('d3', 'port', None, 'portuserdata'),
        ('d4', 'node', 'string', 'url'),
        ('d5', 'node', 'string', 'description'),
        ('d6', 'node', None, 'nodegraphics'),
        ('d7', 'graphml', None, 'resources'),
        ('d8', 'edge', 'string', 'url'),
        ('d9', 'edge', 'string', 'description'),
        ('d10', 'edge', None, 'edgegraphics'),
    ]
    
    for key_id, for_attr, attr_type, name in keys:
        key = ET.SubElement(graphml, 'key')
        key.set('id', key_id)
        key.set('for', for_attr)
        if attr_type:
            key.set('attr.type', attr_type)
            key.set('attr.name', name)
        else:
            key.set('yfiles.type', name)
    
    return graphml


def get_prefix_from_uri(uri, prefixes):
    """Extract prefix:localName from URI using known prefixes"""
    uri_str = str(uri)
    for prefix, namespace in prefixes.items():
        if uri_str.startswith(str(namespace)):
            local_name = uri_str[len(str(namespace)):]
            return f"{prefix}:{local_name}" if prefix else local_name
    
    # Fallback: try to extract from URI structure
    parsed = urlparse(uri_str)
    if '#' in uri_str:
        return uri_str.split('#')[-1]
    elif '/' in parsed.path:
        return parsed.path.split('/')[-1]
    return uri_str


def create_property_node(prop_uri, label, x, y, node_id, prefixes, is_datatype=False, is_external=False):
    """Create a property node in Graffoo format (hexagon for object props, rhombus for datatype props)"""
    node = ET.Element('node')
    node.set('id', f'n{node_id}')
    
    data = ET.SubElement(node, 'data')
    data.set('key', 'd6')
    
    shape_node = ET.SubElement(data, 'y:ShapeNode')
    
    # Geometry - adjust width based on label length
    width = max(120, len(label) * 7 + 30)
    height = 40
    geometry = ET.SubElement(shape_node, 'y:Geometry')
    geometry.set('height', str(height))
    geometry.set('width', str(width))
    geometry.set('x', str(x))
    geometry.set('y', str(y))
    
    # Fill color: orange for object props, green for datatype props
    fill = ET.SubElement(shape_node, 'y:Fill')
    if is_datatype:
        fill.set('color', '#CCFFCC' if not is_external else '#E6FFE6')  # Light green
    else:
        fill.set('color', '#FFB366' if not is_external else '#FFCC99')  # Light orange
    fill.set('transparent', 'false')
    
    # Border
    border = ET.SubElement(shape_node, 'y:BorderStyle')
    border.set('color', '#000000')
    border.set('type', 'line')
    border.set('width', '1.0')
    
    # Label
    node_label = ET.SubElement(shape_node, 'y:NodeLabel')
    node_label.set('alignment', 'center')
    node_label.set('autoSizePolicy', 'content')
    node_label.set('fontFamily', 'Dialog')
    node_label.set('fontSize', '14')
    node_label.set('fontStyle', 'plain')
    node_label.set('hasBackgroundColor', 'false')
    node_label.set('hasLineColor', 'false')
    node_label.set('height', '20.6015625')
    node_label.set('horizontalTextPosition', 'center')
    node_label.set('iconTextGap', '4')
    node_label.set('modelName', 'internal')
    node_label.set('modelPosition', 'c')
    node_label.set('textColor', '#000000')
    node_label.set('verticalTextPosition', 'bottom')
    node_label.set('visible', 'true')
    node_label.set('width', str(len(label) * 7))
    node_label.set('x', str((width - len(label) * 7) / 2))
    node_label.set('y', '9.69921875')
    node_label.text = label
    
    # Shape - hexagon for object props, rhombus for datatype props
    shape = ET.SubElement(shape_node, 'y:Shape')
    shape.set('type', 'diamond' if is_datatype else 'hexagon')
    
    return node


def create_edge(source_id, target_id, label, edge_id, edge_type="subclass"):
    """Create an edge between two nodes"""
    edge = ET.Element('edge')
    edge.set('id', f'e{edge_id}')
    edge.set('source', f'n{source_id}')
    edge.set('target', f'n{target_id}')
    
    data = ET.SubElement(edge, 'data')
    data.set('key', 'd10')
    
    polyline = ET.SubElement(data, 'y:PolyLineEdge')
    
    # Path
    path = ET.SubElement(polyline, 'y:Path')
    path.set('sx', '0.0')
    path.set('sy', '0.0')
    path.set('tx', '0.0')
    path.set('ty', '0.0')
    
    # Line style
    line_style = ET.SubElement(polyline, 'y:LineStyle')
    line_style.set('color', '#000000')
    line_style.set('type', 'line')
    line_style.set('width', '1.0')
    
    # Arrows
    arrows = ET.SubElement(polyline, 'y:Arrows')
    if edge_type == "subclass":
        arrows.set('source', 'none')
        arrows.set('target', 'standard')
    else:  # property edge
        arrows.set('source', 'circle')
        arrows.set('target', 'delta')
    
    # Edge label
    if label:
        edge_label = ET.SubElement(polyline, 'y:EdgeLabel')
        edge_label.set('alignment', 'center')
        edge_label.set('backgroundColor', '#FFFFFF')
        edge_label.set('distance', '2.0')
        edge_label.set('fontFamily', 'Dialog')
        edge_label.set('fontSize', '12')
        edge_label.set('fontStyle', 'plain')
        edge_label.set('hasLineColor', 'false')
        edge_label.set('height', '18.6015625')
        edge_label.set('horizontalTextPosition', 'center')
        edge_label.set('iconTextGap', '4')
        edge_label.set('modelName', 'centered')
        edge_label.set('modelPosition', 'center')
        edge_label.set('preferredPlacement', 'anywhere')
        edge_label.set('ratio', '0.5')
        edge_label.set('textColor', '#000080' if edge_type == "property" else '#000000')
        edge_label.set('verticalTextPosition', 'bottom')
        edge_label.set('visible', 'true')
        edge_label.set('width', str(len(label) * 6))
        edge_label.set('x', str(-(len(label) * 6) / 2))
        edge_label.set('y', '-9.30078125')
        edge_label.text = label
    
    # Bend style
    bend_style = ET.SubElement(polyline, 'y:BendStyle')
    bend_style.set('smoothed', 'false')
    
    return edge


def create_class_node(class_uri, label, x, y, node_id, prefixes, is_external=False):
    """Create a class node in Graffoo format (yellow rounded rectangle)"""
    node = ET.Element('node')
    node.set('id', f'n{node_id}')
    
    data = ET.SubElement(node, 'data')
    data.set('key', 'd6')
    
    shape_node = ET.SubElement(data, 'y:ShapeNode')
    
    # Geometry - adjust width based on label length
    width = max(150, len(label) * 8 + 40)
    height = 44
    geometry = ET.SubElement(shape_node, 'y:Geometry')
    geometry.set('height', str(height))
    geometry.set('width', str(width))
    geometry.set('x', str(x))
    geometry.set('y', str(y))
    
    # Fill color: yellow for classes, light blue for external classes
    fill = ET.SubElement(shape_node, 'y:Fill')
    fill.set('color', '#E6F3FF' if is_external else '#FFFF00')
    fill.set('transparent', 'false')
    
    # Border
    border = ET.SubElement(shape_node, 'y:BorderStyle')
    border.set('color', '#000000')
    border.set('type', 'line')
    border.set('width', '1.0')
    
    # Label
    node_label = ET.SubElement(shape_node, 'y:NodeLabel')
    node_label.set('alignment', 'center')
    node_label.set('autoSizePolicy', 'content')
    node_label.set('fontFamily', 'Dialog')
    node_label.set('fontSize', '16')
    node_label.set('fontStyle', 'plain')
    node_label.set('hasBackgroundColor', 'false')
    node_label.set('hasLineColor', 'false')
    node_label.set('height', '23.6015625')
    node_label.set('horizontalTextPosition', 'center')
    node_label.set('iconTextGap', '4')
    node_label.set('modelName', 'internal')
    node_label.set('modelPosition', 'c')
    node_label.set('textColor', '#000000')
    node_label.set('verticalTextPosition', 'bottom')
    node_label.set('visible', 'true')
    node_label.set('width', str(len(label) * 8))
    node_label.set('x', str((width - len(label) * 8) / 2))
    node_label.set('y', '10.19921875')
    node_label.text = label
    
    # Shape
    shape = ET.SubElement(shape_node, 'y:Shape')
    shape.set('type', 'roundrectangle')
    
    return node


def convert_ttl_to_graphml(ttl_file, output_file=None):
    """Convert TTL file to GraphML format including classes, properties and relationships"""
    
    # Load RDF graph
    g = Graph()
    g.parse(ttl_file, format='turtle')
    
    # Extract namespaces
    prefixes = dict(g.namespaces())
    
    # Common namespaces
    SCHEMA = Namespace("http://schema.org/")
    FOAF = Namespace("http://xmlns.com/foaf/0.1/")
    DATACITE = Namespace("http://purl.org/spar/datacite/")
    TRIPLE = Namespace("https://gotriple.eu/ontology/triple#")
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
    
    # Create GraphML base
    graphml = create_graphml_base()
    
    # Create graph element
    graph = ET.SubElement(graphml, 'graph')
    graph.set('edgedefault', 'directed')
    graph.set('id', 'G')
    
    # Add graph description
    data = ET.SubElement(graph, 'data')
    data.set('key', 'd0')
    data.set('xml:space', 'preserve')
    
    # Find all classes
    classes = []
    for subj in g.subjects(RDF.type, OWL.Class):
        classes.append(subj)
    
    # Find all object properties
    object_properties = []
    for subj in g.subjects(RDF.type, OWL.ObjectProperty):
        object_properties.append(subj)
    
    # Find all datatype properties
    datatype_properties = []
    for subj in g.subjects(RDF.type, OWL.DatatypeProperty):
        datatype_properties.append(subj)
    
    # Layout parameters
    start_x = 100
    start_y = 100
    node_width = 200
    node_height = 60
    cols = 3
    
    node_id = 0
    uri_to_node_id = {}  # Map URIs to node IDs for edges
    
    # Separate triple classes from external classes
    triple_classes = []
    external_classes = []
    
    for cls in classes:
        if str(cls).startswith(str(TRIPLE)):
            triple_classes.append(cls)
        else:
            external_classes.append(cls)
    
    # Add triple classes first (main ontology classes)
    for i, cls in enumerate(triple_classes):
        label = None
        
        # Get label
        for lbl in g.objects(cls, RDFS.label):
            label = str(lbl)
            break
        
        if not label:
            label = get_prefix_from_uri(cls, prefixes)
        
        # Calculate position
        col = i % cols
        row = i // cols
        x = start_x + col * (node_width + 50)
        y = start_y + row * (node_height + 30)
        
        node = create_class_node(cls, label, x, y, node_id, prefixes, is_external=False)
        graph.append(node)
        uri_to_node_id[str(cls)] = node_id
        node_id += 1
    
    # Add external classes (in a separate row)
    external_start_y = start_y + ((len(triple_classes) // cols) + 2) * (node_height + 30)
    
    for i, cls in enumerate(external_classes):
        label = None
        
        # Get label
        for lbl in g.objects(cls, RDFS.label):
            label = str(lbl)
            break
        
        if not label:
            label = get_prefix_from_uri(cls, prefixes)
        
        # Calculate position
        col = i % cols
        row = i // cols
        x = start_x + col * (node_width + 50)
        y = external_start_y + row * (node_height + 30)
        
        node = create_class_node(cls, label, x, y, node_id, prefixes, is_external=True)
        graph.append(node)
        uri_to_node_id[str(cls)] = node_id
        node_id += 1
    
    # Add object properties
    prop_start_y = external_start_y + ((len(external_classes) // cols) + 2) * (node_height + 30)
    
    # Separate triple properties from external properties
    triple_obj_props = []
    external_obj_props = []
    
    for prop in object_properties:
        if str(prop).startswith(str(TRIPLE)):
            triple_obj_props.append(prop)
        else:
            external_obj_props.append(prop)
    
    all_obj_props = triple_obj_props + external_obj_props
    
    for i, prop in enumerate(all_obj_props):
        label = None
        
        # Get label
        for lbl in g.objects(prop, RDFS.label):
            label = str(lbl)
            break
        
        if not label:
            label = get_prefix_from_uri(prop, prefixes)
        
        # Calculate position
        col = i % cols
        row = i // cols
        x = start_x + col * (node_width + 50)
        y = prop_start_y + row * (node_height + 30)
        
        is_external = prop in external_obj_props
        node = create_property_node(prop, label, x, y, node_id, prefixes, is_datatype=False, is_external=is_external)
        graph.append(node)
        uri_to_node_id[str(prop)] = node_id
        node_id += 1
    
    # Add datatype properties
    data_prop_start_y = prop_start_y + ((len(all_obj_props) // cols) + 2) * (node_height + 30)
    
    # Separate triple data properties from external data properties
    triple_data_props = []
    external_data_props = []
    
    for prop in datatype_properties:
        if str(prop).startswith(str(TRIPLE)):
            triple_data_props.append(prop)
        else:
            external_data_props.append(prop)
    
    all_data_props = triple_data_props + external_data_props
    
    for i, prop in enumerate(all_data_props):
        label = None
        
        # Get label
        for lbl in g.objects(prop, RDFS.label):
            label = str(lbl)
            break
        
        if not label:
            label = get_prefix_from_uri(prop, prefixes)
        
        # Calculate position
        col = i % cols
        row = i // cols
        x = start_x + col * (node_width + 50)
        y = data_prop_start_y + row * (node_height + 30)
        
        is_external = prop in external_data_props
        node = create_property_node(prop, label, x, y, node_id, prefixes, is_datatype=True, is_external=is_external)
        graph.append(node)
        uri_to_node_id[str(prop)] = node_id
        node_id += 1
    
    # Add edges for rdfs:subClassOf relationships
    edge_id = 0
    for subj in g.subjects(RDFS.subClassOf):
        for obj in g.objects(subj, RDFS.subClassOf):
            if str(subj) in uri_to_node_id and str(obj) in uri_to_node_id:
                source_id = uri_to_node_id[str(subj)]
                target_id = uri_to_node_id[str(obj)]
                edge = create_edge(source_id, target_id, "rdfs:subClassOf", edge_id, "subclass")
                graph.append(edge)
                edge_id += 1
    
    # Add resources element
    data = ET.SubElement(graphml, 'data')
    data.set('key', 'd7')
    resources = ET.SubElement(data, 'y:Resources')
    
    # Generate output filename if not provided
    if not output_file:
        output_file = ttl_file.replace('.ttl', '_complete.graphml')
    
    # Write to file with pretty printing
    rough_string = ET.tostring(graphml, 'unicode')
    reparsed = minidom.parseString(rough_string)
    pretty = reparsed.toprettyxml(indent='  ')
    
    # Remove empty lines
    pretty_lines = [line for line in pretty.split('\n') if line.strip()]
    pretty = '\n'.join(pretty_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(pretty)
    
    print(f"Converted to GraphML: {output_file}")
    print(f"Classes: {len(classes)} (Triple: {len(triple_classes)}, External: {len(external_classes)})")
    print(f"Object Properties: {len(object_properties)} (Triple: {len(triple_obj_props)}, External: {len(external_obj_props)})")
    print(f"Datatype Properties: {len(datatype_properties)} (Triple: {len(triple_data_props)}, External: {len(external_data_props)})")
    print(f"SubClass relationships: {edge_id}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(description='Convert TTL ontology classes to GraphML format')
    parser.add_argument('input_file', help='Input TTL file')
    parser.add_argument('-o', '--output', help='Output GraphML file (default: input_classes.graphml)')
    
    args = parser.parse_args()
    
    try:
        output_file = convert_ttl_to_graphml(args.input_file, args.output)
        print(f"Successfully converted to: {output_file}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()