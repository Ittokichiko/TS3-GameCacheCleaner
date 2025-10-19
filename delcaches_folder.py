import os
import shutil
caches = ["IGACache", "WorldCaches", "DCCache", "DCBackup"] # Maybe will need to Delete DCBackup!!! Idk!!!
def GetTheSims3Path_Documents():
    docs = os.path.join(os.path.expanduser("~"), "Documents")
    sims3_path = os.path.join(docs, "Electronic Arts", "The Sims 3")
    return sims3_path

def CheckIfTS3IsExists_Docs():
    if not os.listdir(GetTheSims3Path_Documents()):
        return False
    else:
        return True

def DeletesCache():
    if(CheckIfTS3IsExists_Docs() == True):
        for folder_cache in caches:
            folderpath = os.path.join(GetTheSims3Path_Documents(), folder_cache)
            if os.path.isdir(folderpath):
                try:
                    shutil.rmtree(folderpath)
                    print("Successfully Cleared Caches and DCBackup!!!")
                except Exception as e:
                    print("Failed: {}".format(e))
    else:
        print("These Game is not Launched... Pls Launch Game with Mods First or without mods!!!")
        os._exit(355)

def DeletesXML():
    ts3_pathdocs = GetTheSims3Path_Documents()
    if(CheckIfTS3IsExists_Docs() == True):
        print("Trying to Delete All XML Files...")
        deleted_count = 0
        for file in os.listdir(ts3_pathdocs + "*.xml"):
            filep = os.path.join(ts3_pathdocs, file)
            if(os.path.isfile(filep)):
                try:
                    os.remove(filep)
                    print("Deleted: {}".format(filep))
                    deleted_count += 1
                except:
                    print("Failed to Delete XML File or These .XML Files is Already Deleted!!!")
        if deleted_count == 0:
            print("These Game is not Launched... Pls Launch Game with Mods First or without mods or These XML Files is Already Deleted!!!")
        else:
            print("This Files is Already Deleted!!!")
            os._exit(334)

            os._exit(-54)


