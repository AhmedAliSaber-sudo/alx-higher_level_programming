#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome.
 * @head: pointer to the head of linked list.
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list = *head;
	unsigned int size = 0, i = 0;
	int value[10240];

	if (!head)
		return (0);

	if (!*head)
		return (1);

	while (list)
	{
		list = list->next;
		size += 1;
	}
	if (size == 1)
		return (1);

	list = *head;
	while (list)
	{
		value[i++] = list->n;
		list = list->next;
	}

	for (i = 0; i <= (size/2); i++)
	{
		if (value[i] != value[size - i - 1])
			return (0);
	}
	return (1);
}
