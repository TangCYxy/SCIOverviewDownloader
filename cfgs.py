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
    config.read("./config/xxx.properties", encoding="utf-8")
    print(config.sections())
    # print(config['numbers']["a1"] + 1)
    # print(config['strings']["aa"])


def loadCfgs():
    # initForMac()
    initForWin()


def get(key, section=None, default=None):
    if section is None:
        section = defaultSection
    return config[section].get(key, default)
    # return cfgMap.get(key, default)


def getInt(key, section=None, default=None):
    if section is None:
        section = defaultSection
    result = get(key, section=section, default=default)
    if result is not None:
        return int(result)
    return result
