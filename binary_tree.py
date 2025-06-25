
from typing import Optional


class Node:
    """Узел дерева"""
    def __init__(self, value: int):
        """
        :param value: Значение, которое хранит узел.
        """
        self.value = value
        # Ссылки на узлы, если такие имеются
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Tree:
    """Дерево-деревушко"""
    def __init__(self):
        # Корень дерева (изначально пуст)
        self.root: Optional[Node] = None

    def _insert_recursive(self, current_node: Node, value: int) -> None:
        """
        Рекурсивный метод класса, для вставки значения в правильное место.
        :param current_node: Текущий узел.
        :param value: Значение.
        """

        # Если значение меньше текущего - иду влево
        if value < current_node.value:
            # Если левый узел пуст, устанавливаем туда значение
            if current_node.left is None:
                current_node.left = Node(value=value)
            # Если не пуст, то вызываем метод рекурсивно и продолжаем искать меssтечко в левом или правом узле
            # (в зависимости от значения)
            else:
                # Передаём левый узел и значение
                self._insert_recursive(current_node=current_node.left, value=value)
        # Если значение больше или равно - иду вправо
        else:
            # Такая же система, как и с левым узлом
            if current_node.right is None:
                current_node.right = Node(value=value)
            else:
                self._insert_recursive(current_node=current_node.right, value=value)

    def insert(self, value: int) -> None:
        """
        Метод для вставки значений в дерево.

        :param value: Значение.
        """

        # Если корень дерева пуст, устанавливаем значение
        if self.root is None:
            self.root = Node(value=value)
        # Иначе вызываем рекурсивный метод, передавая туда корень
        # (которым является текущим узлом)
        else:
            self._insert_recursive(current_node=self.root, value=value)
