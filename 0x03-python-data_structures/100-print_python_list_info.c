#include "Python.h"

/**
 * print_python_list_info - gives data of the PyListObject.
 *
 * @p: PyObject.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = 0, allocate, index;

	size = PyList_Size(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	while (index < size)
	{
		printf("Element %ld: %s\n",
		       index,
		       (PY_TYPE(PyList_GetItem(p, index)))->tp_name);
	}	
}
