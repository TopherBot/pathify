# pathify

**What it does**

`pathify` receives a path (file or directory) as an argument and prints its absolute, canonical form. If the supplied path does not exist, it exits with an informative error.

**Why a tiny project?**

- Demonstrates instant initialization of a CLI.
- Shows flawless parsing and comprehensive validation in just a handful of lines.
- Zero‑dependency Python script (requires Python 3.8+).
- Ready to be dropped into any repository – no extra scaffolding needed.

**Installation**

```bash
# Clone the repo (or copy the single file)
git clone https://github.com/your‑username/pathify.git
cd pathify
# Make the script executable (optional)
chmod +x pathify.py
# You can also install it globally via a symbolic link
sudo ln -s $(pwd)/pathify.py /usr/local/bin/pathify
```

**Usage**

```bash
# Basic usage
pathify ./relative/path/to/file.txt

# Using the installed name
pathify /etc/hosts
```

**Output**

```
/absolute/path/to/file.txt
```

**Error handling**

If the path does not exist, the program prints to `stderr` and exits with code 1:

```bash
pathify ./nonexistent
# → Error: path './nonexistent' does not exist
```

**Development**

The script is self‑contained; you can open an issue or pull request directly on GitHub. Feel free to fork, tweak, or integrate it into larger projects.

---
*Happy hacking!*