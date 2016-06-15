import DataCollector
DC = DataCollector.DataCollector()
DC.addParams(['i','p']);

for i in range(0, 10):
    p = 2*i
    DC.slurp()
        
DC.get('i')        
DC.get('p')