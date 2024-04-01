
project_name = input("Введите шифр проекта: ")

work_link = "https://raw.githubusercontent.com/lenikitio/" + project_name + "/main/field_data.kml"

with open("Полевые_данные_auto.kml", 'w', encoding= 'utf-8') as data:
    data.write(
        '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        '<Document>\n'
        '	<NetworkLink>\n'
        f'	<name>{project_name}</name>\n'
        '		<Link>\n'
        f'			<href>{work_link}</href>\n'
        '		</Link>\n'
        '	</NetworkLink>\n'
        '</Document>\n'
        '</kml>\n'
    )