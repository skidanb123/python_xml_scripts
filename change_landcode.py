import glob
import xml.etree.ElementTree as ET

xml_list = glob.glob("xml/*.xml")
for xml in xml_list:
    print(xml)
    tree = ET.parse(xml)
    for landCode in tree.findall(".//LandCode"):
        landCode.text = '001.01'
        tree.find(".//DocumentationType").text = '025'
        try:
            tree.find(".//DraftingDate").text = "2021-02-25"
        except:
            print("xml Date insertion Error")
        tree.find(".//CadastralZoneNumber").text = "7422010400:31"
    tree.write(xml, encoding="utf-8")

