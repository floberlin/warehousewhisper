# Warehouse Whisper
This prototype is running in the SAP Cloud Platform using a free 30-days-trail account. A SAP HANA Cloud instance is used as storage database. Connecting directly to the HANA database allows a more modular approach if this solution will be deployed to real world solution. The aggregation of the data can be done directly in the HANA DB and only the neccassary data will then be send to external services. 

This is how the HANA DB setup was prepaired for the prototype:
1. Created basic SAP HANA Cloud instance in SCP
2. Created a technical user "MAGENTA_VOICE" for the connection to the REST Server
3. Created a mapping table consisting of the product name and the amount

The REST server written in javascript (express.js) simply uses the technical user to get the mapping table data accordingly.
# Architecture Overview
![Warehouse Whisper - Architecture Overview](https://github.com/flori28/warehousewhisper/blob/main/docs/WarehouseWhisper.png?raw=true)
# Video 
https://www.youtube.com/watch?v=ZjOKbDATNlk
