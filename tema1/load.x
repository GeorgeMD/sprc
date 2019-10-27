struct request {
    string req<>;
};

struct response {
    string word<>;
    int hits;
};

program START_REQUEST_PROG {
    version START_REQUEST_VERS {
        string START_REQUEST(request) = 1;
    } = 1;
} = 0x31337;

program SEND_ARGUMENT_PROG {
    version SEND_ARGUMENT_VERS {
        response SEND_ARGUMENT(request) = 1;
    } = 1;
} = 31337;