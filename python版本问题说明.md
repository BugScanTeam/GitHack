项目中的py代码在python3版本下运行会报错，一般会报错：

\#common.py

import urlparse

No module named 'urlparse'

\#request.py

import urllib2

No module named 'urllib2'

这是版本问题，因为python3版本中已经将urllib2、urlparse并入了urllib模块中，并且修改urllib模块，其中包含5个子模块：urllib.error,urllib.parse,urllib.request,urllib.response,urllib.robotparser。还有python2和python3版本的try-catch也有点不同。 这个问题只涉及到了lib中的common.py和request.py，所以只需要对这两个文件做出相应修改。

（PS：如果还有其他错，应该是包的问题了，pip install +相应的包就没问题了。）