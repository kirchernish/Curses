import json
import xml.etree.ElementTree as ET

def json_to_xml(json_data):
    root = ET.Element("Users")
    for user in json_data:
        user_element = ET.SubElement(root, "User")
        for key, value in user.items():
            child = ET.SubElement(user_element, key)
            child.text = str(value)
    return ET.tostring(root, encoding='unicode')

def main():
    try:
        with open('data.json', 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            xml_data = json_to_xml(json_data)
            with open('data.xml', 'w', encoding='utf-8') as xml_file:
                xml_file.write(xml_data)
            print("Конвертация завершена. Данные сохранены в data.xml.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
