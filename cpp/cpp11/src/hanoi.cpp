#include <iostream>
#include <list>

using namespace std;


void hanoi(int32_t n,
           list<char> &src,
           list<char> &target,
           list<char> &aux
           ) {

    if(n > 0) {
        hanoi(n-1, src, aux, target);

        target.push_back(src.back());
        src.pop_back();

        hanoi(n-1, aux, target, src);
    }
}


int32_t main(int32_t argc, char **argv) {
    list<char> src{'A', 'B', 'C', 'D'};
    list<char> target{};
    list<char> aux{};

    for(auto src_it = src.begin(); src_it != src.end(); ++ src_it) {
        cout << *src_it << "";
    }
    cout << "\n";

    hanoi(src.size(), src, target, aux);

    for(auto target_it = target.begin(); target_it != target.end(); ++ target_it) {
        cout << *target_it << "";
    }
    cout << "\n";
}
