#include <string.h>

extern "C" char* __gnu_strerror_r(int errnum, char* buf, size_t buflen) {
    if (strerror_r(errnum, buf, buflen) != 0 && buflen > 0) {
        buf[0] = '\0';
    }
    return buf;
}
