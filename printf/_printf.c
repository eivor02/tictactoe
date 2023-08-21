#include "main.h"
/**
 * _printf - Custom printf function
 * @format: Pointer to the format string
 * Return: Number of characters printed
 */
int _printf(const char *format, ...)
{
	int (*pfunc)(va_list, flags_t *);
	const char *p;
	va_list arguments;
	flags_t flags = {0, 0, 0};

	int count = 0;

	va_start(arguments, format);
	if (format == NULL || (format[0] == '%' && format[1] == '\0'))
		return -1;
	for (p = format; *p; p++)
	{
		if (*p == '%')
		{
			p++;
			if (*p == '%')
			{
				count += _putchar('%');
				continue;
			}
			while (get_flag(*p, &flags))
				p++;
			pfunc = get_print(*p);
			count += (pfunc ? pfunc(arguments, &flags) : _printf("%%%c", *p));
		}
		else
		{
			count += _putchar(*p);
		}
	}
	_putchar(-1);
	va_end(arguments);
	return count;
}
