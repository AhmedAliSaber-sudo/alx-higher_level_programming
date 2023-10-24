#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - gives data of the PyFloatObject
 *
 * @pyobj: the PyObject
 */

void print_python_float(PyObject *pyobj)
{
	double data = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (PyFloat_CheckExact(pyobj) == NULL)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	data = ((PyFloatObject *)pyobj)->ob_fval;
	str = PyOS_double_to_string(data, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 *
 * @pyobj: the PyObject
 */

void print_python_bytes(PyObject *pyobj)
{
	Py_ssize_t size = 0;
    i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (PyBytes_CheckExact(pyobj) == NULL)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(pyobj);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(pyobj)), (((PyBytesObject *)(pyobj))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - gives data of the PyListObject
 *
 * @pyobj: the PyObject
 */

void print_python_list(PyObject *pyobj)
{
	Py_ssize_t size = 0;
	PyObject *element;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(pyobj))
	{
		size = PyList_GET_SIZE(pyobj);

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)pyobj)->allocated);

		while (i < size)
		{
			element = PyList_GET_ITEM(pyobj, i);
			printf("Element %d: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			else if (PyFloat_Check(element))
				print_python_float(element);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}