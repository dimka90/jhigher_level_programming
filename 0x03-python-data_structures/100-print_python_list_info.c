#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long int size = PyList_Size(p);
	
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))
->tp_name);
	}
}
