import urllib.parse
import urllib.request

#urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=Nonne,cadefault=False,context=None)
#这是urlopen的api,除了传递基础的url，剩下的还会传递data(附加数据)，timeout(超时时间)

#data参数
#bytes(),第一个参数是字符串（urllib.parse.urlopen()是将字典转化为字符串）,第二个参数是指定编码格式
data = bytes(urllib.parse.urlencode({'name':'germey'}),encoding='utf-8')
response = urllib.request.urlopen('https://www.httpbin.org/post',data=data)
#获取的是模拟表单提交。以post方式传输数据
# print(response.read().decode('utf-8'))

#timeout参数，用于设置超时时间，单位为秒，超过设置时间就会抛出异常
response = urllib.request.urlopen('https://www.httpbin.org/get',timeout=0.1)
print(response.read())

