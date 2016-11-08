from request import crawer_geturl
from lxml import etree


class engine_Manager(object):

    def __init__(self):
        self.engine = engine_Manager()
        self.request_object = None

    def Crawer(self):
        request_object = spider.start_request()
        while True:
            try:
                res_object = request_object.next()
                if (res_object.method == "GET"):
                    response = res_object.get()
                    html = etree.HTML(response.lower.decode("utf-8"))
                    response = res_object.func(html)
                    if(isinstance(response, object)):
                        self.engine.Crawer_next(response)


                elif(res_object.method == "POST"):
                    response = res_object.post()
                    html = etree.HTML(response.lower.decode("utf-8"))
                    res_object.func(html)
                    if (isinstance(response, object)):
                        self.engine.Crawer_next()

            except StopIteration as e:
                pass
                break
    def Crawer_next(self, response):
        while True:




