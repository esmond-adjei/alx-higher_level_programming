#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next; /* move slow pointer by 1 */
		fast = fast->next->next; /* move fast pointer by 2 */

		if (slow == fast) /* if they meet, there is a cycle */
			return (1);
	}

	return (0); /* no cycle found */
}

