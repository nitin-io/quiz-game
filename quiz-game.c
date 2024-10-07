#include <Python.h>

int main(int argc, char *argv[]) {
    // Initialize the Python interpreter
    Py_Initialize();

    // Define the name of the Python script to be executed
    const char* script = "quiz-game.py";

    // Open the Python file
    FILE* fp = fopen(script, "r");

    if (fp != NULL) {
        // Run the Python script
        PyRun_SimpleFile(fp, script);
        fclose(fp);
    } else {
        printf("Error: Could not open file %s\n", script);
    }

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
