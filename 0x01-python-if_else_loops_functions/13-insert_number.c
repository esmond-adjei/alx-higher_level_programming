#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *curr;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = *head;
	while (curr->next != NULL && curr->next->n < number)
	{
		curr = curr->next;
	}
	new_node->next = curr->next;
	curr->next = new_node;

	return (new_node);
}
