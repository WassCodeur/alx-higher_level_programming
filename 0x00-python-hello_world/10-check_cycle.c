#include "lists.h"
/**
 * check_cycle - Enter point
 * @list : pointer to the list to check
 *
 * Return: 1 if the list has a cycle else 0
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *t;
	listint_t *r;

	if (list->next == NULL)
	{
		return 0;
	}
	t = list;
	r = list->next;
	while (r != NULL && r->next != NULL)
	{
		if (t == r)
		{
			return 1;
		}
		t = list->next;
		r = r->next->next;
	}
	return 0;
}
