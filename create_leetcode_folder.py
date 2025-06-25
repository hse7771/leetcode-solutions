import os
import sys

import requests

README_TEMPLATE: str = """
# 🧠 {title}

> **Difficulty:** {circle} **{difficulty}**\\
> 📎 [View on LeetCode]({link})

---

## 📝 Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

## 🔍 Approach
<!-- Describe your approach to solving the problem. -->

## 📊 Complexity

- **Time Complexity:**
<!-- e.g. $$O(n)$$ -->

- **Space Complexity:**
<!-- e.g. $$O(n)$$ -->

---

## 🧩 Code

```python3 []
class Solution:
    def ...

"""


def fetch_problem_metadata(url: str) -> tuple[str, str, str]:
    """
    Fetches problem title, difficulty, and number from the LeetCode GraphQL API.
    Returns: (slug, difficulty, number)
    """
    # Extract slug from URL
    if not url.startswith("https://leetcode.com/problems/"):
        raise ValueError("URL must be a valid LeetCode problem URL.")
    slug = url.strip("/").split("/")[-1]  # e.g., "two-sum"

    # Prepare GraphQL query
    graphql_url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        difficulty
      }
    }
    """
    variables = {"titleSlug": slug}
    response = requests.post(graphql_url, json={"query": query, "variables": variables})

    if response.status_code != 200:
        raise Exception(f"GraphQL query failed with status code {response.status_code}")

    data = response.json()
    question_data = data.get("data", {}).get("question")
    if not question_data:
        raise Exception("Problem data not found. Check the problem slug or the API response.")

    title = question_data["title"]                    # "Two Sum"
    number = question_data["questionFrontendId"]      # "1"
    difficulty = question_data["difficulty"].lower()  # "easy"
    slug = title.lower().replace(" ", "-")            # "two-sum"

    return slug, difficulty, number


def create_problem_folder(name: str, difficulty: str, number: str, link: str) -> None:
    circle = {'easy': '🟢', 'medium': '🟡', 'hard': '🔴'}[difficulty.lower()]
    folder = f"{number.zfill(4)}-{name}"
    os.makedirs(folder, exist_ok=True)

    # solution.py
    with open(os.path.join(folder, "solution.py"), "w") as f:
        f.write(f"# Solution for {name.replace('-', ' ').title()}\n")

    readme_content = README_TEMPLATE.format(
        title=name.replace('-', ' ').title(),
        circle=circle,
        difficulty=difficulty.capitalize(),
        link=link
    )
    # README.md
    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Created `{folder}/` with README.md and solution.py.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_leetcode_folder.py <leetcode-url>")
        sys.exit(1)

    leetcode_url = sys.argv[1]
    try:
        problem_name, problem_difficulty, problem_number = fetch_problem_metadata(leetcode_url)
        create_problem_folder(problem_name, problem_difficulty, problem_number, leetcode_url)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
