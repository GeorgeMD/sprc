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

struct param {
	int a;
	int b;
};

struct student {
	string nume<>;
	string grupa<>;
};

program ADD_PROG {
	version ADD_VERS {
		int GET_ADD(param) = 1;
	} = 1;
} = 123456789;

program CHECKPROG {
	version CHECKVERS {
		string GRADE(student) = 1;
	} = 1;
} = 0x31234567;
