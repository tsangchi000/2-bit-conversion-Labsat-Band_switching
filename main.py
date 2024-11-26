import numpy as np
import os
from tqdm import tqdm  # For better progress tracking


def swap_4bits(data):
    # Unpack all bits at once
    bits = np.unpackbits(data).reshape(-1, 8)
    # Swap first and last 4 bits for all bytes at once
    swapped = np.hstack((bits[:, 4:], bits[:, :4]))
    # Pack bits back to bytes
    return np.packbits(swapped.ravel())


def process_file(filename, output_filename="File_Converted.LS3W", chunk_size=1024 * 1024):
    # Get file size
    file_size = os.path.getsize(filename)
    print(f"Size of File is {file_size:,} bytes")

    # Process file in chunks
    with open(filename, "rb") as infile, open(output_filename, "wb") as outfile:
        # Create progress bar
        with tqdm(total=file_size, unit='B', unit_scale=True, desc="Processing") as pbar:
            while True:
                # Read chunk of data
                chunk = infile.read(chunk_size)
                if not chunk:
                    break

                # Convert chunk to numpy array
                data = np.frombuffer(chunk, dtype=np.uint8)

                # Process the chunk
                processed_data = swap_4bits(data)

                # Write processed chunk
                outfile.write(processed_data.tobytes())

                # Update progress bar
                pbar.update(len(chunk))

    print('Processing completed successfully')


if __name__ == "__main__":
    try:
        filename = input('Please input the name of file: ')
        process_file(filename)
    except Exception as e:
        print(f"Error occurred:", str(e))
