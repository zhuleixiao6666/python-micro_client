# mico-client
Python 3 resolver for [go-micro](https://github.com/micro/go-micro) grpc
services.

## 安装


```shell script
git clone https://gitlab.kalo-app.com/python/micro-client.git
cd micro-client && python setup.py develop
```

## Examples

### Compiling
Make sure you have [the needed protobuf and plugins](https://github.com/micro/go-micro#install-protobuf).

**Notes**:
* You will need to set or replace the variables!
* Make sure you have the python package *grpcio-tools* installed!


```shell
    PATH=$PATH:$GOBIN_PATH protoc -I=$SOURCE_OF_MICRO_PROJECT --proto_path=$GOPATH/src:. --python_out=plugins=micro,grpc:. $PATH_TO_PROTO_FILE
    python -m grpc_tools.protoc -I=$SOURCE_OF_MICRO_PROJECT --python_out=. --grpc_python_out=. $PATH_TO_PROTO_FILE
```

### Etcd
```python
    from micro_client.registry import EtcdRegistry, EtcdClient
    from micro_client.common import Services

    s = Services(EtcdRegistry(EtcdClient(port=2379), '/micro/registry/'))
```

### Use it!
```python
    service = s.resolve('some')
    print(service.address)

    # Import the stub and grpc structures for use
    import grpc
    from some_pb2_grpc import SomeStub
    from some_pb2 import Input, Structures
    
    # Get the stub
    stub = services.insecure('some', SomeStub)
    # Call it
    result = stub.SomeCall(Input(Data=1), Structures(Some="data", ID=1))
```
