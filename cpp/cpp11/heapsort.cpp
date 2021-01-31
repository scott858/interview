#include <iostream>
#include <vector>

using namespace std;

template<typename T>
class HeapSort {
public:
    HeapSort();

    ~HeapSort();

    void sort(vector<T> &v, int32_t end_ix);

    void heapStep(vector<T> &v, int32_t parent_ix, int32_t end_ix);

    void heapify(vector<T> &v);

    void swap(T &e1, T &e2);
};

template<typename T>
void HeapSort<T>::swap(T &e1, T &e2) {
    auto temp = e1;
    e1 = e2;
    e2 = temp;
}

template<typename T>
HeapSort<T>::HeapSort() {}

template<typename T>
HeapSort<T>::~HeapSort() {}

template<typename T>
void HeapSort<T>::sort(vector<T> &v, int32_t end_ix) {
    if(end_ix > 0) {
        swap(v[0], v[end_ix]);
        heapStep(v, 0, end_ix - 1);
        sort(v, end_ix - 1);
    }
}

template<typename T>
void HeapSort<T>::heapify(vector<T> &v) {
    auto half_ix = (v.size() - 1) / 2;
    for(int32_t i = half_ix; i >= 0; --i) {
        heapStep(v, i, v.size() - 1);
    }
}

template<typename T>
void HeapSort<T>::heapStep(vector<T> &v, int32_t parent_ix, int32_t end_ix) {
    auto half_ix = end_ix / 2;
    if (parent_ix <= half_ix) {

        auto left_child_ix = 2 * parent_ix + 1;
        if(left_child_ix <= end_ix) {
            if(v[parent_ix] < v[left_child_ix]) {
                swap(v[parent_ix], v[left_child_ix]);
            }
            heapStep(v, left_child_ix, end_ix);
        }

        auto right_child_ix = 2 * parent_ix + 2;
        if(right_child_ix <= end_ix) {
            if(v[parent_ix] < v[right_child_ix]) {
                swap(v[parent_ix], v[right_child_ix]);
            }
            heapStep(v, right_child_ix, end_ix);
        }
    }
}


int32_t main(int32_t argc, char **argv) {
    vector<double> v{12., 0., 2., 100., 1., 24.};
    auto hp = HeapSort<double>{};
    hp.heapify(v);
    hp.sort(v, v.size() - 1);
    for(auto vv : v) {
        cout << vv << " ";
    }
    cout << "\n";
}
