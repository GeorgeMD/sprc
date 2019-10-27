#/**
#	Sisteme de programe pentru retele de calculatoare
#	
#	Copyright (C) 2008 Ciprian Dobre & Florin Pop
#	Univerity Politehnica of Bucharest, Romania
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
# */

build:
	rpcgen load.x
	gcc -c rpc_client.c -o rpc_client.o
	gcc -c load_clnt.c -o load_clnt.o
	gcc -c load_xdr.c -o load_xdr.o
	gcc -o rpc_client rpc_client.o load_clnt.o load_xdr.o
	gcc -c rpc_client.c rpc_server.c load_xdr.c
	gcc -c rpc_server.c -o rpc_server.o
	gcc -c load_svc.c -o load_svc.o
	gcc -o rpc_server rpc_server.o load_svc.o load_xdr.o

clean:
	rm -f rpc_client rpc_server load.h load_svc.c load_clnt.c load_xdr.c *.o
