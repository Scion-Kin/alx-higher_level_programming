#include "lists.h"

/**
*add_nodeint - adds a new node at the beginning of a listint_t list
*@head: head of listint_t
*@n: int to add in listint_t list
*Return: address of the new element, or NULL if it failed
*/

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
*is_palindrome - identify if a syngle linked list is palindrome
*@head: head of listint_t
*Return: 1 if it is palindrome else 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *new = *head;
	listint_t *trav = NULL, *trav1 = NULL;

	if (*head == NULL || new->next == NULL)
		return (1);
	while (new != NULL)
	{
		add_nodeint(&trav, new->n);
		new = new->next;
	}
	trav1 = trav;
	while (*head != NULL)
	{
		if ((*head)->n != trav1->n)
		{
			free_listint(trav);
			return (0);
		}
		*head = (*head)->next;
		trav1 = trav1->next;
	}
	free_listint(trav);
	return (1);
}