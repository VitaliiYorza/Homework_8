import json
with open('3.1.formats.json.xml/newsafr.json',encoding='utf-8') as f:
    cycle = 0
    list_of_words = []
    repetition_dict = {}
    json_data = json.load(f)
    for number_of_description in range(len(json_data['rss']['channel']['items'])):
            for word in json_data['rss']['channel']['items'][number_of_description]['description'].split():
                if len(word) > 6 :
                    if word in repetition_dict:
                        repetition_dict[word] = repetition_dict[word] + 1
                        continue
                    repetition_dict[word] = 1
    for i in range(1,11):
        for k,v in repetition_dict.items():
            max_ = max(repetition_dict.values())
            if max_ == v:
                print(f'Top {i} is {k} which was used {v} times ')
                break
        del repetition_dict[k]
