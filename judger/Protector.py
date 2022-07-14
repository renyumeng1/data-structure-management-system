import ast
from judger.config import BANNED_IMPORT, BANNED_FUNC


class ProtectFroPython(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.banned = BANNED_IMPORT
        self.ban_func = BANNED_FUNC
        self._allow = True

    def visit_Import(self, node) -> None:
        for names in node.names:
            if names.name in self.banned:
                self._allow = False

    def visit_ImportFrom(self, node) -> None:
        for name in node.names:
            if name in self.banned:
                self._allow = False

    def visit_Assign(self, node) -> None:
        if isinstance(node.value, ast.Call):
            if node.value.func.id in self.ban_func:
                self._allow = False

    def visit_Call(self, node) -> None:
        if isinstance(node.func, ast.Name):
            if node.func.id in self.ban_func:
                self._allow = False

    def Is_safe(self) -> bool:
        return self._allow


if __name__ == "__main__":
    code_read = open('./test.py', "r", encoding="UTF-8")
    code = code_read.read()
    protect = ProtectFroPython()
    protect.visit(ast.parse(code))
    if not protect.Is_safe():
        print(False)
