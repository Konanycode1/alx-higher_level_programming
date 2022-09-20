#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: singly linked list
 * Return: 1 if cycle found 0 else
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list->next;

	while (current != NULL)
	{
		if (current == list)
			return (1);
		current = current->next;
	}
	return (0);
}
