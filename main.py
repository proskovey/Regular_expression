import re
from pprint import pprint
import csv

pattern_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

def fix(contact_list: list):
    list_new = list()
    for contact in contact_list:
        name = ' '.join(contact[:3]).split(' ')
        result = [name[0], name[1], name[2], contact[3], contact[4], re.sub(pattern_phone, 
        sub_phone, contact[5]), contact[6]]
        list_new.append(result)
    return combine(list_new)


def combine(contacts: list):
    for cont in contacts:
        first_name = cont[0]
        last_name = cont[1]
        for cont_new in contacts:
            first_name_new = cont_new[0]
            last_name_new = cont_new[1]
            if first_name == first_name_new and last_name == last_name_new:
                if cont[2] == "": cont[2] = cont_new[2]
                if cont[3] == "": cont[3] = cont_new[3]
                if cont[4] == "": cont[4] = cont_new[4]
                if cont[5] == "": cont[5] = cont_new[5]
                if cont[6] == "": cont[6] = cont_new[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fix(contacts_list))