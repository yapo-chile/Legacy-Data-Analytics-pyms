# pyms
Python Microservice template

## Steps
```
virtualenv --python=python3 <name_virtual_env>
cd <name_virtual_env> && git clone git@github.mpi-internal.com:Yapo/pyms.git
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

## ENV PARAMS (More will be added soon)

*SERVER_PORT* <num>
  
*SERVER_DEBUG* <true/false>
