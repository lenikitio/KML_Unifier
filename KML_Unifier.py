from os import listdir
import os
from zipfile import ZipFile
import xml.etree.ElementTree as ET


# Объединение полётов
file_flight =  '<?xml version="1.0" encoding="UTF-8"?>\n' + \
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n' + \
               '  <Document>\n' + \
               '    <Style id="style_zone">\n' + \
               '      <LineStyle>\n' + \
               '        <color>FFFF0000</color>\n' + \
               '      </LineStyle>\n'+ \
               '    </Style>\n' + \
               '    <Folder>\n' + \
               '      <name>Выполненные_полёты</name>\n' + \
               '      <description>&lt;table border = &quot;1&quot; cellpadding = &quot;2&quot;>&lt;tr>&lt;td>Номер полета&lt;/td>&lt;td>001&lt;/td>&lt;/tr>&lt;tr>&lt;td>Номер борта&lt;/td>&lt;td>20305&lt;/td>&lt;/tr>&lt;tr>&lt;td>Дата&lt;/td>&lt;td>18.06.2023&lt;/td>&lt;/tr>&lt;tr>&lt;td>Время&lt;/td>&lt;td>08:45:08&lt;/td>&lt;/tr>&lt;/table></description>\n' + \
               '    </Folder>\n' + \
               '  </Document>\n' + \
               '</kml>'
fly_tree = ET.ElementTree(ET.fromstring(file_flight))
fly_root = fly_tree.getroot()
for root, dirs, files in os.walk('Отчеты'):
    for file in files:
        if file.endswith(".kml"):
            flight = os.path.join(root, file)
            flag = False
            fly_folder = fly_root[0][1]
            if fly_folder.find('Folder') != None:
                for project in fly_folder.findall('Folder'):
                    if project.attrib['name'] == file[-15: -10]:
                        flag = True
                        board_folder = project
            if flag == False:
                board_folder = ET.SubElement(fly_folder, 'Folder', {'name' : file[-15: -10]})
                sub_name = ET.SubElement(board_folder, 'name')
                sub_name.text = file[-15: -10]
            with open(flight, 'r', encoding= 'utf-8') as fly_data:
                 lines = fly_data.readlines()
                 lines_tree = ET.ElementTree(ET.fromstringlist(lines))
                 lines_root = lines_tree.getroot()
                 for placemark in lines_root[0][1][2].findall('{http://www.opengis.net/kml/2.2}Placemark'):
                    if placemark[0].text == 'Площадная аэрофотосъемка':
                           lines_root[0][1][2].remove(placemark)
                       
                 board_folder.append(lines_root[0][1][2])
fly_to_write = str(ET.tostring(fly_root, encoding= 'utf-8', method= 'xml', xml_declaration=True).decode())
with open("flight_data.kml", 'w', encoding= 'utf-8') as flight_data:
     flight_data.write(fly_to_write)

             


#Объединение КТ из swmaps
file_kml = '<?xml version="1.0" encoding="UTF-8"?>\n' + \
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n' + \
               '  <Document>\n' + \
               '    <Folder>\n' + \
               '      <name>КТ_и_ПБС</name>\n' + \
               '        <Style id="КТ">\n' + \
               '            <IconStyle>\n' + \
               '                <color>FF011DF0</color>\n' + \
               '                <scale>0.5</scale>\n' + \
               '                <Icon>\n' + \
               '                    <href>http://maps.google.com/mapfiles/kml/shapes/donut.png</href>\n' + \
               '                </Icon>\n' + \
               '                <hotSpot x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>\n' + \
               '            </IconStyle>\n' + \
               '            <LabelStyle>\n' + \
               '                <scale>0</scale>\n' + \
               '            </LabelStyle>\n' + \
               '        </Style>\n' + \
               '        <Style id="ПБС">\n' + \
               '            <IconStyle>\n' + \
               '                <scale>0.03</scale>\n' + \
               '                <Icon>\n' + \
               '                    <href>https://cdn.vseinstrumenti.ru/images/goods/4472406/1000x1000/63242250.jpg</href>\n' + \
               '                </Icon>\n' + \
               '                <hotSpot x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>\n' + \
               '            </IconStyle>\n' + \
               '            <LabelStyle>\n' + \
               '                <scale>0</scale>\n' + \
               '            </LabelStyle>\n' + \
               '        </Style>\n' + \
               '        <Style id="ГГС">\n' + \
               '            <IconStyle>\n' + \
               '                <scale>0.02</scale>\n' + \
               '                <Icon>\n' + \
               '                    <href>https://cdn0.iconfinder.com/data/icons/smashicons-design-flat-vol-2/58/94_-_Triangle_design_graphic_tool-1024.png</href>\n' + \
               '                </Icon>\n' + \
               '                <hotSpot x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>\n' + \
               '            </IconStyle>\n' + \
               '            <LabelStyle>\n' + \
               '                <scale>0</scale>\n' + \
               '            </LabelStyle>\n' + \
               '        </Style>\n' + \
               '    </Folder>\n' + \
               '  </Document>\n' + \
               '</kml>'
