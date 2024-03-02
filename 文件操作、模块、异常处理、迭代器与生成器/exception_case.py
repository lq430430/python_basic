# 异常处理--多分支
def except_finally():
        # 例1： try/except/finally
    dict = {"name": "mary", "age": 14}
    try:
        sum = dict["name"] + dict["age"]
    # except TypeError:
    #     print("类型不一致，无法计算")
    except KeyError:
        print("字典中不存在KEY值")
    # except TypeError as e:
    #     print(e)
    except Exception as e:
        print(e)
    finally:
        print("===统一类型后计算===")
        print("__name__:",__name__)
def except_return_finally():
    """
    有返回值时 ，finally的返回值会覆盖try及except中返回值
    :return:
    """
    dict = {"name": "mary", "age": 14}
    try:
        sum = dict["name"] + dict["age"]
        return 1
    except KeyError:
        print("字典中不存在KEY值")
    # except TypeError as e:
    #     print(e)
    except Exception as e:
        print(e)
        return 2
    finally:
        print("===统一类型后计算===")
        return 3
def except_else():
    # 例2 try/except/else
    str = "sorry"
    try:
        for i in range(len(str)):
            print(str[i])
    except IndexError as e:
        print(e)
    else:
        print("输入成功，结束！")

def register():
    username=input('请输入用户名：')
    if len(username)<6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是：{}'.format(username))
if __name__=='__main__':
    # 异常1
    except_finally()
    #
    # #异常2处理
    # except_else()
    #
    # #异常有返回值
    # result=except_return_finally()
    # print(result)
    #
    # #抛出异常raise,自定义异常
    # try:
    #     register()
    # except Exception as err:
    #     print(err)
    #     print('注册失败')
    # else:
    #     print('注册成功')

