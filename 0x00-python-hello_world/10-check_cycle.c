#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *lead;

	current = list, lead = list->next;
	while (lead != NULL && lead->next != NULL)
	{
		current = current->next;
		lead = lead->next->next;

		if (current == lead)
		{
			return (1);
		}
	}
	return (0);
}
