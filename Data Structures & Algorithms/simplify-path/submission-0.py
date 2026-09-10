class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        string = ""
        path += "/"

        for c in path:
            if c == "/":
                if string == ".." and stack:
                        stack.pop()
                elif string and string != "." and string != "..":
                        stack.append(string)
                string = ""
            else:
                string += c

        return "/" + "/".join(stack)
