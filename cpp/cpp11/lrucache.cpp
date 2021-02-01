#include <iostream>
#include <memory>
#include <unordered_map>
#include <list>
#include <vector>

using namespace std;

template<typename X, typename T>
class LruCache {
private:
    struct ListNode {
        explicit ListNode(pair<X, T> data) : data(move(data)) {};

        ~ListNode() { cout << data.first << ": destroyed\n"; };
        pair<X, T> data;
        shared_ptr<struct ListNode> prev;
        shared_ptr<struct ListNode> next;
    };

    shared_ptr<struct ListNode> head;
    shared_ptr<struct ListNode> tail;

    unordered_map<X, shared_ptr<struct ListNode>> lruMap;
    T capacity = 4;
public:
    LruCache() = default;

    ~LruCache() = default;

    T get(X ix);

    void set(pair<X, T> keyValue);

    void printMap();

    void printList();
};

template<typename X, typename T>
void LruCache<X, T>::printMap() {
    for (auto p : lruMap) {
        cout << p.first << " : " << p.second->data.second << "\n";
    }
    cout << "\n";
}

template<typename X, typename T>
void LruCache<X, T>::printList() {
    auto next_node = head;
    while (next_node) {
        auto data = next_node->data;
        cout << "key: " << data.first << ", value: " << data.second << "\n";
        next_node = next_node->next;
    }
    cout << "\n";
}

template<typename X, typename T>
T LruCache<X, T>::get(X ix) {
    auto lru_it = lruMap.find(ix);
    X value = -1;
    if (lru_it != lruMap.end()) {
        auto newHead = lru_it->second;
        value = newHead->data.second;
        auto next = newHead->next;
        auto prev = newHead->prev;

        if (prev) {
            prev->next = next;
        }
        if (next) {
            next->prev = prev;
        }

        newHead->prev = nullptr;
        newHead->next = head;
        head->prev = newHead;
        head = newHead;
    }
    return value;
}

template<typename X, typename T>
void LruCache<X, T>::set(pair<X, T> keyValue) {
    auto oldValue = get(keyValue.first);
    if (oldValue >= 0) {
        head->data.second = keyValue.second;
    } else {
        auto newHead = make_shared<struct ListNode>(keyValue);
        lruMap[keyValue.first] = newHead;
        if (head == nullptr) {
            head = newHead;
            tail = head;
        } else {
            newHead->next = head;
            head->prev = newHead;
            head = newHead;
        }
    }

    if (capacity > 0) {
        --capacity;
    } else {
        /* remove lru, i.e. tail and from map*/
        lruMap.erase(tail->data.first);

        auto newTail = tail->prev;
        newTail->next = nullptr;
        tail = newTail;
    }
}

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
