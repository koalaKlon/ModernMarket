# ModernMarket

Manual
To build this container run in the folder of the docker-compose-file:

```sh
docker-compose build
```
this runs the containers detachted
```sh
docker-compose run
``` 
Create a superuser:
```sh
 python ./market/manage.py createsuperuser
```
Open you favourite browser and go to localhost:8000
To shutdown run 
```sh 
docker-compsose down
 ```
