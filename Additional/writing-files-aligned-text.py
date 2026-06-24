def write_aligned_text(filename):
    # Sample data: list of tuples (Name, Age, Country)
    data = [
        ("Alice", 30, "Australia"),
        ("Bob", 25, "Canada"),
        ("Charlie", 35, "United States"),
        ("Diana", 28, "UK")
    ]

    try:
        with open(filename, "w", encoding="utf-8") as file:
            # Write header with alignment
            file.write(f"{'Name':<15}{'Age':^10}{'Country':>20}\n")
            file.write("-" * 45 + "\n")

            # Write each row with alignment
            for name, age, country in data:
                file.write(f"{name:<15}{age:^10}{country:>20}\n")

        print(f"Data successfully written to '{filename}' with alignment.")

    except OSError as e:
        print(f"File error: {e}")

# Run the function
write_aligned_text("aligned_output.txt")