#include "stdlib.h"
#include "stdio.h"

typedef struct tree_node_tag {
    double data;
    struct tree_node_tag *left;
    struct tree_node_tag *right;
} tree_node_s;

tree_node_s* new_tree_node(double data) {
    tree_node_s *new_node = (tree_node_s*)malloc(sizeof(tree_node_s));
    new_node->data = data;
    return new_node;
}

tree_node_s *prev_node;

void traverse_vertical(tree_node_s *root) {
    if(root->left) {
        traverse_vertical(root->left);
    }

    printf("%.2f, ", root->data);
    if(prev_node != NULL) {
        prev_node->right = root;
        root->left = prev_node;
    }

    prev_node = root;

    if(root->right) {
        traverse_vertical(root->right);
    }
}

void traverse_dll(tree_node_s *node) {
    while(node->left) {
        node = node->left;
    }

    while(node) {
        printf("%.2f, ", node->data);
        node = node->right;
    }
}

int32_t main(void) {
    tree_node_s *root = new_tree_node(10.);
    tree_node_s *node12 = new_tree_node(12.);
    tree_node_s *node15 = new_tree_node(15.);
    tree_node_s *node25 = new_tree_node(25.);
    tree_node_s *node30 = new_tree_node(30.);
    tree_node_s *node36 = new_tree_node(36.);

    root->left = node12;
    root->right = node15;

    node12->left= node25;
    node12->right = node30;

    node15->left= node36;

    traverse_vertical(root);
    printf("\n");
    traverse_dll(root);
}