"""
Check FileType
	★ file.lower().endswith(())
"""
def isImage(single_file):
    if single_file.lower().endswith(('.jpg', '.gif', 'jepg', '.png')):
        return True
    return False

def isMovie(single_file):
    if single_file.lower().endswith(('.flv', '.avi', 'mov', '.wmv', '.mp4', '.mkv')):
        return True
    return False

def isExcel(single_file):
    if single_file.lower().endswith( ('.xls', '.xlt', 'xlsx', '.wmv', '.mp4') ):
        return True
    return False  

def isSql(single_file):
    if single_file.lower().endswith( ('.sql') ):
        return True
    return False  

def isTxt(single_file):
    if single_file.lower().endswith( ('.txt') ):
        return True
    return False  

def isMp3(single_file):
    if single_file.lower().endswith( ('.mp3') ):
        return True
    return False 