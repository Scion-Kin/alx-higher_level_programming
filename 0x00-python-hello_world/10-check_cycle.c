#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *fol = list;
	listint_t *fol_next = list;

	if (list == NULL)
		return (0);

	while (fol && fol_next && fol_next->next)
	{
		fol = fol->next;
		fol_next = fol_next->next;
		fol_next = fol_next->next;
		if (fol == fol_next)
			return (1);
	}

	return (0);
}
