def groupArrayElements(arrayIn, numberOfChunksDesired):
	import math
	retval = []
	# ensure that no negative or 0 chunk values are entered
	if numberOfChunksDesired < 1:
		numberOfChunksDesired = 1
	chunkSize = int(math.ceil(len(arrayIn) / numberOfChunksDesired))
	# ensure that the minimum chunk size is 1 entry
	if chunkSize < 1:
		chunkSize = 1
	# while there are values left to process
	while len(arrayIn) > chunkSize:
		# create a chunk
		chunk = arrayIn[:chunkSize]
		# add the chunk to the returnable value
		retval.append(chunk)
		# prepare the array to be processed for next iteration
		arrayIn = arrayIn[chunkSize:]
	# add any remaining array entries that are less than a standard chunk in length
	retval.append(arrayIn)
	# add None values for chunks beyond the length of the original array
	if len(retval) < numberOfChunksDesired:
		fillerLength = numberOfChunksDesired - len(retval)
		fillerArray = [None] * fillerLength
		retval += fillerArray
	return retval


print(groupArrayElements([1, 2, 3, 4, 5], 1))
# Expected [[1, 2, 3, 4, 5]]
# Generated [[1, 2, 3, 4, 5]]
print(groupArrayElements([1, 2, 3, 4, 5], 2))
# Expected  [[1, 2, 3], [4, 5]]
# Generated [[1, 2, 3], [4, 5]]
print(groupArrayElements([1, 2, 3, 4, 5], 3))
# Expected  [[1, 2], [3, 4], [5]]
# Generated [[1, 2], [3, 4], [5]]
print(groupArrayElements([1, 2, 3, 4, 5], 4))
# Expected  [[1, 2], [3, 4], [5], None]
# Generated [[1, 2], [3, 4], [5], None]
print(groupArrayElements([1, 2, 3, 4, 5], 5))
# Expected  [[1], [2], [3], [4], [5]]
# Generated [[1], [2], [3], [4], [5]]
print(groupArrayElements([1, 2, 3, 4, 5], 6))
# Expected  [[1], [2], [3], [4], [5], None]
# Generated [[1], [2], [3], [4], [5], None]
print(groupArrayElements([1, 2, 3, 4, 5], 10))
# Expected  [[1], [2], [3], [4], [5], None, None, None, None, None]
# Generated [[1], [2], [3], [4], [5], None, None, None, None, None]
print(groupArrayElements([1, 2, 3, 4, 5], -1))
# Expected  [[1, 2, 3, 4, 5]]
# Generated [[1, 2, 3, 4, 5]]
