#include "../inc/lrucache.h"

int32_t main(int32_t argc, char **argv) {
    vector<double> v{12., 0., 2., 100., 1., 24.};
    auto lruCache = LruCache<int32_t, double>{};
    for (auto i = 0; i < v.size(); ++i) {
        lruCache.set(pair<int32_t, double>{i, v[i]});
    }

    lruCache.printMap();

    for (auto key = 0; key < v.size(); ++key) {
        auto value = lruCache.get(key);
        cout << "key: " << key << ", value: " << value << "\n";
    }
    cout << "\n";

    lruCache.printList();

    lruCache.get(4);

    lruCache.printList();

}
