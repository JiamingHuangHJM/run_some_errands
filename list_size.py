import os
import sys

def get_total_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            filepath = os.path.join(root, f)
            # skip if it is a symbolic link
            if not os.path.islink(filepath):
                total_size += os.path.getsize(filepath)
    return total_size

def format_size(size):
    if size >= 1 << 30:
        return f"{size / (1 << 30):.2f} GB"
    elif size >= 1 << 20:
        return f"{size / (1 << 20):.2f} MB"
    elif size >= 1 << 10:
        return f"{size / (1 << 10):.2f} KB"
    elif size > 0:
        return f"{size} B"
    else:
        return "0 B"

def format_name(name):
    if len(name) > 40:
        return name[:30]
    else:
        return name

def list_sizes(directory):
    if not os.path.exists(directory):
        print("A wrong path is given!")
        return
    
    items = [(name, os.path.join(directory, name)) for name in os.listdir(directory)]
    sizes = []
    for name, path in items:
        if os.path.isdir(path):
            size = get_total_size(path)
        else:
            size = os.path.getsize(path)
        sizes.append((name, size))
    
    # Sort items by size in descending order
    sizes.sort(key=lambda item: item[1], reverse=True)
    
    # Print formatted output
    for name, size in sizes:
        formatted_name = format_name(name).ljust(55)
        print(f"{formatted_name} {format_size(size).rjust(10)}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    list_sizes(path)

