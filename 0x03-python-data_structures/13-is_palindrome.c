#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * *reverse_listint - function to reverse a singly linked list
 * @head: double pointer of listint_t type to head of linked list
 * Return: link to the head of reversed link
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *forward;
	listint_t *back = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);
	forward = *head;
	while (forward != NULL)
	{
		forward = forward->next;
		forward = (*head)->next;
		(*head)->next = back;
		back = *head;
		*head = forward;
	}
	*head = back;
	return (*head);
}

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
	int length = 0, count;

	if (*head == NULL || head == NULL)
	{
		return (1);
	}

	while (temp != NULL)
	{
		add_nodeint_end(&temp2, temp->n);
		temp = temp->next;
		length++;
	}
	reverse_listint(&temp2);
	count = 0;
	while (temp1 != NULL && count < (length / 2))
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
