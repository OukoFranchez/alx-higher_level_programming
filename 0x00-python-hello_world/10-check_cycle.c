#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list has a cycle.
 * @list: singly-linked list being checked
 *
 * Return: 0 when no cycle & 1 when there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	slow = list->next;
	fast = list->next->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
