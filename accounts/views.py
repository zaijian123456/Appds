from django.shortcuts import render

# Create your views here.
def index(request):
    """
    @api {GET} /index/? id=1 主页操作
    @apiVersion 1.0.0
    @apiNAme index
    @apiGRoup User
    @apiDescription 这里描述一下这个函数的具体操作
    这一行也是可以的

    @apiParam {Data} name 姓名

    @apiSuccess {object} status 状态码
    @apiSuccess {object} msg 简略描述

    @apiSuccessExample {Json} 成功返回：
        HTTP 1.1/ 200k
        [
             {
                  'id':1,
                  'name':‘张三’
             }，
              {
                  'id':2,
                  'name':‘李四’
             }，
              {
                  'id':3,
                  'name':‘王五’
             }，


        ]
    @apiErrorExample Resesponse-Fail:
        HTTP 1.1/ 404k
        {
             'status':1,
             'msg':'Fail'
        }
        """
    pass