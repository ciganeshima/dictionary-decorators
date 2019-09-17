from collections.abc import MutableMapping
import os


class DirDict(MutableMapping):
    def __init__(self, path):
        if os.path.exists(path):
            self._path = path
        else:
            print('Incorrect path')

    def dict_files(self):
        return os.listdir(self._path)

    def __iter__(self):
        return (key for key in os.listdir(path=self._path))

    def __getitem__(self, key):
        path = self._path + '/' + key
        if key in self.dict_files():
            with open(path, 'r') as f:
                return f.read()
        else:
            raise IndexError(key)

    def __setitem__(self, key, value):
        path = self._path + '/' + key
        try:
            with open(path, 'w') as file:
                file.write(str(value))
        except: any

    def __len__(self):
        return len(os.listdir(self._path))

    def __delitem__(self,key):
        path = self._path + '/' + key
        if os.path.exists(path):
            os.remove(path)
        else:
            raise IndexError(key)



d = DirDict('C:/Users/Acer/PycharmProjects/profile/lang') #init
d['lang'] = 'PythonKappa' #setitem
d['rofl'] = 'asdlkasdl;' #setitem
print(d['lang']) #getitem
print(len(d)) #len
del d['rofl'] #del
print(len(d))
for x in d.items(): #iter
    print(x)


