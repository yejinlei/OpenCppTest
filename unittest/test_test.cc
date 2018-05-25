#include "gtest/gtest.h"


#ifdef __cplusplus
extern "C" {
#endif

    void test1(int, int);

#ifdef __cplusplus
}
#endif
;
TEST(TEST1, 0){
    test1(15, 10);
}

