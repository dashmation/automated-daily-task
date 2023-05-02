import json
import xmltodict

def xmlToJSON():
    with open("temp.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()
        
        json_data = json.dumps(data_dict)

        # print(data_dict['hierarchy']['node']['node']['node']['node']['node'])
        
        # Write the json data to output
        # json file
        # with open("data.json", "w") as json_file:
        #     json_file.write(json_data)
        #     # json_file.close()
    return data_dict['hierarchy']['node']

def searchDOM(dotted_dict):
    number_of_nodes = []
    for key in dotted_dict:
        # print(len(dotted_dict[key]))
        number_of_nodes.append(len(dotted_dict[key]))
    print(number_of_nodes)

    for it in number_of_nodes:
        print()
    



dict_temp = xmlToJSON()
searchDOM(dict_temp)