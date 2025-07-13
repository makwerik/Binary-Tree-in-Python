# Binary Tree in Python 🌳

Простой проект по изучению структуры данных "бинарное дерево" на языке Python.  
Реализована базовая функциональность: вставка узлов и поиск значений.

## 📦 Содержимое

- `Node` — класс для представления узла дерева
- `Tree` — основной класс бинарного дерева
- `insert(value)` — метод для вставки значения в дерево
- `search(value)` — метод для поиска значения в дереве
- `in_order()` - метод для обхода дерева In-order (лево-корень-право)

## 🔧 Использование

```python
from binary_tree import Tree  

tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))    # True
print(tree.search(99))   # False
print(tree.in_order())
