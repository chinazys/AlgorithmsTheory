import time

class BucketSorter:
    def __init__(self):
        self.array = None
        self.bucket_quantity = None

    def reinit(self, array, bucket_quantity):
        self.array = array
        self.bucket_quantity = bucket_quantity
    
    def run(self):
        if self.array is None or self.bucket_quantity is None:
            raise Exception("Sorter is not initted")

        self.time = time.time_ns()
        self.operations = 0

        buckets = []
        for i in range(self.bucket_quantity):
            buckets.append([])
        
        for el in self.array:
            index = int(self.bucket_quantity * el / max(self.array)) 
            buckets[min(index, len(buckets) - 1)].append(el)
            
        for i in range(self.bucket_quantity):
            buckets[i] = sorted(buckets[i])

        self.operations = 0
        for i in range(self.bucket_quantity):
            for j in range(len(buckets[i])):
                self.array[self.operations] = buckets[i][j]
                self.operations += 1

        self.time = (time.time_ns() - self.time) / 1e9
        self.operations += self.bucket_quantity + 2 * len(self.array)
