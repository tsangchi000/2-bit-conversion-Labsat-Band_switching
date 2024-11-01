import os
import time


def switch_bits(input_file, output_file):
    try:
        total_size = os.path.getsize(input_file)
        processed_size = 0
        start_time = time.time()

        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            while True:
                # Read 1 byte at a time
                byte = infile.read(1)
                if not byte:
                    break

                # Convert byte to integer
                value = ord(byte)

                # Switch bits
                new_value = ((value & 0b11001100) >> 2) | ((value & 0b00110011) << 2)

                # Write the new byte
                outfile.write(bytes([new_value]))

                # Update progress
                processed_size += 1
                if processed_size % 1024 == 0:  # Update every 1KB
                    percent_done = (processed_size / total_size) * 100
                    elapsed_time = time.time() - start_time
                    speed = processed_size / elapsed_time if elapsed_time > 0 else 0
                    estimated_time = (total_size - processed_size) / speed if speed > 0 else 0

                    print(f"\rProgress: {percent_done:.2f}% | "
                          f"Speed: {speed:.2f} B/s | "
                          f"Estimated time remaining: {estimated_time:.2f} seconds",
                          end='', flush=True)

        print("\nProcessing complete!")
        print(f"Processed {input_file} and saved result to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to access '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_valid_filename(prompt):
    while True:
        filename = input(prompt)
        if os.path.isfile(filename):
            return filename
        else:
            print(f"The file '{filename}' does not exist. Please enter a valid filename.")


def main():
    print("Bit Switcher Program")
    print("This program switches bits of a binary file every two bits.")

    input_file = get_valid_filename("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    switch_bits(input_file, output_file)


if __name__ == "__main__":
    main()