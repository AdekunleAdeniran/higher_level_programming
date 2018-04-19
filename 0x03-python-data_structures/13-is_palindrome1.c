#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int str[10240];
	int count, length;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	length = 0;
	while (*head != NULL)
	{
		*head = (*head)->next;
		length++;
	}
	count = 0;
	while (temp != NULL)
	{
		str[count] = temp->n;
		temp = temp->next;
		count++;
	}
	count = 0;
	while (count <= length / 2)
	{
		if (str[count] != str[length - 1])
		{
			return (0);
		}
		count++;
		length--;
	}
	return (1);
}
