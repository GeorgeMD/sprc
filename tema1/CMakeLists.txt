cmake_minimum_required(VERSION 3.10)
project(server)
set(CMAKE_CXX_STANDARD 14)
add_executable(fileserver server.cpp load_svc.c load.h)


project(client)
set(CMAKE_CXX_STANDARD 14)
add_executable(fileclient client.cpp load_clnt.c)


project(example)
set(CMAKE_CXX_STANDARD C)
add_executable(test_srv lab2/rpc_server.c lab2/load.h lab2/load_clnt.c lab2/load_svc.c lab2/load_xdr.c)