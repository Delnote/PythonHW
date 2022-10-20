class KeyValueStorage(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


data = {}

f = open('task1.txt', 'rt', encoding='utf-8')
for line in f:
    values = line.replace('\n', '').split('=')
    val = values[1]
    if val.isnumeric():
        val = int(val)
    data[values[0]] = val
f.close()


data_dict = KeyValueStorage(data)
print(f'Access by dot notation result -', data_dict.last_name)
print(f'Access by key in dictionary -', data_dict['name'])
print(f'Value is converted to integer -', isinstance(data_dict.power, int))

data_dict.new = 'one more value'
print(f'Value is added to dictionary using dot notation -', data_dict.new)


