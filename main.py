from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
find_phone = re.compile(r'(^\+7|8)?\s*\(?(\d{3})\)?\-?\s*(\d+)[\s-]*(\d{2})[\s-]*(\d{2})([\s-]*\((\D+\d+)\))?')

contacts_list_dict = {}

row_contacts_list = 0
for contact in contacts_list:
  contact_name = (' ').join(contact[0:3]).split()
  i = 0
  for val in contact_name:
    contact[i] = val
    i += 1
  contact[5] = find_phone.sub(r'+7(\2)\3-\4-\5 \7', contact[5])

  lastname = contact[0]
  data = contact[1:]

  if lastname in contacts_list_dict.keys():
    for number in range(0, 6):
      if contacts_list_dict[lastname][number] == '':
        contacts_list_dict[lastname][number] = contact[number + 1]
  else:
    contacts_list_dict[lastname] = data

  row_contacts_list += 1

contacts_list_edit = []
for key, val in contacts_list_dict.items():
  contacts_list_edit.append([key] + val)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_edit)