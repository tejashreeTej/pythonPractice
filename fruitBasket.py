import json
myVar = json.loads('[{"name" : "banana","baskets":[10,20,30]},{ "name" : "apple","baskets":[5,20,10,10]}]')
#myVar =[{"name" : "banana","baskets":[10,20,30]},{ "name" : "apple","baskets":[5,20,10,10]}]
print "fruit num_basket num_fruit"
print "--------------------------"
for fruit in myVar:
    count =0
    sum =0
    for noOfFruitInEachBasket in fruit['baskets']:
        count =count+1
        sum =sum + noOfFruitInEachBasket
    print fruit['name'],count,sum    