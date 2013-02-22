#include<iostream>
#include<cstring>
#include<algorithm>

#define LEN(x) ( sizeof( x ) / sizeof( ( x )[0] ) )

void swap(char& a, char& b)
{
    //std::cout << "swap(" << a << ", " << b << ")" << std::endl << std::flush;
    if(a!=b){
        a ^= b;
        b ^= a;
        a ^= b;
    }
};

void reverse(char* str)
{ //reverse all but the null termination
    int size = std::strlen(str);
    //std::cout << size << ":" << (size/2) << std::endl << std::flush;
    for(int i = 0; i<size/2; i++)
    {
        //std::cout << i << "/" << (size-i-1) << std::endl << std::flush;
        swap( str[i], str[size-i-1] );
    }
};

void simple_reverse(char * str)
{
    std::reverse(str, str+std::strlen(str));
};

int main()
{
    const char* testdata[6] = {"", "ab", "abc", "abcd", "another longer word","a"}; //odd/even/one/empty
    char rev[512]; //nulltermination handles the rewritting
    for(int i=0; i<LEN(testdata); ++i)
    {
        std::cout << "orginal>" << testdata[i] << std::endl << std::flush; 
        strcpy(rev, testdata[i]);
        reverse(rev);
        std::cout << "    rev>" << rev << std::endl << std::flush;
        strcpy(rev, testdata[i]);
        simple_reverse(rev);
        std::cout << "   srev>" << rev << std::endl << std::flush;
    }
    //testdata still in scope
};

