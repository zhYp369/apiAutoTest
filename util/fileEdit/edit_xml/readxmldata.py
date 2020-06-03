#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement
print("--"*10)
print(root.nodeName)
print("--"*10)
print(root.nodeValue)
print("--"*10)
print(root.nodeType)
print("--"*10)
print(root.ELEMENT_NODE)