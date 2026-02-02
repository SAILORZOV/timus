#include <iomanip>
#include <iostream>
#include <cmath>


class MyVector {
public:
    MyVector() : length(100), fill(0), vec(new uint64_t[length]) {}

    void push(uint64_t x) {
        if (length == fill) grow();
        vec[fill++] = x;
    }
    uint64_t pop() {
        return vec[--fill];
    }
    int getFill() const {
        return fill;
    }

private:
    void grow() {
        length *= 2;
        uint64_t* temp = new uint64_t[length];
        std::copy(vec, vec + fill, temp);
        delete[] vec;
        vec = temp;
    }
    int length, fill;
    uint64_t* vec;
};


int main () {
    MyVector v;
    uint64_t num;
    while (std::cin >> num) {
        v.push(num);
    }
    std::cout << std::fixed << std::setprecision(4);
    int count = v.getFill();
    while (count != 0) {
        std::cout << std::sqrt(static_cast<long double>(v.pop())) << '\n';
        count--;
    }
}