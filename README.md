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
| 0001 | [Two Sum](./problems/0001-two-sum/) | 🟢 | ✔️ |
| 0002 | [Add Two Numbers](./problems/0002-add-two-numbers/) | 🟡 | ✔️ |
| 0003 | [Longest Substring Without Repeating Characters](./problems/0003-longest-substring-without-repeating-characters/) | 🟡 | ✔️ |
| 0006 | [Zigzag Conversion](./problems/0006-zigzag-conversion/) | 🟡 | ✔️ |
| 0007 | [Reverse Integer](./problems/0007-reverse-integer/) | 🟡 | ✔️ |
| 0008 | [String To Integer (Atoi)](./problems/0008-string-to-integer-(atoi)/) | 🟡 | ✔️ |
| 0009 | [Palindrome Number](./problems/0009-palindrome-number/) | 🟢 | ✔️ |
| 0012 | [Integer To Roman](./problems/0012-integer-to-roman/) | 🟡 | ✔️ |
| 0013 | [Roman To Integer](./problems/0013-roman-to-integer/) | 🟢 | ✔️ |
| 0014 | [Longest Common Prefix](./problems/0014-longest-common-prefix/) | 🟢 | ✔️ |
| 0016 | [3Sum Closest](./problems/0016-3sum-closest/) | 🟡 | ✔️ |
| 0020 | [Valid Parentheses](./problems/0020-valid-parentheses/) | 🟢 | ✔️ |
| 0021 | [Merge Two Sorted Lists](./problems/0021-merge-two-sorted-lists/) | 🟢 | ✔️ |
| 0028 | [Find The Index Of The First Occurrence In A String](./problems/0028-find-the-index-of-the-first-occurrence-in-a-string/) | 🟢 | ✔️ |
| 0034 | [Find First And Last Position Of Element In Sorted Array](./problems/0034-find-first-and-last-position-of-element-in-sorted-array/) | 🟡 | ✔️ |
| 0035 | [Search Insert Position](./problems/0035-search-insert-position/) | 🟢 | ✔️ |
| 0058 | [Length Of Last Word](./problems/0058-length-of-last-word/) | 🟢 | ✔️ |
| 0066 | [Plus One](./problems/0066-plus-one/) | 🟢 | ✔️ |
| 0067 | [Add Binary](./problems/0067-add-binary/) | 🟢 | ✔️ |
| 0069 | [Sqrt(X)](./problems/0069-sqrt(x)/) | 🟢 | ✔️ |
| 0070 | [Climbing Stairs](./problems/0070-climbing-stairs/) | 🟢 | ✔️ |
| 0083 | [Remove Duplicates From Sorted List](./problems/0083-remove-duplicates-from-sorted-list/) | 🟢 | ✔️ |
| 0088 | [Merge Sorted Array](./problems/0088-merge-sorted-array/) | 🟢 | ✔️ |
| 0100 | [Same Tree](./problems/0100-same-tree/) | 🟢 | ✔️ |
| 0104 | [Maximum Depth Of Binary Tree](./problems/0104-maximum-depth-of-binary-tree/) | 🟢 | ✔️ |
| 0112 | [Path Sum](./problems/0112-path-sum/) | 🟢 | ✔️ |
| 0118 | [Pascal'S Triangle](./problems/0118-pascal's-triangle/) | 🟢 | ✔️ |
| 0121 | [Best Time To Buy And Sell Stock](./problems/0121-best-time-to-buy-and-sell-stock/) | 🟢 | ✔️ |
| 0125 | [Valid Palindrome](./problems/0125-valid-palindrome/) | 🟢 | ✔️ |
| 0148 | [Sort List](./problems/0148-sort-list/) | 🟡 | ✔️ |
| 0168 | [Excel Sheet Column Title](./problems/0168-excel-sheet-column-title/) | 🟢 | ✔️ |
| 0169 | [Majority Element](./problems/0169-majority-element/) | 🟢 | ✔️ |
| 0171 | [Excel Sheet Column Number](./problems/0171-excel-sheet-column-number/) | 🟢 | ✔️ |
| 0202 | [Happy Number](./problems/0202-happy-number/) | 🟢 | ✔️ |
| 0203 | [Remove Linked List Elements](./problems/0203-remove-linked-list-elements/) | 🟢 | ✔️ |
| 0205 | [Isomorphic Strings](./problems/0205-isomorphic-strings/) | 🟢 | ✔️ |
| 0231 | [Power Of Two](./problems/0231-power-of-two/) | 🟢 | ✔️ |
| 0283 | [Move Zeroes](./problems/0283-move-zeroes/) | 🟢 | ✔️ |
| 0438 | [Find All Anagrams In A String](./problems/0438-find-all-anagrams-in-a-string/) | 🟡 | ✔️ |
| 0713 | [Subarray Product Less Than K](./problems/0713-subarray-product-less-than-k/) | 🟡 | ✔️ |
| 0777 | [Swap Adjacent In Lr String](./problems/0777-swap-adjacent-in-lr-string/) | 🟡 | ✔️ |
| 1493 | [Longest Subarray Of 1'S After Deleting One Element](./problems/1493-longest-subarray-of-1's-after-deleting-one-element/) | 🟡 | ✔️ |
| 1544 | [Make The String Great](./problems/1544-make-the-string-great/) | 🟢 | ✔️ |

</details>

---

## 📄 License

This repository is licensed under the [MIT License](./LICENSE).

It is for educational and reference purposes only.
