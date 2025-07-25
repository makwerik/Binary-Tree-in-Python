from typing import Optional, List


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

    def search(self, value: int) -> bool:
        """Метод для поиска значения в дереве"""
        # Если корень пуст, возвращаем False
        if self.root is None:
            return False
        else:
            return self._search_recursive(current_node=self.root, value=value)

    def _search_recursive(self, current_node: Node, value: int) -> bool:
        """Рекурсивный метод поиска значения"""

        # Если значение текущего узла равно искомому
        if current_node.value == value:
            return True
        # Если текущее значение < значения в узле - идём влево
        elif value < current_node.value:
            # Если узла нет, возвращаем False
            if current_node.left is None:
                return False
            # Иначе ищем дальше
            else:
                return self._search_recursive(current_node=current_node.left, value=value)
        else:
            # Иначе идём вправо
            if current_node.right is None:
                return False
            else:
                # return обязателен, чтобы результат возвращался из глубины наверх, иначе он потеряется
                return self._search_recursive(current_node=current_node.right, value=value)

    def in_order(self) -> List[int]:
        """Метод обхода дерева"""
        # Создаём пустой список
        result: List[int] = []
        # Передаю пустой список в рекурсивный метод
        # Так как списки - изменяемые объекты, то в рекурсии он наполнится нужными значениями
        # (потому что этот список не копируется, а указывает на одну область памяти)
        self._in_order_recursive(current_node=self.root, result=result)
        return result


    def _in_order_recursive(self, current_node: Node, result: List[int]) -> None:
        """
        Рекурсивный метод для обхода дерева In-order (лево-корень-право)

        :param current_node: Текущий узел.

        :param result: Список чисел

        :return:
        """

        # Если узел пустой
        if current_node is None:
            return None

        # Обходим левое поддерево
        if current_node.left:
            # return не использую, чтобы пройти все ветки
            self._in_order_recursive(current_node=current_node.left, result=result)

        # Добавляем значение
        result.append(current_node.value)

        # Обходим правое поддерево
        if current_node.right:
            self._in_order_recursive(current_node=current_node.right, result=result)



if __name__ == '__main__':
    tree = Tree()
    tree.insert(value=15)
    tree.insert(value=13)
    tree.insert(value=20)
    print(tree.in_order())