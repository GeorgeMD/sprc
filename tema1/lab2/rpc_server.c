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
#include <stdlib.h> /* exit */
#include <unistd.h> /* read, write, close */
#include <string.h> /* memcpy, memset */
#include <sys/socket.h> /* socket, connect */
#include <netinet/in.h> /* struct sockaddr_in, struct sockaddr */
#include <netdb.h> /* struct hostent, gethostbyname */

#include "load.h"

int * get_add_1_svc(param *p, struct svc_req *cl){
	static int add;
	
	add = p->a + p->b;
	return &add;
}

int sendStr(int iSock, const char *szStr) {
    int ret;
    int len = strlen(szStr);
    while (len > 0) {
        ret = send(iSock, szStr, len, 0);
        if (ret == -1) {
            //LogToFile("Error while request being sent to the server");
            return -1;
        }
        szStr += ret;
        len -= ret;
    }
    return 0;
}

char ** grade_1_svc(student *stud, struct svc_req *cl) {
	char **res = (char **) malloc(sizeof(char*));
	*res = (char *)malloc(sizeof(char) * 10);
	*res = "test";

	int portno =        80;
    char* host =        "sprc2.dfilip.xyz";
    char* message_fmt = "POST comand=%s%s HTTP/1.0\r\n\r\n";
    // char *message_fmt = "POST /apikey=%s&command=%s HTTP/1.0\r\n\r\n";

    struct hostent *server;
    struct sockaddr_in serv_addr;
    int sockfd, bytes, sent, received, total;
    char message[1024],response[4096];
	/* fill in the parameters */
    strcpy(message, message_fmt);
    sprintf(message, message_fmt, stud->nume, stud->grupa);
    // printf("Request:\n%s\n",message);

    /* create the socket */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) printf("ERROR opening socket\n");
	printf("Socket created\n");

    /* lookup the ip address */
    server = gethostbyname(host);
    if (server == NULL) printf("ERROR, no such host\n");
	printf("%s\n", server->h_name);

    /* fill in the structure */
    memset(&serv_addr,0,sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    memcpy(&serv_addr.sin_addr.s_addr,server->h_addr,server->h_length);
	// serv_addr.sin_addr.s_addr = inet_addr("82.78.81.172");

    /* connect the socket */
    if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0)
        printf("ERROR connecting\n");

    /* send the request */
    total = strlen(message);
    sent = 0;
    do {
        bytes = write(sockfd,message+sent,total-sent);
        if (bytes < 0)
            printf("ERROR writing message to socket\n");
        if (bytes == 0)
            break;
        sent+=bytes;
    } while (sent < total);

    /* receive the response */
    memset(response,0,sizeof(response));
    total = sizeof(response)-1;
    received = 0;
    do {
        bytes = read(sockfd,response+received,total-received);
        if (bytes < 0)
            printf("ERROR reading response from socket\n");
        if (bytes == 0)
            break;
        received+=bytes;
    } while (received < total);

    if (received == total)
        printf("ERROR storing complete response from socket\n");

    /* close the socket */
    close(sockfd);

    /* process response */
    printf("Response:\n%s\n",response);
	return res;
}
