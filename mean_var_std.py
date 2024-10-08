while True:
  list_str=input("Enter the list elements separated by commas ")
  try:
    list=[int(x.strip()) for x in list_str.split(",")]
  except ValueError:
    print("List must contain numbers only")
    continue

  if len(list) != 9:
    print("List must contain nine numbers")
  else:
    break

def calculate(list):
  list_arr=np.array(list).reshape(3,3)
  mean_axis0=list_arr.mean(axis=0).tolist()
  mean_axis1=list_arr.mean(axis=1).tolist()
  mean_flat=list_arr.mean()

  variance_axis0=list_arr.var(axis=0).tolist()
  variance_axis1=list_arr.var(axis=1).tolist()
  variance_flat=list_arr.var()

  standard_deviation_axis0=list_arr.std(axis=0).tolist()
  standard_deviation_axis1=list_arr.std(axis=1).tolist()
  standard_deviation_flat=list_arr.std()
  max=[list_arr.max(axis=0),list_arr.max(axis=1),list_arr.max()]
  min=[list_arr.min(axis=0),list_arr.min(axis=1),list_arr.min()]
  sum=[list_arr.sum(axis=0),list_arr.sum(axis=1),list_arr.sum()]
  return {'mean' : [mean_axis0,mean_axis1,mean_flat],'variance' : [variance_axis0,variance_axis1,variance_flat],'standard deviation' : [standard_deviation_axis0,standard_deviation_axis1,standard_deviation_flat], 'max' : max, 'min' : min, 'sum' : sum}
