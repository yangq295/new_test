import yaml
import os, sys

# 拼接yaml文件所在的data目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
CONFIG_DIR = os.path.join(BASE_DIR, os.path.join('data'))


class YamlUtil:
    """
    Yaml文件操作工具类
    """

    def __init__(self, filename):
        self.path = os.path.join(CONFIG_DIR, filename)

    def read_yaml(self):
        """
        读取Yaml文件中所有数据以dict类型返回
        """
        try:
            with open(self.path, mode='r', encoding='utf-8') as f:
                # 读取yaml文件，并通过yaml.load()转换为字典格式的数据
                data = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
                f.close()
                return data
        except Exception as msg:
            print("异常消息-> {0}".format(msg))

    def read_yaml_data(self, index):
        """
        读取Yaml文件中某一组的data数据以dict类型返回
        """
        try:
            data = self.read_yaml()
            return data[index]['data']
        except IndexError as msg:
            print("异常消息-> {0}".format(msg))

    def read_yaml_assert(self, index):
        """
        读取Yaml文件中某一组的assert数据以dict类型返回
        """
        try:
            data = self.read_yaml()
            return data[index]['assert']
        except IndexError as msg:
            print("异常消息-> {0}".format(msg))


    def write_yaml(self, jsondata=None):
        """
        写入数据到Yaml文件中（追加写入）
        """
        with open(self.path, mode='a', encoding='utf-8') as f:
            # 当data数据中有汉字时，需要加上： encoding='utf-8',allow_unicode=True
            yaml.dump(data=jsondata, stream=f, encoding='utf-8', allow_unicode=True)

    def clear_yaml(self):
        """
        清空Yaml文件中的数据
        """
        with open(self.path, mode='w', encoding='utf-8') as f:
            f.truncate()


# 调用方法
if __name__ == '__main__':
    # 文件夹读取
    path = os.path.join('systemManage_data', 'conftest_data.yaml')
    print(YamlUtil(path).read_yaml_assert(0))
    # #单个文件
    # path=os.path.join( 'login_data.yaml')
    # print(YamlUtil().read_yaml_assert(path))
