# @Function:Ptero添加主线
# @Time: 2020/7/9 上午10:37
# @Authon: flank
import re


def updateAXI(content, num, udpateNum):
    # AXI1-->AXI2
    updateStr = re.sub(r'AXI%s' % num, r'AXI%s' % udpateNum, content)
    # AXI_1--->AXI_2
    updateStr = re.sub(r'AXI_%s' % num, r'AXI_%s' % udpateNum, updateStr)
    # m_axi_1--->m_axi_2
    updateStr = re.sub(r'm_axi_%s' % num, r'm_axi_%s' % udpateNum, updateStr)
    # md_1--->md_2
    updateStr = re.sub(r'md_%s' % num, r'md_%s' % udpateNum, updateStr)
    # md_error_1--->md_error_2
    updateStr = re.sub(r'md_error_%s' % num, r'md_error_%s' % udpateNum, updateStr)
    # md_error1--->md_error2
    updateStr = re.sub(r'md_error%s' % num, r'md_error%s' % udpateNum, updateStr)
    # WaitRead1--->WaitRead2
    updateStr = re.sub(r'WaitRead%s' % num, r'WaitRead%s' % udpateNum, updateStr)
    # AXIFIFOBusy1--->AXIFIFOBusy2
    updateStr = re.sub(r'AXIFIFOBusy%s' % num, r'AXIFIFOBusy%s' % udpateNum, updateStr)
    # GenAddressBeforRead_1-->GenAddressBeforRead_2
    updateStr = re.sub(r'GenAddressBeforRead_%s' % num, r'GenAddressBeforRead_%s' % udpateNum, updateStr)
    # AXI_GenAddressForRead_1-->AXI_GenAddressForRead_2
    updateStr = re.sub(r' AXI_GenAddressForRead_%s' % num, r'AXI_GenAddressForRead_%s' % udpateNum, updateStr)
    return updateStr


if __name__ == "__main__":
    num = 2  # 现在的master
    updateNum = 10  # 要修改的master

    # # read
    readFile = open("ipg/Sheet_2.ipg", 'rb')
    # content = readFile.read()
    # # print(len(content))
    # updateStr=updateAXI(str(content),num,updateNum)

    # #write
    writeFile = open(
        "/media/lmx/5C5409DB5409B932/work/flank/SnowLake/CFD/Ptero/Zu7_3_base_0_null_1/Sheet_%s.ipg" % updateNum, "w")
    for t in readFile:
        writeFile.write(updateAXI(str(t), num, updateNum)[2:-5])
        writeFile.write("\n")
    readFile.close()
    writeFile.close()
