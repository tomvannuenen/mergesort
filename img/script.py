def mergeSort(array):
  arraySize = len(array)

  if arraySize == 1:
    return

  midpoint = arraySize // 2
  leftArray = array[:midpoint]
  rightArray = array[midpoint:]

  mergeSort(leftArray)
  mergeSort(rightArray)

  merge(leftArray, rightArray, array)

  return array

def merge(leftArray, rightArray, array):
  i = 0
  j = 0
  while len(leftArray) and len(rightArray):
    print('array is: ', array)
    if rightArray[0] <= leftArray[0]:
      array[index] = rightArray[0]
      i += 1
    else:
      array[index] = leftArray[0]
      j += 1
    }
  }

  while len(leftArray.length) {
    console.log('left array is: ', leftArray);
    array[index++] = leftArray.shift();
  }

  while (rightArray.length) {
    console.log('right array is: ', rightArray);
    array[index++] = rightArray.shift();
  }

  console.log('** end of merge function ** array is: ', array);
}
