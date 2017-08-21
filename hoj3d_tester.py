#!/usr/bin/env python3

# Python module import
import numpy as np
import math as ma
import os

from PIL import Image


# Ppe module import
import frameHeader
import joint



def write_hoj3d(filename,hoj_3d):
	test_directory = '../hoj_test/'
	if not os.path.exists(os.path.dirname(test_directory+filename)):
		os.makedirs(os.path.dirname(test_directory+filename))
	file = open(test_directory+filename,'wb')
	hoj_array = []
	for line in hoj_3d:
		hoj_array.extend(hoj_3d)
	
	np.save(file, np.asarray(hoj_array))
		
	file.close()

def test_hoj3d():

	test_directory = 'hoj_test/'
	files_in_test_directory = []
	hoj_arrays = []
	test_result = []

	# get all filenames from test_directory
	for filename in os.listdir(test_directory):
		file_to_open = test_directory + filename
		files_in_test_directory.append(open(file_to_open,'rb'))

	# load all hoj sets
	for file in files_in_test_directory:
		hoj_array = np.load(file)
		hoj_arrays.append(hoj_array)
		file.close()

	# for each hoj set calculate the distance to every other hoj set
	for reference_hoj in hoj_arrays:
		result_line = []
		for test_hoj in hoj_arrays:
			difference = reference_hoj - test_hoj
			result = ma.sqrt((difference * difference).sum())
			result_line.append(result)
		test_result.append(result_line)

	# write results to textfile
	result_file = open('test_result.txt','tw')

	for line in test_result:
		for item in line:
			result_file.write(str(item) + '\t;')
		result_file.write('\r\n')

	result_file.close()

	# bonus create Bitmap image of results
	img = Image.new('RGB',(len(test_result),len(test_result)),"black")
	pixels = img.load()

	for i in range(img.size[0]):
		for j in range (img.size[1]):
			pixels[i,j] = (int(255 * ma.exp(- (test_result[i][j] * test_result[i][j]))), int(255 * ma.exp(- ((test_result[i][j] -1) * (test_result[i][j] - 1)))), int(255 * ma.exp(- ((test_result[i][j] -2) * (test_result[i][j] - 2)))))

	img.save('test_result.bmp')

if __name__ == '__main__':
	test_hoj3d()