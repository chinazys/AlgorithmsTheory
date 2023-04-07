class ArrayUnion:
    def __init__(self, a):
        self.a = a

    def merge_sorted(self, b):
        b = sorted(b)

        res = [-1]
        a_ind = 0
        b_ind = 0

        while a_ind < len(self.a) or b_ind < len(b):
            if a_ind == len(self.a):
                if b[b_ind] != res[-1]: 
                    res.append(b[b_ind])
                b_ind += 1
                continue
            if b_ind == len(b):
                if self.a[a_ind] != res[-1]: 
                    res.append(self.a[a_ind])
                a_ind += 1
                continue

            if self.a[a_ind] <= b[b_ind]:
                if self.a[a_ind] != res[-1]: 
                    res.append(self.a[a_ind])
                a_ind += 1
            else:
                if b[b_ind] != res[-1]:
                    res.append(b[b_ind])
                b_ind += 1

        self.a = res[1:]