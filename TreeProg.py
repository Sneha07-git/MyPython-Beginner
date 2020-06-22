picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over the picture

for image in picture:
  for pixcel in image:
    if pixcel == 1:
     print ('*', end= '')
    else:
      print(' ', end= '')
  print('')


