from os import listdir
import shutil
from zipfile import ZipFile
# Объединение полётов
with open("Полевые_данные.kml", 'w', encoding= 'utf-8') as data:
    data.write('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
               '  <Document>\n'
               '    <Style id="style_zone">\n'
               '      <LineStyle>\n'
               '        <color>FFFF0000</color>\n'
               '      </LineStyle>\n'
               '    </Style>\n'
               '    <Folder>\n'
               '      <name>Выполненные_полёты</name>\n'
               '      <description>&lt;table border = &quot;1&quot; cellpadding = &quot;2&quot;>&lt;tr>&lt;td>Номер полета&lt;/td>&lt;td>001&lt;/td>&lt;/tr>&lt;tr>&lt;td>Номер борта&lt;/td>&lt;td>20305&lt;/td>&lt;/tr>&lt;tr>&lt;td>Дата&lt;/td>&lt;td>18.06.2023&lt;/td>&lt;/tr>&lt;tr>&lt;td>Время&lt;/td>&lt;td>08:45:08&lt;/td>&lt;/tr>&lt;/table></description>\n')
    for file in listdir('Отчеты/KML'):
        if file.endswith(".kml"):
                    flight = 'Отчеты/KML/' + file
                    with open(flight, 'r', encoding= 'utf-8') as kml:
                            lines = kml.readlines()
                            count = 0
                            finish = 0

                            for i, elem in enumerate(lines):
                                if elem.__contains__('<name>Площадная аэрофотосъемка</name>\n'):
                                        count += 1
                                        finish = i + 11
                            begin = finish - (12 * count)
                            if begin != 0:
                                data.writelines(lines[11: begin])
                                data.writelines(lines[finish:-3])
                            else:
                                data.writelines(lines[11:-3])

    # Объединение КТ из swmaps
    data.write('    </Folder>\n'
               '    <Folder>\n'
               '      <name>КТ_и_ПБС</name>\n'
               '        <visibility>1</visibility>\n'
               '        <open>0</open>\n'
               '        <Style id="Opoznaki-PointStyle">\n'
               '            <IconStyle>\n'
               '                <color>FF011DF0</color>\n'
               '                <scale>0.5</scale>\n'
               '                <Icon>\n'
               '                    <href>http://maps.google.com/mapfiles/kml/shapes/donut.png</href>\n'
               '                </Icon>\n'
               '                <hotSpot x="0.5" y="0.5" xunits="fraction" yunits="fraction"/>\n'
               '            </IconStyle>\n'
               '            <LabelStyle>\n'
               '                <scale>0</scale>\n'
               '            </LabelStyle>\n'
               '        </Style>\n'
               '        <Style id="Opoznaki-Style">\n'
               '            <LineStyle>\n'
               '                <color>FF011DF0</color>\n'
               '                <width>3</width>\n'
               '            </LineStyle>\n'
               '            <PolyStyle>\n'
               '                <color>509F264E</color>\n'
               '            </PolyStyle>\n'
               '        </Style>/\n')
    
    for dir in listdir('PVP_data/'):
        for group in listdir('PVP_data/' + dir):
                for file in listdir('PVP_data/' + dir + '/' + group + '/Ground_Photo/Export'):
                    if file.endswith(".kmz"):
                        zip_point = 'PVP_data/' + dir + '/' + group + '/Ground_Photo/Export/' + file
                        temp = 'temp_file'
                        with ZipFile(zip_point, 'r') as temp_zip:
                            temp_zip.extractall(temp) 
                        with open(temp + '/doc.kml', 'r', encoding= 'utf-8') as kml:
                            lines = kml.readlines()
                            data.writelines(lines[32: -3])
    shutil.rmtree(temp)

    data.write('    </Folder>\n'
               '  </Document>\n'
               '</kml>')
    