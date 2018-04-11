#include "lists.h"

/**
 * insert_node - function to insert node in sorted list
 * @head: double pointer of listint_t type
 * @number: int type
 * Return: address of new node or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	temp = *head;
	while (number >= temp->next->n)
	{
		temp = temp->next;
	}
	node->next = temp->next;
	temp->next = node;
	return (node);
}
