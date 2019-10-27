#include <rpc/rpc.h>
#include <unordered_map>
#include <fstream>

#include "load.h"

#define YES "YES"
#define NO "NO"
#define SEARCH_REQUEST "SEARCH"
#define APPEND_REQUEST "APPEND"
#define SEARCH_RESPONSE (YES " " SEARCH_REQUEST)
#define APPEND_RESPONSE (YES " " APPEND_REQUEST)
#define APPEND_SUCCESS "APPEND SUCCESSFUL"
#define APPEND_FAIL "APPEND FAILED"

#define FILENAME "file.txt"

#ifndef BUFSIZ
#define BUFSIZ 8192
#endif

static bool isServerInit = false;
static std::unordered_map<std::string, int> word_hits_map;
static char const * last_request = nullptr;

bool init_server();
bool appendFile(char * cPtrWord);
response get_response(char const * respStr, int hits = -1);
bool isNumber(char *str, size_t *outNumber);

char ** start_request_1_svc(request *r, struct svc_req *cl)
{
    static char const * response = NO;
    last_request = nullptr;

    if (!isServerInit) {
        if (!init_server()) {
            return const_cast<char **>(&response);
        }
    }

    if (strcmp(r->req, SEARCH_REQUEST) == 0) {
        response = SEARCH_RESPONSE;
        last_request = SEARCH_REQUEST;
    } else if (strcmp(r->req, APPEND_REQUEST) == 0) {
        response = APPEND_RESPONSE;
        last_request = APPEND_REQUEST;
    } else {
        response = NO;
        last_request = nullptr;
    }

    return const_cast<char **>(&response);
}

response * send_argument_1_svc(request *r, struct svc_req *cl) {
    static response res{nullptr, -1};

    if (!isServerInit) {
        if (!init_server()) {
            return &res;
        }
    }

    if (last_request != nullptr) {
        if (strcmp(last_request, SEARCH_REQUEST) == 0) {
            size_t numChars;
            if (isNumber(r->req, &numChars)) {
                res = get_response("", 0);
                for (auto & it : word_hits_map) {
                    if (it.first.length() == numChars)
                        res.hits++;
                }
            } else {
                res = get_response(r->req, word_hits_map[r->req]);
            }
        } else if (strcmp(last_request, APPEND_REQUEST) == 0) {
            if (appendFile(r->req))
                res = get_response(APPEND_SUCCESS, word_hits_map[r->req]);
            else
                res = get_response(APPEND_FAIL);
        }
    }

    return &res;
}

bool isNumber(char *str, size_t *outNumber) {
    *outNumber = strtoul(str, nullptr, 10);
    return *outNumber != 0ULL;
}

bool init_server() {
    isServerInit = true;

    char buffer[BUFSIZ];
    std::ifstream f(FILENAME);
    std::string word;

    while (getline(f, word)) {
        if (word_hits_map.find(word) == word_hits_map.end())
            word_hits_map[word] = 0;

        ++word_hits_map[word];

    }

    f.close();

   return true;
}

response get_response(char const * respStr, int hits) {
    response resp;
    resp.word = const_cast<char *>(respStr);
    resp.hits = hits;

    return resp;
}

bool appendFile(char * cPtrWord) {
    if (cPtrWord == nullptr)
        return false;

    std::ofstream f(FILENAME, std::ios::app);
    f << cPtrWord << std::endl;

    std::string word(cPtrWord);

    if (word_hits_map.find(word) == word_hits_map.end())
        word_hits_map[word] = 0;

    word_hits_map[word]++;

    f.close();

    return true;
}