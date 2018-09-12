#include <cstdio>
using namespace std;

/**
 * https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1053
 */
int main()
{
    // log2(10e8) ≈ 30
    setvbuf(stdin, new char[1 << 20], _IOFBF, 1 << 20);
    setvbuf(stdout, new char[1 << 20], _IOFBF, 1 << 20);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        printf("%d\n", a + b);
    }
    return 0;
}
