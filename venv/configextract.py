from configparser import ConfigParser
class ConfigExtract:
    def numericaldictionary_extract(self,section_name):
        config = ConfigParser()
        config.read(r"C:\Users\subra\PycharmProjects\pythonProject\pythonProject\pythonProject5\SnakeLadderFinal\venv\config.ini")
        keys=list(config[section_name])
        values=[]
        for iter in list(config[section_name]):
            values.append(config[section_name][iter])
        temp= {int(i): int(j) for i, j in zip(keys, values)}
        return temp

    def dictionary_extract(self,section_name):
        config = ConfigParser()
        config.read(r"C:\Users\subra\PycharmProjects\pythonProject\pythonProject\pythonProject5\SnakeLadderFinal\venv\config.ini")
        keys=list(config[section_name])
        values=[]
        for iter in list(config[section_name]):
            values.append(config[section_name][iter])
        temp= {i: int(j) for i, j in zip(keys, values)}
        return temp