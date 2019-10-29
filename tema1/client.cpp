#include "load.h"

#include <rpc/rpc.h>
#include <iostream>

#define RMACHINE "localhost"
#define TCP "tcp"

#define YES "YES"

std::string readStdin() {
    std::string cmd;
    std::cout << "> "; std::cin >> cmd;

    return cmd;
}

int main() {
    CLIENT *start_request_handle, *send_arg_handle;

    start_request_handle = clnt_create(
            RMACHINE,
            START_REQUEST_PROG,
            START_REQUEST_VERS,
            TCP
    );

    send_arg_handle = clnt_create(
            RMACHINE,
            SEND_ARGUMENT_PROG,
            SEND_ARGUMENT_VERS,
            TCP
    );

    if (start_request_handle == nullptr) {
        perror("start_request_handle");
        return -1;
    }

    if (send_arg_handle == nullptr) {
        perror("send_arg_handle");
        return -1;
    }

    while (true) {
        std::string cmd = readStdin();
        request r{const_cast<char *>(cmd.c_str())};
        char **cPtrResponse = start_request_1(&r, start_request_handle);

        std::cout << "Server responded: " << *cPtrResponse << std::endl;

        std::string strResp(*cPtrResponse);
        std::string expectedResponse(YES" " + cmd);

        if (strResp == expectedResponse) {
            std::string arg = readStdin();
            r.req = const_cast<char *>(arg.c_str());
            response * resp = send_argument_1(&r, send_arg_handle);

            std::string respStr(resp->word);

            if (!respStr.empty() && resp->hits != -1) {
                std::cout << resp->word << " " << resp->hits << std::endl;
            } else if (!respStr.empty()) {
                std::cout << resp->word << std::endl;
            } else if (resp->hits != -1) {
                std::cout << resp->hits << std::endl;
            }
        }
    }

    return 0;
}