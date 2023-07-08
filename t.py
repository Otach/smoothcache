from smoothcache import Cache

Cache.set("test", "testing")
Cache.set("test", "testing two")
res = Cache.get("test")

if res is None:
    print("Cache Miss.")
else:
    print(res.value)
