import xml.etree.ElementTree as ET
repetition_dict = {}
parser = ET.XMLParser(encoding='Utf-8')
tree = ET.parse('3.1.formats.json.xml/newsafr.xml',parser)
root = tree.getroot()
list_of = root.findall('channel/item')
for news in list_of:
    description = news.find('description').text
    for word in description.split():
        if len(word) > 6:
            if word in repetition_dict:
                repetition_dict[word] = repetition_dict[word] + 1
                continue
            repetition_dict[word] = 1
for i in range(1, 11):
    for k, v in repetition_dict.items():
        max_ = max(repetition_dict.values())
        if max_ == v:
            print(f'Top {i} is {k} which was used {v} times ')
            break
    del repetition_dict[k]