import os
import shutil
import time

firstQuery = True
YearStr = "2024"
import logs
import pyautogui
import cfgs
import utils


def ensureAtFirstQueryPage(sciName):
    # 判断左上角的search按钮是否有下划线，有就是first页面
    x, y = utils.findColor(cfgs.getInt("firstQueryPageCheckX1"), cfgs.getInt("firstQueryPageCheckY1"),
                           cfgs.getInt("firstQueryPageCheckX2"), cfgs.getInt("firstQueryPageCheckY2"),
                           cfgs.get("firstQueryPageCheckColor"), 0.9)
    if x is not None and y is not None:
        # 都不为0，说明找到了图片
        print("already in the first query page")
        return True
    else:
        logs.enhanceLog("can not continue due to not at first query page for sci %s" % sciName)
        raise Exception("can not continue due to not at first query page for sci %s" % sciName)


def clickAddRow():
    """
    点击添加规则
    :return:
    """
    while (True):
        # 左侧出现一个“移除额外规则”的符号，检测是否存在
        x, y = utils.findColor(cfgs.getInt("firstCondition2AddedCheckX1"), cfgs.getInt("firstCondition2AddedCheckY1"),
                               cfgs.getInt("firstCondition2AddedCheckX2"), cfgs.getInt("firstCondition2AddedCheckY2"),
                               cfgs.get("firstCondition2AddedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 row added")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.getInt("firstCondition2AddRowX"), cfgs.getInt("firstCondition2AddRowY"), interval=0.3)
        time.sleep(1)
    print("first: condition 2 row added")


def selectConditionPublicationName():
    # 点击condition 2(expand condition 2)
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.getInt("firstCondition2ExpandCheckX1"), cfgs.getInt("firstCondition2ExpandCheckY1"),
                               cfgs.getInt("firstCondition2ExpandCheckX2"), cfgs.getInt("firstCondition2ExpandCheckY2"),
                               cfgs.get("firstCondition2ExpandCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 2 menu is expanded!")
            break

        time.sleep(1)

        # 点击condition 1
        pyautogui.click(cfgs.getInt("firstCondition2ExpandX"), cfgs.getInt("firstCondition2ExpandY"), interval=0.3)
        time.sleep(1)

    # 选择 "publication/source title"
    while (True):
        # 检查当前condition是否已经folded
        x, y = utils.findColor(cfgs.getInt("firstCondition2SelectedCheckX1"), cfgs.getInt("firstCondition2SelectedCheckY1"),
                               cfgs.getInt("firstCondition2SelectedCheckX2"), cfgs.getInt("firstCondition2SelectedCheckY2"),
                               cfgs.get("firstCondition2SelectedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 2 'Publication/Source Titles' is selected!")
            break

        time.sleep(1)

        # 点击"year published"
        pyautogui.click(cfgs.getInt("firstCondition2SelectX"), cfgs.getInt("firstCondition2SelectY"), interval=0.3)
        time.sleep(1)


def inputSciPublicationNames(sciName):
    # 点击输入框（选中时有紫色边框）
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.getInt("firstCondition2ClickedCheckX1"), cfgs.getInt("firstCondition2ClickedCheckY1"),
                               cfgs.getInt("firstCondition2ClickedCheckX2"), cfgs.getInt("firstCondition2ClickedCheckY2"),
                               cfgs.get("firstCondition2ClickedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 input box is selected")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.getInt("firstCondition2InputX"), cfgs.getInt("firstCondition2InputY"), interval=0.3)
        time.sleep(1)

    # 输入数据
    pyautogui.write(sciName, interval=0.3)
    time.sleep(1)
    print("first: condition 2 value is input, data is {}" % sciName)


