#include "lists.h"
#include <stdio.h>

int is_palindrome(listint_t **head)
{
	struct listint_s *node = *head; 
	long long int forward;
	long long int reverce;

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
