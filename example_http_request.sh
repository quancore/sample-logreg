#!/bin/bash
#
# Starting API
python3 api.py 7000 &
sleep 2
#
# POST method predict
curl -d '[
    {"pregnant": 7, "glucose": 100, "bp": 70, "skin": 40, "insulin": 100, "bmi": 40, "pedigree": 0.3, "age": 40}
]' -H "Content-Type: application/json" \
     -X POST http://localhost:7000/predict && \
    echo -e "\n -> predict OK"

# kill running API
for i in $(ps -elf | grep "python3 api.py 7000" | grep -v grep | cut -d " " -f 4); do
    kill -9 $i
done
