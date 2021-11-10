keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
keyvalues=dict(zip(keys,values))

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

person=sample
value=.get(80)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
dic=dict(sampleDict)
dic.pop("name",)
dic.pop("salary")

print(dic)
print(keyvalues)
print(value)
