#include "stdlib.h"
#include "stdio.h"

#define HASH_SIZE 100

typedef struct tree_node_tag {
    double data;
    struct tree_node_tag *left;
    struct tree_node_tag *right;
} tree_node_s;

typedef struct list_node_tag {
    tree_node_s *tree_node;
    struct list_node_tag *next;
} list_node_s;

void add_hash(tree_node_s *tree_node, int32_t horpos);

list_node_s *list_hash[HASH_SIZE];

list_node_s *new_list_node(tree_node_s *tree_node) {
    list_node_s *new_node = (list_node_s *) malloc(sizeof(list_node_s));
    new_node->tree_node = tree_node;
    return new_node;
}

tree_node_s *new_tree_node(double data) {
    tree_node_s *new_node = (tree_node_s *) malloc(sizeof(tree_node_s));
    new_node->data = data;
    return new_node;
}

void traverse_vertical(tree_node_s *root, int32_t horpos) {
    add_hash(root, horpos);

    if (root->left) {
        traverse_vertical(root->left, horpos - 1);
    }

    if (root->right) {
        traverse_vertical(root->right, horpos + 1);
    }
}

void add_hash(tree_node_s *tree_node, int32_t horpos) {

    list_node_s *new_node = new_list_node(tree_node);
    int32_t hash_index = horpos + HASH_SIZE / 2;
    if (list_hash[hash_index]) {
        list_node_s *prev_node = list_hash[hash_index];
        while(prev_node->next) {
            prev_node = prev_node->next;
        }
        prev_node->next = new_node;
    } else {
        list_hash[hash_index] = new_node;
    }

}

void print_list_hash(void) {
    int32_t i;
    for (i = 0; i < HASH_SIZE; ++i) {
        list_node_s *list_node = list_hash[i];
        while (list_node) {
            printf("%.2f, ", list_node->tree_node->data);
            list_node = list_node->next;
        }
    }
}

int32_t main(void) {
    tree_node_s *root = new_tree_node(1.);
    tree_node_s *node2 = new_tree_node(2.);
    tree_node_s *node3 = new_tree_node(3.);
    tree_node_s *node4 = new_tree_node(4.);
    tree_node_s *node5 = new_tree_node(5.);
    tree_node_s *node6 = new_tree_node(6.);
    tree_node_s *node7 = new_tree_node(7.);
    tree_node_s *node8 = new_tree_node(8.);
    tree_node_s *node9 = new_tree_node(9.);

    root->left = node2;
    root->right = node3;

    node2->left = node4;
    node2->right = node5;

    node3->left = node6;
    node3->right = node7;

    node7->left = node8;
    node7->right = node9;

    traverse_vertical(root, 0);
    print_list_hash();
}