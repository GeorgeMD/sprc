/**
	Sisteme de programe pentru retele de calculatoare
	
	Copyright (C) 2008 Ciprian Dobre & Florin Pop
	Univerity Politehnica of Bucharest, Romania

	This program is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 */

#include <stdio.h> 
#include <time.h> 
#include <rpc/rpc.h> 
#include "load.h" 
#define RMACHINE "localhost"

int main(int argc, char *argv[]){

	/* variabila clientului */
	CLIENT *handle, *handle_check;

	int *res;

	char **res_check;
	
	handle=clnt_create(
		RMACHINE,		/* numele masinii unde se afla server-ul */
		ADD_PROG,		/* numele programului disponibil pe server */
		ADD_VERS,		/* versiunea programului */
		"tcp");			/* tipul conexiunii client-server */
	
	handle_check=clnt_create(
		RMACHINE,		/* numele masinii unde se afla server-ul */
		CHECKPROG,		/* numele programului disponibil pe server */
		CHECKVERS,		/* versiunea programului */
		"tcp");			/* tipul conexiunii client-server */

	if(handle == NULL) {
		perror("");
		return -1;
	}

	param p = {1, 2};
	res = get_add_1(&p, handle);

	student stud = {"Andrei-George Turcu", "342C3"};
	printf("aici ajunge?\n");
	res_check = grade_1(&stud, handle_check);
	printf( "Adding %d and %d yields:  %d\n", p.a, p.b, *res);
	printf("Response received: %s\n", *res_check);
	
	return 0;
}
