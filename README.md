# pyms
Python Microservice template

## Requirements
```
python >=3.7 and <=3.8
pip3 install virtualenv
```

## Steps
```
git clone git@github.mpi-internal.com:Yapo/pyms.git
virtualenv --python=python3 app
source app/bin/activate
```

### Run Locally
```
make install
make start-local
```

### Run docker compose
```
make start
```

### Run tests

It's important to run ***make install*** first because it has some libraries dependencies to run this out

```
make tests
```


## ENV PARAMS (More will be added soon)

*SERVER_PORT* <num>
  
*SERVER_DEBUG* <true/false>
