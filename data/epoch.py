# Open the json file and load the records
import json
import datetime

with open('concerts.json', 'r', encoding='utf-8') as input:
    with open('concerts2.json', 'a', encoding='utf-8') as output:
        for line in input:
            if 'date' in line:
                epoch = line[14:26]
                epochnum = int(epoch)
                timestamp = datetime.datetime.fromtimestamp(epochnum/1000)
                date_time = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
                output.write('    '+'"date":'+' "'+date_time+'"')  
            else:
                output.write(line)
                


