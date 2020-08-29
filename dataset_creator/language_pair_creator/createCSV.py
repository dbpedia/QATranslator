import json
import pandas as pd

data = []


def parseJsonData(f):
    global data
    data = []
    while (True):
        line = f.readline()
        if line == '':
            break
        parsed_json = json.loads(line)
        data.append(parsed_json)


def createCSV(name):
    global data
    questions = []
    id = []
    lang = []
    for i in range(len(data)):
        item = data[i]
        questions.append(item['question'])
        lang.append(item['lang'])
        id.append(item["questionId"])

    output = pd.DataFrame({"questionId":id,'questions': questions, 'lang': lang })
    output.to_csv(name+'.csv', index=False)


if __name__ == '__main__':
    for i in range(3, 10):
        with open('qald-'+str(i)+'-train.json', 'r') as f:
            parseJsonData(f)
        createCSV("qald-"+str(i)+"-train")

        with open('qald-'+str(i)+'-test.json','r') as f:
            parseJsonData(f)
        createCSV('qald-'+str(i)+'-test')



