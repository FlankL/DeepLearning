#  @Function:  
#　＠Time:2020/5/22 上午11:30
#  @Author:Flank
def _setupQtDirectories():
    import sys,os
    dirname = os.path.dirname(__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path