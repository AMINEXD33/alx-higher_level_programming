#include "lists.h"
#include <stddef.h>
/**
 *check_cycle- this function uses the technique of slow and
 *fast pointer to check, if a linked list has a cycle
 *@list: the head of the linked list
 *Return: 1 if a cycle is found , 0 otherwise
 */
int check_cycle(listint_t *list)
{
	struct listint_s *fast_p = list;
	struct listint_s *slow_p = list;
	int flag;

	if (list == NULL)
		return (0);
	flag = 0;
	while (1)
	{
		/*point to the next node*/
		fast_p = fast_p->next;

		/*this code is eq to waiting a turn then doing something*/
		if (flag == 0)
			flag = 1;
		else if  (flag == 1)
		{
			flag = 0;
			slow_p = slow_p->next;
		}
		/*if the fast pointer hit the NULL 0, if fast==slow 1*/
		if (fast_p == NULL)
			return (0);
		else if (fast_p == slow_p)
			return (1);
	}
}

