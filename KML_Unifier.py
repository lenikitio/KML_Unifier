from os import listdir
import os
from zipfile import ZipFile
# Объединение полётов
with open("Полёты.kml", 'w', encoding= 'utf-8') as data:
    data.write('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
               '  <Document>\n'
               '    <Style id="style_zone">\n'
               '      <LineStyle>\n'
               '        <color>FFFF0000</color>\n'
               '      </LineStyle>\n'
               '    </Style>\n'
               '    <Folder>\n'
               '      <name>Все_полёты</name>\n'
               '      <description>&lt;table border = &quot;1&quot; cellpadding = &quot;2&quot;>&lt;tr>&lt;td>Номер полета&lt;/td>&lt;td>001&lt;/td>&lt;/tr>&lt;tr>&lt;td>Номер борта&lt;/td>&lt;td>20305&lt;/td>&lt;/tr>&lt;tr>&lt;td>Дата&lt;/td>&lt;td>18.06.2023&lt;/td>&lt;/tr>&lt;tr>&lt;td>Время&lt;/td>&lt;td>08:45:08&lt;/td>&lt;/tr>&lt;/table></description>\n'
               '      <Folder>\n')
    for file in listdir('Отчеты/KML'):
        if file.endswith(".kml"):
                    flight = 'Отчеты/KML/' + file
                    with open(flight, 'r', encoding= 'utf-8') as kml:
                           lines = kml.readlines()
                           data.writelines(lines[13:-4])
    data.write('      </Folder>\n'
                '    </Folder>\n'
               '  </Document>\n'
               '</kml>')
    

    # Объединение КТ из swmaps
with open("КТ_и_ПБС.kml", 'w', encoding= 'utf-8') as kt:
    kt.write('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
               '  <Document>\n'
               '    <name>КТ и ПБС</name>\n'
               '    <open>0</open>\n'
               '    <description>Exported using SW Maps</description>\n'
               '      <Folder>\n')
    for date in listdir('PVP_data/'):
        for group in listdir('PVP_data/' + date):
                for file in listdir('PVP_data/' + date + '/' + group + '/Ground_Photo/Export'):
                    if file.endswith(".kmz"):
                        zip_point = 'PVP_data/' + date + '/' + group + '/Ground_Photo/Export/' + file
                        with ZipFile(zip_point, 'r') as temp_zip:
                            temp_zip.extractall('temp_file') 
                        with open('temp_file/doc.kml', 'r', encoding= 'utf-8') as kml:
                            lines = kml.readlines()
                            kt.writelines(lines[8: -3])

    kt.write('    </Folder>\n'
               '  </Document>\n'
               '</kml>')