#include <iostream>
#include <memory>
#include <queue>

using namespace std;


template<typename T>
class TreeNode {
public:
    TreeNode(T data);

    ~TreeNode();

    void setLeft(unique_ptr<TreeNode<T>> l) { left = move(l); }

    void setRight(unique_ptr<TreeNode<T>> r) { right = move(r); }

    void traverseInOrder();
    void traversePreOrder();
    void traversePostOrder();
    void breadthFirstSearch();

private:
    T data = 0;
    unique_ptr<TreeNode<T>> left;
    unique_ptr<TreeNode<T>> right;
};

template<typename T>
TreeNode<T>::TreeNode(T data) : data(data),
                                left(nullptr),
                                right(nullptr) {}

template<typename T>
TreeNode<T>::~TreeNode() {}

template<typename T>
void TreeNode<T>::breadthFirstSearch() {
    queue<unique_ptr<TreeNode<double>>> q;
    cout << data << " ";
    q.push(move(left));
    q.push(move(right));

    while(!q.empty()) {
        if(q.front()) {
            cout << q.front()->data << " ";
            q.push(move(q.front()->left));
            q.push(move(q.front()->right));
        }
        q.pop();
    }
}

template<typename T>
void TreeNode<T>::traverseInOrder() {
    if (left) {
        left->traverseInOrder();
    }

    cout << data << " ";

    if (right) {
        right->traverseInOrder();
    }
}

template<typename T>
void TreeNode<T>::traversePreOrder() {
    cout << data << " ";

    if (left) {
        left->traversePreOrder();
    }

    if (right) {
        right->traversePreOrder();
    }
}

template<typename T>
void TreeNode<T>::traversePostOrder() {
    if (left) {
        left->traversePostOrder();
    }

    if (right) {
        right->traversePostOrder();
    }

    cout << data << " ";
}

int32_t main(int32_t argc, char **argv) {
    auto root = make_unique<TreeNode<double>>(1);
    auto node1 = make_unique<TreeNode<double>>(2);
    auto node3 = make_unique<TreeNode<double>>(4);
    auto node4 = make_unique<TreeNode<double>>(5);
    node1->setLeft(move(node3));
    node1->setRight(move(node4));

    auto node2 = make_unique<TreeNode<double>>(3);
//    auto node5 = make_unique<TreeNode<double>>(6);
//    auto node6 = make_unique<TreeNode<double>>(7);
//    node2->setLeft(move(node5));
//    node2->setRight(move(node6));

    root->setLeft(move(node1));
    root->setRight(move(node2));

    root->traverseInOrder();
    cout << "\n";
    root->traversePostOrder();
    cout << "\n";
    root->traversePreOrder();
    cout << "\n";
    root->breadthFirstSearch();
}
