#include <iostream>
#include <vector>

using namespace std;

template<typename T>
class MergeSort {
public:
    MergeSort();
    ~MergeSort();

    vector<T> sort(vector<T> &v);
    vector<T> merge(vector<T> &left, vector<T> &right);
    static void printVec(const vector<T> &v);
};

template<typename T>
MergeSort<T>::MergeSort() {}

template<typename T>
MergeSort<T>::~MergeSort() {};

template<typename T>
void MergeSort<T>::printVec(const vector<T> &v) {
    for(auto vv : v) {
        cout << vv << " ";
    }
    cout << "\n";
}

template<typename T>
vector<T> MergeSort<T>::sort(vector<T> &v) {
    if(v.size() > 1) {
        int32_t mid_ix = v.size() / 2;
        auto left = vector<T>{v.begin(), v.begin() + mid_ix};
        auto right = vector<T>{v.begin() + mid_ix, v.end()};
        left = this->sort(left);
        MergeSort<double>::printVec(left);
        right = this->sort(right);
        MergeSort<double>::printVec(right);
        v = this->merge(left, right);
        MergeSort<double>::printVec(v);
        cout << "\n";
    }

    return v;
}

template<typename T>
vector<T> MergeSort<T>::merge(vector<T> &left, vector<T> &right) {
    vector<T> sorted;
    sorted.resize(left.size() + right.size());
    auto sorted_it = sorted.begin();
    auto left_it = left.begin();
    auto right_it = right.begin();
    while(left_it != left.end() && right_it != right.end()) {
        if(*left_it < *right_it) {
            *sorted_it = *left_it;
            ++left_it;
            ++sorted_it;
        }
        else {
            *sorted_it = *right_it;
            ++right_it;
            ++sorted_it;
        }
    }

    while(left_it != left.end()) {
        *sorted_it = *left_it;
        ++left_it;
        ++sorted_it;
    }

    while(right_it != right.end()) {
        *sorted_it = *right_it;
        ++right_it;
        ++sorted_it;
    }

    return sorted;
}

int32_t main(int32_t argc, char **argv) {
    vector<double> v{12., 0., 1., 2., 100., 24.};
    auto ms = MergeSort<double>();
    v = ms.sort(v);
    MergeSort<double>::printVec(v);
}