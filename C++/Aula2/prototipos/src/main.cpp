#include <iostream>
#include "mymath.h" // entre aspas pq estra dentro do diretório que estamos trabalhando

using namespace std;

int main()
{
    int a,b,s = 0;
    a = 10;
    b = 20;
    s = soma(a,b);
    cout<<"Resultado da soma: "<<s<<endl;
    return 0;
}