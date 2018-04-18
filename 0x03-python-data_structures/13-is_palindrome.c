#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function to check if singly linked list is a palidrome
 * @head: double pointer of listint_t type to head of list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *temp1 = *head;
	listint_t *temp2 = NULL;

	if (*head == NULL || head == NULL)
	{
		return (1);
	}

	while (temp != NULL)
	{
		add_nodeint_end(&temp2, temp->n);
		temp = temp->next;
	}
	while (temp1 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
			continue;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
