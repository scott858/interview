#include "stdlib.h"
#include "stdio.h"

typedef struct node_tag {
    double data;
    struct node_tag *next;
} list_node_type;

void print_list(list_node_type *node) {

    while (node) {
        printf("%.2f, ", node->data);
        node = node->next;
    }
    printf("\n");

}

void pre_insert(list_node_type **head, list_node_type *new_head) {
    new_head->next = *head;
    *head = new_head;
}

void pre_insert_dyn(list_node_type ** head, double data) {
    list_node_type *new_head = (list_node_type*)malloc(sizeof(list_node_type));
    new_head->data = data;
    pre_insert(head, new_head);
}

void post_insert(list_node_type *head, list_node_type *new_tail) {
    while (head->next) {
        head = head->next;
    }

    head->next = new_tail;
}

void at_insert(list_node_type *head, list_node_type *new_node, int32_t pos) {
    int32_t pos_count = 0;
    while (head->next) {
        ++pos_count;
        if (pos_count == pos) {
            list_node_type *prev_node = head;
            list_node_type *next_node = head->next;
            prev_node->next = new_node;
            new_node->next = next_node;
        } else {
            head = head->next;
        }
    }
}

list_node_type *get_at(list_node_type *head, int32_t pos) {
    list_node_type *res = head;
    int32_t pos_count = 0;
    while (head->next) {
        pos_count++;
        if (pos_count == pos) {
            res = head->next;
        } else {
            head = head->next;
        }
    }
    return res;
};

list_node_type *pop_head(list_node_type **head) {
    list_node_type *old_head = *head;
    if (*head) {
        list_node_type *new_head = (*head)->next;
        *head = new_head;
    }
    return old_head;
}

list_node_type *pop_tail(list_node_type *head) {
    list_node_type *tail = NULL;
    while (head->next) {
        if (head->next->next == NULL) {
            tail = head->next;
            head->next = NULL;
            break;
        } else {
            head = head->next;
        }
    }
    return tail;
}

list_node_type *delete_at(list_node_type *head, int32_t pos) {
    int32_t pos_count = 0;
    list_node_type *node_at = NULL;
    while (head->next) {
        pos_count++;
        if (pos_count == pos) {
            list_node_type *prev_node = head;
            node_at = head->next;
            if (head->next->next) {
                list_node_type *next_node = head->next->next;
                prev_node->next = next_node;
            }
            break;
        }
    }
    return node_at;
}

int main(void) {
    list_node_type head = {.data=0, .next=NULL};
    list_node_type node1 = {.data=1, .next=NULL};
    list_node_type node2 = {.data=2, .next=NULL};
    list_node_type node3 = {.data=3, .next=NULL};
    list_node_type node4 = {.data=4, .next=NULL};
    list_node_type node5 = {.data=5, .next=NULL};

    head.next = &node1;
    node1.next = &node2;

    list_node_type *head_ptr = &head;

    pre_insert(&head_ptr, &node3);

    post_insert(head_ptr, &node4);

    at_insert(head_ptr, &node5, 3);

    print_list(head_ptr);

    list_node_type *old_head = pop_head(&head_ptr);

    printf("%.2f\n", old_head->data);

    print_list(head_ptr);

    list_node_type *old_tail = pop_tail(head_ptr);

    printf("%.2f\n", old_tail->data);

    print_list(head_ptr);

    list_node_type *node_at = delete_at(head_ptr, 1);

    printf("%.2f\n", node_at->data);

    print_list(head_ptr);

    printf("%.2f\n", get_at(head_ptr, 3)->data);

    pre_insert_dyn(&head_ptr, 100.);

    print_list(head_ptr);

}