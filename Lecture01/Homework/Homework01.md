## 🛠️ **Project Title: “My Favorite Things” Git Practice Project**

### 🎯 Objective:

Learn and practice basic Git commands by creating a small project that lists your favorite things (like favorite food, color, movie, etc.) and track changes using Git.

---

## 📄 Project Instructions (for Students)

### 🔹 Step 1: Create a New Project Folder

```bash
mkdir my-favorite-things
cd my-favorite-things
```

### 🔹 Step 2: Initialize a Git Repository

```bash
git init
```

### 🔹 Step 3: Configure Git (if you haven’t yet)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 🔹 Step 4: Create a File

```bash
echo "My Favorite Things" > favorites.txt
```

### 🔹 Step 5: Check Git Status

```bash
git status
```

### 🔹 Step 6: Add the File to Staging

```bash
git add favorites.txt
```

### 🔹 Step 7: Commit the File

```bash
git commit -m "Add favorites.txt with title"
```

### 🔹 Step 8: Add More Content

```bash
echo "Favorite Color: Blue" >> favorites.txt
echo "Favorite Food: Pizza" >> favorites.txt
```

### 🔹 Step 9: View Changes

```bash
git status
git diff
```

### 🔹 Step 10: Add and Commit Again

```bash
git add favorites.txt
git commit -m "Add favorite color and food"
```

### 🔹 Step 11: Make One More Change

```bash
echo "Favorite Movie: The Lion King" >> favorites.txt
```

### 🔹 Step 12: Final Commit

```bash
git add favorites.txt
git commit -m "Add favorite movie"
```

### 🔹 Step 13: View Commit History

```bash
git log --oneline
```

---

## ✅ **Expected Final File Content: `favorites.txt`**

```txt
My Favorite Things
Favorite Color: Blue
Favorite Food: Pizza
Favorite Movie: The Lion King
```