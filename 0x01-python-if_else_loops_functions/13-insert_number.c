#include "lists.h"

/**
 * insert_node - a num is inserted into the list
 * @head: head pte
 * @number: num to be inserted
 *
 * Return: on failer - NULL.
 * Otherwise - new nod ptr.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