fold = ET.ElementTree(ET.fromstring(file_kml))
root = fold.getroot()
for dir in listdir('PVP_data/'):
    for group in listdir('PVP_data/' + dir):
        if os.path.isdir('PVP_data/' + dir + '/' + group + '/Ground_Photo/Export') != True:
             continue
        for file in listdir('PVP_data/' + dir + '/' + group + '/Ground_Photo/Export'):
            if file.endswith(".kmz"):
                zip_point = 'PVP_data/' + dir + '/' + group + '/Ground_Photo/Export/' + file
                with ZipFile(zip_point, 'r') as zip_file:
                    with zip_file.open('doc.kml', 'r') as kml:
                        lines = [x.decode('utf-8') for x in kml.readlines()]
                        flag = False
                        if root[0][0].find('Folder') != None:
                             for project in root[0][0].findall('Folder'):
                                  if project.attrib['name'] == group:
                                       flag = True
                                       find_group = project
                        if flag == False:
                            find_group = ET.SubElement(root[0][0], 'Folder', {'name' : group})
                            sub_name = ET.SubElement(find_group, 'name')
                            sub_name.text = group
                        date_folder = ET.SubElement(find_group, 'Folder', {'name' : dir})
                        date_folder_name = ET.SubElement(date_folder, 'name')
                        date_folder_name.text = dir
                        new_tree = ET.ElementTree(ET.fromstringlist(lines))
                        new_root = new_tree.getroot()
                        all_placemark = new_root[0][3].findall('{http://www.opengis.net/kml/2.2}Placemark')
                        for elem in all_placemark:
                             type_point = elem[0].text[9]
                             if type_point == 'P':
                                  elem.find('{http://www.opengis.net/kml/2.2}styleUrl').text = '#ПБС'
                             elif type_point.isnumeric() == True:
                                  elem.find('{http://www.opengis.net/kml/2.2}styleUrl').text = '#КТ'
                             else:
                                  elem.find('{http://www.opengis.net/kml/2.2}styleUrl').text = '#ГГС'
                             date_folder.append(elem)
point_to_write = str(ET.tostring(root, encoding= 'utf-8', method= 'xml', xml_declaration=True).decode())
with open("point_data.kml", 'w', encoding= 'utf-8') as points_data:
     points_data.write(point_to_write)

                        

# Создание файла с исходными данными
file_initial = '<?xml version="1.0" encoding="UTF-8"?>\n' + \
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n' + \
               '  <Document>\n' + \
               '   <Folder>\n' + \
               '    <name>Исходные данные</name>\n' + \
               '   </Folder>\n' + \
               '   <Folder>\n' + \
               '    <name>Режимы</name>\n' + \
               '   </Folder>\n' + \
               '  </Document>\n' + \
               '</kml>'
initial_tree = ET.ElementTree(ET.fromstring(file_initial))
initial_root= initial_tree.getroot()
for root, dirs, files in os.walk('Исходные_данные'):
        for file in files:
            if file.endswith(".kml"):
                appended_root = initial_root[0][1]
                if dirs.__contains__('Режимы'):
                    appended_root = initial_root[0][0]
                source = os.path.join(root, file)
                with open(source, 'r', encoding= 'utf-8') as kml:
                     lines = kml.readlines()
                     work_tree = ET.ElementTree(ET.fromstringlist(lines))
                     work_root = work_tree.getroot()
                     document_name = ET.SubElement(work_root[0], 'name')
                     document_name.text = file
                     appended_root.append(work_root[0])
initial_to_write = str(ET.tostring(initial_root, encoding= 'utf-8', method= 'xml', xml_declaration=True).decode())
with open("initial_data.kml", 'w', encoding= 'utf-8') as initial:
     initial.write(initial_to_write)

     
    
