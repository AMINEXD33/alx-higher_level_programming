#include "lists.h"
#include <stdio.h>
/**
 *is_palindrome-this function checks if
 *a a linkd list is palindrome.
 *@head: the head of the linked list
 *Return: 0 if it's not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	struct listint_s *node = *head;
	long long int forward;
	long long int reverce;

	if (*head == NULL)
		return (1);

	forward = 1;
	reverce = 1;
	while (node != NULL)
	{
		forward = ((forward) + (node->n)) % sizeof(long long int) + 1;
		reverce = ((reverce) + (node->n * -1)) % sizeof(long long int) + 1;
		node = node->next;
	}
	if (forward != reverce)
		return (0);
	return (1);
}
