import glob
import xml.etree.ElementTree as ET
import pandas as pd
xml_list = glob.glob("xml/*.xml")

df = pd.DataFrame(columns = ['Номер', 'Площа'])
for xml in xml_list:
    print(xml)
    tree = ET.parse(xml)
    qadNum = tree.find(".//CadastralZoneNumber").text+":"+tree.find(".//CadastralQuarterNumber").text+":"+ tree.find(".//ParcelID").text
    square = tree.find(".//Size").text
    df.loc[len(df.index)] = [qadNum, square]
df.to_csv("table.csv")