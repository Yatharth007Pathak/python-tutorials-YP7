name = input("Enter your name: ")
print("Hello " + name + "!")
print("Hello", name, "!")
print(f"Hello {name}!")

# Input from user

"""
Assemblers, compilers, and interpreters are tools used to translate and execute programs, 
but they operate in different ways and are used for different types of programming languages. 
Here are the main differences between them:

Assembler
Purpose: Translates assembly language code into machine code.
Input Language: Assembly language (low-level, close to machine code).
Output: Machine code (binary instructions that can be directly executed by the CPU).
Process: One-to-one translation of mnemonics to machine instructions.
Usage: Primarily used in system programming, embedded systems, and situations requiring direct hardware manipulation.

Compiler
Purpose: Translates high-level programming language code into machine code or intermediate code.
Input Language: High-level programming languages (e.g., C, C++, Java).
Output: Machine code, bytecode, or intermediate code (e.g., object files, executable files).
Process: Multiple stages, including lexical analysis, syntax analysis, semantic analysis, optimization, and code generation.
Usage: Used in general-purpose programming, application development, and situations requiring optimized and high-performance code.
Execution: Produces a separate executable file that can be run independently of the source code.

Interpreter
Purpose: Executes high-level programming language code directly without translating it into machine code beforehand.
Input Language: High-level programming languages (e.g., Python, JavaScript, Ruby).
Output: None (executes code directly).
Process: Reads and executes code line by line or statement by statement.
Usage: Used in scripting, rapid prototyping, and situations requiring immediate feedback and dynamic execution.
Execution: Executes the source code directly, without producing a separate executable file.

Key Differences

Translation:
Assembler: Converts assembly language to machine code.
Compiler: Converts high-level language to machine code or intermediate code.
Interpreter: Executes high-level language code directly without prior conversion to machine code.

Speed:
Assembler: Produces efficient machine code, resulting in fast execution.
Compiler: Produces optimized machine code for fast execution, but the compilation process itself can take time.
Interpreter: Slower execution compared to compiled code since it translates code on the fly.

Error Handling:
Assembler: Detects errors at assembly time, which are usually low-level hardware-related errors.
Compiler: Detects syntax and semantic errors before execution, providing a chance to correct them.
Interpreter: Detects errors during execution, making it easier to debug but potentially interrupting program flow.

Usage Context:
Assembler: Low-level programming requiring direct hardware control.
Compiler: General-purpose programming requiring efficient, high-performance executables.
Interpreter: Scripting, rapid development, and environments where immediate execution is beneficial.

In summary, assemblers are used for low-level programming, compilers for high-performance and optimized code, 
and interpreters for flexibility and ease of development.
"""