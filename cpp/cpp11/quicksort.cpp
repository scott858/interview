#include <iostream>
#include <vector>
#include <valarray>

using namespace std;


template<typename T>
class QuickSort {
public:
    QuickSort();

    ~QuickSort();

    vector<T> sort(vector<T> &v);

    void swap(T &e1, T &e2);

    static void printVec(const vector<T> &v);
};

template<typename T>
QuickSort<T>::QuickSort() {}

template<typename T>
QuickSort<T>::~QuickSort() {}

template<typename T>
vector<T> QuickSort<T>::sort(vector<T> &v) {
    if (v.size() > 1) {
        auto pivot = v.back();
        int32_t pivot_ix = 0;
        for (int32_t i = 0; i < v.size() - 1; ++i) {
            if (v[i] < pivot) {
                swap(v[i], v[pivot_ix]);
                ++pivot_ix;
            }
        }
        swap(v[pivot_ix], v.back());

        auto left = vector<T>{v.begin(), v.begin() + pivot_ix};
        auto right = vector<T>{v.begin() + pivot_ix + 1, v.end()};

        left = this->sort(left);
        right = this->sort(right);
        left.push_back(pivot);
        left.insert(left.end(), right.begin(), right.end());
        v = left;
    }
    return v;
}

template<typename T>
void QuickSort<T>::swap(T &e1, T &e2) {
    auto temp = e1;
    e1 = e2;
    e2 = temp;
}

template<typename T>
void QuickSort<T>::printVec(const vector<T> &v) {
    for (auto vv : v) {
        cout << vv << " ";
    }
    cout << "\n";
}


int32_t main(int32_t argc, char **argv) {
    vector<double> v{12., 0., 1., 2., 100., 24.};
    auto qs = QuickSort<double>();
    v = qs.sort(v);
    QuickSort<double>::printVec(v);
}
