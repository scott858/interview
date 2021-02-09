#include <iostream>
#include <vector>

using namespace std;

class SelectionSort {
public:
    SelectionSort();

    void sort(vector<double> &v);
    void swap(double &e1, double &e2);
};


SelectionSort::SelectionSort() {}

void SelectionSort::swap(double &e1, double &e2) {
    auto temp = e1;
    e1 = e2;
    e2 = temp;
}

void SelectionSort::sort(vector<double> &v) {
    for(int32_t i = 0; i < v.size(); ++i) {
        auto smallest_ix = i;
        for(int32_t j = i; j < v.size(); ++j) {
            if(v[smallest_ix] > v[j]) {
                smallest_ix = j;
            }
        }
        swap(v[i], v[smallest_ix]);
    }
}

int32_t main() {
    vector<double> v{12., 0., 1., 2., 100., 24.};
    auto ss = SelectionSort();
    ss.sort(v);
    for(auto vv : v) {
        cout << vv << " ";
    }
    return 0;
}
