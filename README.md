# identity-card-crack-tools
## 前言

一个用于枚举可用SFZ号的工具，工具原理十分简单，即使原理很简单，仍然还有一些bug，日后再做相关完善。

**注意**

- 本项目仅用于学习交流，请勿用于非法用途
- 如用于非法用法，产生的后果与本项目无关



## 用法

```sh
python3 identity-card-crack-tools.py -h

usage: identity-card-crack-tools.py [-h] [-i IDENTITY] [-y YEAR] [-o OUT]

optional arguments:
  -h, --help            show this help message and exit
  -i IDENTITY, --identity IDENTITY
                        输入待破解的身份证号，不确定字符用问号?代替
  -y YEAR, --year YEAR  e.2000 爆破2000至今的身份证号
  -o OUT, --out OUT     输出到本地文件
```

该项目提供了四种爆破方式：

1. 爆破SFZ的年份4位（需要`-y`参数）

```
python3 identity-card-crack-tools.py -i "110101????01011009" -y 2000 -o 1.txt
```

2. 爆破SFZ的月日4位（无需`-y`参数）

```
python3 identity-card-crack-tools.py -i "1101011900????1009" -o 1.txt
```

3. 爆破SFZ的年月日8位（需要`-y`参数）

```
python3 identity-card-crack-tools.py -i "110101????????1009" -y 2000 -o 1.txt
```

4. 爆破SFZ的最后4位（无需`-y`参数）

```
python3 identity-card-crack-tools.py -i "11010119000101????" -o 1.txt
```

## TODO & BUG

- 不能爆破末尾带`X`的SFZ【BUG】

- 添加指定男女性别功能【TODO】
