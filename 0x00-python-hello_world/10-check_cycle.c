#include "lists.h"

/**
 * check_cycle - checks if ther is repetition of node values
 * @list: linked list node input
 * Return: 0 if no cycle and 1 if cycle is present
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *trav;
	int a, b;

	current = malloc(sizeof(listint_t));
	trav = malloc(sizeof(listint_t));
	current = list;
	a = current->n;
	trav = current->next;
	b = trav->n;

	while (current->next != NULL)
	{
		current = current->next;
		trav = current->next;
		if (current->n == a && trav->n == b)
			return(1);
	}
	return (0);
}
