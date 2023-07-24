import subprocess

def run_powershell_command(command):
    if command == 'none':
        return 0
    else:
        command = "bard-cli " + '"'+command +'"'
        print(command)
        try:
            # Run the PowerShell command
            resultsub = subprocess.run(["powershell", command], capture_output=True, text=True)

            # Check the return code
            if resultsub.returncode == 0:
                # Display the output
                return resultsub.stdout
                # print("Output:", result.stdout)
            else:
                # Display the error
                return resultsub.stderr
                # print("Error:", result.stderr)
        except Exception as e:
            print("An error occurred:", str(e))

# # Example usage
# input_data = input("Enter data:")
# # command = "bard-cli " + '"'+input_data +'"'

# print(run_powershell_command(input_data))
