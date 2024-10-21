
cfgMap = {}


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
    pass


def loadCfgs():
    print("hello sci!")
    initForMac()
    # initForWin()

def get(key, default=None):
    return cfgMap.get(key, default)

def getInt(key, default=None):
    result = get(key, default)
    if result is not None:
        return int(result)
    return result
