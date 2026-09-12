class Solution:
    def decodeString(self, s: str) -> str:
        # string = ""
        # stack = []
        # c = 0
        
        # while c < len(s):
        #     if s[c] == "[":
        #         continue

        #     elif s[c].isdigit():
        #         if string:
        #             stack.append(string)
        #             string = ""
        #         while c < len(s) and s[c].isdigit():
        #             string += s[c]
        #             c += 1
        #         stack.append(string)
        #         string = ""

        #     elif s[c] == "]":
        #         if string:
        #             stack.append(string)
        #             string = ""

        #     else:
        #         string += s[c]
            
        #     c += 1

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(string * int(num))

        return "".join(stack)

