import string
import subprocess

# https://ctflearn.com/challenge/1003
# Reversing challenge

def main():
    kernel_prefix = "CTFlearn{"
    kernel_suffix = "}"
    kernel = "AAAAAAAAA"    # kernel initialized to 9 A's
                            # ch in the inner loop acts as the 10th
                            # kernel char

    kernel_found = ""

    # iterate over all 10 kernel chars
    for i in range(10):
        # iterate over all printable chars
        for ch in string.printable:
            arg = kernel_prefix + kernel_found + ch + kernel[i:] + kernel_suffix
            output = subprocess.run(["./Rzeszow", arg, "-v"], capture_output=True)
            output_str = output.stdout.decode("utf-8")
            if output_str.count("Woow") > i:
                kernel_found += ch
                break

    print(f"FLAG: {kernel_prefix + kernel_found + kernel_suffix}")

if __name__ == "__main__":
    main()
