
#define LEN(x) (sizeof((x))/sizeof((x)[0]))

#include<iostream>
#include<bitset>

union u_double
{
    double dbl;
    long long lng;
    char data[sizeof(double)];
};

void print_32bit_double(double value)
{
    union u_double d;
    d.dbl = value;

    std::cout << std::bitset<1>(d.lng>>63);
    std::cout << "|" << std::bitset<11>(d.lng>>52);
    std::cout << "|" << std::bitset<52>(d.lng) << std::endl;

};

int main()
{
    print_32bit_double(-8.0);
    print_32bit_double(-7.5);
    print_32bit_double(-7.0);
    print_32bit_double(-6.5);
    print_32bit_double(-6.0);
    print_32bit_double(-5.5);
    print_32bit_double(-5.0);
    print_32bit_double(-4.5);
    print_32bit_double(-4.0);
    print_32bit_double(-3.5);
    print_32bit_double(-3.0);
    print_32bit_double(-2.5);
    print_32bit_double(-2.0);
    print_32bit_double(-1.5);
    print_32bit_double(-1.0);
    print_32bit_double(-0.5);
    print_32bit_double( 0.0); //explicit to avoid calculation roundoffs
    print_32bit_double( 0.5);
    print_32bit_double( 1.0);
    print_32bit_double( 1.5);
    print_32bit_double( 2.0);
    print_32bit_double( 2.5);
    print_32bit_double( 3.0);
    print_32bit_double( 3.5);
    print_32bit_double( 4.0);
    print_32bit_double( 4.5);
    print_32bit_double( 5.0);
    print_32bit_double( 5.5);
    print_32bit_double( 6.0);
    print_32bit_double( 6.5);
    print_32bit_double( 7.0);
    print_32bit_double( 7.5);
    print_32bit_double( 8.0);
    std::cout << "===========" <<std::endl;
    print_32bit_double(-0.1);
    print_32bit_double( 0.1);
};

