#include "stdlib.h"
#include "stdio.h"

#define QUEUE_LENGTH 100

typedef struct node_tag {
    double data;
    struct node_tag *left;
    struct node_tag *right;
} node_s;

static int32_t queue_end_ix = -1;
static int32_t queue_start_ix = -1;
static int32_t queue_spots = QUEUE_LENGTH;
static node_s *queue[QUEUE_LENGTH] = {NULL};

node_s* queue_pop(void );

int32_t queue_push(node_s *node);

node_s *create_node(double data) {
    node_s *node = (node_s *) malloc(sizeof(node_s));
    node->data = data;
    return node;
}

void in_order_traversal(node_s *node) {
    if (node->left) {
        in_order_traversal(node->left);
    }

    printf("%.2f, ", node->data);

    if (node->right) {
        in_order_traversal(node->right);
    }
}

void pre_order_traversal(node_s *node) {
    printf("%.2f, ", node->data);

    if (node->left) {
        pre_order_traversal(node->left);
    }

    if (node->right) {
        pre_order_traversal(node->right);
    }
}

void post_order_traversal(node_s *node) {
    if (node->left) {
        post_order_traversal(node->left);
    }

    if (node->right) {
        post_order_traversal(node->right);
    }

    printf("%.2f, ", node->data);
}

void delete(node_s *node) {
    if (node->left) {
        post_order_traversal(node->left);
    }

    if (node->right) {
        post_order_traversal(node->right);
    }

    printf("%.2f, ", node->data);
    free(node);
}

void breadth_first_search(node_s *node) {
    queue_push(node);

    while(queue_spots < QUEUE_LENGTH) {
        node_s *next_node = queue_pop();
        if(next_node) {
            printf("%.2f, ", next_node->data);
            if(next_node->left) {
                queue_push(next_node->left);
            }
            if(next_node->right) {
                queue_push(next_node->right);
            }
        }
    }
}

int32_t queue_push(node_s *node) {
    int32_t ret = 0;
    if (queue_spots > 0) {
        queue_end_ix++;
        queue_end_ix %= QUEUE_LENGTH;
        queue[queue_end_ix] = node;
        queue_spots--;
    } else {
        ret = -1;
    }

    return ret;
}

node_s* queue_pop(void) {
    node_s *node = NULL;
    if (queue_spots < QUEUE_LENGTH) {
        queue_start_ix++;
        queue_end_ix %= QUEUE_LENGTH;
        node = queue[queue_start_ix];
        queue_spots++;
    }
    return node;
}

int32_t main() {
    node_s *root = create_node(0);
    node_s *node1 = create_node(1);
    node_s *node2 = create_node(2);
    node_s *node3 = create_node(3);
    node_s *node4 = create_node(4);
    node_s *node5 = create_node(5);

    root->left = node1;
    root->right = node2;

    node1->left = node3;
    node1->right = node4;

    node2->left = node5;

    in_order_traversal(root);
    printf("\n");
    pre_order_traversal(root);
    printf("\n");
    post_order_traversal(root);
    printf("\n");
    breadth_first_search(root);
    printf("\n");
    delete(root);
    return 0;
}
