# mico-client
Python 3 resolver for [go-micro](https://github.com/micro/go-micro) grpc
services.

## Installation

```shell
    pip install micro-client
```

### Compiling
Make sure you have [the needed protobuf and plugins](https://github.com/micro/go-micro#install-protobuf).

**Notes**:
* Make sure you have the python package *grpcio-tools* installed!

```shell
    PATH=$PATH:$GOBIN_PATH protoc -I=$SOURCE_OF_MICRO_PROJECT --proto_path=$GOPATH/src:. --python_out=plugins=micro,grpc:. $PATH_TO_PROTO_FILE
    python -m grpc_tools.protoc -I=$SOURCE_OF_MICRO_PROJECT --python_out=. --grpc_python_out=. $PATH_TO_PROTO_FILE
```

### Etcd
```python
    from micro_client.registry import EtcdRegistry, EtcdClient
    from micro_client.common import Services
    
    etcd_client = EtcdClient(host='localhost', port=2379)
    prefix = "/micro/registry/"
    s = Services(EtcdRegistry(etcd_client, prefix))
```

### Consul
```python
    import requests

    from micro_client.registry.consulregistry import Registry
    from micro_client.common import Services

    s = Services('http://127.0.0.1:8500/v1', session=requests.Session()))
```

### Use it!
```python
    # Import the stub and grpc structures for use
    from some_pb2_grpc import SomeStub
    from some_pb2 import Input, Structures
    
    # Get the stub
    stub = s.insecure('base_user_cf', SomeStub)
    # Call it
    result = stub.SomeCall(Input(Data=1), Structures(Some="data", ID=1))

    # 如果 连接无法使用, reset stub
    stub = s.insecure('base_user_cf', SomeStub)
```
