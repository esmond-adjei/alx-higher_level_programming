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
	if (current == NULL || lead == NULL)
		return (0);

	while (current != lead)
	{
		if (lead == NULL || lead->next == NULL)
			return (1);
		current = current->next;
		lead = lead->next->next;
	}
	return (0);
}
