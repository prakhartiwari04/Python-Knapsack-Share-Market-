from collections import OrderedDict 

priceOpen = [10, 15, 20]
priceClose = [25, 25, 40]
priceGain = []
W = int(input("Enter your total budget: "))
share_max = int(input("Enter max shares per company: "))

priceZip = zip(priceOpen,priceClose)
for list1,list2 in priceZip:
  priceGain.append(round(((list2-list1)/list1)*100))

res = dict(zip(priceOpen,priceClose))
sortedDict = dict(sorted(res.items()))



sortedgain = list(sortedDict.keys())
n = len(sortedgain) 

print("--------------Share Market--------------")
print("Price Open\t"+"Price Close")
for key, value in res.items():
    print(+key, '\t\t\t', value)
print("\nYour total budget: "+str(W))   
print("----------------------------------------\n\n")

#priceGain: (priceOpen,priceClose)
data_dict = dict(zip(priceGain,zip(priceOpen,priceClose)))
# sorted priceGain: (priceOpen,priceClose)
sortedData = dict(reversed(sorted(data_dict.items())))

for i in sortedData.items():
  if(W>=i[1][0]*share_max):
    print(str(i[1][0])+"'s shares bought: "+str(share_max))
    W -= i[1][0]*share_max
  elif(W<i[1][0]*share_max):
    sharesBought = W//i[1][0]
    if(sharesBought>share_max):
      sharesBought = share_max
    print(str(i[1][0])+"'s shares bought: "+str(sharesBought))
    W -= i[1][0]*sharesBought
print("Amount left:"+str(W))
    




