import time

firstQuery = True
YearStr = "2024"
import logs
import pyautogui
import cfgs
import utils




def ensureAtFirstQueryPage(sciName):
    # 判断左上角的search按钮是否有下划线，有就是first页面
    x, y = utils.findColor(cfgs.get("firstQueryPageCheckX1"), cfgs.get("firstQueryPageCheckY1"),
                           cfgs.get("firstQueryPageCheckX2"), cfgs.get("firstQueryPageCheckY2"),
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
        x, y = utils.findColor(cfgs.get("firstCondition2AddedCheckX1"), cfgs.get("firstCondition2AddedCheckY1"),
                               cfgs.get("firstCondition2AddedCheckX2"), cfgs.get("firstCondition2AddedCheckY2"),
                               cfgs.get("firstCondition2AddedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 row added")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.get("firstCondition2AddRowX"), cfgs.get("firstCondition2AddRowY"), interval=0.3)
        time.sleep(1)
    print("first: condition 2 row added")


def selectConditionPublicationName():
    # 点击condition 2(expand condition 2)
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.get("firstCondition2ExpandCheckX1"), cfgs.get("firstCondition2ExpandCheckY1"),
                               cfgs.get("firstCondition2ExpandCheckX2"), cfgs.get("firstCondition2ExpandCheckY2"),
                               cfgs.get("firstCondition2ExpandCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 2 menu is expanded!")
            break

        time.sleep(1)

        # 点击condition 1
        pyautogui.click(cfgs.get("firstCondition2ExpandX"), cfgs.get("firstCondition2ExpandY"), interval=0.3)
        time.sleep(1)

    # 选择 "publication/source title"
    while (True):
        # 检查当前condition是否已经folded
        x, y = utils.findColor(cfgs.get("firstCondition2SelectedCheckX1"), cfgs.get("firstCondition2SelectedCheckY1"),
                               cfgs.get("firstCondition2SelectedCheckX2"), cfgs.get("firstCondition2SelectedCheckY2"),
                               cfgs.get("firstCondition2SelectedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 2 'Publication/Source Titles' is selected!")
            break

        time.sleep(1)

        # 点击"year published"
        pyautogui.click(cfgs.get("firstCondition2SelectX"), cfgs.get("firstCondition2SelectY"), interval=0.3)
        time.sleep(1)


def inputSciPublicationNames(sciName):
    # 点击输入框（选中时有紫色边框）
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.get("firstCondition2ClickedCheckX1"), cfgs.get("firstCondition2ClickedCheckY1"),
                               cfgs.get("firstCondition2ClickedCheckX2"), cfgs.get("firstCondition2ClickedCheckY2"),
                               cfgs.get("firstCondition2ClickedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 input box is selected")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.get("firstCondition2InputX"), cfgs.get("firstCondition2InputY"), interval=0.3)
        time.sleep(1)

    # 输入数据
    pyautogui.write(sciName, interval=0.3)
    time.sleep(1)
    print("first: condition 2 value is input, data is {}" % sciName)


def selectRecommendationContent(sciName):
    # 等待10s，尝试得到推荐（输入框左侧有阴影样式，以及看不到下方的输入框蓝色的边框线了
    maxTryCount = cfgs.get("maxPublicationNameRecommendationTryCount")
    recommendationDisplayed = False
    while maxTryCount > 0:
         maxTryCount = maxTryCount - 1

        # 检查颜色
        if hit:
            break
        else:
            time.sleep(1)

    if not recommendationDisplayed:
        logs.enhanceLog("can not get recommendation for sci {}, manually check is needed" % sciName)
        pyautogui.alert('请手动确认网络和登录状态是否正常！')

xxxxxxxxxxxxxxxxx todo
    # 点击推荐项
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.get("firstCondition2ClickedCheckX1"), cfgs.get("firstCondition2ClickedCheckY1"),
                               cfgs.get("firstCondition2ClickedCheckX2"), cfgs.get("firstCondition2ClickedCheckY2"),
                               cfgs.get("firstCondition2ClickedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，ok
            print("first: condition 2 input box is selected")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.get("firstCondition2InputX"), cfgs.get("firstCondition2InputY"), interval=0.3)
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
    selectRecommendationContent()
    #


def clickExport():
    # 点击export，直到export导出列表弹出
    while(xxx)

    # 选择 "all records"

    # 点开 "record content"，选择到custom selection

    # 点击export

    # 将文件重命名，并拷贝到目标folder
    renameAndMoveExportedFile()

    #


def doInputSciYear(yearStr):
    """

    :param yearStr:
    :return:
    """
    # 点击输入框（选中时有紫色边框）
    while (True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.get("firstCondition1ClickedCheckX1"), cfgs.get("firstCondition1ClickedCheckY1"),
                               cfgs.get("firstCondition1ClickedCheckX2"), cfgs.get("firstCondition1ClickedCheckY2"),
                               cfgs.get("firstCondition1ClickedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 input box is selected")
            break

        time.sleep(1)

        # 点击condition 2 的输入框(三次点击，直接框选内容，如果有）
        pyautogui.tripleClick(cfgs.get("firstCondition1InputX"), cfgs.get("firstCondition1InputY"), interval=0.3)
        time.sleep(1)

    # 输入数据
    pyautogui.write(yearStr, interval=0.3)
    time.sleep(1)
    print("first: condition 1 value is input, data is {}" % yearStr)


def selectConditionYear():
    # 点击condition 1(expand condition 1)
    while(True):
        # 检查当前是否已经打开了下拉菜单
        x, y = utils.findColor(cfgs.get("firstCondition1ExpandCheckX1"), cfgs.get("firstCondition1ExpandCheckY1"), cfgs.get("firstCondition1ExpandCheckX2"), cfgs.get("firstCondition1ExpandCheckY2"),
            cfgs.get("firstCondition1ExpandCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 menu is expanded!")
            break

        time.sleep(1)

        # 点击condition 1
        pyautogui.click(cfgs.get("firstCondition1ExpandX"), cfgs.get("firstCondition1ExpandY"), interval=0.3)
        time.sleep(1)

    # 选择year published
    while(True):
        # 检查当前condition是否已经folded
        x, y = utils.findColor(cfgs.get("firstCondition1SelectedCheckX1"), cfgs.get("firstCondition1SelectedCheckY1"),
                               cfgs.get("firstCondition1SelectedCheckX2"), cfgs.get("firstCondition1SelectedCheckY2"),
                               cfgs.get("firstCondition1SelectedCheckColor"), 0.9)
        if x is not None and y is not None:
            # 都不为0，说明当前已经打开了下拉菜单
            print("first: condition 1 'Year Published' is selected!")
            break

        time.sleep(1)

        # 点击"year published"
        pyautogui.click(cfgs.get("firstCondition1SelectX"), cfgs.get("firstCondition1SelectY"), interval=0.3)
        time.sleep(1)



def inputSciYears(yearStr):
    # 点击左侧下拉框，并选择condition = year
    selectConditionYear()

    # 输入实际的sciYear
    doInputSciYear(yearStr)

def firstQueryAndExportSciDetail(sciName):
    # 确认当前在first页面
    ensureAtFirstQueryPage(sciName)
    # 点击输入年份（2024）
    inputSciYears(YearStr)
    # 点击输入期刊名称
    inputSciName(sciName)
    # 点击搜索
    clickSearch()
    # 确保相关的article列表已经列出来了（搜索结果已展示）
    ensureArticleListShows()
    # 点击export
    clickExport()



def queryAndExportSciDetail(sciName):
    global firstQuery
    if (firstQuery):
        # 首次查询
        firstQueryAndExportSciDetail(sciName)
        firstQuery = False
    else:
        # 非首次的查询
        otherQueryAndExportSciDetail(sciName)
