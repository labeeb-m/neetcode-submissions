class Solution:
    def decodeString(self, s: str) -> str:
        string = ""
        stack = []
        # "xyz3[at2[b]4[n]]c"
        # # keep adding to str until a number or [ found
        # [xyz,3,at,2,b]
        "xyz30[a2[b]]c"
        # ["xyz",3,"a","bb"] "" ["b"]

        c = 0
        
        while c < len(s):
            if s[c] == "[":
                continue

            elif s[c].isdigit():
                if string:
                    stack.append(string)
                    string = ""
                while c < len(s) and s[c].isdigit():
                    string += s[c]
                    c += 1
                stack.append(string)
                string = ""

            elif s[c] == "]":
                if string:
                    stack.append(string)
                    string = ""
                arr = []
                while stack and not stack[-1].isdigit():
                    st = stack.pop()
                    arr.append(st)
                arr = arr[::-1]
                res = "".join(arr)
                res *= int(stack.pop())
                stack.append(res)

            else:
                string += s[c]
            
            c += 1

        return "".join(stack) + string

