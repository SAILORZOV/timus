#include <iostream>
#include <string>

int main () {
    int i, count = 1;
    std::string s;
    std::cin >> i >> s;

    int length = s.length();
    while (i > 1) {
        count *= i;
        i -= length;
    }
    std::cout << count << '\n';
}
