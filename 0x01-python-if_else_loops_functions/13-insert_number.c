#include <stddef.h>
#include <stdlib.h>
#include "lists.h"
/**
 * Enter point - insert_node
 * @head: pointer to the first element
 * @number: number to insert
 *
 * Return: the address of the new element
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = (listint_t *)malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else if (number < *head->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		listint_t *current = *head;

		while (current != NULL && number > current->next->n)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = next;

	}
return (new->next);
}
