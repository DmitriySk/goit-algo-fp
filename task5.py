from collections import deque
from task4 import draw_tree, build_heap

def generate_colors(n):
    dark = (13, 27, 42)
    light = (200, 230, 255)
    colors = []
    for i in range(n):
        t = i / max(n - 1, 1)
        r = int(dark[0] + t * (light[0] - dark[0]))
        g = int(dark[1] + t * (light[1] - dark[1]))
        b = int(dark[2] + t * (light[2] - dark[2]))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs_tree(root):
    order, visited, stack = [], set(), [root]
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order


def bfs_tree(root):
    order, visited, queue = [], set(), deque([root])
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order


def collect_all_nodes(root):
    nodes = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            nodes.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return nodes


def visualize_traversal(root, traversal_fn, title):
    for node in collect_all_nodes(root):
        node.color = "#AAAAAA"

    visited = traversal_fn(root)
    palette = generate_colors(len(visited))
    print(palette)
    for i, node in enumerate(visited):
        node.color = palette[i]

    draw_tree(root, title)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    root_dfs = build_heap(nums)
    visualize_traversal(
        root_dfs,
        dfs_tree,
        "Обхід у глибину (DFS) — темний = перший відвіданий, світлий = останній",
    )

    root_bfs = build_heap(nums)
    visualize_traversal(
        root_bfs,
        bfs_tree,
        "Обхід у ширину (BFS) — темний = перший відвіданий, світлий = останній",
    )
