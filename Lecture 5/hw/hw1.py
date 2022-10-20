class ModifiedDict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class KeyValueStorage:

    @classmethod
    def read_file(cls, file_path) -> {}:
        data = {}
        f = open(file_path, 'rt', encoding='utf-8')
        for line in f:
            vals = line.replace('\n', '').split('=')
            val = vals[1]
            if val.isnumeric():
                val = int(val)
            data[vals[0]] = val
        f.close()
        return ModifiedDict(data)


data_dict = KeyValueStorage.read_file('task1.txt')
print(f'Access by dot notation result -', data_dict.last_name)
print(f'Access by key in dictionary -', data_dict['name'])
print(f'Value is converted to integer -', isinstance(data_dict.power, int))

data_dict.new = 'one more value'
data_dict[1] = 'erer'
print(f'Value is added to dictionary using dot notation -', data_dict.new)
