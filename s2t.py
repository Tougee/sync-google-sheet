import opencc
import xml.etree.ElementTree as ET

converter = opencc.OpenCC('s2t.json')

xmlTree = ET.parse('./client/zh.xml')
rootElement = xmlTree.getroot()
for element in rootElement.findall('string'):
    content = element.text
    element.text = converter.convert(content)

xmlTree.write('./client/zh-HK.xml', encoding='UTF-8')
