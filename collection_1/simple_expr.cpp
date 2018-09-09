#include <cstdio>

using namespace std;

double calc(char op,double a,double b);

int main(int argc, char const *argv[])
{
    double a, b;
    char op;
    scanf("%lf %c %lf", &a, &op, &b);
    printf("%.0lf\n",calc(op,a,b));
    return 0;
}

double calc(char op,double a,double b)
{
    switch (op)
    {
    case '+':
        return a + b;
        break;
    case '-':
        return a - b;
        break;
    default:
        return a * b;
    }
}