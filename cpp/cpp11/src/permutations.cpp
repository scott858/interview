#include <iostream>
#include <vector>

using namespace std;

void swap(double &el1, double &el2) {
    auto temp = el1;
    el1 = el2;
    el2 = temp;
}

void permuations(vector<double> vec, int32_t left) {
    auto right = vec.size() - 1;
    if(left < right) {
        for(auto i=left; i<right+1; ++i) {
            swap(vec[left], vec[i]);
            permuations(vec, left + 1);
            swap(vec[left], vec[i]);
        }
    }
    else {
        for(auto d : vec) {
            cout << d << " ";
        }
        cout << "\n";
    }
}

int32_t main(int32_t argc, char **argv) {
//    vector<double> vec{12., 0., 2., 100., 1., 24.};
    vector<double> vec{12., 0., 2., 100.};
    permuations(vec, 0);
    return 0;
}
