#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *curr = *head;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	
	return (prev);
}

int is_palindrome(listint_t **head)
{
	if (*head == NULL || *head->next == NULL)
	{
		return (1);
	}

	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;

	while (fast_ptr->next != NULL && fast_ptr->next->next != NULL)
	{
		slow_ptr = slow->next;
		fast = fast->next->next;
	}

	listint_t *first_half = *head;
	listint_t *second_half = reverse_list(slow->next);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
