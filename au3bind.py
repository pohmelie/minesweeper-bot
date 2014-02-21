from ctypes import *


class POINT(Structure):

    _fields_ = [
        ("x", c_long),
        ("y", c_long)
    ]

types = {
    "void": "None",
    "long": "c_long",
    "LPCWSTR": "c_wchar_p",
    "LPWSTR": "c_wchar_p",
    "LPCSTR": "c_char_p",
    "unsigned long": "c_ulong",
    "int": "c_int",
    "LPPOINT": "POINTER(POINT)"
}

AU3_INTDEFAULT = -2147483647
AU3_RESULT_SIZE = 256


def autoit():

    return AutoItX3.SINGLE_AU3 or AutoItX3()


class AutoItX3():

    SINGLE_AU3 = None

    def __init__(self):

        AutoItX3.SINGLE_AU3 = self
        self.au3 = windll.AutoItX3

        self.au3.AU3_Init.restype = None
        self.au3.AU3_Init.argtypes = ()
        self.AU3_Init = lambda: self.au3.AU3_Init()

        self.AU3_Init()

        self.au3.AU3_AutoItSetOption.restype = c_long
        self.au3.AU3_AutoItSetOption.argtypes = (c_wchar_p, c_long, )
        self.AU3_AutoItSetOption = lambda szOption, nValue: self.au3.AU3_AutoItSetOption(szOption, nValue)

        self.au3.AU3_BlockInput.restype = None
        self.au3.AU3_BlockInput.argtypes = (c_long, )
        self.AU3_BlockInput = lambda nFlag: self.au3.AU3_BlockInput(nFlag)

        self.au3.AU3_CDTray.restype = c_long
        self.au3.AU3_CDTray.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_CDTray = lambda szDrive, szAction: self.au3.AU3_CDTray(szDrive, szAction)

        self.au3.AU3_ClipGet.restype = None
        self.au3.AU3_ClipGet.argtypes = (c_wchar_p, c_int, )
        self.AU3_ClipGet = ResultWrapper(self.au3.AU3_ClipGet)

        self.au3.AU3_ClipPut.restype = None
        self.au3.AU3_ClipPut.argtypes = (c_wchar_p, )
        self.AU3_ClipPut = lambda szClip: self.au3.AU3_ClipPut(szClip)

        self.au3.AU3_ControlClick.restype = c_long
        self.au3.AU3_ControlClick.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_long, c_long, c_long, )
        self.AU3_ControlClick = lambda szTitle, szText, szControl, szButton, nNumClicks, nX=AU3_INTDEFAULT, nY=AU3_INTDEFAULT: self.au3.AU3_ControlClick(szTitle, szText, szControl, szButton, nNumClicks, nX, nY)

        self.au3.AU3_ControlCommand.restype = None
        self.au3.AU3_ControlCommand.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlCommand = ResultWrapper(self.au3.AU3_ControlCommand)

        self.au3.AU3_ControlListView.restype = None
        self.au3.AU3_ControlListView.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlListView = ResultWrapper(self.au3.AU3_ControlListView)

        self.au3.AU3_ControlDisable.restype = c_long
        self.au3.AU3_ControlDisable.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlDisable = lambda szTitle, szText, szControl: self.au3.AU3_ControlDisable(szTitle, szText, szControl)

        self.au3.AU3_ControlEnable.restype = c_long
        self.au3.AU3_ControlEnable.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlEnable = lambda szTitle, szText, szControl: self.au3.AU3_ControlEnable(szTitle, szText, szControl)

        self.au3.AU3_ControlFocus.restype = c_long
        self.au3.AU3_ControlFocus.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlFocus = lambda szTitle, szText, szControl: self.au3.AU3_ControlFocus(szTitle, szText, szControl)

        self.au3.AU3_ControlGetFocus.restype = None
        self.au3.AU3_ControlGetFocus.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlGetFocus = ResultWrapper(self.au3.AU3_ControlGetFocus)

        self.au3.AU3_ControlGetHandle.restype = None
        self.au3.AU3_ControlGetHandle.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlGetHandle = ResultWrapper(self.au3.AU3_ControlGetHandle)

        self.au3.AU3_ControlGetPosX.restype = c_long
        self.au3.AU3_ControlGetPosX.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlGetPosX = lambda szTitle, szText, szControl: self.au3.AU3_ControlGetPosX(szTitle, szText, szControl)

        self.au3.AU3_ControlGetPosY.restype = c_long
        self.au3.AU3_ControlGetPosY.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlGetPosY = lambda szTitle, szText, szControl: self.au3.AU3_ControlGetPosY(szTitle, szText, szControl)

        self.au3.AU3_ControlGetPosHeight.restype = c_long
        self.au3.AU3_ControlGetPosHeight.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlGetPosHeight = lambda szTitle, szText, szControl: self.au3.AU3_ControlGetPosHeight(szTitle, szText, szControl)

        self.au3.AU3_ControlGetPosWidth.restype = c_long
        self.au3.AU3_ControlGetPosWidth.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlGetPosWidth = lambda szTitle, szText, szControl: self.au3.AU3_ControlGetPosWidth(szTitle, szText, szControl)

        self.au3.AU3_ControlGetText.restype = None
        self.au3.AU3_ControlGetText.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlGetText = ResultWrapper(self.au3.AU3_ControlGetText)

        self.au3.AU3_ControlHide.restype = c_long
        self.au3.AU3_ControlHide.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlHide = lambda szTitle, szText, szControl: self.au3.AU3_ControlHide(szTitle, szText, szControl)

        self.au3.AU3_ControlMove.restype = c_long
        self.au3.AU3_ControlMove.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_long, c_long, c_long, c_long, )
        self.AU3_ControlMove = lambda szTitle, szText, szControl, nX, nY, nWidth=-1, nHeight=-1: self.au3.AU3_ControlMove(szTitle, szText, szControl, nX, nY, nWidth, nHeight)

        self.au3.AU3_ControlSend.restype = c_long
        self.au3.AU3_ControlSend.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_long, )
        self.AU3_ControlSend = lambda szTitle, szText, szControl, szSendText, nMode=0: self.au3.AU3_ControlSend(szTitle, szText, szControl, szSendText, nMode)

        self.au3.AU3_ControlSetText.restype = c_long
        self.au3.AU3_ControlSetText.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlSetText = lambda szTitle, szText, szControl, szControlText: self.au3.AU3_ControlSetText(szTitle, szText, szControl, szControlText)

        self.au3.AU3_ControlShow.restype = c_long
        self.au3.AU3_ControlShow.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_ControlShow = lambda szTitle, szText, szControl: self.au3.AU3_ControlShow(szTitle, szText, szControl)

        self.au3.AU3_ControlTreeView.restype = None
        self.au3.AU3_ControlTreeView.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_ControlTreeView = ResultWrapper(self.au3.AU3_ControlTreeView)

        self.au3.AU3_DriveMapAdd.restype = None
        self.au3.AU3_DriveMapAdd.argtypes = (c_wchar_p, c_wchar_p, c_long, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_DriveMapAdd = lambda szDevice, szShare, nFlags, szUser="", szPwd="": ResultWrapper(self.au3.AU3_DriveMapAdd, int)(szDevice, szShare, nFlags, szUser, szPwd)

        self.au3.AU3_DriveMapDel.restype = c_long
        self.au3.AU3_DriveMapDel.argtypes = (c_wchar_p, )
        self.AU3_DriveMapDel = lambda szDevice: self.au3.AU3_DriveMapDel(szDevice)

        self.au3.AU3_DriveMapGet.restype = None
        self.au3.AU3_DriveMapGet.argtypes = (c_wchar_p, c_wchar_p, c_int, )
        self.AU3_DriveMapGet = ResultWrapper(self.au3.AU3_DriveMapGet)

        self.au3.AU3_IniDelete.restype = c_long
        self.au3.AU3_IniDelete.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_IniDelete = lambda szFilename, szSection, szKey: self.au3.AU3_IniDelete(szFilename, szSection, szKey)

        self.au3.AU3_IniRead.restype = None
        self.au3.AU3_IniRead.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_IniRead = ResultWrapper(self.au3.AU3_IniRead)

        self.au3.AU3_IniWrite.restype = c_long
        self.au3.AU3_IniWrite.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_IniWrite = lambda szFilename, szSection, szKey, szValue: self.au3.AU3_IniWrite(szFilename, szSection, szKey, szValue)

        self.au3.AU3_IsAdmin.restype = c_long
        self.au3.AU3_IsAdmin.argtypes = ()
        self.AU3_IsAdmin = lambda: self.au3.AU3_IsAdmin()

        self.au3.AU3_MouseClick.restype = c_long
        self.au3.AU3_MouseClick.argtypes = (c_wchar_p, c_long, c_long, c_long, c_long, )
        self.AU3_MouseClick = lambda szButton="LEFT", nX=AU3_INTDEFAULT, nY=AU3_INTDEFAULT, nClicks=1, nSpeed=-1: self.au3.AU3_MouseClick(szButton, nX, nY, nClicks, nSpeed)

        self.au3.AU3_MouseClickDrag.restype = c_long
        self.au3.AU3_MouseClickDrag.argtypes = (c_wchar_p, c_long, c_long, c_long, c_long, c_long, )
        self.AU3_MouseClickDrag = lambda szButton, nX1, nY1, nX2, nY2, nSpeed=-1: self.au3.AU3_MouseClickDrag(szButton, nX1, nY1, nX2, nY2, nSpeed)

        self.au3.AU3_MouseDown.restype = None
        self.au3.AU3_MouseDown.argtypes = (c_wchar_p, )
        self.AU3_MouseDown = lambda szButton="LEFT": self.au3.AU3_MouseDown(szButton)

        self.au3.AU3_MouseGetCursor.restype = c_long
        self.au3.AU3_MouseGetCursor.argtypes = ()
        self.AU3_MouseGetCursor = lambda: self.au3.AU3_MouseGetCursor()

        self.au3.AU3_MouseGetPosX.restype = c_long
        self.au3.AU3_MouseGetPosX.argtypes = ()
        self.AU3_MouseGetPosX = lambda: self.au3.AU3_MouseGetPosX()

        self.au3.AU3_MouseGetPosY.restype = c_long
        self.au3.AU3_MouseGetPosY.argtypes = ()
        self.AU3_MouseGetPosY = lambda: self.au3.AU3_MouseGetPosY()

        self.au3.AU3_MouseMove.restype = c_long
        self.au3.AU3_MouseMove.argtypes = (c_long, c_long, c_long, )
        self.AU3_MouseMove = lambda nX, nY, nSpeed=-1: self.au3.AU3_MouseMove(nX, nY, nSpeed)

        self.au3.AU3_MouseUp.restype = None
        self.au3.AU3_MouseUp.argtypes = (c_wchar_p, )
        self.AU3_MouseUp = lambda szButton="LEFT": self.au3.AU3_MouseUp(szButton)

        self.au3.AU3_MouseWheel.restype = None
        self.au3.AU3_MouseWheel.argtypes = (c_wchar_p, c_long, )
        self.AU3_MouseWheel = lambda szDirection, nClicks: self.au3.AU3_MouseWheel(szDirection, nClicks)

        self.au3.AU3_Opt.restype = c_long
        self.au3.AU3_Opt.argtypes = (c_wchar_p, c_long, )
        self.AU3_Opt = lambda szOption, nValue: self.au3.AU3_Opt(szOption, nValue)

        self.au3.AU3_PixelChecksum.restype = c_ulong
        self.au3.AU3_PixelChecksum.argtypes = (c_long, c_long, c_long, c_long, c_long, )
        self.AU3_PixelChecksum = lambda nLeft, nTop, nRight, nBottom, nStep=1: self.au3.AU3_PixelChecksum(nLeft, nTop, nRight, nBottom, nStep)

        self.au3.AU3_PixelGetColor.restype = c_long
        self.au3.AU3_PixelGetColor.argtypes = (c_long, c_long, )
        self.AU3_PixelGetColor = lambda nX, nY: self.au3.AU3_PixelGetColor(nX, nY)

        self.au3.AU3_PixelSearch.restype = None
        self.au3.AU3_PixelSearch.argtypes = (c_long, c_long, c_long, c_long, c_long, c_long, c_long, POINTER(POINT), )
        self.AU3_PixelSearch = lambda nLeft, nTop, nRight, nBottom, nCol, nVar, nStep, pPointResult: self.au3.AU3_PixelSearch(nLeft, nTop, nRight, nBottom, nCol, nVar, nStep, pPointResult)

        self.au3.AU3_ProcessClose.restype = c_long
        self.au3.AU3_ProcessClose.argtypes = (c_wchar_p, )
        self.AU3_ProcessClose = lambda szProcess: self.au3.AU3_ProcessClose(szProcess)

        self.au3.AU3_ProcessExists.restype = c_long
        self.au3.AU3_ProcessExists.argtypes = (c_wchar_p, )
        self.AU3_ProcessExists = lambda szProcess: self.au3.AU3_ProcessExists(szProcess)

        self.au3.AU3_ProcessSetPriority.restype = c_long
        self.au3.AU3_ProcessSetPriority.argtypes = (c_wchar_p, c_long, )
        self.AU3_ProcessSetPriority = lambda szProcess, nPriority: self.au3.AU3_ProcessSetPriority(szProcess, nPriority)

        self.au3.AU3_ProcessWait.restype = c_long
        self.au3.AU3_ProcessWait.argtypes = (c_wchar_p, c_long, )
        self.AU3_ProcessWait = lambda szProcess, nTimeout=0: self.au3.AU3_ProcessWait(szProcess, nTimeout)

        self.au3.AU3_ProcessWaitClose.restype = c_long
        self.au3.AU3_ProcessWaitClose.argtypes = (c_wchar_p, c_long, )
        self.AU3_ProcessWaitClose = lambda szProcess, nTimeout=0: self.au3.AU3_ProcessWaitClose(szProcess, nTimeout)

        self.au3.AU3_RegDeleteKey.restype = c_long
        self.au3.AU3_RegDeleteKey.argtypes = (c_wchar_p, )
        self.AU3_RegDeleteKey = lambda szKeyname: self.au3.AU3_RegDeleteKey(szKeyname)

        self.au3.AU3_RegDeleteVal.restype = c_long
        self.au3.AU3_RegDeleteVal.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_RegDeleteVal = lambda szKeyname, szValuename: self.au3.AU3_RegDeleteVal(szKeyname, szValuename)

        self.au3.AU3_RegEnumKey.restype = None
        self.au3.AU3_RegEnumKey.argtypes = (c_wchar_p, c_long, c_wchar_p, c_int, )
        self.AU3_RegEnumKey = ResultWrapper(self.au3.AU3_RegEnumKey)

        self.au3.AU3_RegEnumVal.restype = None
        self.au3.AU3_RegEnumVal.argtypes = (c_wchar_p, c_long, c_wchar_p, c_int, )
        self.AU3_RegEnumVal = ResultWrapper(self.au3.AU3_RegEnumVal)

        self.au3.AU3_RegRead.restype = None
        self.au3.AU3_RegRead.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_RegRead = ResultWrapper(self.au3.AU3_RegRead)

        self.au3.AU3_RegWrite.restype = c_long
        self.au3.AU3_RegWrite.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_RegWrite = lambda szKeyname, szValuename, szType, szValue: self.au3.AU3_RegWrite(szKeyname, szValuename, szType, szValue)

        self.au3.AU3_Run.restype = c_long
        self.au3.AU3_Run.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_Run = lambda szRun, szDir="", nShowFlags=1: self.au3.AU3_Run(szRun, szDir, nShowFlags)

        self.au3.AU3_RunAsSet.restype = c_long
        self.au3.AU3_RunAsSet.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_RunAsSet = lambda szUser, szDomain, szPassword, nOptions: self.au3.AU3_RunAsSet(szUser, szDomain, szPassword, nOptions)

        self.au3.AU3_RunWait.restype = c_long
        self.au3.AU3_RunWait.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_RunWait = lambda szRun, szDir="", nShowFlags=1: self.au3.AU3_RunWait(szRun, szDir, nShowFlags)

        self.au3.AU3_Send.restype = None
        self.au3.AU3_Send.argtypes = (c_wchar_p, c_long, )
        self.AU3_Send = lambda szSendText, nMode=0: self.au3.AU3_Send(szSendText, nMode)

        self.au3.AU3_SendA.restype = None
        self.au3.AU3_SendA.argtypes = (c_char_p, c_long, )
        self.AU3_SendA = lambda szSendText, nMode=0: self.au3.AU3_SendA(szSendText, nMode)

        self.au3.AU3_Shutdown.restype = c_long
        self.au3.AU3_Shutdown.argtypes = (c_long, )
        self.AU3_Shutdown = lambda nFlags: self.au3.AU3_Shutdown(nFlags)

        self.au3.AU3_Sleep.restype = None
        self.au3.AU3_Sleep.argtypes = (c_long, )
        self.AU3_Sleep = lambda nMilliseconds: self.au3.AU3_Sleep(nMilliseconds)

        self.au3.AU3_StatusbarGetText.restype = None
        self.au3.AU3_StatusbarGetText.argtypes = (c_wchar_p, c_wchar_p, c_long, c_wchar_p, c_int, )
        self.AU3_StatusbarGetText = lambda szTitle, szText="", nPart=1: ResultWrapper(self.au3.AU3_StatusbarGetText)(szTitle, szText, nPart)

        self.au3.AU3_ToolTip.restype = None
        self.au3.AU3_ToolTip.argtypes = (c_wchar_p, c_long, c_long, )
        self.AU3_ToolTip = lambda szTip, nX=AU3_INTDEFAULT, nY=AU3_INTDEFAULT: self.au3.AU3_ToolTip(szTip, nX, nY)

        self.au3.AU3_WinActivate.restype = None
        self.au3.AU3_WinActivate.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinActivate = lambda szTitle, szText="": self.au3.AU3_WinActivate(szTitle, szText)

        self.au3.AU3_WinActive.restype = c_long
        self.au3.AU3_WinActive.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinActive = lambda szTitle, szText="": self.au3.AU3_WinActive(szTitle, szText)

        self.au3.AU3_WinClose.restype = c_long
        self.au3.AU3_WinClose.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinClose = lambda szTitle, szText="": self.au3.AU3_WinClose(szTitle, szText)

        self.au3.AU3_WinExists.restype = c_long
        self.au3.AU3_WinExists.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinExists = lambda szTitle, szText="": self.au3.AU3_WinExists(szTitle, szText)

        self.au3.AU3_WinGetCaretPosX.restype = c_long
        self.au3.AU3_WinGetCaretPosX.argtypes = ()
        self.AU3_WinGetCaretPosX = lambda: self.au3.AU3_WinGetCaretPosX()

        self.au3.AU3_WinGetCaretPosY.restype = c_long
        self.au3.AU3_WinGetCaretPosY.argtypes = ()
        self.AU3_WinGetCaretPosY = lambda: self.au3.AU3_WinGetCaretPosY()

        self.au3.AU3_WinGetClassList.restype = None
        self.au3.AU3_WinGetClassList.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_WinGetClassList = lambda szTitle, szText="": ResultWrapper(self.au3.AU3_WinGetClassList)(szTitle, szText)

        self.au3.AU3_WinGetClientSizeHeight.restype = c_long
        self.au3.AU3_WinGetClientSizeHeight.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetClientSizeHeight = lambda szTitle, szText="": self.au3.AU3_WinGetClientSizeHeight(szTitle, szText)

        self.au3.AU3_WinGetClientSizeWidth.restype = c_long
        self.au3.AU3_WinGetClientSizeWidth.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetClientSizeWidth = lambda szTitle, szText="": self.au3.AU3_WinGetClientSizeWidth(szTitle, szText)

        self.au3.AU3_WinGetHandle.restype = None
        self.au3.AU3_WinGetHandle.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_WinGetHandle = lambda szTitle, szText="": ResultWrapper(self.au3.AU3_WinGetHandle)(szTitle, szText)

        self.au3.AU3_WinGetPosX.restype = c_long
        self.au3.AU3_WinGetPosX.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetPosX = lambda szTitle, szText="": self.au3.AU3_WinGetPosX(szTitle, szText)

        self.au3.AU3_WinGetPosY.restype = c_long
        self.au3.AU3_WinGetPosY.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetPosY = lambda szTitle, szText="": self.au3.AU3_WinGetPosY(szTitle, szText)

        self.au3.AU3_WinGetPosHeight.restype = c_long
        self.au3.AU3_WinGetPosHeight.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetPosHeight = lambda szTitle, szText="": self.au3.AU3_WinGetPosHeight(szTitle, szText)

        self.au3.AU3_WinGetPosWidth.restype = c_long
        self.au3.AU3_WinGetPosWidth.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetPosWidth = lambda szTitle, szText="": self.au3.AU3_WinGetPosWidth(szTitle, szText)

        self.au3.AU3_WinGetProcess.restype = None
        self.au3.AU3_WinGetProcess.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_WinGetProcess = lambda szTitle, szText="": ResultWrapper(self.au3.AU3_WinGetProcess, int)(szTitle, szText)

        self.au3.AU3_WinGetState.restype = c_long
        self.au3.AU3_WinGetState.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinGetState = lambda szTitle, szText="": self.au3.AU3_WinGetState(szTitle, szText)

        self.au3.AU3_WinGetText.restype = None
        self.au3.AU3_WinGetText.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_WinGetText = lambda szTitle, szText="": ResultWrapper(self.au3.AU3_WinGetText)(szTitle, szText)

        self.au3.AU3_WinGetTitle.restype = None
        self.au3.AU3_WinGetTitle.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_int, )
        self.AU3_WinGetTitle = lambda szTitle, szText="": ResultWrapper(self.au3.AU3_WinGetTitle)(szTitle, szText)

        self.au3.AU3_WinKill.restype = c_long
        self.au3.AU3_WinKill.argtypes = (c_wchar_p, c_wchar_p, )
        self.AU3_WinKill = lambda szTitle, szText="": self.au3.AU3_WinKill(szTitle, szText)

        self.au3.AU3_WinMenuSelectItem.restype = c_long
        self.au3.AU3_WinMenuSelectItem.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_WinMenuSelectItem = lambda szTitle, szTex, szItem1, szItem2, szItem3, szItem4, szItem5, szItem6, szItem7, szItem8: self.au3.AU3_WinMenuSelectItem(szTitle, szText, szItem1, szItem2, szItem3, szItem4, szItem5, szItem6, szItem7, szItem8)

        self.au3.AU3_WinMinimizeAll.restype = None
        self.au3.AU3_WinMinimizeAll.argtypes = ()
        self.AU3_WinMinimizeAll = lambda: self.au3.AU3_WinMinimizeAll()

        self.au3.AU3_WinMinimizeAllUndo.restype = None
        self.au3.AU3_WinMinimizeAllUndo.argtypes = ()
        self.AU3_WinMinimizeAllUndo = lambda: self.au3.AU3_WinMinimizeAllUndo()

        self.au3.AU3_WinMove.restype = c_long
        self.au3.AU3_WinMove.argtypes = (c_wchar_p, c_wchar_p, c_long, c_long, c_long, c_long, )
        self.AU3_WinMove = lambda szTitle, szText, nX, nY, nWidth=-1, nHeight=-1: self.au3.AU3_WinMove(szTitle, szText, nX, nY, nWidth, nHeight)

        self.au3.AU3_WinSetOnTop.restype = c_long
        self.au3.AU3_WinSetOnTop.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinSetOnTop = lambda szTitle, szText, nFlag: self.au3.AU3_WinSetOnTop(szTitle, szText, nFlag)

        self.au3.AU3_WinSetState.restype = c_long
        self.au3.AU3_WinSetState.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinSetState = lambda szTitle, szText, nFlags: self.au3.AU3_WinSetState(szTitle, szText, nFlags)

        self.au3.AU3_WinSetTitle.restype = c_long
        self.au3.AU3_WinSetTitle.argtypes = (c_wchar_p, c_wchar_p, c_wchar_p, )
        self.AU3_WinSetTitle = lambda szTitle, szText, szNewTitle: self.au3.AU3_WinSetTitle(szTitle, szText, szNewTitle)

        self.au3.AU3_WinSetTrans.restype = c_long
        self.au3.AU3_WinSetTrans.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinSetTrans = lambda szTitle, szText, nTrans: self.au3.AU3_WinSetTrans(szTitle, szText, nTrans)

        self.au3.AU3_WinWait.restype = c_long
        self.au3.AU3_WinWait.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinWait = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWait(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitA.restype = c_long
        self.au3.AU3_WinWaitA.argtypes = (c_char_p, c_char_p, c_long, )
        self.AU3_WinWaitA = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitA(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitActive.restype = c_long
        self.au3.AU3_WinWaitActive.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinWaitActive = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitActive(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitActiveA.restype = c_long
        self.au3.AU3_WinWaitActiveA.argtypes = (c_char_p, c_char_p, c_long, )
        self.AU3_WinWaitActiveA = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitActiveA(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitClose.restype = c_long
        self.au3.AU3_WinWaitClose.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinWaitClose = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitClose(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitCloseA.restype = c_long
        self.au3.AU3_WinWaitCloseA.argtypes = (c_char_p, c_char_p, c_long, )
        self.AU3_WinWaitCloseA = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitCloseA(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitNotActive.restype = c_long
        self.au3.AU3_WinWaitNotActive.argtypes = (c_wchar_p, c_wchar_p, c_long, )
        self.AU3_WinWaitNotActive = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitNotActive(szTitle, szText, nTimeout)

        self.au3.AU3_WinWaitNotActiveA.restype = c_long
        self.au3.AU3_WinWaitNotActiveA.argtypes = (c_char_p, c_char_p, c_long, )
        self.AU3_WinWaitNotActiveA = lambda szTitle, szText="", nTimeout=0: self.au3.AU3_WinWaitNotActiveA(szTitle, szText, nTimeout)


def ResultWrapper(f, ret_factory=lambda x: x):

    def foo(*args):

        buf = create_unicode_buffer(AU3_RESULT_SIZE)
        f(*(args + (buf, AU3_RESULT_SIZE)))
        return ret_factory(buf.value)

    return foo
