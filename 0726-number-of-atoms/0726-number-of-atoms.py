class Solution:
    def countOfAtoms(self, f: str) -> str:
        count = defaultdict(int)
        def helper(i, j, M):
            c = i
            while c < j:
                if f[c].isupper():  # case of a aton name
                    name = f[c]
                    c += 1
                    while c < j and f[c].islower(): # go to find all of the name
                        name += f[c]
                        c += 1
                    # test if this atom has a multiplicity
                    num = 1
                    if c < j and f[c].isdigit():
                        num = f[c]
                        c += 1
                        while c < j and f[c].isdigit(): # go to find all of the miltiplicity
                            num += f[c]
                            c += 1
                    # now we have evry thing so its good let add it into our count
                    count[name] += M * int(num)
                elif f[c] == "(": # we have the case of the inside-formula
                    a = 1
                    c += 1
                    start = c
                    # go until the end of the inside-formula
                    while a:
                        if f[c] == "(":
                            a += 1
                        elif f[c] == ")":
                            a -= 1
                        c += 1
                    end = c - 1
                    # get the miltiplicity
                    num = 1
                    if c < j and f[c].isdigit():
                        num = f[c]
                        c += 1
                        while c < j and f[c].isdigit(): # go to find all of the miltiplicity
                            num += f[c]
                            c += 1
                    helper(start, end, M * int(num))

        helper(0, len(f), 1)
        count = {k : count[k] for k in sorted(count)}
        res = ""
        for k, v in count.items():
            res += k + (str(v) if v > 1 else "")
        return res
                    
                    