# =============================================================================
# Created by- Rupam Hari
# =============================================================================

import os

content=os.listdir()

# =============================================================================
# To remove the file itself from working list
# =============================================================================
main=['files-organiser.py','files-organiser.exe']
for mainfile in main:
    if mainfile in content:
        content.remove(mainfile)


# =============================================================================
# Removing folders from working list
# =============================================================================
files=[]
for file in content:
    if os.path.isfile(file):
        files.append(file)
        
# =============================================================================
# 'files' is our working list
# =============================================================================


def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        

def moveFiles(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")


# =============================================================================
# Utility function to create folder and move files in a single function
# =============================================================================
def util(folderName,files):
    createFolder(folderName)
    moveFiles(folderName,files)



# =============================================================================
# Declaring file extensions
# =============================================================================
docExts=['.pdf','.docx','.doc','.txt','.pptx','.pptm','.ppt']
docsFiles=[]

imgExts=['.jpg','.jpeg','.png','.psd','.tiff','.cr2','.crw','.nef','.pef']
imageFiles=[]

videoExts=['.mp4','.m4a','.m4v','.f4v','.f4a','.m4b','.m4r','.f4b','.mov',
           '.3gp','.3gp2','.3g2','.3gpp','.3gpp2','.ogg','.oga','.ogv','.ogx',
           '.wmv','.webm','.flv','.mkv','.avi','.mpeg']
videoFiles=[]

audioExts=['.mp3','.wma','.aac','.flac','.ac3','.3ga']
audioFiles=[]

zipExts=['.zip','.rar']
zipFiles=[]

exeExts=['.exe','.msi']
exeFiles=[]

others=[]

# =============================================================================
# Declaring Flags
# =============================================================================
docFlag=0
imageFlag=0
videoFlag=0
audioFlag=0
zipFlag=0
exeFlag=0
othersFlag=0


# =============================================================================
# Filtering out different type of files from working list
# =============================================================================
for file in files:
    extension=(os.path.splitext(file)[1]).lower()
    
    
    if extension in docExts:
        docsFiles.append(file)
        docFlag=1
        
    elif extension in imgExts:
        imageFiles.append(file)
        imageFlag=1
        
    elif extension in videoExts:
        videoFiles.append(file)
        videoFlag=1
        
    elif extension in audioExts:
        audioFiles.append(file)
        audioFlag=1
        
    elif extension in zipExts:
        zipFiles.append(file)
        zipFlag=1
        
    elif extension in exeExts:
        exeFiles.append(file)
        exeFlag=1
    else:
        others.append(file)
        othersFlag=1
    



if docFlag==1:
    util('Documents',docsFiles)
    
if imageFlag==1:
    util('Pictures',imageFiles)
    
if videoFlag==1:
    util('Videos',videoFiles)
    
if audioFlag==1:
    util('Music', audioFiles)
    
if zipFlag==1:
    util('Compressed',zipFiles)
    
if exeFlag==1:
    util('Programs',exeFiles)
    
if othersFlag==1:
    util('Others',others)
