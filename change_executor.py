import glob
from lxml import etree

xml_list = glob.glob("xml/*.xml")
parser = etree.XMLParser(remove_blank_text=True)
for xml in xml_list:
    tree = etree.parse(xml, parser)
    etree.strip_elements(tree, 'InfoLandWork')
    object_tag = etree.Element("object")
    object_tag.text = ""
    service_info = tree.find(".//ServiceInfo")
    service_info.addnext(object_tag)
    container = tree.find('.//object')
    parent = container.getparent()
    content_tree = etree.fromstring(file_content)
    parent.replace(container, content_tree)
    tree.write(xml, encoding="utf-8", pretty_print=True)
