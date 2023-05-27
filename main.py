import json
import pickle

# 1. Дано: довільний список словників. Необхідно записати їх у файл за допомогою модуля pickle.
# У кожному словнику однаковий набір ключів, а всі значення представлені у вигляді рядків.

dicts = [
    {'key1': 'los', 'key2': 'John', 'key3': '+15550100482'},
    {'key1': '23564', 'key2': '$', 'key3': 'debt'},
    {'key1': 'Poor', 'key2': 'John', 'key3': 'True'}
]

with open('list_of_dicts.bin', 'wb') as dicts_file:
    pickle.dump(dicts, dicts_file)

# 2. Дано два словники
# A = {'key': 1}
# B = {'key1: 2}
# Необхідно написати код який їх об'єднуватиме
#
# C = {'key': 1, 'key1': 2}
# Але потрібно також враховувати колізії,
# наприклад ситуація коли у нас два однакові ключі
# і щоб не втратити значення потрібно записати в один ключ список в якому будуть значення
#
# Наприклад:
# A = {'key': 1, 'key2': True}
# B = {'key': 'Hello'}
# C = {'key': [1, 'Hello'], 'key2': True}
# Записати результат у файл result.json у форматі JSON.

filename = 'merged_dict.json'
A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}

C = dict(A)  # Копіюємо перший словник, щоб не змінювати його прямо в коді

for key, value in B.items():
    if key in C:
        if not isinstance(C[key], list):
            C[key] = [C[key]]
        C[key].append(value)
    else:
        C[key] = value

with open(filename, 'w') as file:
    json.dump(C, file)
