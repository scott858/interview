#include <iostream>
#include <vector>

using namespace std;

class InsertionSort {
public:
    InsertionSort();

    void sort(vector<double> &v);
    void swap(double &e1, double &e2);
};


InsertionSort::InsertionSort() {}

void InsertionSort::swap(double &e1, double &e2) {
    auto temp = e1;
    e1 = e2;
    e2 = temp;
}

void InsertionSort::sort(vector<double> &v) {
    for(int32_t i=0; i<v.size(); ++i) {
        int32_t active_ix = i;
        while((v[active_ix] < v[active_ix - 1]) && (active_ix > 0)) {
            swap(v[active_ix], v[active_ix - 1]);
            --active_ix;
        }
    }
}

int main() {
    vector<double> v{12., 0., 1., 2., 100., 24.};
    auto is = InsertionSort();
    is.sort(v);

    for(auto vv : v) {
        cout << vv << " ";
    }
    return 0;
}
