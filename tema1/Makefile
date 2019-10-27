CC=g++

.PHONY: build clean

build:
	rpcgen -C load.x
	$(CC) -c client.cpp -o client.o
	$(CC) -c load_clnt.c -o load_clnt.o
	$(CC) -c load_xdr.c -o load_xdr.o
	$(CC) -o client client.o load_clnt.o load_xdr.o
	$(CC) -c client.cpp server.cpp load_xdr.c
	$(CC) -c server.cpp -o server.o
	$(CC) -c load_svc.c -o load_svc.o
	$(CC) -o server server.o load_svc.o load_xdr.o

clean:
	rm *.o load*.c load.h client server