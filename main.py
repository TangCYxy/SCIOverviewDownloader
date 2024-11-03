"""
按照之前的脚本，分结构
"""
import cfgs
import os
import logs
import simulation

defMaps = {}
exportedFileBasePath = ""
inputPublicationFilePath = ""
defaultExportedFileName = ""
defaultExportedFilePath = ""
exportFailedSciNameList = []
succeededSciNameList = []


def mainLoop(sciNameList):
    for sciName in sciNameList:
        try:
            simulation.queryAndExportSciDetail(sciName)
            logs.enhanceLog(f"导出期刊文章成功： {sciName}")
            succeededSciNameList.append(sciName)
        except Exception as e:
            logs.enhanceLog(f"导出期刊文章失败： {sciName}, error is {e}")
            exportFailedSciNameList.append(sciName)

def clearTmpFiles():
    fullPathName = defaultExportedFilePath + defaultExportedFileName
    if os.path.isfile(fullPathName):
        try:
            os.remove(fullPathName)
        except Exception as e:
            logs.enhanceLog(f"删除文件失败： {fullPathName}, error is {e}")


def readTxtFile():
    pass


if __name__ == '__main__':
    print("hello sci!")

    # 从本地load 配置
    cfgs.loadCfgs()


    # 创建导出目录结构
    #
    # # load所有待加载的期刊名称列表
    # sciNameList = readTxtFile()
    #
    # # 清理临时下载目录
    # clearTmpFiles()
    # #
    # mainLoop()

