import argparse
import datetime
import sys

res = []
allcount = 0

def write2txt(filename):
    """
    :param filename: 文件名
    """
    try:
        file_handle = open(filename, mode="w")
        for i in res:
            file_handle.write(i + "\n")
        file_handle.close()
    except:
        print("[Error]: 文件写入失败")
        sys.exit()

def bruteMid8nums(identity, year):
    """
    :param identity: 身份证号 字符串形式
    :param year: 年份 2000代表爆约2000至今的身份证号
    :return: 返回合法身份证号的个数，打印输出合法的身份证号
    """
    count = 0
    for i in range(0, 365 * (datetime.datetime.now().year - year + 1)):
        if year + 1 > int((datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y')):
            break
        tstr = (datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y%m%d')
        tmpidentity = identity.replace("????????", tstr)
        if checkLastNum(tmpidentity):
            count += 1
            res.append(tmpidentity)
    global allcount
    allcount = count
    return count

def bruteMonthDay4nums(identity):
    """
    :param identity: 身份证号 字符串形式
    :return: 返回合法身份证号的个数，打印输出合法的身份证号
    """
    count = 0
    for i in range(0, 366):
        tstr = (datetime.date.today() + datetime.timedelta(i)).strftime('%m%d')
        tmpidentity = identity.replace("????", tstr)
        if checkLastNum(tmpidentity):
            count += 1
            res.append(tmpidentity)
    global allcount
    allcount = count
    return count

def bruteYear4nums(identity, year):
    """
    :param identity: 身份证号 字符串形式
    :param year: 年份 2000代表爆约2000至今的身份证号
    :return: 返回合法身份证号的个数，打印输出合法的身份证号
    """
    count = 0
    for i in range(year, datetime.datetime.now().year + 1):
        tstr = "{:0>4d}".format(i)
        tmpidentity = identity.replace("????", tstr)
        if checkLastNum(tmpidentity):
            count += 1
            res.append(tmpidentity)
    global allcount
    allcount = count
    return count

def bruteLast4nums(identity):
    """
    :param identity: 身份证号 字符串形式
    :return: 返回合法身份证号的个数，打印输出合法的身份证号
    """
    lastChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
    count = 0
    for i in range(1000):
        tstr = str("{:0>3d}".format(i))
        for j in lastChar:
            tmpstr = tstr + j
            tmpidentity = identity.replace("????", tmpstr)
            if checkLastNum(tmpidentity):
                count += 1
                res.append(tmpidentity)
    global allcount
    allcount = count
    return count

def checkLastNum(identity):
    """
    :param identity: 身份证号 字符串形式
    :return: 返回验证身份号是否合法（验证最后一位校验位）
    """
    num = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    verification = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2]
    res = 0
    for i in range(len(identity) - 1):
        res += int(identity[i : i + 1]) * num[i]
    if str(verification[res % 11]) == identity[17:18]:
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--identity", help="输入待破解的身份证号，不确定字符用问号?代替", type=str)
    parser.add_argument("-y", "--year", help="e.2000 爆破2000至今的身份证号", type=int)
    parser.add_argument("-o", "--out", help="输出到本地文件", type=str)
    args = parser.parse_args()
    if not args.identity:
        print("[Error]: 请输入身份证号")
        sys.exit()
    if not args.out:
        print("[Error]: 请输入文件路径")
        sys.exit()
    if "?" not in args.identity:
        print("[Warning]: 请使用?符号进行占位爆破")
        sys.exit()
    if "x" == args.identity[17]:
        tmparg = args.identity.replace("x", "X")
        args.identity = tmparg
    if args.identity:
        if args.identity[6:14] == "????????":
            if not args.year:
                print("[Error]: 缺少-y参数")
                sys.exit()
            else:
                bruteMid8nums(args.identity, args.year)
                write2txt(args.out)
                print("[Info]: 已将%d条数据保存至：%s" % (allcount, args.out))
        elif args.identity[6:10] == "????":
            if not args.year:
                print("[Error]: 缺少-y参数")
                sys.exit()
            else:
                bruteYear4nums(args.identity, args.year)
                write2txt(args.out)
                print("[Info]: 已将%d条数据保存至：%s" % (allcount, args.out))
        elif args.identity[10:14] == "????":
            bruteMonthDay4nums(args.identity)
            write2txt(args.out)
            print("[Info]: 已将%d条数据保存至：%s" % (allcount, args.out))
        elif args.identity[14:18] == "????":
            bruteLast4nums(args.identity)
            write2txt(args.out)
            print("[Info]: 已将%d条数据保存至：%s" % (allcount , args.out))