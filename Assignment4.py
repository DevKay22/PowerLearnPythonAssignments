def process_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = content.upper()

        # Show a preview (first 300 characters only to avoid overload)
        print("\n Preview of modified content:\n")
        print(modified_content[:300] + ("..." if len(modified_content) > 300 else ""))
        print("\n-----------------------------------")
        
        # Ask for confirmation before writing
        choice = input("Do you want to save this modified content? (y/n): ").strip().lower()

        if choice == 'y':
            # Allow user to specify output filename
            output_file = input("Enter the name for the new file (e.g., output.txt): ").strip()

            # Ensure they don't leave it blank
            if not output_file:
                print(" No filename provided. Operation cancelled.")
                return
            
            with open(output_file, 'w') as file:
                file.write(modified_content)
            print(f" File processed successfully! Modified content saved in '{output_file}'.")
        else:
            print(" Operation cancelled. No file was saved.")

    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
process_file()
