#include <iostream>
#include <vector>

using namespace std;

class BubbleSort {
public:
    BubbleSort();

    vector<double> sort(vector<double> v);
    void swap(double &e1, double &e2);

};

BubbleSort::BubbleSort() {}

void BubbleSort::swap(double &e1, double &e2) {
    auto temp = e1;
    e1 = e2;
    e2 = temp;
}

vector<double> BubbleSort::sort(vector<double> v) {
    for (int32_t i = v.size() - 1; i >= 0; --i) {
        for (int32_t j = 0; j < i; ++j) {
            if(v[j] > v[j+1]) {
                swap(v[j], v[j+1]);
            }
        }
    }
    return v;
}


int main() {
    vector<double> v{12., 0., 1., 2., 100., 24.};
    auto b_sort = BubbleSort{};
    v = b_sort.sort(v);
    for(auto vv : v) {
        cout << vv << " ";
    }
    return 0;
}
