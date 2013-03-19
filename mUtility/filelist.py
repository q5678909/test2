__author__ = 'hp'

import os, glob

#Note: this function is the complete function to list all files based on the specific folder !
# param : folder_path is a string type.
def fulllist(folder_path):
	
	if(folder_path.strip().endswith(os.sep)):
		#remove the latest os.sep
		#folder_path = folder_path[:-1]
		print "folder_path : "  + folder_path
	
	allFiles = list()
	
	folderlist = glob.glob(folder_path + os.sep + "*")
	
	for folder in folderlist:
		try:		
			if folder is None or len(folder) == 0:
				folder = os.curdir
			
			if os.path.isdir(folder):
				
				childFile = os.listdir(folder)
				
				fileList = ["%s" % (folder.rstrip(os.sep) + os.path.sep + f) for f in childFile]
				
				while fileList is not None and len(fileList) > 0:
					
					allFiles.append("" + fileList[0])
					
					if os.path.isdir(fileList[0]):
						childFile = os.listdir(fileList[0])
						if childFile is not None and len(childFile) > 0:
							fileList = fileList + ["%s" % (fileList[0] + os.path.sep + ft) for ft in childFile]
						else:
							pass
					else:
						pass
					
					fileList.pop(0)
				
				#end while
				#allFiles.sort()#sort it to make the result looks in the order !
				#print "\n".join(["%s" % f for f in allFiles])
				#return allFiles
			else:
				#print 'not folder, no child'
				allFiles.append(""+folder)
				#return allFiles
				
		except Exception,x:
			print "Exception happened"
			print x
			
	allFiles.sort()
	return allFiles
			
