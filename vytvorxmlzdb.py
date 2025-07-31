import sqlite3
from datetime import datetime

dateAndTime = datetime.now().strftime("%Y-%m-%d_%H:%M")

conn = sqlite3.connect("/home/sysadmin/OTE/relaystatus01.db")
c = conn.cursor()

c.execute("SELECT id, date, time, frequency, UL1, UL2, UL3, IL1, IL2, IL3, PL1, PL2, PL3, impPower, expPower, priceOTE, statusRelay, error FROM cisla WHERE date = DATE('now')")
data = c.fetchall()

import xml.etree.ElementTree as ET

root = ET.Element("elektrodata")

for row in data:
    id = ET.SubElement(root, "elektrodata")
    ET.SubElement(id, "id").text = str(row[0])
    ET.SubElement(id, "date").text = str(row[1])
    ET.SubElement(id, "time").text = str(row[2])
    ET.SubElement(id, "frequency").text = str(row[3])
    ET.SubElement(id, "UL1").text = str(row[4])
    ET.SubElement(id, "UL2").text = str(row[5])
    ET.SubElement(id, "UL3").text = str(row[6])
    ET.SubElement(id, "IL1").text = str(row[7])
    ET.SubElement(id, "IL2").text = str(row[8])
    ET.SubElement(id, "IL3").text = str(row[9])
    ET.SubElement(id, "PL1").text = str(row[10])
    ET.SubElement(id, "PL2").text = str(row[11])
    ET.SubElement(id, "PL3").text = str(row[12])
    ET.SubElement(id, "impPower").text = str(row[13])
    ET.SubElement(id, "expPower").text = str(row[14])
    ET.SubElement(id, "priceOTE").text = str(row[15])
    ET.SubElement(id, "statusRelay").text = str(row[16])
    ET.SubElement(id, "error").text = str(row[17])
    
tree = ET.ElementTree(root)
tree.write(f"/home/sysadmin/OTE/XMLfiles/export_{dateAndTime}.xml", encoding="utf-8", xml_declaration=True)
