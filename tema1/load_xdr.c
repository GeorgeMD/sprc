/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include "load.h"

bool_t
xdr_request (XDR *xdrs, request *objp)
{
	register int32_t *buf;

	 if (!xdr_string (xdrs, &objp->req, ~0))
		 return FALSE;
	return TRUE;
}

bool_t
xdr_response (XDR *xdrs, response *objp)
{
	register int32_t *buf;

	 if (!xdr_string (xdrs, &objp->word, ~0))
		 return FALSE;
	 if (!xdr_int (xdrs, &objp->hits))
		 return FALSE;
	return TRUE;
}