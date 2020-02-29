#!/bin/bash

find build -type f -print0 | xargs -0 -I{} sed -i "s/localhost/${EXTERNAL_IP}/g" "{}"

npx serve -s build -l 5001 &
node api-server &
node flag-server &

while :;do
   sleep 300
   node admin.js
done
