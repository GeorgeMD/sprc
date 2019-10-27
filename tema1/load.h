/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#ifndef _LOAD_H_RPCGEN
#define _LOAD_H_RPCGEN

#include <rpc/rpc.h>


#ifdef __cplusplus
extern "C" {
#endif


struct request {
	char *req;
};
typedef struct request request;

struct response {
	char *word;
	int hits;
};
typedef struct response response;

#define START_REQUEST_PROG 0x31337
#define START_REQUEST_VERS 1

#if defined(__STDC__) || defined(__cplusplus)
#define START_REQUEST 1
extern  char ** start_request_1(request *, CLIENT *);
extern  char ** start_request_1_svc(request *, struct svc_req *);
extern int start_request_prog_1_freeresult (SVCXPRT *, xdrproc_t, caddr_t);

#else /* K&R C */
#define START_REQUEST 1
extern  char ** start_request_1();
extern  char ** start_request_1_svc();
extern int start_request_prog_1_freeresult ();
#endif /* K&R C */

#define SEND_ARGUMENT_PROG 31337
#define SEND_ARGUMENT_VERS 1

#if defined(__STDC__) || defined(__cplusplus)
#define SEND_ARGUMENT 1
extern  response * send_argument_1(request *, CLIENT *);
extern  response * send_argument_1_svc(request *, struct svc_req *);
extern int send_argument_prog_1_freeresult (SVCXPRT *, xdrproc_t, caddr_t);

#else /* K&R C */
#define SEND_ARGUMENT 1
extern  response * send_argument_1();
extern  response * send_argument_1_svc();
extern int send_argument_prog_1_freeresult ();
#endif /* K&R C */

/* the xdr functions */

#if defined(__STDC__) || defined(__cplusplus)
extern  bool_t xdr_request (XDR *, request*);
extern  bool_t xdr_response (XDR *, response*);

#else /* K&R C */
extern bool_t xdr_request ();
extern bool_t xdr_response ();

#endif /* K&R C */

#ifdef __cplusplus
}
#endif

#endif /* !_LOAD_H_RPCGEN */