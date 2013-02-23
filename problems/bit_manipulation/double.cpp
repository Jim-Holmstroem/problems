
#define LEN(x) (sizeof((x))/sizeof((x)[0]))

#include<iostream>
#include<bitset>

union u_double
{
    double dbl;
    char data[sizeof(double)];
};

void print_32bit_double(double value)
{
    union u_double d;
    d.dbl = value;
    //for(int i=LEN(d.data); i-->0;) //little endian
    //{
    //    std::cout << std::bitset<8>(d.data[i]) << " ";
    //}
    //std::cout << std::endl;

    //any bits outside the 32bits
    if(std::bitset<4>(d.data[5]).any() /*the lower 4bits*/ || std::bitset<8>(d.data[6]).any() || std::bitset<8>(d.data[7]).any())
    {
        std::cout << "ERROR" << std::endl;
    }
    std::cout << "0.";

    //inside the 32bits
    std::cout << std::bitset<4>(d.data[1]);
    std::cout << std::bitset<8>(d.data[2]);
    std::cout << std::bitset<8>(d.data[3]);
    std::cout << std::bitset<8>(d.data[4]);
    std::cout << std::bitset<4>(d.data[5]>>4); //shift down the higher 4bits
    std::cout << std::endl;
};

int main()
{
    std::cout << std::bitset<4>(0).none() << std::endl;
    print_32bit_double(-2.5);
    print_32bit_double(-2.0);
    print_32bit_double(-1.5);
    print_32bit_double(-1.0);
    print_32bit_double(-0.5);
    print_32bit_double( 0.0);
    print_32bit_double( 0.5);
    print_32bit_double( 1.0);
    print_32bit_double( 1.5);
    print_32bit_double( 2.0);
    print_32bit_double( 2.5);
    std::cout << "===========" <<std::endl;
    print_32bit_double(-0.1);
    print_32bit_double( 0.1);
};

