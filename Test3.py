import subprocess

def run_command(command):
        """Runs a command in PowerShell or Command Prompt and returns the
  output."""
        output = subprocess.run(command, shell=True, capture_output=True,
  text=True)
        return output.stdout

if __name__ == "__main__":
        command = "dir"
        output = run_command(command)
        print(output)