from os import listdir

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