import os

output = open(os.environ['response'], 'w')
inventoryNumber = "IDA2345"
output.write(inventoryNumber)
