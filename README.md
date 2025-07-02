# 📝 LeetCode Solutions

<!-- right-floating LeetCode card -->
<img src="https://leetcard.jacoblin.cool/TheDarkLordOfTheReptils?theme=dark" alt="LeetCode Stats" width="460" align="right"/>

### Welcome!

This repository contains my personal solutions to  
[LeetCode](https://leetcode.com) problems.

The problems are organized by problem number and title, with clean,  
readable solutions in Python and sometimes other languages.

<br clear="right"/>

---

## 📂 Repository Structure

```
leetcode-solutions/
├── 0001-two-sum/
│   ├── solution.py
│   └── README.md
├── 0002-add-two-numbers/
│   ├── solution.py
│   └── README.md
└── ...
```

---

## 🛠️ Automation & Scripts

This repository is maintained with the help of custom Python scripts:

- **Folder Generation:**  
  Use [`scripts/create_leetcode_folder.py`](./scripts/create_leetcode_folder.py) to automatically generate a new problem folder with the correct naming, solution template, and README for each LeetCode problem.

- **Dynamic Indexing:**  
  The [`scripts/generate_index.py`](./scripts/generate_index.py) script scans all problems and updates the [README index](./README.md) with an up-to-date table of solved problems and available languages.  
  This script is run automatically via [GitHub Actions](./.github/workflows/update-readme.yml) on every push that changes solutions or documentation.

### 🚀 Creating a New Problem Folder

To add a new problem folder automatically:

```bash
  python scripts/create_leetcode_folder.py leetcode-problem-url
```

---

## 🏷️ Difficulty Legend

- **Easy** 🟢
- **Medium** 🟡
- **Hard** 🔴

---

## 📋 Index

<details>
  <summary>Click to expand problem index</summary>

| Number | Problem | Difficulty | Python |
|--------|--------|--------|--------|
| 0007 | [Reverse Integer](./problems/0007-reverse-integer/) | 🟡 | ✔️ |
| 0008 | [String To Integer (Atoi)](./problems/0008-string-to-integer-(atoi)/) | 🟡 | ✔️ |
| 0009 | [Palindrome Number](./problems/0009-palindrome-number/) | 🟢 | ✔️ |
| 0012 | [Integer To Roman](./problems/0012-integer-to-roman/) | 🟡 | ✔️ |
| 0013 | [Roman To Integer](./problems/0013-roman-to-integer/) | 🟢 | ✔️ |
| 0014 | [Longest Common Prefix](./problems/0014-longest-common-prefix/) | 🟢 | ✔️ |
| 0020 | [Valid Parentheses](./problems/0020-valid-parentheses/) | 🟢 | ✔️ |
| 0021 | [Merge Two Sorted Lists](./problems/0021-merge-two-sorted-lists/) | 🟢 | ✔️ |
| 0028 | [Find The Index Of The First Occurrence In A String](./problems/0028-find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 | ✔️ |
| 0035 | [Search Insert Position](./problems/0035-search-insert-position/) | 🟢 | ✔️ |
| 0058 | [Length Of Last Word](./problems/0058-length-of-last-word/) | 🟢 | ✔️ |
| 0066 | [Plus One](./problems/0066-plus-one/) | 🟢 | ✔️ |
| 0069 | [Sqrt(X)](./problems/0069-sqrt(x)/) | 🟢 | ✔️ |
| 0070 | [Climbing Stairs](./problems/0070-climbing-stairs/) | 🟢 | ✔️ |
| 0205 | [Isomorphic Strings](./problems/0205-isomorphic-strings/) | 🟢 | ✔️ |
| 0713 | [Subarray Product Less Than K](./problems/0713-subarray-product-less-than-k/) | 🟡 | ✔️ |
| 1544 | [Make The String Great](./problems/1544-make-the-string-great/) | 🟢 | ✔️ |

</details>

---

## 📄 License

This repository is licensed under the [MIT License](./LICENSE).

It is for educational and reference purposes only.
