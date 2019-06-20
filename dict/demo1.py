import getpass
import hashlib

pwd = getpass.getpass("password:")
print(pwd)

#hash对象
# hash = hashlib.md5()

# 算法加盐
hash = hashlib.md5("#$ggj".encode())
hash.update(pwd.encode())  # 算法加密
pwd = hash.hexdigest()  # 提取加密后的密码
print(pwd)