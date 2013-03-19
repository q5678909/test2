__author__ = 'hp'

import os, glob

#source_path: the log file need to re_arrange
#keywords_list: the key worid 's list for arrange useage
#after execution, will create a result_xxx.txt for convenience reading log pattern

def re_dump(source_path, keywords_list):
	
	#check the source_path is existed or not
	if os.path.exists(source_path.strip()) == False :
		print source_path + " not existed, exit"
		return
	
	out_path = os.sep.join(["%s" % item for item in source_path.strip().split(os.sep)[0:-1]]) + "/result_" + source_path.strip().split(os.sep)[-1]
	out_file = open(out_path, "w")
	
	try:
		for line in open(source_path):
			for each_keyword in keywords_list:
				if each_keyword in line:
					#dump to console
					print line.rstrip()
					#dump to file
					out_file.write("%s" % line)
					break
	except Exception,x:
		print "Exception happened"
		print x
	finally:
		out_file.close()