def selectRecommendationContent(sciName):
    # 等待10s，尝试得到推荐（输入框左侧有阴影样式，以及看不到下方的输入框蓝色的边框线了
    maxTryCount = cfgs.getInt("maxPublicationNameRecommendationTryCount")
    recommendationDisplayed = False
    while maxTryCount > 0:
        maxTryCount = maxTryCount - 1
        # 检查颜色
        x, y = utils.findColor(cfgs.getInt("firstCondition2InputRecommendationCheckX1"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckY1"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckX2"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckY2"),
                               cfgs.get("firstCondition2InputRecommendationCheckColor"), 0.9)
        if x is not None and y is not None:
            # 找不到输入框的蓝色下边框了
            time.sleep(1)
        else:
            print("first: publication title recommendation displayed!")
            recommendationDisplayed = True
            break

    # 判断是否已经找到了推荐的期刊名
    if not recommendationDisplayed:
        logs.enhanceLog("can not get recommendation for sci {}, manually check is needed" % sciName)
        pyautogui.alert('请手动确认网络和登录状态是否正常！')

    # 点击推荐项
    while (True):
        # 推荐窗口不再存在
        x, y = utils.findColor(cfgs.getInt("firstCondition2InputRecommendationCheckX1"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckY1"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckX2"),
                               cfgs.getInt("firstCondition2InputRecommendationCheckY2"),
                               cfgs.get("firstCondition2InputRecommendationCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 publication title recommendation is selected")
            break

        time.sleep(1)

        # 点击condition 2 的推荐项
        pyautogui.click(cfgs.getInt("firstCondition2InputRecommendationClickX"),
                        cfgs.getInt("firstCondition2InputRecommendationClickY"), interval=0.3)
        time.sleep(1)

    print("first: condition 2 recommendation publication name selected")


def inputSciName(sciName):
    # 点击添加规则
    clickAddRow()
    # 选择条件为publication name
    selectConditionPublicationName()
    # 点击输入框并输入文章名字
    inputSciPublicationNames(sciName)
    # 选择下方的推荐内容(如果10s内没有出现推荐，可能是因为登录失败了，需要人工确认一下）
    selectRecommendationContent(sciName)
    #


def openExportExcelDialog():
    # 点击export按钮, 看到下拉菜单
    while (True):
        x, y = utils.findColor(cfgs.getInt("exportButtonExpandCheckX1"),
                               cfgs.getInt("exportButtonExpandCheckY1"),
                               cfgs.getInt("exportButtonExpandCheckX2"),
                               cfgs.getInt("exportButtonExpandCheckY2"),
                               cfgs.getInt("exportButtonExpandCheckColor"), 0.9)
        # 如果出现了下拉菜单，跳出
        if x is not None and y is not None:
            # 都不为0，ok
            print("export: export menu expanded")
            break
        else:
            pyautogui.click(cfgs.getInt("exportButtonExpandClickX"), cfgs.get("exportButtonExpandClickY"),
                            interval=0.3)
            time.sleep(1)

    # 点击菜单中对应的excel选项，打开二级对话框
    while (True):
        x, y = utils.findColor(cfgs.getInt("exportDialogDisplayCheckX1"),
                               cfgs.getInt("exportDialogDisplayCheckY1"),
                               cfgs.getInt("exportDialogDisplayCheckX2"),
                               cfgs.getInt("exportDialogDisplayCheckY2"),
                               cfgs.get("exportDialogDisplayCheckColor"), 0.9)
        # 如果出现了export对话框，ok
        if x is not None and y is not None:
            # 都不为0，ok
            print("export: export sub dialog displayed!")
            break
        else:
            pyautogui.click(cfgs.getInt("exportMenuClickX"), cfgs.getInt("exportMenuClickY"),
                            interval=0.3)
            time.sleep(1)


def selectAllDisplayedRecords():
    # 点击records from x to x 的单选框
    while (True):
        x, y = utils.findColor(cfgs.getInt("exportDialogAllRecordSelectedCheckX1"),
                               cfgs.getInt("exportDialogAllRecordSelectedCheckY1"),
                               cfgs.getInt("exportDialogAllRecordSelectedCheckX2"),
                               cfgs.getInt("exportDialogAllRecordSelectedCheckY2"),
                               cfgs.get("exportDialogAllRecordSelectedCheckColor"), 0.9)
        # 如果出现了下拉菜单，跳出
        if x is not None and y is not None:
            # 都不为0，ok
            print("export dialog: all records selected")
            break
        else:
            pyautogui.click(cfgs.getInt("exportDialogAllRecordClickX"), cfgs.getInt("exportDialogAllRecordClickY"),
                            interval=0.3)
            time.sleep(1)


def selectCustomContentSelection():
    # 打开下拉列表框——点击records content下拉列表框，如果出现了蓝色的选中颜色，则说明已打开
    while (True):
        x, y = utils.findColor(cfgs.getInt("exportDialogRecordContentExpandedCheckX1"),
                               cfgs.getInt("exportDialogRecordContentExpandedCheckY1"),
                               cfgs.getInt("exportDialogRecordContentExpandedCheckX2"),
                               cfgs.getInt("exportDialogRecordContentExpandedCheckY2"),
                               cfgs.get("exportDialogRecordContentExpandedCheckColor"), 0.9)
        # 如果出现了下拉菜单，跳出
        if x is not None and y is not None:
            # 都不为0，ok
            print("export dialog: record content menu expanded!")
            break
        else:
            pyautogui.click(cfgs.getInt("exportDialogRecordContentExpandClickX"), cfgs.getInt("exportDialogRecordContentExpandClickY"),
                            interval=0.3)
            time.sleep(1)

    # 选择"custom selection"——回到了export的dialog页面
    while (True):
        x, y = utils.findColor(cfgs.getInt("exportDialogDisplayCheckX1"),
                               cfgs.getInt("exportDialogDisplayCheckY1"),
                               cfgs.getInt("exportDialogDisplayCheckX2"),
                               cfgs.getInt("exportDialogDisplayCheckY2"),
                               cfgs.get("exportDialogDisplayCheckColor"), 0.9)
        # 如果出现了export对话框，ok
        if x is not None and y is not None:
            # 都不为0，ok
            print("export dialog: record content selection changed!")
            break
        else:
            pyautogui.click(cfgs.getInt("exportDialogRecordContentMenuClickX"), cfgs.getInt("exportDialogRecordContentMenuClickY"),
                            interval=0.3)
            time.sleep(1)


def isTmpFileDownloaded():
    fullPathName = cfgs.get("export", "defaultExportedFilePath") + cfgs.get("export", "defaultExportedFileName")
    return os.path.isfile(fullPathName) and os.path.exists(fullPathName)


def clickExport():
    #
    while True:
        # 先看下目标文件是否已经存在，如果存在，则说明下载完毕
        if isTmpFileDownloaded():
            logs.enhanceLog("export: file exported")
            break

        # 检查导出按钮是否已经按下（正在导出中）——一部分文字变成了背景色
        x, y = utils.findColor(cfgs.getInt("exportButtonExportingCheckX1"),
                               cfgs.getInt("exportButtonExportingCheckY1"),
                               cfgs.getInt("exportButtonExportingCheckX2"),
                               cfgs.getInt("exportButtonExportingCheckY2"),
                               cfgs.get("exportButtonExportingCheckColor"), 0.9)
        # 如果出现了下拉菜单，跳出
        if x is not None and y is not None:
            # 都不为0
            print("export: is exporting, wait every 2 seconds")
            time.sleep(2)
        else:
            pyautogui.click(cfgs.getInt("exportButtonExportingClickX"), cfgs.getInt("exportButtonExportingClickY"),
                            interval=0.3)
            time.sleep(1)


def renameAndMoveExportedFile(sciName):

    sourceFileFullPathName = cfgs.get("export", "defaultExportedFilePath") + cfgs.get("export", "defaultExportedFileName")

    targetFileFullPathName = cfgs.get("export", "exportedFileBasePath") + sciName

    shutil.move(sourceFileFullPathName, targetFileFullPathName)

    logs.enhanceLog("sci overview downloaded for sci {} as file {}" % {sciName, targetFileFullPathName})

def exportSearchResult(sciName):
    # 点击export，直到export导出列表弹出
    openExportExcelDialog()

    # 选择 "all records"
    selectAllDisplayedRecords()

    # 点开 "record content"，选择到custom selection
    selectCustomContentSelection()

    # 点击export
    clickExport()

    # 将文件重命名，并拷贝到目标folder
    renameAndMoveExportedFile(sciName)

    #


def doInputSciYear(yearStr):
    """

    :param yearStr:
    :return:
    """
    # 点击输入框（选中时有紫色边框）
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.getInt("firstCondition1ClickedCheckX1"), cfgs.getInt("firstCondition1ClickedCheckY1"),
                               cfgs.getInt("firstCondition1ClickedCheckX2"), cfgs.getInt("firstCondition1ClickedCheckY2"),
                               cfgs.get("firstCondition1ClickedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 input box is selected")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.getInt("firstCondition1InputX"), cfgs.getInt("firstCondition1InputY"), interval=0.3)
        time.sleep(1)

    # 输入数据
    pyautogui.write(yearStr, interval=0.3)
    time.sleep(1)
    print("first: condition 1 value is input, data is {}" % yearStr)


def selectConditionYear():
    # 点击condition 1(expand condition 1)
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.getInt("firstCondition1ExpandCheckX1"), cfgs.getInt("firstCondition1ExpandCheckY1"),
                               cfgs.getInt("firstCondition1ExpandCheckX2"), cfgs.getInt("firstCondition1ExpandCheckY2"),
                               cfgs.get("firstCondition1ExpandCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 menu is expanded!")
            break

        time.sleep(1)

        # 点击condition 1
        pyautogui.click(cfgs.getInt("firstCondition1ExpandX"), cfgs.getInt("firstCondition1ExpandY"), interval=0.3)
        time.sleep(1)

    # 选择year published
    while (True):
        # 检查当前condition是否已经folded
        x, y = utils.findColor(cfgs.getInt("firstCondition1SelectedCheckX1"), cfgs.getInt("firstCondition1SelectedCheckY1"),
                               cfgs.getInt("firstCondition1SelectedCheckX2"), cfgs.getInt("firstCondition1SelectedCheckY2"),
                               cfgs.get("firstCondition1SelectedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 'Year Published' is selected!")
            break

        time.sleep(1)

        # 点击"year published"
        pyautogui.click(cfgs.getInt("firstCondition1SelectX"), cfgs.getInt("firstCondition1SelectY"), interval=0.3)
        time.sleep(1)


def inputSciYears(yearStr):
    # 点击左侧下拉框，并选择condition = year
    selectConditionYear()

    # 输入实际的sciYear
    doInputSciYear(yearStr)


def firstClickSearch():
    # 点击search按钮，要么能看到searching，代表正在搜索中，要么看到左上角已经进入了搜索结果页，否则继续搜索
    while (True):
        # search页面的title是否还能找到底色（进入结果页）
        x1, y1 = utils.findColor(cfgs.getInt("firstCondition2SearchingCheck1X1"),
                                 cfgs.getInt("firstCondition2SearchingCheck1Y1"),
                                 cfgs.getInt("firstCondition2SearchingCheck1X2"),
                                 cfgs.getInt("firstCondition2SearchingCheck1Y2"),
                                 cfgs.get("firstCondition2SearchingCheck1Color"), 0.9)
        # 如果出现了结果页，说明出现了搜索结果，跳出
        if x1 is not None and y1 is not None:
            # 都不为0，ok
            print("first: search ok")
            time.sleep(1)
            break

        # search按钮是否还是亮的（代表没有在搜索）
        x2, y2 = utils.findColor(cfgs.getInt("firstCondition2SearchingCheck2X1"),
                                 cfgs.getInt("firstCondition2SearchingCheck2Y1"),
                                 cfgs.getInt("firstCondition2SearchingCheck2X2"),
                                 cfgs.getInt("firstCondition2SearchingCheck2Y2"),
                                 cfgs.get("firstCondition2SearchingCheck2Color"), 0.9)
        # 如果出现了未点击的搜索按钮，就选择点击
        if x2 is not None and y2 is not None:
            pyautogui.click(cfgs.getInt("firstCondition2SearchButtonX"), cfgs.getInt("firstCondition2SearchButtonY"),
                            interval=0.3)
            time.sleep(1)
        else:
            # 搜索中
            print("first: searching, wait every 2 seconds")


def ensureArticleListShows():
    #
    pass


def firstQueryAndExportSciDetail(sciName):
    # 确认当前在first页面
    ensureAtFirstQueryPage(sciName)
    # 点击输入年份（2024）
    inputSciYears(YearStr)
    # 点击输入期刊名称
    inputSciName(sciName)
    # 点击搜索
    firstClickSearch()
    # 确保相关的article列表已经列出来了（搜索结果已展示）
    # ensureArticleListShows()
    # 点击export
    exportSearchResult(sciName)


def otherQueryAndExportSciDetail(sciName):
    print("xxxxx")
    pass


def queryAndExportSciDetail(sciName):
    global firstQuery
    if (firstQuery):
        # 首次查询
        firstQueryAndExportSciDetail(sciName)
        firstQuery = False
    else:
        # 非首次的查询
        otherQueryAndExportSciDetail(sciName)
