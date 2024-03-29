# challenges/compiler.py

import subprocess
from pathlib import Path

class CCodeCompiler:
    def __init__(self):
        # Specify full paths for file handling using Path
        current_file = Path(__file__).resolve()
        self.temp_code_path = current_file.parent / 'temp_code.c'
        self.executable_path = current_file.parent / 'temp_code'

    def compile_with_test_case(self, code, input_data):
        try:
            # print("=== Code to be compiled ===")
            # print(code)

            # Write code to a temporary file
            with open(self.temp_code_path, 'w', encoding='utf-8') as file:
                file.write(code)

            # Compile the code using the local GCC compiler
            # compilation_result = subprocess.run(['gcc', str(self.temp_code_path), '-o', str(self.executable_path)],
            #                                     capture_output=True,
                                                # text=True)
                
            # print(f"Compilation Command: {' '.join(['gcc', '-mconsole', str(self.temp_code_path), '-o', str(self.executable_path)])}")


            compilation_result = subprocess.run(['gcc', '-mconsole', str(self.temp_code_path), '-o', str(self.executable_path)],
                                    capture_output=True,
                                    text=True)


            if compilation_result.returncode != 0:
                # Compilation failed, print errors
                print("=== Compilation Errors ===")
                print(compilation_result.stderr)
                return "Compilation Error", compilation_result.stderr

            # Execute the compiled code against the test case
            result = subprocess.run(
                [str(self.executable_path)],
                input=f"{input_data}\n",  # No need to encode here
                capture_output=True,
                text=True
            )

            return result.stdout, result.stderr
        except Exception as e:
            print(f"Exception during execution: {e}")
            return str(e)
        finally:
            # Clean up: remove temporary files
            self.temp_code_path.unlink(missing_ok=True)
            self.executable_path.unlink(missing_ok=True)