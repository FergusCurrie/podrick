# Podrick

Compose for app stack. 


docker compose up -d 
docker compose up -d --build frontdoor

## Services 


### Loki 

- Data persisted with volume 
- Currently directly using file system... could be switch to minio?
- labels = categorisation of the log. 

### Alloy 

- 4 volumes. 
    - alloy config
    - docker socket
    - docker containers
    - alloy data volume 

### Grafana 

- 2 volumes 
    - settings
    - graphana volume

