#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: A singly-Linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */



int check_cycle(listint_t *list)
{
    listint_t *ptr, *ptr1;

    if (!list)
        return (0);
    
    ptr = list;
    ptr1 = list->next;

    while (ptr1)
    {
        if (ptr1 == ptr)
            return (1);
        ptr1 = ptr1->next;  
    }
    return (0);
}
