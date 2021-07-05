class HashTable:

    def __init__(self, table_size=100):
        # 引数でテーブルサイズを変更できる
        self.data = [[] for i in range(table_size)]
        self.n = table_size

    def get_hash(self, v):
        # オブジェクトのハッシュ値を計算する
        return hash(v) % self.n

    def search(self, key):
        # Keyを使って値を探す
        i = self.get_hash(key)
        for j, v in enumerate(self.data[i]):
            if v[0] == key:
                return (i, j)
        return (i, -1)

    def set(self, key, value):
        # データを格納すべき場所を探す
        i, j = self.search(key)
        if j != -1:
            self.data[i][j][1] = value
        else:
            # 新たなデータとして付け加える
            self.data[i].append([key, value])

    def get(self, key):
        i, j = self.search(key)
        if j != -1:
            return self.data[i][j][1]
        return KeyError(f'{key} was not found in this Hashtable!')


my_hash_table = HashTable()
my_hash_table.set('taro', 10)
my_hash_table.get('taro')
