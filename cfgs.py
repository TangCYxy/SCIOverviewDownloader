import configparser
cfgMap = {}

config = configparser.ConfigParser()
defaultSection = "positions"
def initForMac():
    # first 输入sciYear的坐标轴
    cfgMap['firstSciYearInputX'] = 100
    cfgMap['firstSciYearInputY'] = 100
    cfgMap['firstSciYearConditionFoldedX'] = 100
    cfgMap['firstSciYearConditionFoldedY'] = 100
    cfgMap['firstSciYearConditionExpandedX'] = 100
    cfgMap['firstSciYearConditionExpandedY'] = 100
    return cfgMap


def initForWin():
    config.read("./config/xxx.properties")
    print(config.sections())
    print(config['numbers']["a1"] + 1)
    print(config['strings']["aa"])




def loadCfgs():
    # initForMac()
    initForWin()

def get(section, key, default=None):
    return config[section].get(key, default)
    # return cfgMap.get(key, default)

def get(key, default=None):
    return get(defaultSection, key, default)

def getInt(section, key, default=None):
    result = get(section, key, default)
    if result is not None:
        return int(result)
    return result
def getInt(key, default=None):
    result = get(key, default)
    if result is not None:
        return int(result)
    return result
