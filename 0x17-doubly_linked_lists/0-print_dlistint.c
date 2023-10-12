#include <stdio.h>
/**
 * print_dlistint-print the values of nodes in a linked list
 * @h: head of the linked list
 * Return: the size of the linked list
 */
size_t print_dlistint(const dlistint_t *h)
{
	struct dlistint_t *node = h;
	unsigned int count;


	count = 0;
	while (node != NULL)
	{
		printf("%d\n", node->n);
		node = node->next;
	}
	return (count);
}
