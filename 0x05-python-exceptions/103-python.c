#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    // Additional information retrieval as needed...
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %zd\n", size);

    printf("[*] First 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02x ", (unsigned char)((char *)(void *)p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = ((PyFloatObject *)p)->ob_fval;
    printf("[*] Python float info\n");
    printf("[*] Value: %f\n", value);
}
