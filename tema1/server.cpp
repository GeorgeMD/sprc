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

bool initServer();

bool appendFile(char * word);

// Intoarce o structura response ce contine parametrii dati functiei.
response getResponse(char const * respStr = "", int hits = -1);

// Verifica daca sirul dat ca argument este un numar, intorcand true si numarul
// parsat in al doilea parametru, sau false si o valoare necunoscuta in
// al doilea parametru.
bool isNumber(char *str, size_t *outNumber);

// Functie RPC prin care clientul transmite ce request face (SEARCH / APPEND)
char ** start_request_1_svc(request *r, struct svc_req *cl)
{
    static char const * response = NO;
    last_request = nullptr;

    if (!isServerInit) {
        if (!initServer()) {
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

// Functie RPC prin care clientul transmite argumentul cererii.
response * send_argument_1_svc(request *r, struct svc_req *cl) {
    static response res = getResponse();

    if (!isServerInit) {
        if (!initServer()) {
            return &res;
        }
    }

    // un client implementat gresit incearca sa trimita un argument fara sa fi
    // specificat ce fel de operatie vrea sa execute in prealabil
    if (last_request != nullptr) {
        if (strcmp(last_request, SEARCH_REQUEST) == 0) {
            size_t numChars;
            if (isNumber(r->req, &numChars)) {
                // cerere SEARCH cu numar
                res = getResponse("", 0);
                for (auto & it : word_hits_map) {
                    if (it.first.length() == numChars)
                        res.hits++;
                }
            } else {
                // cerere SEARCH cu cuvant
                int hits = 0;
                if (word_hits_map.find(r->req) != word_hits_map.end())
                    hits = word_hits_map[r->req];

                // daca aici as fi folosit word_hits_map[r->req] ca al doilea
                // argument pentru getResponse, atunci in cazul in care cuvantul
                // cautat nu exista in map acesta ar fi fost introdus in map
                res = getResponse(r->req, hits);
            }
        } else if (strcmp(last_request, APPEND_REQUEST) == 0) {
            if (appendFile(r->req))
                res = getResponse(APPEND_SUCCESS, word_hits_map[r->req]);
            else
                res = getResponse(APPEND_FAIL);
        }
    }

    return &res;
}

bool isNumber(char *str, size_t *outNumber) {
    *outNumber = strtoul(str, nullptr, 10);
    return std::to_string(*outNumber) == std::string(str);
}

bool initServer() {
    isServerInit = true;

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

response getResponse(char const * respStr, int hits) {
    response resp;
    resp.word = const_cast<char *>(respStr);
    resp.hits = hits;

    return resp;
}

bool appendFile(char * word) {
    if (word == nullptr)
        return false;

    std::ofstream f(FILENAME, std::ios::app);
    if (!f)
        return false;

    // nu scrie newline pentru primul cuvant din fisier
    if (f.tellp() != 0)
        f << "\n";
    f << word;

    if (word_hits_map.find(word) == word_hits_map.end())
        word_hits_map[word] = 0;

    word_hits_map[word]++;

    f.close();

    return true;
}